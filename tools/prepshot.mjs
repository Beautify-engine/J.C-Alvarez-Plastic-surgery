import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1})).newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
p.on('requestfailed',r=>errs.push('REQFAIL '+r.url().slice(-44)));
await p.goto('http://localhost:8787/preparation.html',{waitUntil:'networkidle'});
const H=await p.evaluate(()=>document.body.scrollHeight);
for(let y=0;y<H;y+=500){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(120); }
await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(900);
console.log(JSON.stringify(await p.evaluate(()=>({
  h1: document.querySelectorAll('h1').length,
  heads: [...document.querySelectorAll('h1,h2,h3')].map(h=>h.tagName+' '+h.textContent.trim().slice(0,38)),
  imgsOk: [...document.querySelectorAll('img')].every(i=>i.naturalWidth>0),
  overflow: document.documentElement.scrollWidth>document.documentElement.clientWidth,
  footer: !!document.querySelector('footer.ft'),
})),null,1));
console.log('errors:', errs.length?errs:'none');
await p.screenshot({path:'design/shots/prep-d.png', fullPage:true});
await b.close();
