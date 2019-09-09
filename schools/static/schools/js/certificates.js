$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-certificate").modal("show");
            },
            success: function (data) {
                $("#modal-certificate .modal-content").html(data.html_form);
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
                    $("#certificate-table tbody").html(data.html_certificate_list);
                    $("#modal-certificate").modal("hide");
                } else {
                    $("#modal-certificate .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create certificate
    $(".js-create-certificate").click(loadForm);
    $("#modal-certificate").on("submit", ".js-certificate-create-form", saveForm);

    // Update certificate
    $("#certificate-table").on("click", ".js-update-certificate", loadForm);
    $("#modal-certificate").on("submit", ".js-certificate-update-form", saveForm);


    // Delete certificate
    $("#certificate-table").on("click", ".js-delete-certificate", loadForm);
    $("#modal-certificate").on("submit", ".js-certificate-delete-form", saveForm);

});