import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
await p.waitForTimeout(2500);
await p.addStyleTag({content:'.ho-label{display:none !important}'});
const sec = p.locator('section.hA').first();
await sec.scrollIntoViewIfNeeded();
const times = [0.3, 2.7, 4.6, 6.4, 8.5, 10.6, 11.6];
for (const t of times) {
  await p.evaluate(async (t) => {
    const v = document.querySelector('section.hA video.hero-v');
    v.pause();
    await new Promise(r => { v.onseeked = () => r(); v.currentTime = t; setTimeout(r, 900); });
  }, t);
  await p.waitForTimeout(300);
  await sec.screenshot({path:`design/shots/ms-${String(t).replace('.','_')}.png`});
}
console.log('ok');
await b.close();
