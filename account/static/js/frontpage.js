

$(document).ready(function(){

    var login = true;
    $('#login-trigger').click(function(){
        $('#login').modal({
            onOpen: function (dialog) {
                var sm = this;
                dialog.overlay.slideDown('fast', function () {
                    dialog.data.hide();
                    dialog.container.slideDown('fast', function () {
                        dialog.data.slideDown('fast');
                    });
                });
                dialog.container.animate({height: 300, width: 600}, 500, function () {
                    sm.setPosition();
                });
            },
            onClose: function (dialog) {
                dialog.data.slideUp('fast', function () {
                    dialog.container.hide('fast', function () {
                        dialog.overlay.slideUp('fast', function () {
                            $.modal.close();
                        });
                    });
                });
            }
        });
    });
    $('#register-trigger').click(function(){
        $('#register').modal({
            onOpen: function (dialog) {
                var sm = this;
                console.log(dialog.container)
                dialog.overlay.slideDown('fast', function () {
                    dialog.data.hide();
                    dialog.container.slideDown('fast', function () {
                        dialog.data.slideDown('fast');
                    });
                });
                dialog.container.animate({height:355, width: 600}, 500, function () {
                    sm.setPosition();
                });
            },
            onClose: function (dialog) {
                dialog.data.slideUp('fast', function () {
                    dialog.container.hide('fast', function () {
                        dialog.overlay.slideUp('fast', function () {
                            $.modal.close();
                        });
                    });
                });
            }
        });
    })

    $('.fb_login').click(function(){
       window.location='/facebook/login';
    });
});