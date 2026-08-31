import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
await p.waitForTimeout(1200);
const st = () => p.evaluate(() => {
  const mq = document.querySelector('.mq'), btn = document.querySelector('.mq__pause');
  return { paused: mq.hasAttribute('data-paused'),
           playState: getComputedStyle(mq.querySelector('.mq__inner')).animationPlayState,
           pressed: btn.getAttribute('aria-pressed'),
           label: btn.querySelector('.vh').textContent,
           dur: getComputedStyle(mq.querySelector('.mq__inner')).animationDuration };
});
console.log('initial ', JSON.stringify(await st()));
await p.locator('.mq__pause').first().click();
console.log('clicked ', JSON.stringify(await st()));
await p.locator('.mq__pause').first().click();
console.log('again   ', JSON.stringify(await st()));
// keyboard reachability
const focusable = await p.evaluate(() => {
  const b = document.querySelector('.mq__pause'); b.focus();
  return document.activeElement === b;
});
console.log('keyboard focusable:', focusable);
await b.close();
