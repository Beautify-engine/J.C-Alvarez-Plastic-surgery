import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/preparation.html',{waitUntil:'networkidle'});
await p.waitForTimeout(700);
console.log(JSON.stringify(await p.evaluate(()=>{
  const q=document.querySelector('.pr-band__q'), pEl=q.querySelector('p');
  const r=e=>{const b=e.getBoundingClientRect();return {l:Math.round(b.left),w:Math.round(b.width)}};
  return {align:getComputedStyle(pEl).textAlign, q:r(q), wrap:r(q.closest('.wrap')),
          band:r(document.querySelector('.pr-band')),
          bookImg:(()=>{const i=document.querySelector('.lib__th--book img');const b=i.getBoundingClientRect();return Math.round(b.width)+'x'+Math.round(b.height)})()};
}),null,1));
await b.close();
