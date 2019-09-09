$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-hostel").modal("show");
            },
            success: function (data) {
                $("#modal-hostel .modal-content").html(data.html_form);
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
                    $("#hostel-table tbody").html(data.html_hostel_list);
                    $("#modal-hostel").modal("hide");
                } else {
                    $("#modal-hostel .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create hostel
    $(".js-create-hostel").click(loadForm);
    $("#modal-hostel").on("submit", ".js-hostel-create-form", saveForm);

    // Update hostel
    $("#hostel-table").on("click", ".js-update-hostel", loadForm);
    $("#modal-hostel").on("submit", ".js-hostel-update-form", saveForm);


    // Delete hostel
    $("#hostel-table").on("click", ".js-delete-hostel", loadForm);
    $("#modal-hostel").on("submit", ".js-hostel-delete-form", saveForm);

});