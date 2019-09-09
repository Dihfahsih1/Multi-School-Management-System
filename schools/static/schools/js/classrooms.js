$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-classroom").modal("show");
            },
            success: function (data) {
                $("#modal-classroom .modal-content").html(data.html_form);
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
                    $("#classroom-table tbody").html(data.html_classroom_list);
                    $("#modal-classroom").modal("hide");
                } else {
                    $("#modal-classroom .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create classroom
    $(".js-create-classroom").click(loadForm);
    $("#modal-classroom").on("submit", ".js-classroom-create-form", saveForm);

     // view classroom
     $("#classroom-table").on("click", ".js-view-classroom", loadForm);
    $("#modal-classroom").on("submit", ".js-classroom-view-form", saveForm);

    // Update classroom
    $("#classroom-table").on("click", ".js-update-classroom", loadForm);
    $("#modal-classroom").on("submit", ".js-classroom-update-form", saveForm);

    // Delete classroom
    $("#classroom-table").on("click", ".js-delete-classroom", loadForm);
    $("#modal-classroom").on("submit", ".js-classroom-delete-form", saveForm);

});