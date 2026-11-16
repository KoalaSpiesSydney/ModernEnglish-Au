/* Teacher Tools service worker (scope: /teachertools/)
   - Pages: network first, so teachers always get the latest version; the saved copy is used when offline.
   - Files the tools need (scripts, styles, fonts, libraries): served from the saved copy, refreshed in the background.
   - Ads, analytics, YouTube and TikTok are never saved: they always go straight to the network.
   To publish an update to this file, change VERSION. */
const VERSION = 'v1';
const PAGES = 'tt-pages-' + VERSION;
const ASSETS = 'tt-assets-' + VERSION;

const PRECACHE = [
  '/teachertools/TeacherToolDirectory.html',
  '/teachertools/offline.html',
  '/teachertools/pwa.js',
  '/teachertools/manifest.webmanifest',
  '/teachertools/icons/icon-192.png',
  '/teachertools/icons/icon-512.png'
];

const NEVER_CACHE = /(googlesyndication|googletagmanager|google-analytics|doubleclick|googleadservices|adservice\.google|fundingchoicesmessages|youtube\.com|youtube-nocookie|ytimg\.com|tiktok)/i;
const CDN = /^https:\/\/(cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|unpkg\.com|fonts\.googleapis\.com|fonts\.gstatic\.com)\//i;

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(PAGES).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('tt-') && !k.endsWith(VERSION)).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

function pageKey(url) { return url.origin + url.pathname; }   // ignore ?source=app and similar

async function networkFirstPage(request) {
  const url = new URL(request.url);
  const cache = await caches.open(PAGES);
  try {
    const fresh = await fetch(request);
    if (fresh.ok && fresh.type === 'basic') cache.put(pageKey(url), fresh.clone());
    return fresh;
  } catch (e) {
    return (await cache.match(pageKey(url))) || (await cache.match('/teachertools/offline.html')) || Response.error();
  }
}

async function staleWhileRevalidate(request) {
  const cache = await caches.open(ASSETS);
  const saved = await cache.match(request);
  const refresh = fetch(request)
    .then((res) => { if (res && (res.ok || res.type === 'opaque')) cache.put(request, res.clone()); return res; })
    .catch(() => saved);
  return saved || refresh;
}

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (NEVER_CACHE.test(url.href)) return;                                   // ads, analytics, video: network only

  if (url.origin === self.location.origin) {
    if (request.mode === 'navigate') {
      if (url.pathname.startsWith('/teachertools/')) event.respondWith(networkFirstPage(request));
      return;
    }
    event.respondWith(staleWhileRevalidate(request));                     // the site's own scripts, styles, images
    return;
  }
  if (CDN.test(url.href)) event.respondWith(staleWhileRevalidate(request)); // libraries and fonts the tools use
});
