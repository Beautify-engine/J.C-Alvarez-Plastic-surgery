import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8787/',{waitUntil:'domcontentloaded'});
await p.waitForTimeout(120);
const early=await p.evaluate(()=>{
  const h=document.querySelector('.hero h1 .ln');
  return {opacity:getComputedStyle(h).opacity, anim:getComputedStyle(h).animationName};
});
await p.waitForTimeout(1600);
const late=await p.evaluate(()=>getComputedStyle(document.querySelector('.hero h1 .ln')).opacity);
console.log('hero line at 120ms:', JSON.stringify(early));
console.log('hero line at 1.7s :', late);
await p.evaluate(()=>window.scrollTo(0,1600)); await p.waitForTimeout(900);
const revealed=await p.evaluate(()=>document.querySelectorAll('[data-rise].in,[data-rise-group].in').length);
console.log('revealed on scroll:', revealed, 'of', await p.evaluate(()=>document.querySelectorAll('[data-rise],[data-rise-group]').length));
const grain=await p.evaluate(()=>getComputedStyle(document.querySelector('.hero'),'::after').opacity);
console.log('grain layer opacity:', grain);
await b.close();
