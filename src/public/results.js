/* /results — procedure filtering and the case viewer.
   No dependency: filtering is a class toggle, the viewer is a native <dialog>,
   which gives focus trapping and Esc-to-close for free (§6, no library >15kb). */
(function () {
  var grid = document.getElementById('galGrid');
  if (!grid) return;

  var items   = Array.prototype.slice.call(grid.querySelectorAll('.gal__i'));
  var buttons = Array.prototype.slice.call(document.querySelectorAll('.gal__filters button'));
  var count   = document.querySelector('.gal__count');
  var total   = items.length;

  function apply(filter) {
    var shown = 0;
    items.forEach(function (li) {
      var hit = filter === 'all' || li.dataset.procedure === filter;
      li.hidden = !hit;
      if (hit) shown++;
    });
    buttons.forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.filter === filter));
    });
    var label = buttons.filter(function (b) { return b.dataset.filter === filter; })[0];
    var name  = label ? label.firstChild.textContent.trim() : '';
    count.textContent = filter === 'all'
      ? 'Showing all ' + total + ' cases'
      : 'Showing ' + shown + ' ' + name + (shown === 1 ? ' case' : ' cases');
    // keep the filter in the URL so a procedure view can be linked and shared
    var url = new URL(window.location.href);
    if (filter === 'all') url.searchParams.delete('p'); else url.searchParams.set('p', filter);
    history.replaceState(null, '', url);
  }

  buttons.forEach(function (b) {
    b.addEventListener('click', function () { apply(b.dataset.filter); });
  });

  var start = new URL(window.location.href).searchParams.get('p');
  if (start && buttons.some(function (b) { return b.dataset.filter === start; })) apply(start);

  /* ---- case viewer ---- */
  var lb = document.getElementById('lb');
  if (!lb || !lb.showModal) return;          // no <dialog>: cards stay inert, grid still works
  var lbImg = document.getElementById('lbImg'),
      lbT = document.getElementById('lbTitle');

  grid.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('.gal__c');
    if (!btn) return;
    var thumb = btn.querySelector('img');
    // the grid shows a 600px copy; the viewer loads his full-size slide
    lbImg.src = btn.dataset.full || thumb.src;
    lbImg.alt = thumb.alt;
    lbT.textContent = btn.querySelector('.gal__proc').textContent + ' · case '
                    + btn.querySelector('.gal__n').textContent;
    lb.showModal();
  });

  lb.addEventListener('click', function (e) {
    // backdrop click, and the explicit close button
    if (e.target === lb || (e.target.closest && e.target.closest('[data-lb-close]'))) lb.close();
  });
})();
