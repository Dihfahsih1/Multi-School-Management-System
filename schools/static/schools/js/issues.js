$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-issue").modal("show");
            },
            success: function (data) {
                $("#modal-issue .modal-content").html(data.html_form);
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
                    $("#issue-table tbody").html(data.html_issue_list);
                    $("#modal-issue").modal("hide");
                } else {
                    $("#modal-issue .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create issue
    $(".js-create-issue").click(loadForm);
    $("#modal-issue").on("submit", ".js-issue-create-form", saveForm);

    // Update issue
    $("#issue-table").on("click", ".js-update-issue", loadForm);
    $("#modal-issue").on("submit", ".js-issue-update-form", saveForm);


    // Delete issue
    $("#issue-table").on("click", ".js-delete-issue", loadForm);
    $("#modal-issue").on("submit", ".js-issue-delete-form", saveForm);

});