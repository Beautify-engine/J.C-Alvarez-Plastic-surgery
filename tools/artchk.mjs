import { chromium } from 'playwright';
/* Verifies the BUILT artifact renders identically to the dev page. The builder
   strips the document head, so anything that lived there silently disappears —
   which is exactly how a 46px headline shipped at ~150px. Compare, don't assume. */
const probe = async (p) => p.evaluate(() => {
  const h1 = document.querySelector('.hA h1.h--two');
  const by = document.querySelector('.hA__by');
  const more = document.querySelector('.hA__more');
  const v = document.querySelector('video.hero-v');
  const cs = e => e && getComputedStyle(e);
  return {
    h1px:   Math.round(parseFloat(cs(h1).fontSize)),
    h1lines: Math.round(h1.getBoundingClientRect().height / parseFloat(cs(h1).lineHeight)),
    byCase: cs(by).textTransform,
    moreCase: cs(more).textTransform,
    proof:  !!document.querySelector('.hA__proof'),
    faces:  document.querySelectorAll('.faces img').length,
    vidW:   v && v.videoWidth,
  };
});

const b = await chromium.launch();
let bad = 0;
for (const [w, h, tag] of [[1440, 900, 'desktop'], [390, 844, 'mobile']]) {
  const out = {};
  for (const [name, url] of [['dev', 'http://localhost:8787/hero-headlines.html'],
                             ['art', 'http://localhost:8787/_artchk.html']]) {
    const p = await (await b.newContext({ viewport: { width: w, height: h } })).newPage();
    const errs = [];
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    p.on('requestfailed', r => errs.push('REQFAIL ' + r.url().slice(0, 70)));
    await p.goto(url, { waitUntil: 'networkidle' });
    await p.waitForTimeout(2200);
    out[name] = await probe(p);
    if (errs.length) { console.log(tag, name, 'ERRORS', errs.slice(0, 3)); bad++; }
    await p.close();
  }
  const keys = Object.keys(out.dev);
  const diff = keys.filter(k => JSON.stringify(out.dev[k]) !== JSON.stringify(out.art[k]));
  console.log(`${tag.padEnd(8)} dev ${JSON.stringify(out.dev)}`);
  console.log(`${''.padEnd(8)} art ${JSON.stringify(out.art)}`);
  if (diff.length) { console.log(`  ✗ MISMATCH: ${diff.join(', ')}`); bad++; }
  else console.log('  ✓ artifact matches dev');
}
await b.close();
process.exit(bad ? 1 : 0);
