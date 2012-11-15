function display_alert(alert, $form, typealert){
    $form.find('#error_list').after('<div class="alert '+typealert+'"><button type="button" class="close" data-dismiss="alert">×</button>' + alert + '</div>');
}


$(document).ready(function() {
    document.getElementById('sbmtypeid').setAttribute('type','button');
    $('#error_list').after('<input id="Reset" type="reset" style="display:none">');
    $('#push_form').live('click', function(){
        var status = $('#status');
        $('#add_form').ajaxSubmit({
            complete: function(xhr) {
                status.html(xhr.responseText);
            },
            success: function(data, statusText, xhr, $form) {
                $form.find('.alert').remove();
                if (data['result'] == 'success') {
                    $('#Reset').click();
                    $("textarea[id='id_text']").click();
                    display_alert(data['response'], $form,'alert-success');
                }
                else if (data['result'] == 'error') {
                    display_alert(data['response'], $form, 'alert-block');
                }
            },
            dataType: 'json'
        })
    })
})
