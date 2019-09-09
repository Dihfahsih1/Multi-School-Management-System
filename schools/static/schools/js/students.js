$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-student").modal("show");
            },
            success: function (data) {
                $("#modal-student .modal-content").html(data.html_form);
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
                    $("#student-table tbody").html(data.html_student_list);
                    $("#modal-student").modal("hide");
                } else {
                    $("#modal-student .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create student
    $(".js-create-student").click(loadForm);
    $("#modal-student").on("submit", ".js-student-create-form", saveForm);

     // view student
     $("#student-table").on("click", ".js-view-student", loadForm);
    $("#modal-student").on("submit", ".js-student-view-form", saveForm);

    // Update student
    $("#student-table").on("click", ".js-update-student", loadForm);
    $("#modal-student").on("submit", ".js-student-update-form", saveForm);

    // Delete student
    $("#student-table").on("click", ".js-delete-student", loadForm);
    $("#modal-student").on("submit", ".js-student-delete-form", saveForm);

});