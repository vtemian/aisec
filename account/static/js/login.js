$(document).ready(function(){
    $('#signin').click(function(){
        $('#login-form').submit();
    });
    $('#login-form').submit(function() {
        validate($(this));
        return false;
    });
});