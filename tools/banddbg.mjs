import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
const r=await p.evaluate(()=>{
  const q=s=>{const e=document.querySelector(s); if(!e)return null;
    const b=e.getBoundingClientRect(), c=getComputedStyle(e);
    return {sel:s,h:Math.round(b.height),w:Math.round(b.width),display:c.display,
            flexDir:c.flexDirection,aspect:c.aspectRatio,pos:c.position};};
  const item=document.querySelector('.trk__item');
  const img=document.querySelector('.trk__fig img');
  return {
    boxes:['.band','.band .wrap','.trk','.trk__item','.trk__fig'].map(q),
    imgH: img?Math.round(img.getBoundingClientRect().height):null,
    figAspect: getComputedStyle(document.querySelector('.trk__fig')).aspectRatio,
    itemFlex: item?getComputedStyle(item).flex:null
  };
});
console.log(JSON.stringify(r,null,1));
await b.close();
