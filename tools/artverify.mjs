import { chromium } from 'playwright';
/* Verify a BUILT artifact in isolation.
   Every earlier check copied the artifact into src/public and served it from there,
   so any path the builder forgot to inline still resolved against the real asset
   tree — which is exactly the bug the check existed to catch (D-055). This serves
   the file from a directory containing nothing else, so a missed inline 404s here
   the same way it 404s on claude.ai. */
const url = process.argv[2];                      // isolated artifact URL
const label = process.argv[3] || 'artifact';
const b = await chromium.launch();
let bad = 0;
for (const [w, h, tag] of [[1440, 900, 'desktop'], [390, 844, 'mobile']]) {
  const p = await (await b.newContext({ viewport: { width: w, height: h } })).newPage();
  const misses = [];
  p.on('requestfailed', r => misses.push('FAIL ' + r.url().slice(0, 70)));
  p.on('response', r => { if (r.status() >= 400) misses.push(r.status() + ' ' + r.url().slice(0, 70)); });
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.querySelectorAll('[data-rise],[data-reveal],[data-rise-group]')
    .forEach(e => e.classList.add('is-in')));
  const H = await p.evaluate(() => document.body.scrollHeight);
  for (let y = 0; y < H; y += 500) { await p.evaluate(v => scrollTo(0, v), y); await p.waitForTimeout(110); }
  // Carousels scroll HORIZONTALLY, so vertical scrolling never fires loading="lazy"
  // on their off-screen tiles — which produced a false "broken image" twice before.
  await p.evaluate(async () => {
    const tracks = [...document.querySelectorAll('*')].filter(e => {
      const o = getComputedStyle(e).overflowX;
      return (o === 'auto' || o === 'scroll') && e.scrollWidth > e.clientWidth + 40;
    });
    for (const t of tracks) {
      for (let x = 0; x <= t.scrollWidth; x += Math.max(200, t.clientWidth - 60)) {
        t.scrollLeft = x;
        await new Promise(r => setTimeout(r, 90));
      }
      t.scrollLeft = 0;
    }
  });
  await p.evaluate(() => scrollTo(0, 0));
  await p.waitForTimeout(3000);
  const r = await p.evaluate(() => {
    const v = document.getElementById('heroVid');
    const imgs = [...document.querySelectorAll('img')];
    return {
      // "broken" means: it should have loaded and didn't. A lazy image parked
      // off-screen has legitimately not loaded — counting it produced two false
      // failures already. Flag lazy images only when they are actually in view.
      brokenImgs: imgs.filter(i => {
        if (i.naturalWidth !== 0) return false;
        // an intentionally empty <img src=""> (the case viewer fills it on open)
        // is not a broken image
        if (!i.getAttribute('src')) return false;
        if (i.loading !== 'lazy') return true;
        const r = i.getBoundingClientRect();
        return r.width > 0 && r.bottom > 0 && r.top < innerHeight
                           && r.right > 0 && r.left < innerWidth;
      }).map(i => ({ src: (i.currentSrc || i.src).slice(0, 30), alt: i.alt.slice(0, 28) })),
      avatars: [...document.querySelectorAll('.faces img')].map(i => i.naturalWidth),
      video: v ? { src: (v.currentSrc || '').slice(0, 26), w: v.videoWidth, playing: !v.paused, rs: v.readyState } : null,
    };
  });
  const fail = r.brokenImgs.length || (r.video && (!r.video.w || !r.video.playing))
            || (r.avatars.length && r.avatars.some(x => !x)) || misses.length;
  console.log(`${label} ${tag}: video ${JSON.stringify(r.video)} avatars ${JSON.stringify(r.avatars)}`);
  if (r.brokenImgs.length) console.log('   broken imgs:', r.brokenImgs.slice(0, 5));
  if (misses.length) console.log('   network:', misses.slice(0, 5));
  console.log(fail ? '   ✗ FAIL' : '   ✓ ok');
  if (fail) bad++;
  await p.close();
}
await b.close();
process.exit(bad ? 1 : 0);
