$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-exam_grade").modal("show");
            },
            success: function (data) {
                $("#modal-exam_grade .modal-content").html(data.html_form);
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
                    $("#exam_grade-table tbody").html(data.html_exam_grade_list);
                    $("#modal-exam_grade").modal("hide");
                } else {
                    $("#modal-exam_grade .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create exam_grade
    $(".js-create-exam_grade").click(loadForm);
    $("#modal-exam_grade").on("submit", ".js-exam_grade-create-form", saveForm);

    // Update exam_grade
    $("#exam_grade-table").on("click", ".js-update-exam_grade", loadForm);
    $("#modal-exam_grade").on("submit", ".js-exam_grade-update-form", saveForm);


    // Delete exam_grade
    $("#exam_grade-table").on("click", ".js-delete-exam_grade", loadForm);
    $("#modal-exam_grade").on("submit", ".js-exam_grade-delete-form", saveForm);

});