$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-exam_suggestion").modal("show");
            },
            success: function (data) {
                $("#modal-exam_suggestion .modal-content").html(data.html_form);
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
                    $("#exam_suggestion-table tbody").html(data.html_exam_suggestion_list);
                    $("#modal-exam_suggestion").modal("hide");
                } else {
                    $("#modal-exam_suggestion .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create exam_suggestion
    $(".js-create-exam_suggestion").click(loadForm);
    $("#modal-exam_suggestion").on("submit", ".js-exam_suggestion-create-form", saveForm);

    // Update exam_suggestion
    $("#exam_suggestion-table").on("click", ".js-update-exam_suggestion", loadForm);
    $("#modal-exam_suggestion").on("submit", ".js-exam_suggestion-update-form", saveForm);


    // Delete exam_suggestion
    $("#exam_suggestion-table").on("click", ".js-delete-exam_suggestion", loadForm);
    $("#modal-exam_suggestion").on("submit", ".js-exam_suggestion-delete-form", saveForm);

});