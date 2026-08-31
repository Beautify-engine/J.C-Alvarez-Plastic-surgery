import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844}})).newPage();
await p.goto('http://localhost:8799/',{waitUntil:'networkidle'});
const H=await p.evaluate(()=>document.body.scrollHeight);
for(let y=0;y<H;y+=500){ await p.evaluate(v=>scrollTo(0,v),y); await p.waitForTimeout(110); }
await p.waitForTimeout(2000);
console.log(await p.evaluate(()=>[...document.querySelectorAll('img')].filter(i=>i.naturalWidth===0).map(i=>({
  cls: i.className||'(none)', parent: i.parentElement.tagName+'.'+(i.parentElement.className||''),
  sect: (i.closest('section')||{className:'?'}).className.split(' ')[0],
  alt: i.alt.slice(0,30), hasSrcset: i.hasAttribute('srcset'), len:(i.currentSrc||'').length
}))));
await b.close();
