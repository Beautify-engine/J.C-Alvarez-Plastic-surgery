import { chromium } from 'playwright';
const b = await chromium.launch();
const ctx = await b.newContext({viewport:{width:1440,height:900}});
const p = await ctx.newPage();
const fails=[];
p.on('response', r=>{ if(r.status()>=400) fails.push(r.status()+' '+r.url()); });
await p.goto('http://localhost:8787/carousels.html',{waitUntil:'networkidle'});
await p.waitForTimeout(2500);
const info = await p.evaluate(()=>[...document.querySelectorAll('.trk__item img')].map((i,n)=>({
  n, src:i.currentSrc.split('/').pop(), complete:i.complete, nw:i.naturalWidth,
  loading:i.loading, vis:i.getBoundingClientRect().width>0
})));
console.log(JSON.stringify(info,null,1));
console.log('failed responses:', fails.length? fails : 'none');
await b.close();
