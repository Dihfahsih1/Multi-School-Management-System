$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-image").modal("show");
            },
            success: function (data) {
                $("#modal-image .modal-content").html(data.html_form);
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
                    $("#image-table tbody").html(data.html_image_list);
                    $("#modal-image").modal("hide");
                } else {
                    $("#modal-image .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create image
    $(".js-create-image").click(loadForm);
    $("#modal-image").on("submit", ".js-image-create-form", saveForm);

    // Update image
    $("#image-table").on("click", ".js-update-image", loadForm);
    $("#modal-image").on("submit", ".js-image-update-form", saveForm);


    // Delete image
    $("#image-table").on("click", ".js-delete-image", loadForm);
    $("#modal-image").on("submit", ".js-image-delete-form", saveForm);

});