$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-subject").modal("show");
            },
            success: function (data) {
                $("#modal-subject .modal-content").html(data.html_form);
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
                    $("#subject-table tbody").html(data.html_subject_list);
                    $("#modal-subject").modal("hide");
                } else {
                    $("#modal-subject .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create subject
    $(".js-create-subject").click(loadForm);
    $("#modal-subject").on("submit", ".js-subject-create-form", saveForm);

    // Update subject
    $("#subject-table").on("click", ".js-update-subject", loadForm);
    $("#modal-subject").on("submit", ".js-subject-update-form", saveForm);


    // Delete subject
    $("#subject-table").on("click", ".js-delete-subject", loadForm);
    $("#modal-subject").on("submit", ".js-subject-delete-form", saveForm);

});