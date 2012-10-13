$(document).ready(function(){
    $('#signup').click(function(){
        $('#sign_up_form').submit();
    })
    $('#sign_up_form').submit(function() {
        validate($(this));
        return false;
    });
});