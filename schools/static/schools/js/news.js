$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-news").modal("show");
            },
            success: function (data) {
                $("#modal-news .modal-content").html(data.html_form);
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
                    $("#news-table tbody").html(data.html_news_list);
                    $("#modal-news").modal("hide");
                } else {
                    $("#modal-news .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create news
    $(".js-create-news").click(loadForm);
    $("#modal-news").on("submit", ".js-news-create-form", saveForm);

    // Update news
    $("#news-table").on("click", ".js-update-news", loadForm);
    $("#modal-news").on("submit", ".js-news-update-form", saveForm);


    // Delete news
    $("#news-table").on("click", ".js-delete-news", loadForm);
    $("#modal-news").on("submit", ".js-news-delete-form", saveForm);

});