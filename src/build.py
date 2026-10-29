#!/usr/bin/env python3
"""Builds the Medora RCM static site: shared header/footer + 6 pages."""
import os, html
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
BRAND = "Medora"
TAG = "RCM"

ICON = {
 "brain":'<path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V4.5A2.5 2.5 0 0 0 9 4zM15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
 "pulse":'<path d="M3 12h4l3-8 4 16 3-8h4"/>',
 "chart":'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "shield":'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "steth":'<path d="M6 3v6a5 5 0 0 0 10 0V3"/><path d="M11 14v2a5 5 0 0 0 10 0v-2"/><circle cx="21" cy="12" r="2"/>',
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "bed":'<path d="M3 18V6M3 13h18v5M21 13a4 4 0 0 0-4-4h-6v4"/><circle cx="7" cy="10" r="2"/>',
 "chair":'<circle cx="10" cy="5" r="2"/><path d="M10 8v6h6l3 5M10 11h5"/><path d="M7 11a6 6 0 1 0 9 7"/>',
 "hosp":'<path d="M4 21V5h16v16M9 21v-4h6v4M12 8v5M9.5 10.5h5"/>',
 "map":'<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 "link":'<path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>',
 "doc":'<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
 "check":'<path d="M5 12l4 4 10-10"/>',
 "users":'<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0M16 4a3 3 0 0 1 0 6M21 20a6 6 0 0 0-4-5.6"/>',
 "bolt":'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "chat":'<path d="M21 12a8 8 0 0 1-12 7l-5 1 1-4a8 8 0 1 1 16-4z"/>',
 "cloud":'<path d="M7 18a5 5 0 1 1 1-9.9A6 6 0 0 1 19 9a4.5 4.5 0 0 1-1 9z"/>',
 "award":'<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/>',
 "heart":'<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"/>',
 "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 "grad":'<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "lock":'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 "money":'<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/>',
}
def ic(name): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
ARROW = '<span aria-hidden="true">→</span>'

NAV = [
 ("index.html","Home",[]),
 ("about.html","About",[("about.html#overview","Company overview"),("about.html#journey","Our journey"),("about.html#awards","Awards & recognition"),("about.html#leadership","Leadership")]),
 ("specialties.html","Specialities",[("specialties.html#anesthesia","Anesthesia"),("specialties.html#dme","DME & HME"),("specialties.html#eye","Eye care"),("specialties.html#hospitals","Hospitals & health systems"),("specialties.html#practices","Practices & ASCs"),("specialties.html#rural","Rural health services"),("specialties.html#partners","Channel partners"),("specialties.html#services","Services: front to back end")]),
 ("platforms.html","Platforms & AI",[("platforms.html#ai","AI capabilities"),("platforms.html#agents","AI agents"),("platforms.html#platforms","Platforms"),("platforms.html#integrations","Integrations"),("platforms.html#security","Security & compliance")]),
 ("resources.html","Resources",[("resources.html#all","All resources"),("resources.html?f=article#all","Articles & blogs"),("resources.html?f=case#all","Case studies"),("resources.html?f=news#all","News & press"),("resources.html?f=event#all","Upcoming events")]),
 ("careers.html","Careers",[]),
]

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Outfit:wght@500;600;700&display=swap">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
'''

def logo(footer=False):
    # Footer sits on a dark background, so the white-background logo gets a white tile there.
    style = ' style="background:#fff;border-radius:12px;padding:6px;display:inline-block"' if footer else ''
    return f'<a class="logo" href="index.html" aria-label="Avesha Healthcare home"{style}><img src="assets/logo.png" alt="Avesha Healthcare" width="634" height="504" style="height:104px;width:auto;display:block"></a>'

def header(active):
    items = []
    for href, label, sub in NAV:
        cur = ' aria-current="page"' if href == active else ''
        if sub:
            drop = "".join(f'<a href="{h}">{html.escape(t)}</a>' for h, t in sub)
            items.append(f'<div class="nav-item"><a class="nav-link" href="{href}" data-drop aria-haspopup="true"{cur}>{label}{CHEV}</a><div class="drop">{drop}</div></div>')
        else:
            items.append(f'<div class="nav-item"><a class="nav-link" href="{href}"{cur}>{label}</a></div>')
    return f'''<div class="topbar"><div class="wrap"><span>Latest: {BRAND} launches its AI denial-prevention agent. <a href="resources.html?f=news#all">Read the news {ARROW}</a></span><span class="badges"><span>18+ years in RCM</span><span>HIPAA · SOC 2 · ISO 27001</span><span>+1 (800) 555-0142</span></span></div></div>
<header class="header"><div class="wrap">{logo()}
<nav class="nav" aria-label="Main">{"".join(items)}<a class="btn btn-primary" href="#contact" data-modal="#contact-modal">Connect with a specialist</a></nav>
<a class="btn btn-primary" href="#contact" data-modal="#contact-modal">Connect with a specialist</a>
<button class="burger" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<main>
'''

def contact_form(ok="Thank you. A revenue cycle specialist will contact you within one business day."):
    return f'''<form class="form" data-ok="{ok}">
<div class="two"><label>Full name<input name="name" required autocomplete="name"></label><label>Work email<input type="email" name="email" required autocomplete="email"></label></div>
<div class="two"><label>Organization<input name="org" required autocomplete="organization"></label><label>Phone<input type="tel" name="phone" autocomplete="tel"></label></div>
<label>Specialty<select name="specialty"><option>Anesthesia</option><option>DME &amp; HME</option><option>Eye care</option><option>Hospital or health system</option><option>Physician practice or ASC</option><option>Rural health</option><option>Other</option></select></label>
<label>How can we help?<textarea name="msg" rows="3" placeholder="Denials, A/R backlog, credentialing, a full RCM partnership…"></textarea></label>
<button class="btn btn-primary" type="submit">Request a consultation {ARROW}</button>
<p class="form-ok" role="status"></p>
</form>'''

def footer():
    return f'''</main>
<section class="cta-band"><div class="wrap"><div><h2>Ready to see what your revenue cycle could recover?</h2><p>Talk with a specialist who knows your payers, your codes and your workflows. We'll map where revenue is leaking and what it takes to fix it.</p></div><div class="row" style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-light" href="#contact" data-modal="#contact-modal">Connect with a specialist</a><a class="btn btn-ghost" href="specialties.html#services">See our capabilities</a></div></div></section>
<footer class="footer"><div class="wrap">
<div class="foot-grid">
 <div style="display:grid;gap:16px;align-content:start">{logo(footer=True)}<p>Specialty-focused revenue cycle management for providers who need cleaner claims, fewer denials and faster cash. Built on 18+ years of RCM work and an AI-enabled platform.</p><p>hello@medora-rcm.example<br>+1 (800) 555-0142</p></div>
 <div><h4>Company</h4><ul><li><a href="about.html">About us</a></li><li><a href="about.html#leadership">Leadership</a></li><li><a href="about.html#awards">Awards</a></li><li><a href="careers.html">Careers</a></li><li><a href="#contact" data-modal="#contact-modal">Contact</a></li></ul></div>
 <div><h4>Platforms &amp; AI</h4><ul><li><a href="platforms.html#platforms">Platforms</a></li><li><a href="platforms.html#agents">AI agents</a></li><li><a href="platforms.html#integrations">Integrations</a></li><li><a href="platforms.html#security">Security</a></li></ul></div>
 <div><h4>Get started</h4><ul><li><a href="#contact" data-modal="#contact-modal">Schedule a demo</a></li><li><a href="index.html#calculator">Recovery estimate</a></li><li><a href="specialties.html">Specialities</a></li><li><a href="resources.html">Resources</a></li></ul></div>
</div>
<div class="badges-row" style="margin-top:34px">{"".join(f'<span class="cert" style="background:transparent;border-color:#1b3352;color:#cfdcea"><i>✓</i>{c}</span>' for c in ["HIPAA","SOC 2 Type II","ISO 27001","ISO 9001","PCI DSS","HITRUST"])}</div>
<div class="foot-bottom"><span>© <span id="yr">2026</span> {BRAND} {TAG}. All rights reserved. Sample website template.</span><nav><a href="#">Privacy policy</a><a href="#">Terms of use</a><a href="#">Cookie policy</a><a href="#">LinkedIn</a></nav></div>
</div></footer>
<div class="modal" id="contact-modal" role="dialog" aria-modal="true" aria-labelledby="cm-title"><div class="modal-box"><button class="modal-x" aria-label="Close">×</button><p class="eyebrow">Free consultation</p><h2 id="cm-title" style="font-size:1.6rem;margin:6px 0 16px">Connect with a specialist</h2>{contact_form()}</div></div>
<button class="to-top" aria-label="Back to top">↑</button>
<script src="assets/script.js"></script>
</body>
</html>
'''

def page_hero(img_var, eyebrow, title, lead, crumb, ctas=""):
    return f'''<section class="hero page-hero" style="--hero-img:var({img_var})"><div class="wrap">
<p class="crumbs"><a href="index.html">Home</a> / {crumb}</p>
<p class="eyebrow" style="color:#7ad143">{eyebrow}</p><h1>{title}</h1><p class="lead">{lead}</p>{ctas}
</div></section>'''

def card(icon, title, text, tag="", link=""):
    t = f'<span class="tag">{tag}</span>' if tag else ""
    l = f'<a class="link-arrow" href="{link}">Learn more {ARROW}</a>' if link else ""
    return f'<article class="card reveal"><div class="icon">{ic(icon)}</div>{t}<h3>{title}</h3><p>{text}</p>{l}</article>'

def write(name, body):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f: f.write(body)

# =========================== HOME ===========================
home = head(f"{BRAND} {TAG} | Specialty Revenue Cycle Management", "Specialty-intelligent, AI-enabled revenue cycle management for anesthesia, DME, eye care, hospitals and physician groups.") + header("index.html") + f'''
<section class="hero"><div class="wrap">
<div class="tags"><span>Specialty-intelligent</span><span>AI-enabled</span><span>Outcomes-focused</span></div>
<h1>Recover more revenue. <span>Return to care.</span></h1>
<p class="lead">{BRAND} runs the revenue cycle for specialty providers end to end, from eligibility to the final payment, so your team spends its time on patients instead of payers.</p>
<div class="ctas"><a class="btn btn-primary" href="#contact" data-modal="#contact-modal">Connect with a specialist {ARROW}</a><a class="btn btn-ghost" href="#calculator">Estimate your recovery</a></div>
<div class="meta"><span><b>Since 2008</b> in healthcare RCM</span><span><b>98%</b> clean-claim rate</span><span><b>24/7</b> global delivery</span></div>
</div></section>

<section class="section" style="padding-top:0;padding-bottom:48px"><div class="wrap">
<div class="stats">
 <div class="stat"><b data-count="35" data-suffix="+">35+</b><span>Specialties supported</span></div>
 <div class="stat"><b data-count="18" data-suffix="+">18+</b><span>Years of RCM expertise</span></div>
 <div class="stat"><b data-count="2500" data-suffix="+">2,500+</b><span>Specialists worldwide</span></div>
 <div class="stat"><b data-count="40" data-suffix="%">40%</b><span>Average drop in A/R days</span></div>
</div></div></section>
<div class="ticker" aria-hidden="true"><div class="ticker-track">{"".join(f"<span>{s}</span>" for s in ["Anesthesia","Eye & specialty care","DME & HME","Hospitals & health systems","Ambulatory surgery centers","Multispecialty groups","Rural health clinics","Radiology","Laboratory"]*2)}</div></div>

<section class="section"><div class="wrap">
<div class="sec-head center"><p class="eyebrow">How we're different</p><h2>Three ideas behind every engagement</h2></div>
<div class="grid g3">
{card("steth","Specialty-intelligent","Coders, billers and AR teams organized by specialty, trained on the payer rules and modifiers your claims actually live with.")}
{card("brain","AI-enabled","Agents predict denials before submission, prioritize follow-up and draft appeals, with people reviewing every decision that matters.")}
{card("chart","Outcomes-focused","We agree on clean-claim rate, denial rate, A/R days and collections up front, then report on them every month.")}
</div></div></section>

<section class="section alt"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Who we serve</p><h2>Built for the hardest reimbursement environments</h2><p class="lead">Complex coding, prior authorizations and documentation-heavy payers are where revenue slips. That's where we work best.</p></div>
<div class="grid g4">
<a class="photo-card reveal" href="specialties.html#dme" style="background-image:var(--img-spec)"><div><span class="tag" style="color:#7ad143">DME & HME</span><h3>Documentation-ready claims</h3><p>CMN, PA and rental-cycle tracking that keeps recurring revenue moving.</p></div></a>
<a class="photo-card reveal" href="specialties.html#anesthesia" style="background-image:var(--img-about)"><div><span class="tag" style="color:#7ad143">Anesthesia</span><h3>Time units, done right</h3><p>Base units, modifiers and concurrency rules applied on every case.</p></div></a>
<a class="photo-card reveal" href="specialties.html#eye" style="background-image:var(--img-home)"><div><span class="tag" style="color:#7ad143">Eye care</span><h3>Medical and vision, together</h3><p>Coordination across vision plans, medical payers and optical sales.</p></div></a>
<a class="photo-card reveal" href="specialties.html#hospitals" style="background-image:var(--img-resources)"><div><span class="tag" style="color:#7ad143">Health systems</span><h3>Scale without the backlog</h3><p>Flexible teams that absorb volume spikes and aged A/R projects.</p></div></a>
</div></div></section>

<section class="section"><div class="wrap split">
<div class="split-img reveal" style="background-image:var(--img-platform)"><div class="float"><b>-32%</b><span>Average denial rate reduction in year one</span></div></div>
<div style="display:grid;gap:18px"><p class="eyebrow">Why {BRAND}</p><h2>One connected system, from first call to final payment</h2><p class="lead">Most revenue problems start upstream. We connect patient access, coding, billing and collections in one workflow, so a fix in one stage shows up as cash in the next.</p>
<ul class="checks"><li>Eligibility and prior authorization checked before the visit</li><li>Certified coders with specialty-specific audit programs</li><li>Denial root-cause reporting fed back to the front desk</li><li>Transparent dashboards with daily KPI updates</li></ul>
<a class="link-arrow" href="about.html#overview">How we operate {ARROW}</a></div>
</div></section>

<section class="section dark"><div class="wrap">
<div class="sec-head center"><p class="eyebrow" style="color:#7ad143">The {BRAND} effect</p><h2>Small gains at each stage compound into results</h2></div>
<div class="steps">
<div class="step reveal"><b>01</b><h3>Specialty expertise</h3><p>Teams matched to your specialty and payer mix.</p></div>
<div class="step reveal"><b>02</b><h3>Cleaner claims</h3><p>AI scrubbing and coder review before submission.</p></div>
<div class="step reveal"><b>03</b><h3>Fewer denials</h3><p>Predict and prevent the denials that repeat.</p></div>
<div class="step reveal"><b>04</b><h3>Faster payment</h3><p>Prioritized follow-up on the dollars that matter most.</p></div>
<div class="step reveal"><b>05</b><h3>Stronger margins</h3><p>Lower cost to collect and more predictable cash.</p></div>
</div></div></section>

<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Results</p><h2>Proof in the hardest segments</h2><p class="lead">Sample case studies. Replace them with your own client outcomes.</p></div>
<div class="grid g2">
<article class="case reveal"><div class="case-top" style="background-image:var(--img-spec)"><span>DME supplier</span></div><div class="case-body"><h3>A national DME supplier moved billing to {BRAND} in one week</h3><div class="case-metrics"><div><b>1 wk</b><span>to go live</span></div><div><b>30%</b><span>lower cost to collect</span></div><div><b>50%</b><span>less aged A/R</span></div></div><a class="link-arrow" href="resources.html?f=case#all">Read the case study {ARROW}</a></div></article>
<article class="case reveal"><div class="case-top" style="background-image:var(--img-resources)"><span>Multispecialty group</span></div><div class="case-body"><h3>A 120-provider group cut denials and A/R days in six months</h3><div class="case-metrics"><div><b>38%</b><span>fewer denials</span></div><div><b>21</b><span>days off A/R</span></div><div><b>$4.2M</b><span>recovered</span></div></div><a class="link-arrow" href="resources.html?f=case#all">Read the case study {ARROW}</a></div></article>
</div></div></section>

<section class="section alt"><div class="wrap">
<div class="sec-head"><p class="eyebrow">End-to-end capability</p><h2>Every stage of the revenue cycle, under one roof</h2></div>
<div class="grid g4">
{card("users","Front end","Patient registration, eligibility and benefits verification, prior authorization and patient estimates.")}
{card("doc","Mid-cycle","Medical coding, charge capture, clinical documentation review and coding audits.")}
{card("money","Back end","Claims submission, payment posting, denial management, A/R follow-up and appeals.")}
{card("award","Value-added","Provider credentialing and enrollment, analytics, patient billing support and contract review.")}
</div>
<p style="margin-top:26px"><a class="link-arrow" href="specialties.html#services">See all services {ARROW}</a></p>
</div></section>

<section class="section" id="calculator"><div class="wrap">
<div class="sec-head center"><p class="eyebrow">Recovery calculator</p><h2>Estimate what better RCM could recover</h2><p class="lead">Move the sliders to match your organization. The estimate updates as you go.</p></div>
<div class="calc" id="calc">
<div>
<div class="field"><label for="c-rev">Annual net patient revenue <output id="o-rev">$25M</output></label><input type="range" id="c-rev" min="1" max="500" step="1" value="25"></div>
<div class="field"><label for="c-den">Initial denial rate <output id="o-den">12%</output></label><input type="range" id="c-den" min="2" max="30" step="1" value="12"></div>
<div class="field"><label for="c-fpy">First-pass yield <output id="o-fpy">85%</output></label><input type="range" id="c-fpy" min="60" max="99" step="1" value="85"></div>
<div class="field"><label for="c-ar">Average A/R days <output id="o-ar">48 days</output></label><input type="range" id="c-ar" min="20" max="120" step="1" value="48"></div>
</div>
<div class="results" aria-live="polite">
<p class="eyebrow" style="color:#7ad143">Live estimate</p>
<div class="row"><span>Recovered denials</span><b id="r-den">$0</b></div>
<div class="row"><span>Leakage prevented</span><b id="r-leak">$0</b></div>
<div class="row"><span>One-time cash acceleration</span><b id="r-cash">$0</b></div>
<div class="row total" style="border:0"><span>Year-1 revenue impact</span><b id="r-total">$0</b></div>
<p class="fine">Illustrative only. Assumes 35% recovery of denials above a 5% benchmark, 12% of the first-pass gap to 95% recovered, and A/R reduced halfway toward 35 days.</p>
<a class="btn btn-primary" href="#contact" data-modal="#contact-modal">Get a precise assessment</a>
</div></div></div></section>

<section class="section alt"><div class="wrap">
<div class="sec-head center"><p class="eyebrow">What clients say</p><h2>Trusted by practices and health systems</h2></div>
<div class="quotes">
<blockquote class="quote reveal"><p>Our denial rate fell within the first quarter, and for the first time we can see exactly why claims are rejected.</p><footer><span class="avatar">MG</span><span><b>Practice administrator</b><br>Multispecialty group</span></footer></blockquote>
<blockquote class="quote reveal"><p>They understood anesthesia billing on day one. Time units, modifiers, medical direction: all handled without hand-holding.</p><footer><span class="avatar">AP</span><span><b>Revenue cycle director</b><br>Anesthesia partners</span></footer></blockquote>
<blockquote class="quote reveal"><p>The aged A/R project paid for itself in two months. Communication is clear and the reporting is honest.</p><footer><span class="avatar">CH</span><span><b>Chief financial officer</b><br>Community health system</span></footer></blockquote>
</div><p class="fine" style="color:var(--muted);text-align:center;margin-top:16px">Sample testimonials for this template.</p></div></section>

<section class="section"><div class="wrap split">
<div style="display:grid;gap:18px"><p class="eyebrow">Trust & compliance</p><h2>Security built into every workflow</h2><p class="lead">Protected health information is handled under strict access controls, audited processes and encrypted systems.</p>
<ul class="checks"><li>Role-based access, MFA and full audit trails</li><li>Encrypted data at rest and in transit</li><li>Annual third-party audits and penetration testing</li><li>Business associate agreements with every client</li></ul></div>
<div class="badges-row">{"".join(f'<span class="cert"><i>✓</i>{c}</span>' for c in ["HIPAA compliant","SOC 2 Type II","ISO 27001","ISO 9001","PCI DSS","HITRUST"])}</div>
</div></section>
''' + footer()
write("index.html", home)

# =========================== ABOUT ===========================
about = head(f"About | {BRAND} {TAG}", f"About {BRAND} RCM: our story, values, leadership and recognition.") + header("about.html") + page_hero("--img-about","About us","Revenue cycle partners with a care-first mindset","For more than 18 years we've helped providers get paid accurately and on time, so clinicians can stay focused on patients.","About") + f'''
<section class="section" id="overview"><div class="wrap split">
<div style="display:grid;gap:18px"><p class="eyebrow">Company overview</p><h2>Specialists in the business side of healthcare</h2>
<p class="lead">{BRAND} began in 2008 as a small coding team serving anesthesia groups. Today we support more than 35 specialties with 2,500 people across delivery centers in the US and India.</p>
<p style="color:var(--muted)">Our model is simple: pair specialty-trained people with technology that removes repetitive work, then measure everything. Each client gets a dedicated account team, agreed KPIs and complete visibility into their revenue cycle.</p>
<a class="btn btn-outline" href="careers.html" style="justify-self:start">Join our team</a></div>
<div class="split-img reveal" style="background-image:var(--img-home)"><div class="float"><b>96%</b><span>Client retention year over year</span></div></div>
</div></section>

<section class="section alt"><div class="wrap">
<div class="sec-head center"><p class="eyebrow">Mission and values</p><h2>What guides our work</h2></div>
<div class="grid g4">
{card("heart","Care comes first","Every process we improve gives clinicians more time with patients.")}
{card("check","Accuracy over speed","We code and bill correctly the first time, then make it fast.")}
{card("chart","Radical transparency","Clients see the same dashboards and numbers we do.")}
{card("users","Own the outcome","We're accountable for results, not just tasks completed.")}
</div></div></section>

<section class="section" id="journey"><div class="wrap split" style="align-items:start">
<div style="display:grid;gap:14px;position:sticky;top:110px"><p class="eyebrow">Our journey</p><h2>From a coding team to a full RCM partner</h2><p class="lead">Milestones from our first client to today. Sample timeline for this template.</p></div>
<div class="timeline">
<div class="tl reveal"><b>2008</b><h3>Founded</h3><p style="color:var(--muted)">Started with a 12-person anesthesia coding team.</p></div>
<div class="tl reveal"><b>2012</b><h3>Full-cycle billing</h3><p style="color:var(--muted)">Expanded into billing, A/R follow-up and payment posting.</p></div>
<div class="tl reveal"><b>2016</b><h3>DME and eye care</h3><p style="color:var(--muted)">Launched dedicated teams for two documentation-heavy specialties.</p></div>
<div class="tl reveal"><b>2020</b><h3>Security certifications</h3><p style="color:var(--muted)">Achieved SOC 2 Type II and ISO 27001.</p></div>
<div class="tl reveal"><b>2024</b><h3>AI platform</h3><p style="color:var(--muted)">Released AI agents for denial prediction and appeal drafting.</p></div>
<div class="tl reveal"><b>2026</b><h3>2,500 specialists</h3><p style="color:var(--muted)">Serving providers in all 50 states.</p></div>
</div></div></section>

<section class="section dark" id="awards"><div class="wrap">
<div class="sec-head center"><p class="eyebrow" style="color:#7ad143">Awards and recognition</p><h2>Recognized for outcomes and workplace culture</h2><p class="lead">Placeholder awards for this template.</p></div>
<div class="grid g4">
{card("award","Top RCM Partner","Healthcare Finance Awards, 2025","2025")}
{card("award","Best Place to Work","Regional Workplace Awards, 2025","2025")}
{card("award","AI Innovation in RCM","Digital Health Summit, 2024","2024")}
{card("award","Client Satisfaction Leader","Independent provider survey, 2024","2024")}
</div></div></section>

<section class="section" id="leadership"><div class="wrap">
<div class="sec-head center"><p class="eyebrow">Leadership</p><h2>The team behind {BRAND}</h2><p class="lead">Replace these placeholders with your leadership team's names and photos.</p></div>
<div class="grid g4">
{"".join(f'<article class="card person reveal"><span class="avatar">{i}</span><h3>{n}</h3><p class="tag">{r}</p><p>{d}</p></article>' for i,n,r,d in [("CE","Leader name","Chief Executive Officer","Leads strategy and client partnerships."),("CO","Leader name","Chief Operating Officer","Runs global delivery and quality."),("CT","Leader name","Chief Technology Officer","Builds the AI platform and integrations."),("CC","Leader name","Chief Compliance Officer","Owns security, privacy and audits.")])}
</div></div></section>
''' + footer()
write("about.html", about)

# =========================== SPECIALTIES ===========================
specs = [
 ("anesthesia","bed","Anesthesia","Time-based billing done precisely","Base units, time units, modifiers, medical direction and concurrency rules applied to every case, with pain-management and CRNA billing included.",["ASA crosswalk and base-unit validation","Medical direction and QZ/QK/QX modifiers","Pain-management and procedure coding","Surgeon and facility data reconciliation"]),
 ("dme","chair","DME & HME","Documentation that payers accept","We track CMNs, written orders, prior authorizations and rental cycles so recurring revenue doesn't stall.",["Documentation and face-to-face checks","Rental cycle and capped-rental tracking","Medicare DMEPOS and Medicaid rules","Resupply and refill billing"]),
 ("eye","eye","Eye care","Medical and vision billing in one place","Coordinated billing across vision plans and medical insurance, plus optical sales and surgical care.",["Vision plan and medical payer coordination","Retina, cataract and glaucoma coding","Optical and contact-lens billing","Global surgical period tracking"]),
 ("hospitals","hosp","Hospitals & health systems","Capacity when you need it","Flexible teams for coding backlogs, aged A/R and denial projects, working inside your systems.",["Inpatient and outpatient coding","Aged A/R and denial recovery projects","Hospital and professional fee billing","Interim staffing for revenue cycle teams"]),
 ("practices","steth","Practices & ASCs","Full-cycle support for growing groups","From single-specialty practices to multi-site ASCs, we run the revenue cycle so you can grow.",["Multispecialty coding and billing","ASC facility billing","Patient statements and support","Monthly performance reviews"]),
 ("rural","map","Rural health services","Reimbursement rules for rural care","Billing for RHCs, FQHCs and critical access hospitals, including encounter-based and cost-report-aware billing.",["RHC and FQHC encounter billing","Critical access hospital support","Telehealth billing","Grant and sliding-fee reporting support"]),
 ("partners","link","Channel partners","Grow with an RCM partner","White-label RCM services for software vendors, billing companies and MSOs that want to extend their offer.",["White-label delivery teams","API and workflow integration","Shared KPIs and reporting","Partner enablement"]),
]
spec_cards = "".join(f'''<article class="card reveal" id="{sid}" style="scroll-margin-top:110px"><div class="icon">{ic(icon)}</div><span class="tag">{name}</span><h3>{title}</h3><p>{text}</p><ul class="checks" style="margin-top:6px">{"".join(f"<li>{x}</li>" for x in bullets)}</ul><a class="link-arrow" href="#contact" data-modal="#contact-modal">Talk to a {name.split(" ")[0].lower()} specialist {ARROW}</a></article>''' for sid,icon,name,title,text,bullets in specs)
services = [("Front end","users",["Patient registration","Eligibility & benefits verification","Prior authorization","Patient cost estimates","Referral management"]),("Mid-cycle","doc",["Medical coding (CPC, CCS)","Charge capture & entry","Clinical documentation review","Coding audits & education","HCC risk adjustment"]),("Back end","money",["Claims submission & scrubbing","Payment posting & reconciliation","Denial management & appeals","A/R follow-up","Patient billing & support"]),("Credentialing","award",["Provider enrollment","Re-credentialing","CAQH profile management","Payer contracting support","License tracking"])]
spec = head(f"Specialities | {BRAND} {TAG}", "Specialty RCM for anesthesia, DME, eye care, hospitals, practices, rural health and channel partners.") + header("specialties.html") + page_hero("--img-spec","Specialities","Revenue cycle expertise for your specialty","Each specialty has its own codes, payer rules and pitfalls. Our teams are organized around them.","Specialities", '<div class="ctas"><a class="btn btn-primary" href="#contact" data-modal="#contact-modal">Connect with a specialist</a></div>') + f'''
<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Where we win</p><h2>Seven areas of focus</h2><p class="lead">Choose your area to see how we work with organizations like yours.</p></div>
<div class="grid g3">{spec_cards}</div></div></section>
<section class="section dark" id="services" style="scroll-margin-top:90px"><div class="wrap">
<div class="sec-head center"><p class="eyebrow" style="color:#7ad143">Services</p><h2>End-to-end revenue cycle services</h2><p class="lead">Take the full cycle, or start with the stage that hurts most.</p></div>
<div class="grid g4">{"".join(f'<article class="card reveal"><div class="icon">{ic(i)}</div><h3>{t}</h3><ul class="checks" style="color:#d4e2f0">{"".join(f"<li>{x}</li>" for x in xs)}</ul></article>' for t,i,xs in services)}</div>
</div></section>
<section class="section alt"><div class="wrap split">
<div class="split-img reveal" style="background-image:var(--img-about)"><div class="float"><b>45 days</b><span>Typical time from kickoff to full go-live</span></div></div>
<div style="display:grid;gap:18px"><p class="eyebrow">Onboarding</p><h2>A transition plan that protects your cash flow</h2>
<ul class="checks"><li><b>Week 1–2:</b> discovery, system access and KPI baseline</li><li><b>Week 3–4:</b> parallel processing with your current team</li><li><b>Week 5–6:</b> full go-live with daily check-ins</li><li><b>Day 90:</b> first quarterly business review</li></ul></div>
</div></section>
''' + footer()
write("specialties.html", spec)

# =========================== PLATFORMS ===========================
plat = head(f"Platforms & AI | {BRAND} {TAG}", "AI agents, RCM platforms, integrations and security behind Medora RCM.") + header("platforms.html") + page_hero("--img-platform","Platforms & AI","AI that works alongside your revenue cycle team","Our agents handle the repetitive work: checking, predicting, drafting and prioritizing. Specialists make the decisions.","Platforms &amp; AI", '<div class="ctas"><a class="btn btn-primary" href="#contact" data-modal="#contact-modal">Book a platform demo</a><a class="btn btn-ghost" href="#integrations">See integrations</a></div>') + f'''
<section class="section" id="ai"><div class="wrap">
<div class="sec-head"><p class="eyebrow">AI capabilities</p><h2>Intelligence at every stage of the claim</h2></div>
<div class="grid g3">
{card("pulse","Denial prediction","Scores every claim for denial risk before it is submitted, with the reason and suggested fix.")}
{card("doc","Coding assistance","Suggests codes and modifiers from clinical notes for certified coders to confirm.")}
{card("bolt","Smart A/R prioritization","Ranks follow-up work by dollar value, payer behavior and timely-filing risk.")}
{card("chat","Appeal drafting","Drafts payer-specific appeal letters with the supporting documentation attached.")}
{card("clock","Eligibility automation","Runs batch eligibility and benefits checks days before each appointment.")}
{card("chart","Conversational analytics","Ask questions about your revenue cycle in plain English and get charts back.")}
</div></div></section>

<section class="section dark" id="agents"><div class="wrap split">
<div style="display:grid;gap:18px"><p class="eyebrow" style="color:#7ad143">AI agents</p><h2>Meet the digital workforce</h2><p class="lead">Each agent handles a defined task, logs every action, and hands exceptions to a person.</p>
<ul class="checks" style="color:#d4e2f0"><li>Claim status agent checks payer portals around the clock</li><li>Posting agent reconciles ERAs and flags underpayments</li><li>Authorization agent tracks pending prior auths</li><li>Human review on every agent decision that affects revenue</li></ul></div>
<div class="grid" style="gap:14px">
{"".join(f'<div class="card reveal" style="grid-template-columns:52px 1fr;align-items:center"><div class="icon">{ic(i)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in [("bolt","Claim status agent","1.2M status checks a month"),("money","Payment posting agent","98% auto-posting accuracy"),("shield","Authorization agent","40% faster authorization turnaround")])}
</div></div></section>

<section class="section" id="platforms"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Platforms</p><h2>Purpose-built tools for each part of the cycle</h2><p class="lead">Product names here are placeholders for this template.</p></div>
<div class="grid g3">
{card("chart","Insight dashboard","Daily KPIs, denial trends and payer scorecards for every location and provider.","Analytics")}
{card("award","CredTrack","Credentialing and enrollment tracking with expiry alerts and document storage.","Credentialing")}
{card("users","WorkQueue","Prioritized work lists that route each task to the right specialist.","Operations")}
</div></div></section>

<section class="section alt" id="integrations"><div class="wrap">
<div class="sec-head center"><p class="eyebrow">Integrations</p><h2>Works with the systems you already use</h2><p class="lead">We work inside your EHR and practice management system, connected through APIs, HL7 and secure portal access.</p></div>
<div class="badges-row" style="justify-content:center">{"".join(f'<span class="cert"><i>{ic("link")}</i>{x}</span>' for x in ["EHR systems","Practice management","Clearinghouses","Payer portals","HL7 / FHIR APIs","SFTP & EDI 835/837","Patient payment tools","BI & data warehouses"])}</div>
</div></section>

<section class="section" id="security"><div class="wrap split">
<div class="split-img reveal" style="background-image:var(--img-platform)"><div class="float"><b>0</b><span>Reportable data breaches since founding (sample figure)</span></div></div>
<div style="display:grid;gap:18px"><p class="eyebrow">Security & compliance</p><h2>Enterprise-grade protection for patient data</h2>
<ul class="checks"><li>HIPAA-compliant processes with signed BAAs</li><li>SOC 2 Type II, ISO 27001 and HITRUST controls</li><li>Encrypted data, MFA and least-privilege access</li><li>24/7 monitoring and incident response</li><li>Secure delivery centers with clean-desk policies</li></ul>
<div class="badges-row">{"".join(f'<span class="cert"><i>✓</i>{c}</span>' for c in ["HIPAA","SOC 2","ISO 27001","HITRUST"])}</div></div>
</div></section>
''' + footer()
write("platforms.html", plat)

# =========================== RESOURCES ===========================
res_items = [
 ("article","Article","Five front-end fixes that prevent most denials","Eligibility, authorization and registration errors cause many avoidable denials. Here's where to start.","May 2026","6 min read","--img-home"),
 ("case","Case study","How a DME supplier went live in one week","A national DME supplier's move to a new billing partner, and the results after 90 days.","Apr 2026","Case study","--img-spec"),
 ("news","Press release",f"{BRAND} launches its AI denial-prevention agent","The new agent scores claims for denial risk before submission and suggests fixes.","Apr 2026","News","--img-platform"),
 ("event","Webinar","Anesthesia billing changes for 2027","A live session on upcoming modifier and payment updates. 45 minutes plus Q&A.","Nov 18, 2026","Online event","--img-about"),
 ("article","Blog","A/R days: what's normal for your specialty?","Benchmarks by specialty and what to do when your numbers drift.","Mar 2026","5 min read","--img-resources"),
 ("case","Case study","Recovering $4.2M in aged A/R for a multispecialty group","Six months, 120 providers and a structured denial recovery program.","Feb 2026","Case study","--img-careers"),
 ("news","News",f"{BRAND} named a top RCM partner","Recognized for client outcomes and data security practices.","Jan 2026","Awards","--img-spec"),
 ("event","Conference","Meet us at the regional HFMA conference","Stop by our booth to see the AI platform in action.","Dec 4, 2026","In person","--img-home"),
 ("article","Insights","Prior authorization: a practical playbook","Tracking, escalation and documentation steps that shorten turnaround.","Dec 2025","8 min read","--img-about"),
]
res_cards = "".join(f'''<article class="card res-card reveal" data-cat="{c}"><div class="thumb" style="background-image:var({img})"></div><span class="tag">{t}</span><h3>{h}</h3><p>{d}</p><div class="meta"><span>{dt}</span><span>·</span><span>{m}</span></div><a class="link-arrow" href="#" onclick="return false">{"Register" if c=="event" else "Read more"} {ARROW}</a></article>''' for c,t,h,d,dt,m,img in res_items)
res = head(f"Resources | {BRAND} {TAG}", "Articles, case studies, news and events on revenue cycle management.") + header("resources.html") + page_hero("--img-resources","Resources","Insights for healthier revenue cycles","Articles, case studies, news and events from our specialists.","Resources") + f'''
<section class="section" id="all" style="scroll-margin-top:90px"><div class="wrap">
<div class="filters" data-filter-group="#res-grid" role="group" aria-label="Filter resources">
<button class="chip" data-f="all" aria-pressed="true">All</button><button class="chip" data-f="article" aria-pressed="false">Articles &amp; blogs</button><button class="chip" data-f="case" aria-pressed="false">Case studies</button><button class="chip" data-f="news" aria-pressed="false">News &amp; press</button><button class="chip" data-f="event" aria-pressed="false">Events</button>
</div>
<div class="grid g3" id="res-grid">{res_cards}</div>
<p data-empty hidden style="color:var(--muted)">Nothing here yet. Try another filter.</p>
<p class="fine" style="color:var(--muted);margin-top:20px">Sample resources for this template. Link each card to your own article pages.</p>
</div></section>
<section class="section alt"><div class="wrap split">
<div style="display:grid;gap:14px"><p class="eyebrow">Newsletter</p><h2>RCM insights, once a month</h2><p class="lead">Payer updates, coding changes and benchmarks in one short email.</p></div>
<form class="form" data-ok="You're subscribed. Look out for the next issue."><div class="two"><label>Name<input name="n" required></label><label>Work email<input type="email" name="e" required></label></div><button class="btn btn-primary" type="submit" style="justify-self:start">Subscribe</button><p class="form-ok" role="status"></p></form>
</div></section>
<script>(function(){{var f=new URLSearchParams(location.search).get("f");if(f){{var b=document.querySelector('.chip[data-f="'+f+'"]');if(b)setTimeout(function(){{b.click();}},0);}}}})();</script>
''' + footer()
write("resources.html", res)

# =========================== CAREERS ===========================
jobs = [
 ("Certified Medical Coder (Anesthesia)","Coding","Remote, US","Full-time","coding"),
 ("AR Follow-up Specialist","Billing & AR","Chennai, India","Full-time","billing"),
 ("Denial Management Analyst","Billing & AR","Hybrid, Dallas TX","Full-time","billing"),
 ("Credentialing Coordinator","Operations","Remote, US","Full-time","ops"),
 ("Machine Learning Engineer","Technology","Bengaluru, India","Full-time","tech"),
 ("Client Success Manager","Operations","Hybrid, Atlanta GA","Full-time","ops"),
 ("Prior Authorization Specialist","Billing & AR","Noida, India","Full-time","billing"),
 ("Full-Stack Developer","Technology","Remote","Contract","tech"),
]
job_html = "".join(f'''<article class="job" data-cat="{c}"><div style="display:grid;gap:6px"><h3>{t}</h3><div class="meta"><span class="pill">{team}</span><span>{loc}</span><span>{typ}</span></div></div><a class="btn btn-outline" href="#apply" data-modal="#apply-modal" data-role="{t}">Apply now</a></article>''' for t,team,loc,typ,c in jobs)
careers = head(f"Careers | {BRAND} {TAG}", "Join Medora RCM: open roles in coding, billing, operations and technology.") + header("careers.html") + page_hero("--img-careers","Careers","Build a career in healthcare, behind the scenes","Join 2,500 specialists who help providers get paid accurately, so care can keep going.","Careers", '<div class="ctas"><a class="btn btn-primary" href="#openings">See open roles</a></div>') + f'''
<section class="section"><div class="wrap">
<div class="sec-head center"><p class="eyebrow">Life at {BRAND}</p><h2>Why people build their careers here</h2></div>
<div class="grid g4">
{card("grad","Learn and certify","Paid coding certifications (CPC, CCS, CRC) and specialty training tracks.")}
{card("heart","Health and wellbeing","Medical cover for you and your family, plus wellness days.")}
{card("globe","Flexible work","Remote and hybrid roles across our US and India centers.")}
{card("chart","Clear growth paths","Defined promotion criteria and internal-first hiring.")}
</div></div></section>
<section class="section alt" id="openings" style="scroll-margin-top:90px"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Open roles</p><h2>Current openings</h2><p class="lead">Sample listings for this template.</p></div>
<div class="row" style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:20px"><input type="search" id="job-search" placeholder="Search roles or locations" aria-label="Search roles" style="font:inherit;border:1px solid var(--line);border-radius:999px;padding:10px 16px;min-width:0;flex:1 1 240px;max-width:360px">
<div class="filters" data-filter-group="#jobs" role="group" aria-label="Filter by team" style="margin:0"><button class="chip" data-f="all" aria-pressed="true">All teams</button><button class="chip" data-f="coding" aria-pressed="false">Coding</button><button class="chip" data-f="billing" aria-pressed="false">Billing &amp; AR</button><button class="chip" data-f="ops" aria-pressed="false">Operations</button><button class="chip" data-f="tech" aria-pressed="false">Technology</button></div></div>
<div id="jobs">{job_html}</div>
<p data-empty hidden style="color:var(--muted)">No roles in this team right now. Send us your CV anyway.</p>
</div></section>
<section class="section"><div class="wrap split">
<div class="split-img reveal" style="background-image:var(--img-about)"><div class="float"><b>4.5 / 5</b><span>Employee satisfaction score (sample)</span></div></div>
<div style="display:grid;gap:18px"><p class="eyebrow">Hiring process</p><h2>Four simple steps</h2>
<ul class="checks"><li><b>Apply</b> online with your CV</li><li><b>Screening call</b> with our talent team</li><li><b>Skills assessment</b> or technical interview</li><li><b>Offer</b>, usually within two weeks</li></ul>
<a class="btn btn-primary" href="#apply" data-modal="#apply-modal" style="justify-self:start">Send a general application</a></div>
</div></section>
<div class="modal" id="apply-modal" role="dialog" aria-modal="true" aria-labelledby="ap-title"><div class="modal-box"><button class="modal-x" aria-label="Close">×</button><p class="eyebrow">Careers</p><h2 id="ap-title" style="font-size:1.6rem;margin:6px 0 16px">Apply to {BRAND}</h2>
<form class="form" data-ok="Application received. Our talent team will reply within 5 working days.">
<div class="two"><label>Full name<input name="name" required></label><label>Email<input type="email" name="email" required></label></div>
<div class="two"><label>Phone<input type="tel" name="phone"></label><label>Role<select name="role"><option>General application</option>{"".join(f"<option>{t}</option>" for t,*_ in jobs)}</select></label></div>
<label>CV / resume<input type="file" name="cv" accept=".pdf,.doc,.docx"></label>
<label>Cover note<textarea name="note" rows="3"></textarea></label>
<button class="btn btn-primary" type="submit">Submit application</button><p class="form-ok" role="status"></p></form></div></div>
''' + footer()
write("careers.html", careers)
print("built", sorted(os.listdir(OUT)))
