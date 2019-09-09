$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-income").modal("show");
            },
            success: function (data) {
                $("#modal-income .modal-content").html(data.html_form);
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
                    $("#income-table tbody").html(data.html_income_list);
                    $("#modal-income").modal("hide");
                } else {
                    $("#modal-income .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create income
    $(".js-create-income").click(loadForm);
    $("#modal-income").on("submit", ".js-income-create-form", saveForm);

    // Update income
    $("#income-table").on("click", ".js-update-income", loadForm);
    $("#modal-income").on("submit", ".js-income-update-form", saveForm);


    // Delete income
    $("#income-table").on("click", ".js-delete-income", loadForm);
    $("#modal-income").on("submit", ".js-income-delete-form", saveForm);

});