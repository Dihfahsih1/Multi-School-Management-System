$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-syllabus").modal("show");
            },
            success: function (data) {
                $("#modal-syllabus .modal-content").html(data.html_form);
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
                    $("#syllabus-table tbody").html(data.html_syllabus_list);
                    $("#modal-syllabus").modal("hide");
                } else {
                    $("#modal-syllabus .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create syllabus
    $(".js-create-syllabus").click(loadForm);
    $("#modal-syllabus").on("submit", ".js-syllabus-create-form", saveForm);

    // Update syllabus
    $("#syllabus-table").on("click", ".js-update-syllabus", loadForm);
    $("#modal-syllabus").on("submit", ".js-syllabus-update-form", saveForm);


    // Delete syllabus
    $("#syllabus-table").on("click", ".js-delete-syllabus", loadForm);
    $("#modal-syllabus").on("submit", ".js-syllabus-delete-form", saveForm);

});