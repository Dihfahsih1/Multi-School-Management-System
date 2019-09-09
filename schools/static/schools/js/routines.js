$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-routine").modal("show");
            },
            success: function (data) {
                $("#modal-routine .modal-content").html(data.html_form);
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
                    $("#routine-table tbody").html(data.html_routine_list);
                    $("#modal-routine").modal("hide");
                } else {
                    $("#modal-routine .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create routine
    $(".js-create-routine").click(loadForm);
    $("#modal-routine").on("submit", ".js-routine-create-form", saveForm);

    // Update routine
    $("#routine-table").on("click", ".js-update-routine", loadForm);
    $("#modal-routine").on("submit", ".js-routine-update-form", saveForm);


    // Delete routine
    $("#routine-table").on("click", ".js-delete-routine", loadForm);
    $("#modal-routine").on("submit", ".js-routine-delete-form", saveForm);

});