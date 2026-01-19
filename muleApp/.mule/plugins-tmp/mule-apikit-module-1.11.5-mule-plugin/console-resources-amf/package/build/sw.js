/**
 * Welcome to your Workbox-powered service worker!
 *
 * You'll need to register this file in your web app and you should
 * disable HTTP caching for this file too.
 * See https://goo.gl/nhQhGp
 *
 * The rest of the code is auto-generated. Please don't update this file
 * directly; instead, make changes to your Workbox build configuration
 * and re-run your build process.
 * See https://goo.gl/2aRDsh
 */

importScripts("https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js");

self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

/**
 * The workboxSW.precacheAndRoute() method efficiently caches and responds to
 * requests for URLs in the manifest.
 * See https://goo.gl/S9QRab
 */
self.__precacheManifest = [
  {
    "url": "api-console-37db0d6e.js",
    "revision": "b17bd6328bf1f43a5331d77ee193e91e"
  },
  {
    "url": "index.html",
    "revision": "e8052ee2c8dcd7b35f9baeda5e9d625b"
  },
  {
    "url": "legacy/api-console-27b1c6af.js",
    "revision": "1d9e03df3558ff197eaa657fb365ac99"
  },
  {
    "url": "polyfills/core-js.c54a2cfc5c515e908a81db4704fbe204.js",
    "revision": "c54a2cfc5c515e908a81db4704fbe204"
  },
  {
    "url": "polyfills/custom-elements-es5-adapter.cff507bc95ad1d6bf1a415cc9c8852b0.js",
    "revision": "cff507bc95ad1d6bf1a415cc9c8852b0"
  },
  {
    "url": "polyfills/dynamic-import.08b86a7f56c6f0d65265654299b16d74.js",
    "revision": "08b86a7f56c6f0d65265654299b16d74"
  },
  {
    "url": "polyfills/fetch.0e67b62a23f4e9bd88d6d0485c24e420.js",
    "revision": "0e67b62a23f4e9bd88d6d0485c24e420"
  },
  {
    "url": "polyfills/regenerator-runtime.6d5da0232f4ab85670e271f840b48b03.js",
    "revision": "6d5da0232f4ab85670e271f840b48b03"
  },
  {
    "url": "polyfills/systemjs.7f2f505ec63ab981209af53ce7f0f503.js",
    "revision": "7f2f505ec63ab981209af53ce7f0f503"
  },
  {
    "url": "polyfills/webcomponents.d43d14353b5efb829a6185511b3e4dbf.js",
    "revision": "d43d14353b5efb829a6185511b3e4dbf"
  }
].concat(self.__precacheManifest || []);
workbox.precaching.precacheAndRoute(self.__precacheManifest, {});

workbox.routing.registerNavigationRoute(workbox.precaching.getCacheKeyForURL("/index.html"));
