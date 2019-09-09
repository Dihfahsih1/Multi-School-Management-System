$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-slider").modal("show");
            },
            success: function (data) {
                $("#modal-slider .modal-content").html(data.html_form);
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
                    $("#slider-table tbody").html(data.html_slider_list);
                    $("#modal-slider").modal("hide");
                } else {
                    $("#modal-slider .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create slider
    $(".js-create-slider").click(loadForm);
    $("#modal-slider").on("submit", ".js-slider-create-form", saveForm);

    // Update slider
    $("#slider-table").on("click", ".js-update-slider", loadForm);
    $("#modal-slider").on("submit", ".js-slider-update-form", saveForm);


    // Delete slider
    $("#slider-table").on("click", ".js-delete-slider", loadForm);
    $("#modal-slider").on("submit", ".js-slider-delete-form", saveForm);

});