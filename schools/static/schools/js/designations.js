$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-designation").modal("show");
            },
            success: function (data) {
                $("#modal-designation .modal-content").html(data.html_form);
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
                    $("#designation-table tbody").html(data.html_designation_list);
                    $("#modal-designation").modal("hide");
                } else {
                    $("#modal-designation .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create designation
    $(".js-create-designation").click(loadForm);
    $("#modal-designation").on("submit", ".js-designation-create-form", saveForm);

     // view designation
     $("#designation-table").on("click", ".js-view-designation", loadForm);
    $("#modal-designation").on("submit", ".js-designation-view-form", saveForm);

    // Update designation
    $("#designation-table").on("click", ".js-update-designation", loadForm);
    $("#modal-designation").on("submit", ".js-designation-update-form", saveForm);

    // Delete designation
    $("#designation-table").on("click", ".js-delete-designation", loadForm);
    $("#modal-designation").on("submit", ".js-designation-delete-form", saveForm);

});