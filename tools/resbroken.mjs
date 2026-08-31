import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
const bad=[]; p.on('response',r=>{ if(r.status()>=400) bad.push(r.status()+' '+r.url().split('/').pop()); });
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.waitForTimeout(1500);
console.log('HTTP failures:', bad.length ? bad.slice(0,8) : 'none', bad.length>8?`(+${bad.length-8})`:'');
const info = await p.evaluate(()=>{
  const imgs=[...document.querySelectorAll('.res img')];
  const broken=imgs.filter(i=>i.naturalWidth===0);
  return { total: imgs.length, broken: broken.length,
           sample: broken.slice(0,4).map(i=>i.getAttribute('src')),
           okSample: imgs.filter(i=>i.naturalWidth>0).slice(0,2).map(i=>i.getAttribute('src')) };
});
console.log(JSON.stringify(info,null,1));
await b.close();
