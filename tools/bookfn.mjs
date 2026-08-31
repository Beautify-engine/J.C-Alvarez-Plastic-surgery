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
await p.click('input[value="tummy-tuck"] + .bopt__box');
await p.click('input[value="bbl"] + .bopt__box');
await p.click('input[value="not-sure"] + .bopt__box');
console.log('EXCLUSIVE after not-sure:', await p.$$eval('input[name="procedure"]:checked', n=>n.map(x=>x.value)));
await p.click('input[value="rhinoplasty"] + .bopt__box');
console.log('EXCLUSIVE after re-pick:', await p.$$eval('input[name="procedure"]:checked', n=>n.map(x=>x.value)));

// --- 3. validation blocks empty step ---
await p.click('input[value="rhinoplasty"] + .bopt__box'); // uncheck -> none
await p.click('#bNext');
console.log('BLOCKED on empty procedure:', await p.locator('#e-procedure').isVisible());

// --- 4. keyboard-only through the whole form ---
await p.click('input[value="facelift"] + .bopt__box');
await p.click('#bNext'); await p.click('input[value="asap"] + .bopt__box'); await p.click('#bNext');
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
