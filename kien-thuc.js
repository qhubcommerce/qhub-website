(function () {
  "use strict";
  var header = document.querySelector(".site-header"), toggle = document.querySelector(".menu-toggle");
  if (toggle) toggle.addEventListener("click", function () {
    var open = header.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
  var q = document.getElementById("kt-q"), list = document.getElementById("kt-list");
  if (q && list) {
    var norm = function (s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d"); };
    var cards = Array.prototype.slice.call(list.querySelectorAll(".kt-card"));
    q.addEventListener("input", function () {
      var v = norm(q.value.trim());
      cards.forEach(function (c) { c.hidden = v && norm(c.textContent).indexOf(v) < 0; });
    });
  }
})();
