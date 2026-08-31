import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal],[data-rise-group]').forEach(e=>e.classList.add('is-in')));
await p.waitForTimeout(1200);
const info = await p.evaluate(() => {
  const secs=[...document.querySelectorAll('main > section, main section')].filter(s=>s.parentElement.tagName==='MAIN'||s.parentElement.tagName==='BODY');
  return {
    order: [...document.querySelectorAll('section')].map(s=>s.className.split(' ')[0]),
    h2s: [...document.querySelectorAll('h1,h2')].map(h=>h.tagName+': '+h.textContent.trim().slice(0,44)),
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  };
});
console.log(JSON.stringify(info,null,1));
console.log('console errors:', errs.length?errs.slice(0,4):'none');
await p.screenshot({path:'design/shots/full-d.png', fullPage:true});
await b.close();
