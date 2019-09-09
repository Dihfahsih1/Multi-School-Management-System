$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-due_fee_email").modal("show");
            },
            success: function (data) {
                $("#modal-due_fee_email .modal-content").html(data.html_form);
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
                    $("#due_fee_email-table tbody").html(data.html_due_fee_email_list);
                    $("#modal-due_fee_email").modal("hide");
                } else {
                    $("#modal-due_fee_email .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create due_fee_email
    $(".js-create-due_fee_email").click(loadForm);
    $("#modal-due_fee_email").on("submit", ".js-due_fee_email-create-form", saveForm);

    // Update due_fee_email
    $("#due_fee_email-table").on("click", ".js-update-due_fee_email", loadForm);
    $("#modal-due_fee_email").on("submit", ".js-due_fee_email-update-form", saveForm);


    // Delete due_fee_email
    $("#due_fee_email-table").on("click", ".js-delete-due_fee_email", loadForm);
    $("#modal-due_fee_email").on("submit", ".js-due_fee_email-delete-form", saveForm);

});