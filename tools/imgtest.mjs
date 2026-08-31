import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('http://localhost:8787/carousels.html');
const r = await p.evaluate(async () => {
  const out = [];
  for (const u of ['/img/procedures/bbl-600.jpg','/img/procedures/bbl-1200.jpg','/img/hero-poster.jpg']) {
    const i = new Image();
    await new Promise(res => { i.onload = res; i.onerror = res; i.src = u; });
    out.push({u, nw:i.naturalWidth, nh:i.naturalHeight});
  }
  return out;
});
console.log(JSON.stringify(r,null,1));
await b.close();
