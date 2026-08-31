import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage({viewport:{width:1440,height:900}});
p.on('pageerror',e=>console.log('PAGE ERROR:', e.message));
await p.goto('http://localhost:8787/book/?procedure=rhinoplasty',{waitUntil:'networkidle'});
await p.click('#bNext');
await p.click('input[name=timing][value="3m"]');
await p.click('#bNext');
await p.click('#bNext');
await p.fill('#f-name','Tatiana');
await p.fill('#f-email','not-an-email');
await p.click('#bNext');
await p.fill('#f-email','t@example.com');
console.log('before:', await p.evaluate(()=>{
  const f=document.getElementById('bookForm');
  return { name:JSON.stringify(f.elements['name'].value), email:JSON.stringify(f.elements['email'].value),
    nameErr:!document.getElementById('e-name').hidden, emailErr:!document.getElementById('e-email').hidden };
}));
await p.click('#bNext');
console.log('after :', await p.evaluate(()=>({
  panel:[...document.querySelectorAll('.bpanel')].filter(x=>!x.hidden).map(x=>x.id),
  nameErr:!document.getElementById('e-name').hidden, emailErr:!document.getElementById('e-email').hidden })));
await b.close();
