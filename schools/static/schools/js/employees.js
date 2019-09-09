$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-employee").modal("show");
            },
            success: function (data) {
                $("#modal-employee .modal-content").html(data.html_form);
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
                    $("#employee-table tbody").html(data.html_employee_list);
                    $("#modal-employee").modal("hide");
                } else {
                    $("#modal-employee .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create employee
    $(".js-create-employee").click(loadForm);
    $("#modal-employee").on("submit", ".js-employee-create-form", saveForm);

     // view employee
     $("#employee-table").on("click", ".js-view-employee", loadForm);
    $("#modal-employee").on("submit", ".js-employee-view-form", saveForm);

    // Update employee
    $("#employee-table").on("click", ".js-update-employee", loadForm);
    $("#modal-employee").on("submit", ".js-employee-update-form", saveForm);

    // Delete employee
    $("#employee-table").on("click", ".js-delete-employee", loadForm);
    $("#modal-employee").on("submit", ".js-employee-delete-form", saveForm);

});