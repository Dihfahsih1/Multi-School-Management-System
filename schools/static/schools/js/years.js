$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-year").modal("show");
            },
            success: function (data) {
                $("#modal-year .modal-content").html(data.html_form);
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
                    $("#year-table tbody").html(data.html_year_list);
                    $("#modal-year").modal("hide");
                } else {
                    $("#modal-year .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create year
    $(".js-create-year").click(loadForm);
    $("#modal-year").on("submit", ".js-year-create-form", saveForm);

    // Update year
    $("#year-table").on("click", ".js-update-year", loadForm);
    $("#modal-year").on("submit", ".js-year-update-form", saveForm);


    // Delete year
    $("#year-table").on("click", ".js-delete-year", loadForm);
    $("#modal-year").on("submit", ".js-year-delete-form", saveForm);

});