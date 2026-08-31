import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.waitForTimeout(800);
console.log(await p.evaluate(()=>[...document.querySelectorAll('main section, footer')].map(s=>{
  const bg=getComputedStyle(s).backgroundColor;
  const m=bg.match(/\d+/g)||[0,0,0];
  const l=(0.2126*m[0]+0.7152*m[1]+0.0722*m[2])/255;
  return (s.className.split(' ')[0]||s.tagName.toLowerCase()).padEnd(8)+' '+(l>0.5?'LIGHT':'dark ')+'  '+bg;
}).join('\n')));
await b.close();
