function display_alert_errors(errors, $form, typealert){
    for (var k in errors){
        $form.find('#id_'+k+'_error').after('<p><div class="error"><span class="label label-important">' + errors[k] + '</span></div></p>');
    }
}

function display_alert_success(alert, $form, typealert){
    $('#notification').after('<div class="alert '+typealert+'"><button type="button" class="close" data-dismiss="alert">×</button><b>' + alert + '</b></div>');
}

$(document).ready(function() {
    document.getElementById('sbmtypeid').setAttribute('type','button');
    $('#id_text').after('<input id="Reset" type="reset" style="display:none">');
    $('#push_form').live('click', function(){
        var status = $('#status');
        $('#add_form').ajaxSubmit({
            complete: function(xhr) {
                status.html(xhr.responseText);
            },
            success: function(data, statusText, xhr, $form) {
                $form.find('.error').remove();
                
                if (data['result'] == 'success') {
                    $('#Reset').click();
                    $("textarea[id='id_text']").click();
                    $('.alert').remove();
                    $form.find('#image_remove').click();
                    display_alert_success(data['response'], $form,'alert-success');
                }
                else if (data['result'] == 'error') {
                    $form.find('.error').remove();
                    display_alert_errors(data['response'], $form, 'alert-block');
                }
            },
            dataType: 'json'
        })
    })
})
