$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-transport_member").modal("show");
            },
            success: function (data) {
                $("#modal-transport_member .modal-content").html(data.html_form);
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
                    $("#transport_member-table tbody").html(data.html_transport_member_list);
                    $("#modal-transport_member").modal("hide");
                } else {
                    $("#modal-transport_member .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create transport_member
    $(".js-create-transport_member").click(loadForm);
    $("#modal-transport_member").on("submit", ".js-transport_member-create-form", saveForm);

    // Update transport_member
    $("#transport_member-table").on("click", ".js-update-transport_member", loadForm);
    $("#modal-transport_member").on("submit", ".js-transport_member-update-form", saveForm);


    // Delete transport_member
    $("#transport_member-table").on("click", ".js-delete-transport_member", loadForm);
    $("#modal-transport_member").on("submit", ".js-transport_member-delete-form", saveForm);

});