$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-page").modal("show");
            },
            success: function (data) {
                $("#modal-page .modal-content").html(data.html_form);
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
                    $("#page-table tbody").html(data.html_page_list);
                    $("#modal-page").modal("hide");
                } else {
                    $("#modal-page .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create page
    $(".js-create-page").click(loadForm);
    $("#modal-page").on("submit", ".js-page-create-form", saveForm);

    // Update page
    $("#page-table").on("click", ".js-update-page", loadForm);
    $("#modal-page").on("submit", ".js-page-update-form", saveForm);


    // Delete page
    $("#page-table").on("click", ".js-delete-page", loadForm);
    $("#modal-page").on("submit", ".js-page-delete-form", saveForm);

});