import { chromium } from 'playwright';
const b = await chromium.launch();
for (const n of ['privacy','accessibility']) {
  const p = await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1})).newPage();
  const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await p.goto(`http://localhost:8787/${n}.html`,{waitUntil:'networkidle'});
  await p.waitForTimeout(600);
  const r = await p.evaluate(()=>({
    h1: document.querySelectorAll('h1').length,
    heads: [...document.querySelectorAll('h2')].map(h=>h.textContent.trim().slice(0,40)),
    footer: !!document.querySelector('footer.ft'),
    overflow: document.documentElement.scrollWidth>document.documentElement.clientWidth,
    measure: Math.round(document.querySelector('.legal p').getBoundingClientRect().width),
  }));
  console.log(n, JSON.stringify(r), errs.length?errs:'');
  await p.screenshot({path:`design/shots/${n}.png`, fullPage:true});
  await p.close();
}
await b.close();
