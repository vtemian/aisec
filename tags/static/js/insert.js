$(document).ready(function(){
  var tags = [];
  $('#id_autocomplete').keypress(function(e){
    if(e.keyCode == 13){
      val = $(this).val();
      $input = $(this);
      $.get('/tag/exists/'+val, function(result){
        if (result == 'True'){
          if ($.inArray(val, tags) == -1){
            $('#hidden_tags').val($('#hidden_tags').val() + val + ';');
            $('#tags').append('<label>'+val+'</label>');
            tags.push(val);
          }else{
            console.log('Already this tag');
          }
        }else{
          console.log('Not here!');
        }
        $input.val('');
      });
      return false;
    }
  });
});