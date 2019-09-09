$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-email").modal("show");
            },
            success: function (data) {
                $("#modal-email .modal-content").html(data.html_form);
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
                    $("#email-table tbody").html(data.html_email_list);
                    $("#modal-email").modal("hide");
                } else {
                    $("#modal-email .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create email
    $(".js-create-email").click(loadForm);
    $("#modal-email").on("submit", ".js-email-create-form", saveForm);

    // Update email
    $("#email-table").on("click", ".js-update-email", loadForm);
    $("#modal-email").on("submit", ".js-email-update-form", saveForm);


    // Delete email
    $("#email-table").on("click", ".js-delete-email", loadForm);
    $("#modal-email").on("submit", ".js-email-delete-form", saveForm);

});