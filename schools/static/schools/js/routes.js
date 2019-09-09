$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-route").modal("show");
            },
            success: function (data) {
                $("#modal-route .modal-content").html(data.html_form);
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
                    $("#route-table tbody").html(data.html_route_list);
                    $("#modal-route").modal("hide");
                } else {
                    $("#modal-route .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create route
    $(".js-create-route").click(loadForm);
    $("#modal-route").on("submit", ".js-route-create-form", saveForm);

    // Update route
    $("#route-table").on("click", ".js-update-route", loadForm);
    $("#modal-route").on("submit", ".js-route-update-form", saveForm);


    // Delete route
    $("#route-table").on("click", ".js-delete-route", loadForm);
    $("#modal-route").on("submit", ".js-route-delete-form", saveForm);

});