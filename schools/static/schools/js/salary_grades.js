$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-salary_grade").modal("show");
            },
            success: function (data) {
                $("#modal-salary_grade .modal-content").html(data.html_form);
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
                    $("#salary_grade-table tbody").html(data.html_salary_grade_list);
                    $("#modal-salary_grade").modal("hide");
                } else {
                    $("#modal-salary_grade .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create salary_grade
    $(".js-create-salary_grade").click(loadForm);
    $("#modal-salary_grade").on("submit", ".js-salary_grade-create-form", saveForm);

    // Update salary_grade
    $("#salary_grade-table").on("click", ".js-update-salary_grade", loadForm);
    $("#modal-salary_grade").on("submit", ".js-salary_grade-update-form", saveForm);


    // Delete salary_grade
    $("#salary_grade-table").on("click", ".js-delete-salary_grade", loadForm);
    $("#modal-salary_grade").on("submit", ".js-salary_grade-delete-form", saveForm);

});