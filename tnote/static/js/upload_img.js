function display_alert_img(alert, $form, typealert){
    $form.find('#list_message').after('<div class="alert '+typealert+'"><button type="button" class="close" data-dismiss="alert">×</button>' + alert + '</div>');
}

function tstFile(val){
    var v = val.value;
    if (v!==false){
        $('#sbmuploadimg').click();
    }    
}

$(document).ready(function() {
    document.getElementById('sbmuploadimg').setAttribute('type','button');
    document.getElementById('sbmuploadimg').setAttribute('style','display:none');
    document.getElementById('id_imagefile').setAttribute('onchange', 'tstFile(this)');
    $('#list_message').after('<input id="Reset_form_upload_image" type="reset" style="display:none">');
    $('#push_form_upload_image').live('click', function(){
        var status = $('#status');
        $('#form_upload_image').ajaxSubmit({
            complete: function(xhr) {
                status.html(xhr.responseText);
            },
            success: function(data, statusText, xhr, $form) {
                $form.find('.alert').remove();
                $('#add_form').find('.alert').remove();
                if (data['result'] == 'success') {
                    $('#Reset_form_upload_image').click();
                    display_alert_img(data['response'], $form,'alert-success');
                    $('#id_text').val($('#id_text').val()+'<img src="..'+data['imgurl']+'" width="100" height="100" />');
                    $("textarea[id='id_text']").click();
                }
                else if (data['result'] == 'error') {
                    display_alert_img(data['response'], $form, 'alert-block');
                }
            },
            dataType: 'json'
        })
    })
})
