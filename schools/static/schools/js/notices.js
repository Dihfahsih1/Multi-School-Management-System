$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-notice").modal("show");
            },
            success: function (data) {
                $("#modal-notice .modal-content").html(data.html_form);
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
                    $("#notice-table tbody").html(data.html_notice_list);
                    $("#modal-notice").modal("hide");
                } else {
                    $("#modal-notice .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create notice
    $(".js-create-notice").click(loadForm);
    $("#modal-notice").on("submit", ".js-notice-create-form", saveForm);

    // Update notice
    $("#notice-table").on("click", ".js-update-notice", loadForm);
    $("#modal-notice").on("submit", ".js-notice-update-form", saveForm);


    // Delete notice
    $("#notice-table").on("click", ".js-delete-notice", loadForm);
    $("#modal-notice").on("submit", ".js-notice-delete-form", saveForm);

});