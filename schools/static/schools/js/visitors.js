$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-visitor").modal("show");
            },
            success: function (data) {
                $("#modal-visitor .modal-content").html(data.html_form);
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
                    $("#visitor-table tbody").html(data.html_visitor_list);
                    $("#modal-visitor").modal("hide");
                } else {
                    $("#modal-visitor .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create visitor
    $(".js-create-visitor").click(loadForm);
    $("#modal-visitor").on("submit", ".js-visitor-create-form", saveForm);

    // Update visitor
    $("#visitor-table").on("click", ".js-update-visitor", loadForm);
    $("#modal-visitor").on("submit", ".js-visitor-update-form", saveForm);


    // Delete visitor
    $("#visitor-table").on("click", ".js-delete-visitor", loadForm);
    $("#modal-visitor").on("submit", ".js-visitor-delete-form", saveForm);

});