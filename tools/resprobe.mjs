import { chromium } from 'playwright';
const b = await chromium.launch();
for (const w of [1440, 390]) {
  const p = await (await b.newContext({viewport:{width:w,height:900}})).newPage();
  await p.goto('http://localhost:8787/',{waitUntil:'networkidle'});
  await p.waitForTimeout(1200);
  console.log(w, JSON.stringify(await p.evaluate(()=>{
    const c=document.querySelector('.res__case[data-off="0"]')||document.querySelector('.res__case');
    const f=c.querySelector('.res__frame'), i=c.querySelector('img');
    const r=e=>{const b=e.getBoundingClientRect();return Math.round(b.width)+'x'+Math.round(b.height)};
    return {card:r(c), frame:r(f), img:r(i), ar:getComputedStyle(c).aspectRatio,
            flowH:Math.round(document.querySelector('.res__flow').getBoundingClientRect().height)};
  })));
  await p.close();
}
await b.close();
