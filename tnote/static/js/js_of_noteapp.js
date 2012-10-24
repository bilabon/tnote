$(function() {
    $("label[for='id_text']").html("Text: 0")
    $("textarea[id='id_text']").keyup(function count(){
    number = $("textarea[id='id_text']").val().length;
    $("label[for='id_text']").html("Text: "+number)
        ;})
        ;})

function display_form_errors(errors, $form) {
    for (var k in errors) {
        $form.find('.error_list').after('<div class="alert alert-block"><button type="button" class="close" data-dismiss="alert">×</button><strong>Warning! </strong> '+errors[k]+'</div>');
    }
}

$(document).ready(function() {
    $('#push_form').live('click', function() {
        $('#add_form').ajaxSubmit({
            success: function(data, statusText, xhr, $form) {
                // remove errors
                $form.find('.alert').remove();
                if (data['result'] == 'success') {
                    $('#id_text').val('');
                    $("label[for='id_text']").html("Text: 0")
                    $form.find('.error_list').after('<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert">×</button><strong>'+data['response']+ '</strong></div>');
                }
                else if (data['result'] == 'error') {
                    // display errors
                    display_form_errors(data['response'], $form);
                }
            },
            dataType: 'json'
        });
    });
}
)
