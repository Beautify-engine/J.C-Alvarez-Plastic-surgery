import { chromium } from 'playwright';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:940},deviceScaleFactor:2});
const p=await ctx.newPage();
const bad=[]; p.on('response',r=>{ if(r.status()>=400) bad.push(r.status()+' '+r.url().split('/').pop()); });
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.locator('section.res').scrollIntoViewIfNeeded();
await p.waitForTimeout(800);
await p.locator('.res__open').first().click();
await p.waitForTimeout(900);
const st=await p.evaluate(()=>{
  const d=document.getElementById('lb');
  const B=document.getElementById('lbB'), A=document.getElementById('lbA');
  return {open:d.open, cap:document.getElementById('lbCap').textContent,
          bSrc:(B.currentSrc||'').split('/').pop(), bW:B.naturalWidth,
          aSrc:(A.currentSrc||'').split('/').pop(), aW:A.naturalWidth};
});
console.log(JSON.stringify(st,null,1));
await p.locator('#lbNext').click(); await p.waitForTimeout(600);
console.log('after next:', await p.evaluate(()=>document.getElementById('lbCap').textContent));
await p.locator('.lb').screenshot({path:'design/shots/lightbox.png'});
console.log('bad responses:', bad.length? bad : 'none');
await b.close();
