

$(document).ready(function(){
    parallax.add("register", $("#register-page"));
    parallax.add("login", $("#login-page"));
    parallax.login.bottom();
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

    $('#create-account').click(function(){
      parallax.register.bottom(); //We got callbacks too ;)
    })
    $('#login-account').click(function(){
      parallax.login.top(); //We got callbacks too ;)
    })
});