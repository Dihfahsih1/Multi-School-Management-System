$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-assignment").modal("show");
            },
            success: function (data) {
                $("#modal-assignment .modal-content").html(data.html_form);
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
                    $("#assignment-table tbody").html(data.html_assignment_list);
                    $("#modal-assignment").modal("hide");
                } else {
                    $("#modal-assignment .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create assignment
    $(".js-create-assignment").click(loadForm);
    $("#modal-assignment").on("submit", ".js-assignment-create-form", saveForm);

    // Update assignment
    $("#assignment-table").on("click", ".js-update-assignment", loadForm);
    $("#modal-assignment").on("submit", ".js-assignment-update-form", saveForm);


    // Delete assignment
    $("#assignment-table").on("click", ".js-delete-assignment", loadForm);
    $("#modal-assignment").on("submit", ".js-assignment-delete-form", saveForm);

});