import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
await p.waitForTimeout(2000);
await p.addStyleTag({content:'.ho-label{display:none !important}'});
const sec = p.locator('section.hA').first();
await sec.scrollIntoViewIfNeeded();
// restart the loop, then sample it as it plays
await p.evaluate(() => { const v=document.querySelector('section.hA video.hero-v'); v.currentTime=0; v.play(); });
for (let i = 0; i < 7; i++) {
  await p.waitForTimeout(i === 0 ? 400 : 1750);
  const t = await p.evaluate(() => document.querySelector('section.hA video.hero-v').currentTime);
  await sec.screenshot({path:`design/shots/mp-${i}.png`});
  console.log(i, t.toFixed(2));
}
await b.close();
