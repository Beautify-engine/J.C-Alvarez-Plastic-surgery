import { chromium } from 'playwright';
const b = await chromium.launch();
// 200% zoom ≈ half the CSS viewport at 1280 physical
const p = await (await b.newContext({viewport:{width:640,height:512},deviceScaleFactor:2,
  reducedMotion:'reduce'})).newPage();
await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
const overflow = await p.evaluate(()=>document.documentElement.scrollWidth > document.documentElement.clientWidth);
console.log('200% zoom horizontal overflow:', overflow);
await p.click('input[value="tummy-tuck"] + .bopt__box');
await p.waitForTimeout(500);
console.log('reduced-motion animation on panel:', await p.evaluate(()=>
  getComputedStyle(document.getElementById('p1')).animationName));
await p.screenshot({path:'design/shots/BK-zoom200.png', fullPage:true});
await b.close();
