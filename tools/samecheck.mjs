import { chromium } from 'playwright';
const probe = async (p) => p.evaluate(() => {
  const g = (sel, prop) => { const e = document.querySelector(sel); return e ? getComputedStyle(e)[prop] : null; };
  const box = sel => { const e = document.querySelector(sel); if(!e) return null;
    const b = e.getBoundingClientRect(); return Math.round(b.width)+'x'+Math.round(b.height); };
  return {
    h1font:  g('h1','fontFamily').split(',')[0],
    h1size:  g('h1','fontSize'),
    bodyfont:g('.hA__who, .res__lede, p','fontFamily').split(',')[0],
    bodysize:g('.res__lede','fontSize'),
    heroBox: box('.hA'),
    resBg:   g('.res','backgroundColor'),
    aboutBg: g('.about','backgroundColor'),
    accent:  getComputedStyle(document.documentElement).getPropertyValue('--accent-light').trim(),
    sections:[...document.querySelectorAll('section')].map(s=>s.className.split(' ')[0]).join('>'),
    reviews: document.querySelectorAll('.rev__q').length,
    cases:   document.querySelectorAll('.res__case').length,
  };
});
const b = await chromium.launch();
for (const [w,h,tag] of [[1440,900,'desktop'],[390,844,'mobile']]) {
  const out = {};
  for (const [n,url] of [['dev','http://localhost:8787/'],['ghl','http://localhost:8787/_x/home.html']]) {
    const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
    await p.goto(url,{waitUntil:'networkidle'}); await p.waitForTimeout(1800);
    out[n] = await probe(p); await p.close();
  }
  const diff = Object.keys(out.dev).filter(k=>JSON.stringify(out.dev[k])!==JSON.stringify(out.ghl[k]));
  console.log(`\n${tag}`);
  console.log('  dev', JSON.stringify(out.dev));
  console.log('  ghl', JSON.stringify(out.ghl));
  console.log(diff.length ? '  ✗ DIFFERS: '+diff.join(', ') : '  ✓ identical');
}
await b.close();
