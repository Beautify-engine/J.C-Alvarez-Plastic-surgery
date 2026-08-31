import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1})).newPage();
await p.goto('http://localhost:8787/about.html',{waitUntil:'networkidle'});
const H = await p.evaluate(()=>document.body.scrollHeight);
for (let y=0;y<H;y+=500){ await p.evaluate(v=>window.scrollTo(0,v),y); await p.waitForTimeout(120); }
await p.waitForTimeout(700);
for (const [sel,n] of [['.bk','book'],['.ab-team-s','team']]) {
  const el = p.locator(sel); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
  await el.screenshot({path:`design/shots/ab-${n}.png`});
}
await b.close();
