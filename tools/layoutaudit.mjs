import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,90));});
await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));
await p.waitForTimeout(1200);
const r=await p.evaluate(()=>{
  const out=[];
  document.querySelectorAll('section').forEach(s=>{
    const b=s.getBoundingClientRect();
    const cls=s.className.split(' ')[0];
    const hidden=[...s.querySelectorAll('[data-rise],[data-rise-group]')].filter(e=>!e.classList.contains('in')).length;
    out.push({cls, h:Math.round(b.height), overflowX: s.scrollWidth>document.documentElement.clientWidth+2, unrevealed:hidden});
  });
  return {sections:out, docW:document.documentElement.clientWidth, bodyW:document.body.scrollWidth};
});
console.log('page width', r.docW, '| body scrollWidth', r.bodyW, r.bodyW>r.docW+2?'  <-- HORIZONTAL OVERFLOW':'');
r.sections.forEach(s=>console.log(`  ${s.cls.padEnd(8)} h=${String(s.h).padStart(5)}  overflowX=${s.overflowX}  unrevealed=${s.unrevealed}`));
console.log('console errors:', errs.length?errs:'none');
await b.close();
