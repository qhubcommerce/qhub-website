(function () {
  "use strict";
  var H = window.QHUB_HERBAL || { products: [] };
  var C = window.QHUB_CONTACT || {};
  var vnd = function (n) { return n.toLocaleString("vi-VN") + "đ"; };
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* Mobile menu */
  var header = $(".site-header"), toggle = $(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$(".nav a").forEach(function (a) {
      a.addEventListener("click", function () { header.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); });
    });
  }

  /* Pain checklist */
  var pains = $("#pains");
  if (pains) {
    var res = $("#pain-result"), txt = $("#pain-text");
    pains.addEventListener("change", function () {
      var n = $$("input:checked", pains).length;
      if (n === 0) { txt.textContent = "Chọn những ô đúng với anh chị."; res.classList.remove("on"); }
      else if (n < 3) { txt.textContent = "Đã chọn " + n + " vấn đề. Doanh nghiệp đang có điểm nghẽn cần xử lý sớm."; res.classList.remove("on"); }
      else { txt.textContent = "Đã chọn " + n + " vấn đề. Đây là lúc nên nhìn lại cả hệ thống bán hàng."; res.classList.add("on"); }
    });
  }

  /* Tiers tabs */
  var tabs = $$('.tier-list [role="tab"]');
  if (tabs.length) {
    var select = function (t) {
      tabs.forEach(function (x) {
        var on = x === t;
        x.setAttribute("aria-selected", on ? "true" : "false");
        x.tabIndex = on ? 0 : -1;
        document.getElementById(x.getAttribute("aria-controls")).hidden = !on;
      });
    };
    tabs.forEach(function (t, i) {
      t.tabIndex = t.getAttribute("aria-selected") === "true" ? 0 : -1;
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var k = e.key, j = null;
        if (k === "ArrowDown" || k === "ArrowLeft") j = (i - 1 + tabs.length) % tabs.length; // list is visually reversed
        if (k === "ArrowUp" || k === "ArrowRight") j = (i + 1) % tabs.length;
        if (j !== null) { e.preventDefault(); select(tabs[j]); tabs[j].focus(); }
      });
    });
  }

  /* Image with graceful placeholder */
  function img(src, alt) {
    var el = document.createElement("img");
    el.src = src; el.alt = alt; el.loading = "lazy"; el.decoding = "async";
    el.onerror = function () { el.remove(); };
    return el;
  }

  /* Product cards (trang chủ + trang thương hiệu) */
  var grid = $("#product-grid");
  if (grid) {
    var pct = Math.round((1 - H.price / H.priceOld) * 100);
    H.products.forEach(function (p) {
      var art = document.createElement("article");
      art.className = "product"; art.id = p.id;
      art.style.setProperty("--pc", p.color); art.style.setProperty("--pt", p.tint);
      art.innerHTML =
        '<a class="pimg" href="' + p.slug + '"><span class="badge">Mua 2 tặng 1</span></a>' +
        '<div class="pbody"><p class="tag"></p><h3><a href="' + p.slug + '"></a></h3><p class="ing"></p><p class="desc"></p>' +
        '<div class="price"><span class="now">' + vnd(H.price) + '</span><span class="old">' + vnd(H.priceOld) + '</span><span class="off">-' + pct + '%</span></div>' +
        '<div class="row"><button class="btn btn-forest" type="button" data-buy="' + p.id + '">Mua ngay</button><a class="btn btn-line" href="' + p.slug + '">Xem chi tiết</a></div></div>';
      $(".pimg", art).appendChild(img("p-" + p.id + ".jpg", "Hộp " + p.name + " QHUB HERBAL"));
      $(".tag", art).textContent = p.tagline;
      $("h3 a", art).textContent = p.name;
      $(".ing", art).textContent = p.ing.length + " vị: " + p.ing.join(", ").replace(/ \d+%/g, "");
      $(".desc", art).textContent = p.desc;
      grid.appendChild(art);
    });
  }

  /* Trang chi tiết: gallery + số lượng */
  var gal = $(".pd-gallery");
  if (gal) {
    var main = $(".pd-main img", gal), thumbs = $$(".pd-thumbs button", gal);
    thumbs.forEach(function (b) {
      b.addEventListener("click", function () {
        thumbs.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        main.src = b.getAttribute("data-src"); main.alt = b.getAttribute("data-alt");
      });
    });
  }
  var pq = $("#pd-qty");
  if (pq) {
    var clampQ = function () { pq.value = Math.max(1, Math.min(99, parseInt(pq.value, 10) || 1)); updPd(); };
    var updPd = function () {
      var q = parseInt(pq.value, 10) || 1, g = Math.floor(q / H.giftEvery);
      $("#pd-calc").textContent = "Nhận " + (q + g) + " hộp" + (g ? " (tặng " + g + ")" : "") + " · Tạm tính " + vnd(q * H.price);
    };
    $("#pd-minus").addEventListener("click", function () { pq.value = (parseInt(pq.value, 10) || 1) - 1; clampQ(); });
    $("#pd-plus").addEventListener("click", function () { pq.value = (parseInt(pq.value, 10) || 1) + 1; clampQ(); });
    pq.addEventListener("change", clampQ); pq.addEventListener("input", updPd); updPd();
  }

  /* Order modal */
  var modal = $("#order-modal");
  if (modal) {
    var form = $("#order-form"), sel = $("#o-product"), qty = $("#o-qty"), msg = $("#order-msg");
    H.products.forEach(function (p) {
      var o = document.createElement("option"); o.value = p.name; o.textContent = p.name; o.dataset.id = p.id; sel.appendChild(o);
    });
    var lastFocus = null;
    var calc = function () {
      var q = Math.max(1, Math.min(99, parseInt(qty.value, 10) || 1));
      qty.value = q;
      var gift = Math.floor(q / H.giftEvery);
      $("#s-qty").textContent = q + " hộp × " + vnd(H.price);
      $("#s-gift").textContent = gift > 0 ? "+" + gift + " hộp" : "Mua thêm " + (H.giftEvery - q % H.giftEvery) + " hộp để được tặng 1";
      $("#s-get").textContent = (q + gift) + " hộp";
      $("#s-total").textContent = vnd(q * H.price);
      $("#f-gift").value = gift + " hộp"; $("#f-total").value = vnd(q * H.price); $("#f-get").value = (q + gift) + " hộp";
    };
    var open = function (id, q) {
      lastFocus = document.activeElement;
      $$("option", sel).forEach(function (o) { if (o.dataset.id === id) sel.value = o.value; });
      qty.value = q || 2; calc(); msg.textContent = ""; msg.className = "msg";
      modal.classList.add("open"); document.body.style.overflow = "hidden";
      setTimeout(function () { sel.focus(); }, 30);
    };
    var close = function () {
      modal.classList.remove("open"); document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    };
    document.addEventListener("click", function (e) {
      var b = e.target.closest("[data-buy]");
      if (b) { e.preventDefault(); var qi = b.getAttribute("data-qty") ? $(b.getAttribute("data-qty")) : null; open(b.getAttribute("data-buy"), qi ? parseInt(qi.value, 10) : 2); }
    });
    $$("[data-close]", modal).forEach(function (b) { b.addEventListener("click", close); });
    modal.addEventListener("click", function (e) { if (e.target === modal) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("open")) close(); });
    $("#q-minus").addEventListener("click", function () { qty.value = (parseInt(qty.value, 10) || 1) - 1; calc(); });
    $("#q-plus").addEventListener("click", function () { qty.value = (parseInt(qty.value, 10) || 1) + 1; calc(); });
    qty.addEventListener("input", calc);
    submitForm(form, msg, "Đã nhận đơn. QHUB sẽ gọi xác nhận trong giờ làm việc. Đơn được miễn phí giao hàng và thanh toán khi nhận hàng.", function () { form.reset(); calc(); });
  }

  /* Lead form */
  var lead = $("#lead-form");
  if (lead) submitForm(lead, $("#lead-msg"), "Đã gửi đăng ký. QHUB sẽ gọi lại cho anh chị trong giờ làm việc.", function () { lead.reset(); });

  function submitForm(form, msgEl, okText, done) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var bad = $$("[required]", form).filter(function (i) { return i.type === "checkbox" ? !i.checked : !i.value.trim(); });
      if (bad.length) { msgEl.textContent = bad[0].type === "checkbox" ? "Vui lòng tích ô đồng ý với Chính sách bảo mật." : "Vui lòng điền đủ các ô bắt buộc."; msgEl.className = msgEl.className.replace(/ ?(ok|err)/g, "") + " err"; bad[0].focus(); return; }
      var phone = $('[type="tel"]', form);
      if (phone && !/^[0-9 +().-]{9,15}$/.test(phone.value.trim())) { msgEl.textContent = "Số điện thoại chưa đúng. Vui lòng kiểm tra lại."; msgEl.className = msgEl.className.replace(/ ?(ok|err)/g, "") + " err"; phone.focus(); return; }
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = data[k] ? data[k] + ", " + v : v; });
      var btn = $('[type="submit"]', form); var label = btn.textContent;
      btn.disabled = true; btn.textContent = "Đang gửi…";
      fetch(C.formEndpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false" || j.success === false) throw new Error(j.message || "send failed"); }); })
        .then(function () { msgEl.textContent = okText; msgEl.className = msgEl.className.replace(/ ?(ok|err)/g, "") + " ok"; done(); })
        .catch(function () { msgEl.innerHTML = 'Chưa gửi được. Vui lòng gọi <a href="tel:' + C.phone + '">' + C.phoneText + '</a> hoặc nhắn Zalo để được hỗ trợ ngay.'; msgEl.className = msgEl.className.replace(/ ?(ok|err)/g, "") + " err"; })
        .then(function () { btn.disabled = false; btn.textContent = label; });
    });
  }
})();
