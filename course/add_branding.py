"""Adds the Modern English Au header and footer to a Rise 360 export.
Run from the lesson folder:  python add_branding.py
Safe to run again: it replaces its own earlier insert."""
import re, pathlib
p = pathlib.Path("index.html")
t = p.read_text(encoding="utf8")
t = re.sub(r"\s*<!-- MEA-BRANDING START -->.*?<!-- MEA-BRANDING END -->", "", t, flags=re.S)

HEAD = r'''
<!-- MEA-BRANDING START -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;700&family=Source+Serif+4:opsz,wght@8..60,800&display=swap" rel="stylesheet">
<style>
:root{--mea-band:#1c1c1c;--mea-paper:#f8fafc;--mea-muted:#94a3b8;--mea-accent:#3968ea;--mea-highlight:#fde047;--mea-line:#2c3234}
.mea-header{position:relative;background:var(--mea-band);overflow:hidden}
.mea-header::before{content:"";position:absolute;inset:0;pointer-events:none;
  background-image:linear-gradient(rgba(255,255,255,.024) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.024) 1px,transparent 1px);
  background-size:48px 48px;animation:mea-grid 24s linear infinite}
@keyframes mea-grid{from{transform:translate(0,0)}to{transform:translate(48px,48px)}}
.mea-header::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;
  background:linear-gradient(90deg,transparent 0%,rgba(37,99,235,.55) 20%,#60a5fa 50%,rgba(37,99,235,.55) 80%,transparent 100%)}
.mea-wrap{position:relative;z-index:1;max-width:1160px;margin:0 auto;padding:14px clamp(16px,4vw,36px) 16px;
  display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.mea-brand{font-family:"Source Serif 4",Georgia,serif;font-weight:800;font-size:clamp(1.25rem,3.2vw,2rem);
  letter-spacing:3px;text-transform:uppercase;line-height:1.05;text-decoration:none;color:var(--mea-paper);
  background:linear-gradient(100deg,#f8fafc 0%,#f8fafc 18%,#fff 30%,#a5c4fd 42%,#fff 56%,#f8fafc 70%,#f8fafc 100%);
  background-size:250% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  animation:mea-shimmer 3.5s linear infinite}
@keyframes mea-shimmer{from{background-position:200% center}to{background-position:-50% center}}
.mea-kss{font-family:"Source Sans 3",system-ui,sans-serif;font-weight:700;font-size:.8rem;letter-spacing:5px;
  text-transform:uppercase;color:var(--mea-highlight);text-decoration:none}
.mea-kss:hover{text-decoration:underline;text-underline-offset:4px}
/* Rise keeps the page itself fixed and scrolls inside the lesson,
   so the page becomes a column: header, lesson (fills the rest), slim footer. */
html,body{height:100%}
body{display:flex;flex-direction:column}
.mea-header,.mea-footer{flex:0 0 auto}
#app{flex:1 1 auto;min-height:0;height:auto !important;position:relative}
/* Rise sizes these to the full window; make them fit the space between header and footer */
#app .lessonNavigation__wrapper,#app .lesson__sidebar,#app .nav-sidebar__content{height:var(--mea-avail,100vh) !important}
#app .lesson__content{max-height:var(--mea-avail,100vh) !important}
.mea-footer{background:var(--mea-band);border-top:2px solid var(--mea-accent);
  font-family:"Source Sans 3",system-ui,sans-serif;font-size:.88rem;
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.3rem 1.2rem;
  padding:.45rem clamp(16px,4vw,36px)}
.mea-footer p{margin:0;color:var(--mea-muted)}
.mea-nav{display:flex;flex-wrap:wrap;gap:.2rem 1rem}
.mea-nav a{color:#8fb0ff;text-decoration:none}
.mea-nav a:hover{color:#fff;text-decoration:underline;text-underline-offset:3px}
@media (max-width:600px){.mea-brand{letter-spacing:1.5px}.mea-kss{letter-spacing:3px;font-size:.65rem}.mea-wrap{padding-block:10px 12px}.mea-footer{font-size:.72rem;justify-content:center;text-align:center}.mea-nav{justify-content:center}.mea-footer p{display:none}}
@media (prefers-reduced-motion:reduce){.mea-header::before,.mea-brand{animation:none}.mea-brand{-webkit-text-fill-color:var(--mea-paper)}}
</style>
<!-- MEA-BRANDING END -->
'''
TOP = '''
<!-- MEA-BRANDING START -->
<header class="mea-header"><div class="mea-wrap">
  <a href="https://modernenglish.au/" class="mea-brand">Modern English Au</a>
  <a href="https://koalaspiessydney.github.io/KoalaSpiesSyd/" class="mea-kss">Koala Spies Sydney</a>
</div></header>
<!-- MEA-BRANDING END -->'''
BOTTOM = '''
<!-- MEA-BRANDING START -->
<footer class="mea-footer">
  <p>© Koala Spies Sydney · Modern English Australia</p>
  <nav class="mea-nav">
    <a href="https://modernenglish.au/">Home</a>
    <a href="https://modernenglish.au/dictation.html">Dictation &amp; Situations</a>
    <a href="https://modernenglish.au/repeat.html">Repeat Sentence</a>
    <a href="https://modernenglish.au/vocab.html">Vocabulary</a>
    <a href="https://modernenglish.au/contact.html">Contact</a>
  </nav>
</footer>
<script>
/* keeps --mea-avail equal to the space between the header and footer */
(function(){
  var h=document.querySelector(".mea-header"), f=document.querySelector(".mea-footer");
  function fit(){document.documentElement.style.setProperty("--mea-avail",
    (window.innerHeight-h.offsetHeight-f.offsetHeight)+"px");}
  fit(); window.addEventListener("resize",fit);
  if(window.ResizeObserver){var ro=new ResizeObserver(fit);ro.observe(h);ro.observe(f);}
})();
</script>
<!-- MEA-BRANDING END -->'''
t = t.replace("</head>", HEAD + "</head>", 1)
t = t.replace('<div id="app"></div>', TOP.strip("\n") + '\n    <div id="app"></div>' + BOTTOM, 1)
p.write_text(t, encoding="utf8")
print("Branding added.")
