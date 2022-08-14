const GIVEN_TIME = "25:00"
const BREAK_TIME = "0:02"
const TOKEN = "{{ TOKEN }}"
const REST_API_URL = "{{ REST_API_URL }}"
const UID = "{{ UID }}"
const AUDIO = "/static/audio/timer.mp3"

let csrf_token = $("[name='csrfmiddlewaretoken']").attr("value")
let isPaused = false
let isStartEnabled = true
let isPauseEnabled = false
let isStopEnabled = false

$("#countdown").html(GIVEN_TIME)

/**
 * Pomodoro alert
 * */
const pomodoroAlert = (status) => {
    let alertStatus
    let msg

    if (status === "start") {
        alertStatus = "alert-info"
        msg = "Pomodoro started, focus on your task."
    }

    if (status === "success") {
        alertStatus = "alert-success"
        msg = "Nice! 1 pomodoro added."
    }

    const _HTML = `<div class="alert ${alertStatus}" role="alert"><p class="m-0">${msg}</p></div>`
    $(".pomodoro-alert").html(_HTML)
}

/**
 * Ringtone
 * */
const playRingtone = () => {
    const audio = new Audio(AUDIO)
    audio.play()

    // audio length = 3 seconds, therefore sleep for 3 seconds
    setTimeout(function () {
        console.log('after 5 seconds')
        //startBreakTimer()
    }, 3000)
}

/**
 * Save pomodoro
 * */
const savePomodoro = () => {
    let settings = {
        "url": `${REST_API_URL}/pomodoro/`, "method": "POST", "timeout": 0, "headers": {
            "Authorization": `Basic ${TOKEN}`, "Content-Type": "application/json", "X-CSRFToken": csrf_token
        }, "data": JSON.stringify({
            "pomodoro": 1, "short_break": 0, "long_break": 0, "remarks": $("#id_remarks").val(), "author": UID
        }),
    };

    $.ajax(settings).done(function () {
        pomodoroAlert('success')
    }).fail(function (jqXHR, textStatus) {
        console.log(`status: ${jqXHR.status} > ${jqXHR.statusText}`)
    })
}

/**
 * Get Pomodoro from REST API
 * */
const getPomodoro = () => {
    var settings = {
        "url": `${REST_API_URL}/pomodoro/`, "method": "GET", "timeout": 0, "headers": {
            "Authorization": `Basic ${TOKEN}`,
        },
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

/**
 * Start
 * */
$("#start").click(function () {
    isStartEnabled = false
    $("#start").prop("disabled", true)

    if (!isPauseEnabled) {
        isPauseEnabled = true
        $("#pause").prop("disabled", false)
    }

    if (!isStopEnabled) {
        isStopEnabled = true
        $("#stop").prop("disabled", false)
    }

    (!isPaused) ? startTimer(GIVEN_TIME) : isPaused = false;
    pomodoroAlert('start')
})

/**
 * Pause
 * */
$("#pause").click(function () {
    isPauseEnabled = false
    $("#pause").prop("disabled", true)

    if (!isStartEnabled) {
        isStartEnabled = true
        $("#start").prop("disabled", false)
    }

    isPaused = true;
})

/**
 * When timer is 00:00
 * */
const endTimer = (minutes, seconds, interval) => {
    if (minutes == 0 && seconds == 0) {
        clearInterval(interval)

        if (!isStartEnabled) {
            isStartEnabled = true
            $("#start").prop("disabled", false)
        }

        if (isPauseEnabled) {
            isPauseEnabled = false
            $("#pause").prop("disabled", true)
        }

        if (isStopEnabled) {
            isStopEnabled = false
            $("#stop").prop("disabled", true)
        }

        playRingtone()
        savePomodoro()

        $("#countdown").html(GIVEN_TIME)
        $("#id_remarks").val("")
    }
}

/**
 * Start timer
 * */
const startTimer = (timer2) => {
    let interval = setInterval(function () {

        if (!isPaused) {
            let timer = timer2.split(":")

            let minutes = parseInt(timer[0], 10)
            let seconds = parseInt(timer[1], 10)

            --seconds;

            minutes = (seconds < 0) ? --minutes : minutes;

            if (minutes < 0) clearInterval(interval)

            seconds = (seconds < 0) ? 59 : seconds;
            seconds = (seconds < 10) ? '0' + seconds : seconds;

            $("#countdown").html(minutes + ':' + seconds)
            timer2 = minutes + ':' + seconds;

            endTimer(minutes, seconds, interval)
        }
    }, 1000)
}

/**
 * Stop
 * */
$("#stop").click(function () {
    location.reload()
    //$(".pomodoro-alert").hide()
    /** console.log("stopped!")
     $("#countdown").html(GIVEN_TIME)
     clearInterval(interval)
     */
})

/**
 * Break (5 minutes): todo: incomplete
 * */

const startBreakTimer = () => {
    console.log('starting break...')
    $("#countdown").html(BREAK_TIME)
}