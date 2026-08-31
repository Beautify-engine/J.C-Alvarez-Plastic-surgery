import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1})).newPage();
await p.goto('http://localhost:8787/about.html',{waitUntil:'networkidle'});
await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));
await p.waitForTimeout(1600);
await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(500);
for (const [sel,name] of [['.ab-arc__top','arc-top'],['.ab-why','why'],['.ab-team-s','team']]) {
  const el = p.locator(sel); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
  await el.screenshot({path:`design/shots/ab-${name}.png`});
}
await b.close();
