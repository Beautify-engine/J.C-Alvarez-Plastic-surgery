import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
await p.click('input[value="tummy-tuck"] + .bopt__box');
await p.waitForTimeout(1200);
console.log(await p.evaluate(()=>{
  const dd=document.querySelector('[data-brief="procedure"]');
  const cs=getComputedStyle(dd);
  return {text:dd.textContent, cls:dd.className, color:cs.color, opacity:cs.opacity,
          font:cs.fontFamily.slice(0,30), size:cs.fontSize};
}));
await b.close();
