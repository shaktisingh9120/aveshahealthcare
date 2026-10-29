/* Medora RCM — shared interactions */
(function(){
  const $ = (s, r=document) => r.querySelector(s);
  const $$ = (s, r=document) => [...r.querySelectorAll(s)];

  /* Mobile menu */
  const header = $(".header"), burger = $(".burger");
  if (burger) burger.addEventListener("click", () => { const open = header.classList.toggle("open"); burger.setAttribute("aria-expanded", open); });
  $$(".nav-item > .nav-link[data-drop]").forEach(btn => btn.addEventListener("click", e => {
    if (!header.classList.contains("open")) return; // desktop uses hover/focus
    e.preventDefault(); const item = btn.parentElement; const ex = item.classList.toggle("expanded"); btn.setAttribute("aria-expanded", ex);
  }));
  document.addEventListener("keydown", e => { if (e.key === "Escape"){ header?.classList.remove("open"); closeModals(); } });

  /* Counters */
  const counters = $$("[data-count]");
  const run = el => { const end = +el.dataset.count, suf = el.dataset.suffix || "", dur = 1400, t0 = performance.now();
    const step = t => { const k = Math.min(1, (t - t0) / dur); el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3))).toLocaleString("en-US") + suf; if (k < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step); };
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if ("IntersectionObserver" in window && !reduce){
    const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting){ run(en.target); io.unobserve(en.target); } }), {threshold:.4});
    counters.forEach(c => io.observe(c));
    const rv = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting){ en.target.classList.add("in"); rv.unobserve(en.target); } }), {threshold:.12});
    $$(".reveal").forEach(el => { const r = el.getBoundingClientRect(); if (r.top > innerHeight){ el.classList.add("anim"); rv.observe(el); } });
  }

  /* Revenue calculator */
  const calc = $("#calc");
  if (calc){
    const f = n => "$" + Math.round(n).toLocaleString("en-US");
    const upd = () => {
      const rev = +$("#c-rev").value * 1e6, den = +$("#c-den").value, fpy = +$("#c-fpy").value, ar = +$("#c-ar").value;
      $("#o-rev").textContent = "$" + (+$("#c-rev").value).toLocaleString("en-US") + "M"; $("#o-den").textContent = den + "%"; $("#o-fpy").textContent = fpy + "%"; $("#o-ar").textContent = ar + " days";
      // Illustrative model: recover 35% of excess denials above 5%, cut leakage tied to first-pass gaps, speed cash for A/R above 35 days
      const denials = rev * Math.max(0, den - 5) / 100 * 0.35;
      const leakage = rev * Math.max(0, 95 - fpy) / 100 * 0.12;
      const cash = rev / 365 * Math.max(0, ar - 35) * 0.5;
      $("#r-den").textContent = f(denials); $("#r-leak").textContent = f(leakage); $("#r-cash").textContent = f(cash); $("#r-total").textContent = f(denials + leakage);
    };
    $$("input", calc).forEach(i => i.addEventListener("input", upd)); upd();
  }

  /* Filters (resources, careers) */
  $$("[data-filter-group]").forEach(group => {
    const target = $(group.dataset.filterGroup);
    group.addEventListener("click", e => {
      const chip = e.target.closest(".chip"); if (!chip) return;
      $$(".chip", group).forEach(c => c.setAttribute("aria-pressed", c === chip));
      const v = chip.dataset.f; let shown = 0;
      $$("[data-cat]", target).forEach(it => { const ok = v === "all" || it.dataset.cat.split(" ").includes(v); it.hidden = !ok; if (ok) shown++; });
      const empty = $("[data-empty]", target.parentElement); if (empty) empty.hidden = shown > 0;
    });
  });
  const search = $("#job-search");
  if (search) search.addEventListener("input", () => { const q = search.value.toLowerCase(); $$(".job").forEach(j => j.hidden = !j.textContent.toLowerCase().includes(q)); });

  /* Modals */
  function closeModals(){ $$(".modal.open").forEach(m => m.classList.remove("open")); }
  $$("[data-modal]").forEach(b => b.addEventListener("click", e => { e.preventDefault(); const m = $(b.dataset.modal); if (!m) return; const role = b.dataset.role; if (role){ const sel = $("select[name=role]", m); if (sel) sel.value = role; } m.classList.add("open"); setTimeout(() => $("input,select,textarea", m)?.focus(), 30); }));
  $$(".modal").forEach(m => m.addEventListener("click", e => { if (e.target === m || e.target.closest(".modal-x")) closeModals(); }));

  /* Forms: no backend in this template — show a confirmation */
  $$("form.form").forEach(f => f.addEventListener("submit", e => {
    e.preventDefault(); if (!f.checkValidity()){ f.reportValidity(); return; }
    const ok = $(".form-ok", f); if (ok){ ok.classList.add("show"); ok.textContent = f.dataset.ok || "Thank you. We'll be in touch within one business day."; }
    f.reset();
  }));

  /* Back to top */
  const tt = $(".to-top");
  if (tt){ addEventListener("scroll", () => tt.classList.toggle("show", scrollY > 700), {passive:true}); tt.addEventListener("click", () => scrollTo({top:0, behavior: reduce ? "auto" : "smooth"})); }

  const yr = $("#yr"); if (yr) yr.textContent = new Date().getFullYear();
})();
