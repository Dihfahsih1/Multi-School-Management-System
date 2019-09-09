$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-superuser").modal("show");
            },
            success: function (data) {
                $("#modal-superuser .modal-content").html(data.html_form);
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
                    $("#superuser-table tbody").html(data.html_superuser_list);
                    $("#modal-superuser").modal("hide");
                } else {
                    $("#modal-superuser .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create superuser
    $(".js-create-superuser").click(loadForm);
    $("#modal-superuser").on("submit", ".js-superuser-create-form", saveForm);

     // view superuser
     $("#superuser-table").on("click", ".js-view-superuser", loadForm);
    $("#modal-superuser").on("submit", ".js-superuser-view-form", saveForm);

    // Update superuser
    $("#superuser-table").on("click", ".js-update-superuser", loadForm);
    $("#modal-superuser").on("submit", ".js-superuser-update-form", saveForm);

    // Delete superuser
    $("#superuser-table").on("click", ".js-delete-superuser", loadForm);
    $("#modal-superuser").on("submit", ".js-superuser-delete-form", saveForm);

});