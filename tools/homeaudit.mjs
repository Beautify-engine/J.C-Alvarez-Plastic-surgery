import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-reveal],[data-rise-group]').forEach(e=>e.classList.add('is-in')));
const H=await p.evaluate(()=>document.body.scrollHeight);
for(let y=0;y<H;y+=600){ await p.evaluate(v=>window.scrollTo(0,v),y); await p.waitForTimeout(120); }
await p.waitForTimeout(800);
const rows = await p.evaluate(()=>{
  return [...document.querySelectorAll('main section')].map(s=>{
    const r=s.getBoundingClientRect();
    const h=s.querySelector('h1,h2');
    return { cls:s.className.split(' ')[0], h: h?h.textContent.trim().slice(0,46):'(none)',
             px: Math.round(r.height),
             imgs: s.querySelectorAll('img').length,
             broken: [...s.querySelectorAll('img')].filter(i=>i.naturalWidth===0).length };
  });
});
console.log(JSON.stringify(rows,null,1));
console.log('reviews on page:', await p.evaluate(()=>document.querySelectorAll('.rev__q').length));
console.log('errors:', errs.length?errs.slice(0,4):'none');
await b.close();
