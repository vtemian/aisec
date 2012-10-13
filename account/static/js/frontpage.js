$(document).ready(function(){
    $('#mustFixIt').live('click' , function(){
        $('#notifications_bar').html("We will fix that soon!").slideDown(200).delay(1000);
    });
    $('#reset-a').click(function(){
        $('#reset-password').modal({
            onOpen: function (dialog) {
                var sm = this;

                dialog.overlay.fadeIn('fast', function () {
                    dialog.data.hide();
                    dialog.container.fadeIn('fast', function () {
                        dialog.data.slideDown('fast');
                    });
                });
                dialog.container.animate({height: 100, width: 300}, 500, function () {
                    sm.setPosition();
                });
            },
            onClose: function (dialog) {
                dialog.data.fadeOut('fast', function () {
                    dialog.container.hide('fast', function () {
                        dialog.overlay.slideUp('fast', function () {
                            $.modal.close();
                        });
                    });
                });
            }
        });
    });
    $('#reset-form').submit(function(){
        var $form = $(this);
        $.modal.close();
        $('#notifications_bar').html("Reseting password...").slideDown(200).delay(1000).slideUp(200);
        $.post($form.attr('action'), $form.serializeArray(), function(data){
            data = $.parseJSON(data);
            $('#notifications_bar').html(data.message).slideDown(200).delay(1000).slideUp(200);
        });
        return false;
    });
    $('#tour-a').click(function(){
        $('#tour-flash').modal({
            onOpen: function (dialog) {
                var sm = this;

                dialog.overlay.fadeIn('fast', function () {
                    dialog.data.hide();
                    dialog.container.fadeIn('fast', function () {
                        dialog.data.slideDown('fast');
                    });
                });
                dialog.container.animate({height: 403, width: 550}, 500, function () {
                    sm.setPosition();
                });
            },
            onClose: function (dialog) {
                dialog.data.fadeOut('fast', function () {
                    dialog.container.hide('fast', function () {
                        dialog.overlay.slideUp('fast', function () {
                            $.modal.close();
                        });
                    });
                });
            }
        });
    });
});