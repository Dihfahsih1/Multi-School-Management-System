$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-due_fee_sms").modal("show");
            },
            success: function (data) {
                $("#modal-due_fee_sms .modal-content").html(data.html_form);
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
                    $("#due_fee_sms-table tbody").html(data.html_due_fee_sms_list);
                    $("#modal-due_fee_sms").modal("hide");
                } else {
                    $("#modal-due_fee_sms .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create due_fee_sms
    $(".js-create-due_fee_sms").click(loadForm);
    $("#modal-due_fee_sms").on("submit", ".js-due_fee_sms-create-form", saveForm);

    // Update due_fee_sms
    $("#due_fee_sms-table").on("click", ".js-update-due_fee_sms", loadForm);
    $("#modal-due_fee_sms").on("submit", ".js-due_fee_sms-update-form", saveForm);


    // Delete due_fee_sms
    $("#due_fee_sms-table").on("click", ".js-delete-due_fee_sms", loadForm);
    $("#modal-due_fee_sms").on("submit", ".js-due_fee_sms-delete-form", saveForm);

});