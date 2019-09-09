$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-guardian").modal("show");
            },
            success: function (data) {
                $("#modal-guardian .modal-content").html(data.html_form);
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
                    $("#guardian-table tbody").html(data.html_guardian_list);
                    $("#modal-guardian").modal("hide");
                } else {
                    $("#modal-guardian .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create guardian
    $(".js-create-guardian").click(loadForm);
    $("#modal-guardian").on("submit", ".js-guardian-create-form", saveForm);

     // view guardian
     $("#guardian-table").on("click", ".js-view-guardian", loadForm);
    $("#modal-guardian").on("submit", ".js-guardian-view-form", saveForm);

    // Update guardian
    $("#guardian-table").on("click", ".js-update-guardian", loadForm);
    $("#modal-guardian").on("submit", ".js-guardian-update-form", saveForm);

    // Delete guardian
    $("#guardian-table").on("click", ".js-delete-guardian", loadForm);
    $("#modal-guardian").on("submit", ".js-guardian-delete-form", saveForm);

});