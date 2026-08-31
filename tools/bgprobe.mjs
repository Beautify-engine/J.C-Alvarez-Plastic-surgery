import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:1000}})).newPage();
await p.goto('http://localhost:8787/gallery-options.html',{waitUntil:'networkidle'});
await p.waitForTimeout(800);
const r = await p.evaluate(()=>{
  const out=[];
  document.querySelectorAll('*').forEach(el=>{
    const c=getComputedStyle(el), bg=c.backgroundColor;
    if(bg && bg!=='rgba(0, 0, 0, 0)' && bg!=='transparent'){
      const rect=el.getBoundingClientRect();
      out.push({tag:el.tagName.toLowerCase(), cls:(el.className||'').toString().slice(0,42),
                bg, pos:c.position, w:Math.round(rect.width), h:Math.round(rect.height)});
    }
  });
  return out.filter(o=>/165, 211, 222|a5d3de|214, 223, 226/.test(o.bg));
});
console.log(JSON.stringify(r,null,1));
await b.close();
