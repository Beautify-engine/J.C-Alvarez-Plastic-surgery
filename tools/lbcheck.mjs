import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
const got = [];
p.on('response', r => { const u=r.url(); if(u.includes('/img/cases/')) got.push(u.split('/').pop()); });
await p.goto('http://localhost:8787/_final/results.html',{waitUntil:'networkidle'});
await p.waitForTimeout(800);
const before = got.length;
// open three cases and confirm each pulls its full-size slide
for (const i of [0,1,2]) {
  await p.locator('.gal__c').nth(i).click();
  await p.waitForTimeout(700);
  await p.keyboard.press('Escape');
  await p.waitForTimeout(200);
}
const full = got.filter(f => /^[a-z-]+-\d+\.jpg$/.test(f));
console.log('case requests before opening any:', before);
console.log('full-size slides pulled by the lightbox:', [...new Set(full)]);
await b.close();
