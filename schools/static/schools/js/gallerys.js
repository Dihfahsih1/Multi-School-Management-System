$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-gallery").modal("show");
            },
            success: function (data) {
                $("#modal-gallery .modal-content").html(data.html_form);
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
                    $("#gallery-table tbody").html(data.html_gallery_list);
                    $("#modal-gallery").modal("hide");
                } else {
                    $("#modal-gallery .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create gallery
    $(".js-create-gallery").click(loadForm);
    $("#modal-gallery").on("submit", ".js-gallery-create-form", saveForm);

    // Update gallery
    $("#gallery-table").on("click", ".js-update-gallery", loadForm);
    $("#modal-gallery").on("submit", ".js-gallery-update-form", saveForm);


    // Delete gallery
    $("#gallery-table").on("click", ".js-delete-gallery", loadForm);
    $("#modal-gallery").on("submit", ".js-gallery-delete-form", saveForm);

});