import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:2})).newPage();
await p.goto('http://localhost:8787/_artchk.html',{waitUntil:'networkidle'});
await p.waitForTimeout(2400);
await p.addStyleTag({content:'.ho-label{display:none !important}'});
const s = p.locator('section.hA').nth(1);   // variant 2 — the one in the screenshot
await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(600);
await s.screenshot({path:'design/shots/art-v2-d.png'});
await b.close();
