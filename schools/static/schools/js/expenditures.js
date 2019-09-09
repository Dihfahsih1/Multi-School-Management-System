$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-expenditure").modal("show");
            },
            success: function (data) {
                $("#modal-expenditure .modal-content").html(data.html_form);
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
                    $("#expenditure-table tbody").html(data.html_expenditure_list);
                    $("#modal-expenditure").modal("hide");
                } else {
                    $("#modal-expenditure .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create expenditure
    $(".js-create-expenditure").click(loadForm);
    $("#modal-expenditure").on("submit", ".js-expenditure-create-form", saveForm);

    // Update expenditure
    $("#expenditure-table").on("click", ".js-update-expenditure", loadForm);
    $("#modal-expenditure").on("submit", ".js-expenditure-update-form", saveForm);


    // Delete expenditure
    $("#expenditure-table").on("click", ".js-delete-expenditure", loadForm);
    $("#modal-expenditure").on("submit", ".js-expenditure-delete-form", saveForm);

});