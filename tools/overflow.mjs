import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:+(process.argv[3] || 390),height:844}});
await p.goto(process.argv[2], {waitUntil:'networkidle'});
const out = await p.evaluate(()=>{
  const vw = document.documentElement.clientWidth;
  const bad = [];
  document.querySelectorAll('*').forEach(el=>{
    const r = el.getBoundingClientRect();
    if (r.width===0) return;
    if (r.right > vw + 1 || r.left < -1) {
      bad.push({tag:el.tagName.toLowerCase(), cls:el.className&&el.className.toString().slice(0,50),
                left:Math.round(r.left), right:Math.round(r.right), w:Math.round(r.width)});
    }
  });
  return {vw, scrollW: document.documentElement.scrollWidth, bad: bad.slice(0,25)};
});
console.log(JSON.stringify(out,null,1));
await b.close();
