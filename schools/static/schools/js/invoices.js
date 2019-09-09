$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-invoice").modal("show");
            },
            success: function (data) {
                $("#modal-invoice .modal-content").html(data.html_form);
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
                    $("#invoice-table tbody").html(data.html_invoice_list);
                    $("#modal-invoice").modal("hide");
                } else {
                    $("#modal-invoice .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create invoice
    $(".js-create-invoice").click(loadForm);
    $("#modal-invoice").on("submit", ".js-invoice-create-form", saveForm);

     // view invoice
     $("#invoice-table").on("click", ".js-view-invoice", loadForm);
    $("#modal-invoice").on("submit", ".js-invoice-view-form", saveForm);

    // Update invoice
    $("#invoice-table").on("click", ".js-update-invoice", loadForm);
    $("#modal-invoice").on("submit", ".js-invoice-update-form", saveForm);

    // Delete invoice
    $("#invoice-table").on("click", ".js-delete-invoice", loadForm);
    $("#modal-invoice").on("submit", ".js-invoice-delete-form", saveForm);

});