import { chromium } from 'playwright';
const probe = async p => p.evaluate(() => {
  const q = s => document.querySelector(s);
  const img = q('.about__fig img');
  return {
    marks:  document.querySelectorAll('.creds__marks img').length,
    marksLoaded: [...document.querySelectorAll('.creds__marks img')].every(i => i.naturalWidth > 0),
    certLabel: !!q('.about__markslabel'),
    note:   !!q('.note'),
    noteFont: q('.note p') && getComputedStyle(q('.note p')).fontFamily.split(',')[0],
    sig:    q('.note__mark') && q('.note__mark').naturalWidth > 0,
    pulls:  document.querySelectorAll('.about blockquote.pull').length,
    quoteMark: getComputedStyle(q('.note blockquote p'), '::before').content,
    bioGone: !document.body.innerHTML.includes('worked four months'),
    fivePt: !!q('.creds ol'),        // must be false — removed
    portrait: img && img.naturalWidth > 0,
    marquee: !!q('.mq'),          // must be false — it moved to About
    order:  [...document.querySelectorAll('section')].map(x=>x.className.split(' ')[0]).join('>'),
  };
});
const b = await chromium.launch();
let bad = 0;
for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const out = {};
  for (const [name,url] of [['dev','http://localhost:8787/'],['art','http://localhost:8787/_homechk.html']]) {
    const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
    await p.goto(url,{waitUntil:'networkidle'});
    await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal]').forEach(e=>e.classList.add('is-in')));
    await p.waitForTimeout(1500);
    out[name] = await probe(p);
    await p.close();
  }
  const diff = Object.keys(out.dev).filter(k => JSON.stringify(out.dev[k]) !== JSON.stringify(out.art[k]));
  console.log(`${tag.padEnd(8)} dev ${JSON.stringify(out.dev)}`);
  console.log(`${''.padEnd(8)} art ${JSON.stringify(out.art)}`);
  if (diff.length) { console.log('  ✗ MISMATCH:', diff.join(', ')); bad++; }
  else console.log('  ✓ artifact matches dev');
}
await b.close();
process.exit(bad?1:0);
