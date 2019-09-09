$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-exam").modal("show");
            },
            success: function (data) {
                $("#modal-exam .modal-content").html(data.html_form);
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
                    $("#exam-table tbody").html(data.html_exam_list);
                    $("#modal-exam").modal("hide");
                } else {
                    $("#modal-exam .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create exam
    $(".js-create-exam").click(loadForm);
    $("#modal-exam").on("submit", ".js-exam-create-form", saveForm);

    // Update exam
    $("#exam-table").on("click", ".js-update-exam", loadForm);
    $("#modal-exam").on("submit", ".js-exam-update-form", saveForm);


    // Delete exam
    $("#exam-table").on("click", ".js-delete-exam", loadForm);
    $("#modal-exam").on("submit", ".js-exam-delete-form", saveForm);

});