import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
await p.waitForTimeout(2000);
await p.addStyleTag({content:'.ho-label{display:none !important}'});
const sec = p.locator('section.hA').first();
await sec.scrollIntoViewIfNeeded();
for (const t of [0, 3, 6, 9, 11.5]) {
  await p.evaluate(async (t) => {
    const v = document.querySelector('section.hA video');
    v.pause(); v.currentTime = t;
    await new Promise(r => v.readyState >= 2 ? setTimeout(r,120) : v.onseeked = () => setTimeout(r,120));
  }, t);
  await p.waitForTimeout(350);
  await sec.screenshot({path:`design/shots/mob-t${String(t).replace('.','_')}.png`});
}
console.log('captured');
await b.close();
