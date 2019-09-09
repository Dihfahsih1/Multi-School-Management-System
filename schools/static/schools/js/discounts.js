$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-discount").modal("show");
            },
            success: function (data) {
                $("#modal-discount .modal-content").html(data.html_form);
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
                    $("#discount-table tbody").html(data.html_discount_list);
                    $("#modal-discount").modal("hide");
                } else {
                    $("#modal-discount .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create discount
    $(".js-create-discount").click(loadForm);
    $("#modal-discount").on("submit", ".js-discount-create-form", saveForm);

    // Update discount
    $("#discount-table").on("click", ".js-update-discount", loadForm);
    $("#modal-discount").on("submit", ".js-discount-update-form", saveForm);


    // Delete discount
    $("#discount-table").on("click", ".js-delete-discount", loadForm);
    $("#modal-discount").on("submit", ".js-discount-delete-form", saveForm);

});