$(document).ready(function(){
   $('#password-form').submit(function(){
       var $form = $(this);
       validate($form, function(data){
           console.log(data);
           if(data.message != undefined){
               setTimeout(function(){
                window.location = "/";
               }, 400);
           }
       });
       return false;
   });
});