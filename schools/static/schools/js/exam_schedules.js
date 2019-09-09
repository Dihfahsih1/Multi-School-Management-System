$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-exam_schedule").modal("show");
            },
            success: function (data) {
                $("#modal-exam_schedule .modal-content").html(data.html_form);
            }
        });
    };

       var saveForm = function () {
        var form = $(this);
        var formData = new FormData(form[0]);
        $.ajax({
            url: form.attr("action"),
            data: formData,
            type: form.attr("method"),
            dataType: 'json',
            async: true,
            cache: false,
            contentType: false,
            enctype: form.attr("enctype"),
            processData: false,
            success: function (data) {
                if (data.form_is_valid) {
                    $("#exam_schedule-table tbody").html(data.html_exam_schedule_list);
                    $("#modal-exam_schedule").modal("hide");
                } else {
                    $("#modal-exam_schedule .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create exam_schedule
    $(".js-create-exam_schedule").click(loadForm);
    $("#modal-exam_schedule").on("submit", ".js-exam_schedule-create-form", saveForm);

    // Update exam_schedule
    $("#exam_schedule-table").on("click", ".js-update-exam_schedule", loadForm);
    $("#modal-exam_schedule").on("submit", ".js-exam_schedule-update-form", saveForm);


    // Delete exam_schedule
    $("#exam_schedule-table").on("click", ".js-delete-exam_schedule", loadForm);
    $("#modal-exam_schedule").on("submit", ".js-exam_schedule-delete-form", saveForm);

});