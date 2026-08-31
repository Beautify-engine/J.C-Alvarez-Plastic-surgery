import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1})).newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
p.on('requestfailed',r=>errs.push('REQFAIL '+r.url().slice(-46)));
await p.goto('http://localhost:8787/about.html',{waitUntil:'networkidle'});
await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal]').forEach(e=>e.classList.add('is-in')));
await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));
await p.waitForTimeout(1600);
await p.evaluate(()=>window.scrollTo(0,0));
await p.waitForTimeout(600);
const info = await p.evaluate(()=>({
  h1: document.querySelectorAll('h1').length,
  heads: [...document.querySelectorAll('h1,h2,h3')].map(h=>h.tagName+' '+h.textContent.trim().slice(0,40)),
  overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  footer: !!document.querySelector('footer.ft'),
  timeline: document.querySelectorAll('.tl__i').length,
  imgsOk: [...document.querySelectorAll('img')].every(i=>i.naturalWidth>0),
}));
console.log(JSON.stringify(info,null,1));
console.log('errors:', errs.length?errs:'none');
await p.screenshot({path:'design/shots/aboutpage-d.png', fullPage:true});
await b.close();
