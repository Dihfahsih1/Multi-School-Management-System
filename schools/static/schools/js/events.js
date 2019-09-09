$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-event").modal("show");
            },
            success: function (data) {
                $("#modal-event .modal-content").html(data.html_form);
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
                    $("#event-table tbody").html(data.html_event_list);
                    $("#modal-event").modal("hide");
                } else {
                    $("#modal-event .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create event
    $(".js-create-event").click(loadForm);
    $("#modal-event").on("submit", ".js-event-create-form", saveForm);

    // Update event
    $("#event-table").on("click", ".js-update-event", loadForm);
    $("#modal-event").on("submit", ".js-event-update-form", saveForm);


    // Delete event
    $("#event-table").on("click", ".js-delete-event", loadForm);
    $("#modal-event").on("submit", ".js-event-delete-form", saveForm);

});