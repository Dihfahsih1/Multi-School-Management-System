$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-holiday").modal("show");
            },
            success: function (data) {
                $("#modal-holiday .modal-content").html(data.html_form);
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
                    $("#holiday-table tbody").html(data.html_holiday_list);
                    $("#modal-holiday").modal("hide");
                } else {
                    $("#modal-holiday .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create holiday
    $(".js-create-holiday").click(loadForm);
    $("#modal-holiday").on("submit", ".js-holiday-create-form", saveForm);

    // Update holiday
    $("#holiday-table").on("click", ".js-update-holiday", loadForm);
    $("#modal-holiday").on("submit", ".js-holiday-update-form", saveForm);


    // Delete holiday
    $("#holiday-table").on("click", ".js-delete-holiday", loadForm);
    $("#modal-holiday").on("submit", ".js-holiday-delete-form", saveForm);

});