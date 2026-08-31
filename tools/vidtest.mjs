import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/videos.html',{waitUntil:'networkidle'});
const ext=[]; p.on('request',r=>{const u=r.url(); if(!u.includes('localhost')) ext.push(u.split('/')[2]);});
await p.waitForTimeout(1000);
console.log('third-party requests on load:', [...new Set(ext)].length ? [...new Set(ext)] : 'none');
console.log('iframes before click:', await p.locator('.vid__frame iframe').count());
await p.locator('.vid__play').first().click();
await p.waitForTimeout(1200);
console.log('iframes after click:', await p.locator('.vid__frame iframe').count());
console.log('src:', ((await p.locator('.vid__frame iframe').first().getAttribute('src'))||'').slice(0,60));
// filter check
await p.locator('.vid__filters button[data-f="tummy-tuck"]').click();
await p.waitForTimeout(400);
console.log('visible after Tummy Tuck filter:', await p.locator('.vid__item:not(.vid__hidden)').count());
await b.close();
