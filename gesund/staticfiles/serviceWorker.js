let STATIC_GESUND = "gesund-app-v1"
let ASSETS = [
    "/static/css/main.css",
    "/static/dist/bootstrap/css/bootstrap.min.css",
    "/static/dist/fontawesome/css/all.min.css",
    "/static/dist/jquery-ui/jquery-ui.min.css",


    "/static/dist/jquery/jquery-3.6.0.min.js",
    "/static/dist/jquery-ui/jquery-ui.min.js",
    "/static/dist/bootstrap/js/bootstrap.bundle.min.js",
    "/static/dist/bootstrap/js/bootstrap.min.js",
    "/static/dist/chartjs/chartjs.min.js",
    "/static/dist/fontawesome/js/all.min.js",
    "/static/js/main.js",
    "/static/js/sparkline.js",
    "/static/js/utils.js",

    "/static/audio/timer.mp3",

    "/static/images/beer.png",
    "/static/images/bottle.png",
    "/static/images/burger.png",
    "/static/images/calories.png",
    "/static/images/chocolate.png",
    "/static/images/favicon-16x16.png",
    "/static/images/favicon-32x32.png",
    "/static/images/favicon.ico",
    "/static/images/food_1.jpg",
    "/static/images/food_2.jpg",
    "/static/images/food_sugarfree_3.jpg",
    "/static/images/heart.png",
    "/static/images/logo-50x50.png",
    "/static/images/logo.png",
    "/static/images/mstile-150x150.png",
    "/static/images/pomodoro_1.jpg",
    "/static/images/profil.png",
    "/static/images/safari-pinned-tab.svg",
    "/static/images/smoking.png",
    "/static/images/steps.png",
    "/static/images/steps_walking_1.png",
    "/static/images/steps_walking_2.jpg",
    "/static/images/steps_walking_3.jpg",
    "/static/images/steps_walking_4.jpg",
    "/static/images/stopwatch.png",
    "/static/images/sugar-cube.png",
    "/static/images/tomato.png",
    "/static/images/water_1.jpg",
    "/static/images/water_intake_1.png",
    "/static/images/water.png",
    "/static/images/wine.png"
]


self.addEventListener("install", installEvent => {
    installEvent.waitUntil(caches.open(STATIC_GESUND).then(cache => {
        cache.addAll(ASSETS)
    }))
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(caches.match(fetchEvent.request).then(res => {
        return res || fetch(fetchEvent.request)
    }))
})