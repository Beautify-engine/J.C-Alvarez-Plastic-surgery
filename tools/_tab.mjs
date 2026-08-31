import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [w,h,name] of [[1440,900,'desktop'],[390,844,'iPhone']]) {
  const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
  await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
  await p.waitForTimeout(400);
  await p.evaluate(()=>document.querySelector('input[name="procedure"]').focus());
  let hidden=0, checked=0;
  for (let i=0;i<11;i++){
    await p.keyboard.press('Tab'); await p.waitForTimeout(140);
    const r = await p.evaluate(()=>{
      const a=document.activeElement; if(!a||a.name!=='procedure') return null;
      const card=a.closest('.pcard'); if(!card) return null;
      const b=card.getBoundingClientRect(), bar=document.querySelector('.bnav').getBoundingClientRect();
      return {covered: b.bottom > bar.top && b.top < bar.bottom, label:a.value};
    });
    if(r){ checked++; if(r.covered){hidden++; console.log('   covered:', r.label);} }
  }
  console.log(`${name}: ${checked} cards tabbed, ${hidden} hidden behind the sticky bar`);
  await p.context().close();
}
await b.close();
