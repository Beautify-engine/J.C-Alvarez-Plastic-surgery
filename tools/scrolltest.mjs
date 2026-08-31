import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
const h=await p.evaluate(()=>document.body.scrollHeight);
for(let y=0;y<h;y+=700){ await p.evaluate(v=>window.scrollTo(0,v),y); await p.waitForTimeout(160); }
await p.waitForTimeout(700);
const r=await p.evaluate(()=>({
  revealed:document.querySelectorAll('[data-rise].in,[data-rise-group].in').length,
  total:document.querySelectorAll('[data-rise],[data-rise-group]').length,
  hidden:[...document.querySelectorAll('[data-rise],[data-rise-group]')]
          .filter(e=>!e.classList.contains('in')).map(e=>e.className.split(' ')[0])
}));
console.log(JSON.stringify(r));
await b.close();
