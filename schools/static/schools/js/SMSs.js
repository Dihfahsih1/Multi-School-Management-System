$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-SMS").modal("show");
            },
            success: function (data) {
                $("#modal-SMS .modal-content").html(data.html_form);
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
                    $("#SMS-table tbody").html(data.html_SMS_list);
                    $("#modal-SMS").modal("hide");
                } else {
                    $("#modal-SMS .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create SMS
    $(".js-create-SMS").click(loadForm);
    $("#modal-SMS").on("submit", ".js-SMS-create-form", saveForm);

    // Update SMS
    $("#SMS-table").on("click", ".js-update-SMS", loadForm);
    $("#modal-SMS").on("submit", ".js-SMS-update-form", saveForm);


    // Delete SMS
    $("#SMS-table").on("click", ".js-delete-SMS", loadForm);
    $("#modal-SMS").on("submit", ".js-SMS-delete-form", saveForm);

});