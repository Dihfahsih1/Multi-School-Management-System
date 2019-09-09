$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-income_head").modal("show");
            },
            success: function (data) {
                $("#modal-income_head .modal-content").html(data.html_form);
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
                    $("#income_head-table tbody").html(data.html_income_head_list);
                    $("#modal-income_head").modal("hide");
                } else {
                    $("#modal-income_head .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create income_head
    $(".js-create-income_head").click(loadForm);
    $("#modal-income_head").on("submit", ".js-income_head-create-form", saveForm);

    // Update income_head
    $("#income_head-table").on("click", ".js-update-income_head", loadForm);
    $("#modal-income_head").on("submit", ".js-income_head-update-form", saveForm);


    // Delete income_head
    $("#income_head-table").on("click", ".js-delete-income_head", loadForm);
    $("#modal-income_head").on("submit", ".js-income_head-delete-form", saveForm);

});