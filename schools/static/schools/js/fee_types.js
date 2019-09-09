$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-fee_type").modal("show");
            },
            success: function (data) {
                $("#modal-fee_type .modal-content").html(data.html_form);
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
                    $("#fee_type-table tbody").html(data.html_fee_type_list);
                    $("#modal-fee_type").modal("hide");
                } else {
                    $("#modal-fee_type .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create fee_type
    $(".js-create-fee_type").click(loadForm);
    $("#modal-fee_type").on("submit", ".js-fee_type-create-form", saveForm);

    // Update fee_type
    $("#fee_type-table").on("click", ".js-update-fee_type", loadForm);
    $("#modal-fee_type").on("submit", ".js-fee_type-update-form", saveForm);


    // Delete fee_type
    $("#fee_type-table").on("click", ".js-delete-fee_type", loadForm);
    $("#modal-fee_type").on("submit", ".js-fee_type-delete-form", saveForm);

});