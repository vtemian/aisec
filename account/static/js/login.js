$(document).ready(function(){
    $('#login-btn').click(function(){
       $('#login-div').modal({
           opacity:80,
			overlayCss: {backgroundColor:"#5b5b5b"},
            minHeight:400,
	        minWidth: 600,
       })
    });


    $('#login-form').ketchup({
            validateEvents: 'keyup'
    });

    $('#login-form').submit(function() {
        validate($(this));
        return false;
    });
});