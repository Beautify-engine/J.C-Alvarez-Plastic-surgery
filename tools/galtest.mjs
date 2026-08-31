import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:1000},deviceScaleFactor:1})).newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('http://localhost:8787/results.html',{waitUntil:'networkidle'});
await p.waitForTimeout(800);

const base = await p.evaluate(()=>({
  h1: document.querySelectorAll('h1').length,
  cases: document.querySelectorAll('.gal__i').length,
  visible: [...document.querySelectorAll('.gal__i')].filter(e=>!e.hidden).length,
  filters: document.querySelectorAll('.gal__filters button').length,
  count: document.querySelector('.gal__count').textContent,
  firstProc: document.querySelector('.gal__i').dataset.procedure,
  overflow: document.documentElement.scrollWidth>document.documentElement.clientWidth,
}));
console.log('load  ', JSON.stringify(base));

// filter
await p.click('.gal__filters button[data-filter="rhinoplasty"]');
await p.waitForTimeout(300);
console.log('filter', JSON.stringify(await p.evaluate(()=>({
  visible: [...document.querySelectorAll('.gal__i')].filter(e=>!e.hidden).length,
  allRhino: [...document.querySelectorAll('.gal__i')].filter(e=>!e.hidden).every(e=>e.dataset.procedure==='rhinoplasty'),
  count: document.querySelector('.gal__count').textContent,
  url: location.search,
  pressed: document.querySelector('[data-filter="rhinoplasty"]').getAttribute('aria-pressed'),
}))));

// deep link
await p.goto('http://localhost:8787/results.html?p=facelift',{waitUntil:'networkidle'});
await p.waitForTimeout(500);
console.log('deep  ', JSON.stringify(await p.evaluate(()=>({
  visible: [...document.querySelectorAll('.gal__i')].filter(e=>!e.hidden).length,
  count: document.querySelector('.gal__count').textContent,
}))));

// viewer
await p.goto('http://localhost:8787/results.html',{waitUntil:'networkidle'});
await p.waitForTimeout(500);
await p.click('.gal__c');
await p.waitForTimeout(400);
console.log('viewer', JSON.stringify(await p.evaluate(()=>({
  open: document.getElementById('lb').open,
  title: document.getElementById('lbTitle').textContent,
  imgLoaded: document.getElementById('lbImg').naturalWidth>0,
  src: document.getElementById('lbImg').src.split('/').pop(),
}))));
await p.keyboard.press('Escape'); await p.waitForTimeout(300);
console.log('esc   ', JSON.stringify(await p.evaluate(()=>({open: document.getElementById('lb').open}))));
console.log('errors:', errs.length?errs.slice(0,3):'none');
await b.close();
