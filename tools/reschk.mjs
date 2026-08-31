import { chromium } from 'playwright';
const probe = async p => p.evaluate(()=>({
  cases: document.querySelectorAll('.gal__i').length,
  filters: document.querySelectorAll('.gal__filters button').length,
  count: document.querySelector('.gal__count').textContent,
  imgsOk: [...document.querySelectorAll('.gal__i img')].every(i=>i.naturalWidth>0),
  h1px: Math.round(parseFloat(getComputedStyle(document.querySelector('h1')).fontSize)),
  overflow: document.documentElement.scrollWidth>document.documentElement.clientWidth,
}));
const b = await chromium.launch(); let bad=0;
for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const out={};
  for (const [n,url] of [['dev','http://localhost:8787/results.html'],['art','http://localhost:8787/_reschk.html']]) {
    const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
    const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
    await p.goto(url,{waitUntil:'networkidle'});
    const H=await p.evaluate(()=>document.body.scrollHeight);
    for(let y=0;y<H;y+=500){ await p.evaluate(v=>window.scrollTo(0,v),y); await p.waitForTimeout(110); }
    await p.waitForTimeout(900);
    out[n]=await probe(p);
    if(errs.length){console.log(tag,n,'ERRORS',errs.slice(0,3));bad++;}
    await p.close();
  }
  const diff=Object.keys(out.dev).filter(k=>JSON.stringify(out.dev[k])!==JSON.stringify(out.art[k]));
  console.log(`${tag.padEnd(8)} dev ${JSON.stringify(out.dev)}`);
  console.log(`${''.padEnd(8)} art ${JSON.stringify(out.art)}`);
  if(diff.length){console.log('  ✗ MISMATCH:',diff.join(', '));bad++;} else console.log('  ✓ artifact matches dev');
}
await b.close(); process.exit(bad?1:0);
