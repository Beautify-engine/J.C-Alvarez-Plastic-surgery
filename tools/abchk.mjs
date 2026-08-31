import { chromium } from 'playwright';
const probe = async p => p.evaluate(() => {
  const q = s => document.querySelector(s);
  return {
    h1:   document.querySelectorAll('h1').length,
    tl:   document.querySelectorAll('.tl__i').length,
    quotes: document.querySelectorAll('.tl__q').length,
    marks: document.querySelectorAll('.creds__marks img').length,
    sig:  q('.note__mark') && q('.note__mark').naturalWidth > 0,
    portrait: q('.ab-intro__fig img') && q('.ab-intro__fig img').naturalWidth > 0,
    team:     q('.ab-team-s__fig img') && q('.ab-team-s__fig img').naturalWidth > 0,
    interview:q('.ab-arc__fig img') && q('.ab-arc__fig img').naturalWidth > 0,
    consult:  q('.ab-why__fig img') && q('.ab-why__fig img').naturalWidth > 0,
    book:     q('.bk__fig img') && q('.bk__fig img').naturalWidth > 0,
    imgsOk:   [...document.querySelectorAll('img')].every(i => i.naturalWidth > 0),
    vhHidden: Math.round(q('h2.vh').getBoundingClientRect().height) <= 1,
    footer: !!q('footer.ft'),
    h1px: Math.round(parseFloat(getComputedStyle(q('h1')).fontSize)),
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  };
});
const b = await chromium.launch(); let bad = 0;
for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const out = {};
  for (const [n,url] of [['dev','http://localhost:8787/about.html'],['art','http://localhost:8787/_abchk.html']]) {
    const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
    const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
    await p.goto(url,{waitUntil:'networkidle'});
    // step-scroll: an instant jump to the bottom does not fire loading="lazy",
    // which made this check report images as broken when they were fine
    const H = await p.evaluate(()=>document.body.scrollHeight);
    for (let y=0; y<H; y+=500){ await p.evaluate(v=>window.scrollTo(0,v), y); await p.waitForTimeout(140); }
    await p.waitForTimeout(900);
    await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(400);
    out[n] = await probe(p);
    if (errs.length){ console.log(tag,n,'ERRORS',errs.slice(0,3)); bad++; }
    await p.close();
  }
  const diff = Object.keys(out.dev).filter(k=>JSON.stringify(out.dev[k])!==JSON.stringify(out.art[k]));
  console.log(`${tag.padEnd(8)} dev ${JSON.stringify(out.dev)}`);
  console.log(`${''.padEnd(8)} art ${JSON.stringify(out.art)}`);
  if (diff.length){ console.log('  ✗ MISMATCH:',diff.join(', ')); bad++; } else console.log('  ✓ artifact matches dev');
}
await b.close(); process.exit(bad?1:0);
