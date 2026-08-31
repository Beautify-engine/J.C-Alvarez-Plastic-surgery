import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:2})).newPage();
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.waitForTimeout(1500);
const el=p.locator(process.argv[2]);
await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(700);
await el.screenshot({path:`design/shots/${process.argv[3]}.png`});
console.log('ok'); await b.close();
