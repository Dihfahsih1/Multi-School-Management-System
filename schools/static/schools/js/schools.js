$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-school").modal("show");
            },
            success: function (data) {
                $("#modal-school .modal-content").html(data.html_form);
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
                    $("#school-table tbody").html(data.html_school_list);
                    $("#modal-school").modal("hide");
                } else {
                    $("#modal-school .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create school
    $(".js-create-school").click(loadForm);
    $("#modal-school").on("submit", ".js-school-create-form", saveForm);

     // view school
     $("#school-table").on("click", ".js-view-school", loadForm);
    $("#modal-school").on("submit", ".js-school-view-form", saveForm);

    // Update school
    $("#school-table").on("click", ".js-update-school", loadForm);
    $("#modal-school").on("submit", ".js-school-update-form", saveForm);

    // Delete school
    $("#school-table").on("click", ".js-delete-school", loadForm);
    $("#modal-school").on("submit", ".js-school-delete-form", saveForm);

});