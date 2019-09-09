$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-hostel_member").modal("show");
            },
            success: function (data) {
                $("#modal-hostel_member .modal-content").html(data.html_form);
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
                    $("#hostel_member-table tbody").html(data.html_hostel_member_list);
                    $("#modal-hostel_member").modal("hide");
                } else {
                    $("#modal-hostel_member .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create hostel_member
    $(".js-create-hostel_member").click(loadForm);
    $("#modal-hostel_member").on("submit", ".js-hostel_member-create-form", saveForm);

    // Update hostel_member
    $("#hostel_member-table").on("click", ".js-update-hostel_member", loadForm);
    $("#modal-hostel_member").on("submit", ".js-hostel_member-update-form", saveForm);


    // Delete hostel_member
    $("#hostel_member-table").on("click", ".js-delete-hostel_member", loadForm);
    $("#modal-hostel_member").on("submit", ".js-hostel_member-delete-form", saveForm);

});