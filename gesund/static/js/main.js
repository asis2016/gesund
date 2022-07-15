$(function () {
    $("#id_datestamp").datepicker({
        dateFormat: "yy-mm-dd"
    })

    let toggle_local_value = localStorage.getItem("toggle")

    if (toggle_local_value === "yes") {
        $(".sidebar").addClass("toggled")
    }

    if (toggle_local_value === "no") {
        $('.sidebar').removeClass('toggled')
    }


    // Toggle the side navigation
    $("#menu").on('click', function (e) {
        //$("body").toggleClass("sidebar-toggled")

        $(".sidebar").toggleClass("toggled")

        if ($(".sidebar").hasClass("toggled")) {
            $('.sidebar').collapse('hide')
        }

        // toggle in local storage
        let toggle_status = $(".sidebar").hasClass("toggled")
        toggle_status ? localStorage.setItem("toggle", "yes") : localStorage.setItem("toggle", "no")
    });


});

//tooltips
let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})