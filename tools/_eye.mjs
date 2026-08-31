import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:900,height:700},deviceScaleFactor:2})).newPage();
await p.goto('file:///tmp/eye.html'); await p.waitForTimeout(300);
await p.screenshot({path:'/tmp/eye.png'}); await b.close();
