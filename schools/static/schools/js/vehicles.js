$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-vehicle").modal("show");
            },
            success: function (data) {
                $("#modal-vehicle .modal-content").html(data.html_form);
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
                    $("#vehicle-table tbody").html(data.html_vehicle_list);
                    $("#modal-vehicle").modal("hide");
                } else {
                    $("#modal-vehicle .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create vehicle
    $(".js-create-vehicle").click(loadForm);
    $("#modal-vehicle").on("submit", ".js-vehicle-create-form", saveForm);

    // Update vehicle
    $("#vehicle-table").on("click", ".js-update-vehicle", loadForm);
    $("#modal-vehicle").on("submit", ".js-vehicle-update-form", saveForm);


    // Delete vehicle
    $("#vehicle-table").on("click", ".js-delete-vehicle", loadForm);
    $("#modal-vehicle").on("submit", ".js-vehicle-delete-form", saveForm);

});