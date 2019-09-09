$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-bulk_student").modal("show");
            },
            success: function (data) {
                $("#modal-bulk_student .modal-content").html(data.html_form);
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
                    $("#bulk_student-table tbody").html(data.html_bulk_student_list);
                    $("#modal-bulk_student").modal("hide");
                } else {
                    $("#modal-bulk_student .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create bulk_student
    $(".js-create-bulk_student").click(loadForm);
    $("#modal-bulk_student").on("submit", ".js-bulk_student-create-form", saveForm);

    // Update bulk_student
    $("#bulk_student-table").on("click", ".js-update-bulk_student", loadForm);
    $("#modal-bulk_student").on("submit", ".js-bulk_student-update-form", saveForm);


    // Delete bulk_student
    $("#bulk_student-table").on("click", ".js-delete-bulk_student", loadForm);
    $("#modal-bulk_student").on("submit", ".js-bulk_student-delete-form", saveForm);

});