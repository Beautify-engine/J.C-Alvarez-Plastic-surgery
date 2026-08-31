import { chromium } from 'playwright';
const b = await chromium.launch();
const ctx = await b.newContext({viewport:{width:1440,height:900}});
// block the actual YouTube request; we only care that the right URL is asked for
await ctx.route('**://*.youtube-nocookie.com/**', r => r.abort());
const p = await ctx.newPage();

// 1) homepage library cards — plain links
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
console.log('homepage library cards:');
console.log(' ', await p.$$eval('.lib__c', els => els.map(a => a.getAttribute('href'))));

// 2) preparation cards
await p.goto('http://localhost:8787/preparation.html',{waitUntil:'networkidle'});
console.log('preparation cards:');
console.log(' ', await p.$$eval('.lib__c', els => els.map(a => a.getAttribute('href'))));

// 3) procedure page — click the talk row, expect an iframe + a watch link
await p.goto('http://localhost:8787/procedures/bbl.html',{waitUntil:'networkidle'});
await p.evaluate(()=>document.getElementById('pvid').scrollIntoView());
await p.waitForTimeout(400);
await p.click('.pvid__row');
await p.waitForTimeout(600);
console.log('procedures/bbl talk row after click:');
console.log(' ', await p.evaluate(()=>{
  const f=document.querySelector('#pvid iframe'), a=document.querySelector('#pvid .pvid__src');
  return { iframe: f?f.src:null, title: f?f.title.slice(0,44):null, link: a?a.href:null };
}));

// 4) video library — click a card
await p.goto('http://localhost:8787/videos.html',{waitUntil:'networkidle'});
await p.waitForTimeout(400);
await p.click('.vid__item button, .vid__item a, .vid__frame');
await p.waitForTimeout(600);
console.log('videos.html after click:');
console.log(' ', await p.evaluate(()=>{
  const f=document.querySelector('iframe');
  return { iframe: f?f.src:null, count: document.querySelectorAll('iframe').length };
}));
await b.close();
