import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
const r = await p.evaluate(()=>{
  const q=s=>{const e=document.querySelector(s); if(!e) return null;
    const b=e.getBoundingClientRect(), c=getComputedStyle(e);
    return {sel:s,left:Math.round(b.left),width:Math.round(b.width),
      ml:c.marginLeft,mr:c.marginRight,maxW:c.maxWidth,display:c.display,alignSelf:c.alignSelf};};
  return ['.hero','.hero > .wrap','.hero__inner','.hero__facts .wrap','.hero h1'].map(q);
});
console.log(JSON.stringify(r,null,1));
await b.close();
