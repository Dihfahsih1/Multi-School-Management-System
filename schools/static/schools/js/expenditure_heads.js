$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-expenditure_head").modal("show");
            },
            success: function (data) {
                $("#modal-expenditure_head .modal-content").html(data.html_form);
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
                    $("#expenditure_head-table tbody").html(data.html_expenditure_head_list);
                    $("#modal-expenditure_head").modal("hide");
                } else {
                    $("#modal-expenditure_head .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create expenditure_head
    $(".js-create-expenditure_head").click(loadForm);
    $("#modal-expenditure_head").on("submit", ".js-expenditure_head-create-form", saveForm);

    // Update expenditure_head
    $("#expenditure_head-table").on("click", ".js-update-expenditure_head", loadForm);
    $("#modal-expenditure_head").on("submit", ".js-expenditure_head-update-form", saveForm);


    // Delete expenditure_head
    $("#expenditure_head-table").on("click", ".js-delete-expenditure_head", loadForm);
    $("#modal-expenditure_head").on("submit", ".js-expenditure_head-delete-form", saveForm);

});