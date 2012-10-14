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
            $('#tags').append('<label>'+val+'<span data-value="'+val+'" class="delete-tags"><i class="icon-remove icon-remove-custom"></i></label>');
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
  $('.delete-tags').live('click', function(){
    to_delete = $(this).data('value');
    tags.pop(to_delete);
    all_tags = $('#hidden_tags').val();
    $('#hidden_tags').val(all_tags.replace(to_delete + ';', ''));
    $(this).parent().remove();
  });
});