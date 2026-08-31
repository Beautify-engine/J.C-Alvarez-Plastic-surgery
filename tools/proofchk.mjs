import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/hero-headlines.html',{waitUntil:'networkidle'});
await p.waitForTimeout(1200);
const r = await p.evaluate(()=>{
  const proof=document.querySelector('.hA__proof');
  const ul=document.querySelector('.faces');
  const img=document.querySelector('.faces img');
  const cs=e=>e?getComputedStyle(e):null;
  return {
    proofDisplay: cs(proof).display,
    facesDisplay: cs(ul).display,
    facesListStyle: cs(ul).listStyleType,
    imgW: cs(img).width, imgH: cs(img).height,
    imgRadius: cs(img).borderRadius,
    liMargin: cs(document.querySelector('.faces li')).marginLeft,
  };
});
console.log(JSON.stringify(r,null,1));
await b.close();
