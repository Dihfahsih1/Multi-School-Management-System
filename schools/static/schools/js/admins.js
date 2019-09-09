$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-admin").modal("show");
            },
            success: function (data) {
                $("#modal-admin .modal-content").html(data.html_form);
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
                    $("#admin-table tbody").html(data.html_admin_list);
                    $("#modal-admin").modal("hide");
                } else {
                    $("#modal-admin .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create admin
    $(".js-create-admin").click(loadForm);
    $("#modal-admin").on("submit", ".js-admin-create-form", saveForm);

     // view admin
     $("#admin-table").on("click", ".js-view-admin", loadForm);
    $("#modal-admin").on("submit", ".js-admin-view-form", saveForm);

    // Update admin
    $("#admin-table").on("click", ".js-update-admin", loadForm);
    $("#modal-admin").on("submit", ".js-admin-update-form", saveForm);

    // Delete admin
    $("#admin-table").on("click", ".js-delete-admin", loadForm);
    $("#modal-admin").on("submit", ".js-admin-delete-form", saveForm);

});