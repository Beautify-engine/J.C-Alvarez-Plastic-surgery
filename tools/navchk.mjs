import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:390,height:844}})).newPage();
await p.goto('http://localhost:8787/results.html',{waitUntil:'networkidle'});
console.log(JSON.stringify(await p.evaluate(()=>{
  const nav=document.querySelector('nav.nav .wrap ul')||document.querySelector('nav.nav');
  const cs=getComputedStyle(nav);
  return {scrollW:nav.scrollWidth, clientW:nav.clientWidth,
          scrollable:nav.scrollWidth>nav.clientWidth, overflowX:cs.overflowX,
          docOverflow: document.documentElement.scrollWidth>document.documentElement.clientWidth};
}),null,1));
await b.close();
