const staticGesund = "gesund-app-v1"
const assets = [
    "/static/css/bootstrap.min.css",
    "/static/css/style.css",
    "/static/css/login.css",
    "/static/css/screen.css",
    "/static/css/jquery.datetimepicker.min.css",

    "/static/images/android-launchericon-192-192.png",
    "/static/images/logo.png"
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