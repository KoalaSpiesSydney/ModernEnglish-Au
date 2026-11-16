/* Teacher Tools app helper. Add to every page in /teachertools/:
     <link rel="manifest" href="/teachertools/manifest.webmanifest">
     <meta name="theme-color" content="#1c1c1c">
     <script src="/teachertools/pwa.js" defer></script>
   It turns on offline use, and remembers which tools this teacher has used (on their own device only). */
(function () {
  'use strict';

  // 1. Offline support
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('/teachertools/sw.js', { scope: '/teachertools/' }).catch(function () {});
    });
  }

  // 2. Remember this tool as recently used (stored only in this browser)
  var NOT_TOOLS = /^(TeacherToolDirectory|offline|custom-tools|workshops|sponsor)\.html$/i;
  var file = location.pathname.split('/').pop();
  var studentLink = /^#play=/.test(location.hash);   // a student opening a lesson isn't a teacher using the tool
  if (file && /\.html$/i.test(file) && !NOT_TOOLS.test(file) && !studentLink) {
    try {
      var list = JSON.parse(localStorage.getItem('tt.recent') || '[]').filter(function (f) { return f !== file; });
      list.unshift(file);
      localStorage.setItem('tt.recent', JSON.stringify(list.slice(0, 8)));
    } catch (e) {}
  }

  // 3. Analytics: count app opens and installs (shows in Google Analytics > Events)
  function track(name, params) { try { if (typeof gtag === 'function') gtag('event', name, params || {}); } catch (e) {} }
  var standalone = (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true;
  if (standalone) track('app_open', { page: file || 'index' });
  window.addEventListener('appinstalled', function () { track('app_installed'); });
})();
