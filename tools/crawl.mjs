/* Walks every internal link and asset reference from the homepage outward and
   reports what does not resolve. Run it before claiming any page is finished —
   the .html-suffixed checks the other tools use never touch a real link. */
import { chromium } from 'playwright';
const BASE = process.argv[2] || 'http://localhost:8787';
const b = await chromium.launch();
const ctx = await b.newContext({viewport:{width:1280,height:900}});
const seen = new Set(), queue = ['/'], badLinks = new Map(), badAssets = new Map(), consoleErrs = new Map();
const status = async u => (await ctx.request.get(BASE+u, {maxRedirects:5})).status();

while (queue.length) {
  const path = queue.shift();
  if (seen.has(path)) continue;
  seen.add(path);
  const p = await ctx.newPage();
  const failed = [];
  p.on('response', r => { if (r.status() >= 400) failed.push(`${r.status()} ${r.url().replace(BASE,'')}`); });
  p.on('pageerror', e => { const a = consoleErrs.get(path)||[]; a.push(String(e).split('\n')[0]); consoleErrs.set(path,a); });
  let resp;
  try { resp = await p.goto(BASE+path, {waitUntil:'networkidle', timeout:30000}); }
  catch (e) { badLinks.set(path, 'NAV FAIL'); await p.close(); continue; }
  if (!resp || resp.status() >= 400) badLinks.set(path, String(resp && resp.status()));
  const hrefs = await p.$$eval('a[href]', as => as.map(a => a.getAttribute('href')));
  await p.close();
  if (failed.length) badAssets.set(path, [...new Set(failed)]);
  for (const h of hrefs) {
    if (!h || h.startsWith('#') || /^(https?:|mailto:|tel:|javascript:)/.test(h)) continue;
    const u = new URL(h, BASE+path).pathname;
    if (!seen.has(u) && !queue.includes(u)) queue.push(u);
  }
}
console.log(`crawled ${seen.size} pages\n`);
const dump = (t,m) => { if (!m.size) return console.log(`✓ ${t}: none`);
  console.log(`✗ ${t}:`); for (const [k,v] of m) console.log(`   ${k}\n      ${[].concat(v).join('\n      ')}`); };
// which pages link to each dead route
const dead = [...badLinks.keys()];
if (dead.length) {
  const refs = new Map();
  for (const path of seen) {
    const p = await ctx.newPage();
    try { await p.goto(BASE+path,{waitUntil:'domcontentloaded',timeout:20000});
      const hs = await p.$$eval('a[href]', as=>as.map(a=>a.getAttribute('href')));
      for (const h of hs) { if(!h) continue; try{ const u=new URL(h,BASE+path).pathname;
        if (dead.includes(u)) { const s=refs.get(u)||new Set(); s.add(path); refs.set(u,s);} }catch{} }
    } catch {} finally { await p.close(); }
  }
  console.log('✗ dead routes, and what links to them:');
  for (const [u,s] of refs) console.log(`   ${u}  (${badLinks.get(u)})  ← linked from ${[...s].join(', ')}`);
} else console.log('✓ dead routes: none');
dump('pages with failing sub-resources', badAssets);
dump('pages throwing JS errors', consoleErrs);
await b.close();
