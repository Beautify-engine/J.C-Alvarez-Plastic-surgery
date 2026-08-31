import { chromium } from 'playwright';
const b = await chromium.launch();

// --- 1. no-JS: every question reachable, one submit ---
const nojs = await b.newContext({javaScriptEnabled:false, viewport:{width:390,height:844}});
const p1 = await nojs.newPage();
await p1.goto('http://localhost:8787/book/',{waitUntil:'load'});
console.log('NO-JS visible panels:', await p1.locator('.bpanel:visible').count(),
            '| procedure inputs:', await p1.locator('input[name="procedure"]:visible').count(),
            '| submit visible:', await p1.locator('#bSend').isVisible(),
            '| Continue hidden:', !(await p1.locator('#bNext').isVisible()),
            '| brief hidden:', !(await p1.locator('#bBrief').isVisible()));
await nojs.close();

// --- 2. exclusive option ---
const ctx = await b.newContext({viewport:{width:1440,height:900}});
const p = await ctx.newPage();
await p.goto('http://localhost:8787/book/',{waitUntil:'networkidle'});
await p.click('label:has(input[value=\"tummy-tuck\"])');
await p.click('label:has(input[value=\"bbl\"])');
await p.click('label:has(input[value=\"not-sure\"])');
console.log('EXCLUSIVE after not-sure:', await p.$$eval('input[name="procedure"]:checked', n=>n.map(x=>x.value)));
await p.click('label:has(input[value=\"rhinoplasty\"])');
console.log('EXCLUSIVE after re-pick:', await p.$$eval('input[name="procedure"]:checked', n=>n.map(x=>x.value)));

// --- 2b. contextual proof follows the most recent selection ---
const clearProcs = async () => { for (const el of await p.$$('input[name="procedure"]:checked'))
  await p.click(`label:has(input[value="${await el.getAttribute('value')}"])`); };
const voice = async () => (await p.locator('.bvoice__q:visible footer span').first().textContent()).trim();
for (const [slug, expect] of [['rhinoplasty','Rhinoplasty + otoplasty'],
                              ['breast-augmentation','Breast augmentation'],
                              ['tummy-tuck','Liposuction'],
                              ['facelift','Consultation and follow-up']]) {
  await clearProcs();
  await p.click(`label:has(input[value="${slug}"])`);
  const got = await voice();
  console.log(`VOICE ${slug.padEnd(20)} -> ${got}   ${got===expect?'ok':'MISMATCH, expected '+expect}`);
}
await clearProcs();
await p.click('label:has(input[value="tummy-tuck"])');
await p.click('label:has(input[value="rhinoplasty"])');
console.log('VOICE tummy-tuck then rhinoplasty ->', await voice(), '(should follow the newest pick)');
console.log('visible quotes at any time:', await p.locator('.bvoice__q:visible').count());
await clearProcs();

// --- 3. validation blocks empty step (clearProcs above left nothing selected) ---
await p.click('#bNext');
console.log('BLOCKED on empty procedure:', await p.locator('#e-procedure').isVisible());

// --- 4. keyboard-only through the whole form ---
await p.click('label:has(input[value=\"facelift\"])');
await p.click('#bNext'); await p.click('label:has(input[value=\"asap\"])'); await p.click('#bNext');
await p.fill('#f-name','Ana Duarte'); await p.fill('#f-email','ana@example.com');
await p.keyboard.press('Enter');   // Enter should advance, not submit
await p.waitForTimeout(300);
console.log('ENTER advanced to review:', await p.locator('#p4').isVisible(),
            '| form still present:', await p.locator('#bookForm').isVisible());

// --- 5. edit link jumps back ---
await p.locator('.breview__edit').first().click();
await p.waitForTimeout(250);
console.log('EDIT jumped to step 1:', await p.locator('#p1').isVisible());

// --- 6. save & resume across a reload ---
await p.reload({waitUntil:'networkidle'});
await p.waitForTimeout(400);
console.log('RESUMED procedure:', await p.$$eval('input[name="procedure"]:checked', n=>n.map(x=>x.value)),
            '| name:', await p.inputValue('#f-name'),
            '| notice shown:', await p.locator('#bResume').isVisible());
await p.click('#bClear'); await p.waitForTimeout(200);
console.log('AFTER start over:', await p.$$eval('input[name="procedure"]:checked', n=>n.map(x=>x.value)),
            '| name:', JSON.stringify(await p.inputValue('#f-name')));

// --- 7. ?procedure= deep link beats a stored draft ---
await p.goto('http://localhost:8787/book/?procedure=bbl&utm_source=instagram',{waitUntil:'networkidle'});
await p.waitForTimeout(300);
console.log('DEEP LINK:', await p.$$eval('input[name="procedure"]:checked', n=>n.map(x=>x.value)),
            '| source:', await p.inputValue('#fSource'));
await b.close();
