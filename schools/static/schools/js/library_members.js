$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-library_member").modal("show");
            },
            success: function (data) {
                $("#modal-library_member .modal-content").html(data.html_form);
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
                    $("#library_member-table tbody").html(data.html_library_member_list);
                    $("#modal-library_member").modal("hide");
                } else {
                    $("#modal-library_member .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create library_member
    $(".js-create-library_member").click(loadForm);
    $("#modal-library_member").on("submit", ".js-library_member-create-form", saveForm);

    // Update library_member
    $("#library_member-table").on("click", ".js-update-library_member", loadForm);
    $("#modal-library_member").on("submit", ".js-library_member-update-form", saveForm);


    // Delete library_member
    $("#library_member-table").on("click", ".js-delete-library_member", loadForm);
    $("#modal-library_member").on("submit", ".js-library_member-delete-form", saveForm);

});