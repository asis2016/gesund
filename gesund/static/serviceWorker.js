const staticGesund = "gesund-app-v1"
const assets = [
    "/static/css/base.css",
    "/static/css/bootstrap.min.css",
    "/static/css/login.css",
    "/static/css/screen.css",
    "/static/css/style.css",

    "/static/dist/fontawesome/css/all.min.css",
    "/static/dist/fontawesome/js/all.min.js",
    "/static/dist/fontawesome/webfonts/fa-brands-400.ttf",
    "/static/dist/fontawesome/webfonts/fa-brands-400.woff2",
    "/static/dist/fontawesome/webfonts/fa-regular-400.ttf",
    "/static/dist/fontawesome/webfonts/fa-regular-400.woff2",
    "/static/dist/fontawesome/webfonts/fa-solid-900.ttf",
    "/static/dist/fontawesome/webfonts/fa-solid-900.woff2",
    "/static/dist/fontawesome/webfonts/fa-v4compatibility.ttf",
    "/static/dist/fontawesome/webfonts/fa-v4compatibility.woff2",

    "/static/dist/jquery-ui-1.13.2/jquery-ui.min.css",
    "/static/dist/jquery-ui-1.13.2/jquery-ui.min.js",

    "/static/images/android-chrome-96x96.png",
    "/static/images/android-launchericon-192-192.png",
    "/static/images/apple-touch-icon.png",
    "/static/images/apple-touch-icon-60x60.png",
    "/static/images/apple-touch-icon-76x76.png",
    "/static/images/apple-touch-icon-120x120.png",
    "/static/images/beer.png",
    "/static/images/burger.png",
    "/static/images/chocolate.png",
    "/static/images/favicon.ico",
    "/static/images/favicon-16x16.png",
    "/static/images/favicon-32x32.png",
    "/static/images/heart.png",
    "/static/images/logo.png",
    "/static/images/logo-50x50.png",
    "/static/images/mstile-150x150.png",
    "/static/images/profil.png",
    "/static/images/safari-pinned-tab.svg",
    "/static/images/smoking.png",
    "/static/images/sugar-cube.png",
    "/static/images/wine.png",

    "/static/js/chartjs.min.js",
    "/static/js/jquery-3.6.0.min.js",
    "/static/js/main.js",
    "/static/js/sparkline.js",
    "/static/js/utils.js"
]


self.addEventListener("install", installEvent => {
    installEvent.waitUntil(
        caches.open(staticGesund).then(cache => {
            cache.addAll(assets)
        })
    )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
        caches.match(fetchEvent.request).then(res => {
            return res || fetch(fetchEvent.request)
        })
    )
})
