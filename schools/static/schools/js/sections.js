$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-section").modal("show");
            },
            success: function (data) {
                $("#modal-section .modal-content").html(data.html_form);
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
                    $("#section-table tbody").html(data.html_section_list);
                    $("#modal-section").modal("hide");
                } else {
                    $("#modal-section .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create section
    $(".js-create-section").click(loadForm);
    $("#modal-section").on("submit", ".js-section-create-form", saveForm);

     // view section
     $("#section-table").on("click", ".js-view-section", loadForm);
    $("#modal-section").on("submit", ".js-section-view-form", saveForm);

    // Update section
    $("#section-table").on("click", ".js-update-section", loadForm);
    $("#modal-section").on("submit", ".js-section-update-form", saveForm);

    // Delete section
    $("#section-table").on("click", ".js-delete-section", loadForm);
    $("#modal-section").on("submit", ".js-section-delete-form", saveForm);

});