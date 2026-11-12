/* QHUB HERBAL – site.js (không phụ thuộc thư viện) */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var fmt = function (n) { return n.toLocaleString('vi-VN') + 'đ'; };

  // Menu mobile
  var burger = $('.hdr__burger'), nav = $('#nav');
  if (burger) burger.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', open);
  });
  $$('#nav a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('is-open'); burger && burger.setAttribute('aria-expanded', false); }); });

  // Lọc sản phẩm theo nhu cầu
  $$('.chip').forEach(function (c) {
    c.addEventListener('click', function () {
      var f = c.getAttribute('data-filter');
      $$('.chip').forEach(function (x) { x.classList.toggle('is-on', x === c); x.setAttribute('aria-selected', x === c); });
      $$('#pgrid .card').forEach(function (card) { card.hidden = !(f === 'all' || card.getAttribute('data-cat') === f); });
    });
  });

  // Thư viện ảnh trang sản phẩm
  var main = $('#pdMain'), stage = $('#pdStage');
  $$('.pd__thumbs button').forEach(function (b) {
    b.addEventListener('click', function () {
      main.src = b.getAttribute('data-src');
      if (stage) stage.classList.toggle('is-photo', !!b.getAttribute('data-photo'));
      $$('.pd__thumbs button').forEach(function (x) { x.classList.toggle('is-on', x === b); });
    });
  });

  // Lọc bài viết (hỗ trợ ?c=thao-moc)
  function pfilter(f) {
    $$('[data-pfilter]').forEach(function (x) { var on = x.getAttribute('data-pfilter') === f; x.classList.toggle('is-on', on); x.setAttribute('aria-selected', on); });
    $$('#postgrid .post').forEach(function (p) { p.hidden = !(f === 'all' || p.getAttribute('data-cat') === f); });
  }
  $$('[data-pfilter]').forEach(function (c) { c.addEventListener('click', function () { pfilter(c.getAttribute('data-pfilter')); }); });
  var qc = (location.search.match(/[?&]c=([\w-]+)/) || [])[1];
  if (qc && location.pathname === '/kien-thuc/') location.replace('/kien-thuc/chu-de/' + qc + '/');

  // Lightbox ảnh
  var lb = $('#lb');
  if (lb) {
    $$('[data-lb]').forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); $('img', lb).src = a.getAttribute('href'); lb.classList.add('is-on'); });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.tagName === 'BUTTON') lb.classList.remove('is-on'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') lb.classList.remove('is-on'); });
  }

  // Thanh mua dính khi cuộn qua khung giá
  var sb = $('#stickyBuy'), bb = $('#buybox'), od = $('#dat-hang');
  if (sb && bb && 'IntersectionObserver' in window) {
    var past = false, inOrder = false;
    var upd = function () { sb.classList.toggle('is-on', past && !inOrder); };
    new IntersectionObserver(function (es) { past = !es[0].isIntersecting && es[0].boundingClientRect.top < 0; upd(); }).observe(bb);
    if (od) new IntersectionObserver(function (es) { inOrder = es[0].isIntersecting; upd(); }).observe(od);
  }

  function initOrder() {
  // ===== Form đặt hàng =====
  var form = $('#oform');
  if (!form) return null;
  var items = $$('.pick__item', form);

  function recalc() {
    var n = 0, kinds = 0;
    items.forEach(function (it) {
      var cb = $('input[type=checkbox]', it), q = $('.qty__n', it);
      if (cb.checked) { kinds++; n += Math.max(1, parseInt(q.value, 10) || 1); }
    });
    var g = Math.floor(n / 2);
    $('#osum').textContent = fmt(n * QH.price);
    $('#ocount').textContent = n ? (n + ' hộp' + (g ? ' + tặng ' + g + ' hộp = nhận ' + (n + g) + ' hộp' : '') + ' · tiết kiệm ' + fmt(n * (QH.list - QH.price) + g * QH.list) + ' so với giá niêm yết') : 'Chưa chọn sản phẩm';
    var hint = $('#ohint');
    if (hint) { hint.hidden = !(n % 2 === 1); hint.textContent = n === 1 ? 'Thêm 1 hộp nữa (loại nào cũng được) để được TẶNG 1 hộp bạn tự chọn.' : 'Thêm 1 hộp nữa để được tặng thêm 1 hộp.'; }
    renderGifts(g);
  }
  var gbox = $('#ogift', form), glist = $('#ogiftl', form), gtpl = $('#ogiftt', form);
  function firstPicked() { var c = $('.pick__item input[type=checkbox]:checked', form); return c ? c.value : null; }
  function renderGifts(g) {
    if (!gbox) return;
    gbox.hidden = !g; $('#ogiftn', form).textContent = g;
    var cur = $$('select', glist);
    while (cur.length > g) { glist.removeChild(cur.pop()); }
    while (cur.length < g) {
      var sel = gtpl.content.firstElementChild.cloneNode(true);
      var fp = firstPicked(); if (fp) sel.value = fp;
      glist.appendChild(sel); cur.push(sel);
    }
  }
  function giftLine() {
    if (!glist) return '';
    var c = {}; $$('select', glist).forEach(function (s) { c[s.value] = (c[s.value] || 0) + 1; });
    return Object.keys(c).map(function (k) { return k + ' x ' + c[k]; }).join(', ');
  }
  items.forEach(function (it) {
    var q = $('.qty__n', it);
    $$('.qty__b', it).forEach(function (b) {
      b.addEventListener('click', function (e) {
        e.preventDefault(); e.stopPropagation();
        q.value = Math.min(99, Math.max(1, (parseInt(q.value, 10) || 1) + parseInt(b.getAttribute('data-d'), 10)));
        recalc();
      });
    });
    q.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); q.focus(); });
    q.addEventListener('input', recalc);
    $('input[type=checkbox]', it).addEventListener('change', function () { $('[data-err=sp]', form).hidden = true; recalc(); });
  });

  function select(slugs, qty) {
    slugs.forEach(function (s) {
      var cb = $('input[data-slug="' + s + '"]', form);
      if (cb) { cb.checked = true; if (qty) { var q = $('.qty__n', cb.closest('.pick__item')); if (q) q.value = Math.max(parseInt(q.value, 10) || 1, qty); } }
    });
    recalc();
  }
  $$('[data-order]').forEach(function (a) {
    a.addEventListener('click', function () { select(a.getAttribute('data-order').split(','), parseInt(a.getAttribute('data-qty') || '0', 10)); });
  });
  recalc();
  window.QHselect = select;

  // Nguồn truy cập (UTM, trang đầu tiên)
  try {
    var qs = location.search;
    if (qs.indexOf('utm_') > -1 && !sessionStorage.getItem('qh_src')) sessionStorage.setItem('qh_src', qs.slice(1));
    if (!sessionStorage.getItem('qh_land')) sessionStorage.setItem('qh_land', location.pathname + ' | ref: ' + (document.referrer || 'trực tiếp'));
  } catch (e) {}

  function showErr(name, show) { var el = $('[data-err=' + name + ']', form); if (el) el.hidden = !show; var f = form.elements[name]; if (f && f.classList) f.classList.toggle('is-bad', show); }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var ten = form.ten.value.trim(), sdt = form.sdt.value.replace(/[\s.\-()]/g, ''), dc = form.diachi.value.trim();
    if (sdt.indexOf('+84') === 0) sdt = '0' + sdt.slice(3);
    var lines = [], n = 0;
    items.forEach(function (it) {
      var cb = $('input[type=checkbox]', it);
      if (cb.checked) { var q = Math.max(1, parseInt($('.qty__n', it).value, 10) || 1); n += q; lines.push(cb.value + ' x ' + q); }
    });
    var ok = true;
    showErr('sp', !lines.length); if (!lines.length) ok = false;
    showErr('ten', ten.length < 2); if (ten.length < 2) ok = false;
    var badPhone = !/^0\d{9}$/.test(sdt); showErr('sdt', badPhone); if (badPhone) ok = false;
    showErr('diachi', dc.length < 6); if (dc.length < 6) ok = false;
    var agree = form.dongy && form.dongy.checked; showErr('dongy', !agree); if (!agree) ok = false;
    if (!ok) { var first = $('.oform__err:not([hidden])', form); first && first.scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }
    if (form.website.value) return; // chặn bot

    var btn = $('#osubmit'), fail = $('#ofail');
    fail.hidden = true; btn.disabled = true; btn.textContent = 'Đang gửi đơn…';
    var src = ''; try { src = (sessionStorage.getItem('qh_land') || '') + (sessionStorage.getItem('qh_src') ? ' | ' + sessionStorage.getItem('qh_src') : ''); } catch (x) {}
    var sdtFmt = sdt.slice(0, 4) + ' ' + sdt.slice(4, 7) + ' ' + sdt.slice(7);
    var gl = giftLine(), gn = Math.floor(n / 2);
    var data = { ten: ten, sdt: sdtFmt, diachi: dc, sp: lines.join('; ') + (gl ? ' | TẶNG (mua 2 tặng 1): ' + gl : ''), tong: n + ' hộp – ' + fmt(n * QH.price) + (gn ? ' (+ tặng ' + gn + ' hộp)' : ''), nguon: location.pathname + (src ? ' | ' + src : '') };
    var body = new URLSearchParams();
    Object.keys(QH.fields).forEach(function (k) { if (data[k] !== undefined) body.append(QH.fields[k], data[k]); });

    if (!QH.formAction) { btn.disabled = false; btn.textContent = 'Gửi đơn đặt hàng'; fail.hidden = false; return; }
    var done = false;
    var timer = setTimeout(function () { if (!done) { done = true; btn.disabled = false; btn.textContent = 'Gửi đơn đặt hàng'; fail.hidden = false; } }, 15000);
    fetch(QH.formAction, { method: 'POST', mode: 'no-cors', body: body })
      .then(function () {
        if (done) return; done = true; clearTimeout(timer);
        try { sessionStorage.setItem('qh_last', JSON.stringify({ ten: ten, sp: gl ? lines.concat(['Quà tặng: ' + gl]) : lines, tong: data.tong })); } catch (x) {}
        if (window.gtag) { var its = lines.map(function (l) { var m = l.match(/^(.*) x (\d+)$/); return { item_name: m ? m[1] : l, quantity: m ? +m[2] : 1, price: QH.price }; }); gtag('event', 'generate_lead', { currency: 'VND', value: n * QH.price }); gtag('event', 'purchase', { transaction_id: 'W' + Date.now(), currency: 'VND', value: n * QH.price, items: its }); }
        location.href = '/cam-on/';
      })
      .catch(function () { if (done) return; done = true; clearTimeout(timer); btn.disabled = false; btn.textContent = 'Gửi đơn đặt hàng'; fail.hidden = false; });
  });
  }
  var slot = $('#order-slot');
  if (slot) {
    var pre = slot.getAttribute('data-pre');
    fetch('/assets/order.html?v=' + (QH.v || '')).then(function (r) { return r.text(); }).then(function (h) {
      var t = document.createElement('div'); t.innerHTML = h; var sec = t.firstElementChild; slot.parentNode.replaceChild(sec, slot);
      initOrder(); if (pre && window.QHselect) window.QHselect([pre]);
      if (location.hash === '#dat-hang') sec.scrollIntoView();
    }).catch(function () {});
  } else initOrder();
})();

// ===== Ẩn nút treo khi đang ở form đặt hàng =====
(function () {
  var f = document.querySelector('.fpromo'); if (!f || !('IntersectionObserver' in window)) return;
  var inOrder = false, top = true;
  var upd = function () { f.classList.toggle('is-hide', inOrder || top); };
  var onS = function () { top = window.scrollY < 500; upd(); }; window.addEventListener('scroll', onS, { passive: true }); onS();
  var watch = function () { var od = document.getElementById('dat-hang'); if (!od) return;
    new IntersectionObserver(function (es) { inOrder = es[0].isIntersecting; upd(); }, { threshold: 0.15 }).observe(od.closest('section') || od); };
  watch(); setTimeout(watch, 2500);
})();

// ===== Slider kiến thức tự lướt 5 giây =====
(function () {
  document.querySelectorAll('.ks').forEach(function (ks) {
    var tr = ks.querySelector('.ks__track'), ms = parseInt(ks.getAttribute('data-auto') || '5000', 10), paused = false, timer;
    var bar = document.createElement('div'); bar.className = 'ks__bar'; bar.innerHTML = '<i></i>'; ks.parentNode.insertBefore(bar, ks.nextSibling);
    var bi = bar.firstChild;
    function step(dir) {
      var card = tr.querySelector('.post'); if (!card) return;
      var w = card.getBoundingClientRect().width + parseFloat(getComputedStyle(tr).columnGap || 24);
      var max = tr.scrollWidth - tr.clientWidth - 4;
      if (dir > 0 && tr.scrollLeft >= max) tr.scrollTo({ left: 0 }); else if (dir < 0 && tr.scrollLeft <= 4) tr.scrollTo({ left: max }); else tr.scrollBy({ left: dir * w });
    }
    function restart() { clearInterval(timer); bi.classList.remove('run'); void bi.offsetWidth; if (!paused) { bi.classList.add('run'); timer = setInterval(function () { step(1); bi.classList.remove('run'); void bi.offsetWidth; bi.classList.add('run'); }, ms); } }
    ks.querySelector('.ks__next').addEventListener('click', function () { step(1); restart(); });
    ks.querySelector('.ks__prev').addEventListener('click', function () { step(-1); restart(); });
    ['mouseenter', 'focusin', 'touchstart'].forEach(function (ev) { ks.addEventListener(ev, function () { paused = true; restart(); }, { passive: true }); });
    ['mouseleave', 'focusout'].forEach(function (ev) { ks.addEventListener(ev, function () { paused = false; restart(); }); });
    ks.addEventListener('touchend', function () { setTimeout(function () { paused = false; restart(); }, 6000); }, { passive: true });
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) paused = true;
    restart();
  });
})();

// ===== Video YouTube (tự phát không tiếng khi cuộn tới) =====
(function () {
  document.querySelectorAll('.vbox[data-yt]').forEach(function (v) {
    var id = v.getAttribute('data-yt');
    function play(sound) { if (v.querySelector('iframe')) return; var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&mute=' + (sound ? 0 : 1) + '&loop=1&playlist=' + id + '&playsinline=1&rel=0&modestbranding=1';
      f.allow = 'autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen = true; f.title = 'Video vùng nguyên liệu QHUB HERBAL'; v.appendChild(f); }
    v.querySelector('.vbox__play').addEventListener('click', function () { play(true); });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es, o) { if (es[0].isIntersecting) { play(false); o.disconnect(); } }, { threshold: 0.5 }).observe(v);
  });
})();
