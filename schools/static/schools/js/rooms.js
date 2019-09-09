$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-room").modal("show");
            },
            success: function (data) {
                $("#modal-room .modal-content").html(data.html_form);
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
                    $("#room-table tbody").html(data.html_room_list);
                    $("#modal-room").modal("hide");
                } else {
                    $("#modal-room .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create room
    $(".js-create-room").click(loadForm);
    $("#modal-room").on("submit", ".js-room-create-form", saveForm);

    // Update room
    $("#room-table").on("click", ".js-update-room", loadForm);
    $("#modal-room").on("submit", ".js-room-update-form", saveForm);


    // Delete room
    $("#room-table").on("click", ".js-delete-room", loadForm);
    $("#modal-room").on("submit", ".js-room-delete-form", saveForm);

});