$(function() {
    $("label[for='id_text']").html("Text: 0");
    $("textarea[id='id_text']").click();
    $("label[for='id_text']").html("Text: " + $("textarea[id='id_text']").val().length);
    $("textarea[id='id_text']").bind('change click keyup', function count() {
        number = $("textarea[id='id_text']").val().length;
        $("label[for='id_text']").html("Text: " + number);
    })
    ;
})

function tstFile(val) {
    var v = val.value;
    if (v != 0) {
        $('#pushimg').click();
    }

}

function display_form_errors(errors, $form) {
    for (var k in errors) {
        $form.find('.error_list').after('<div class="alert alert-block"><button type="button" class="close" data-dismiss="alert">×</button><strong>Warning! </strong> ' + errors[k] + '</div>');
    }
}

$(document).ready(function() {
    
    $('#push_form').live('click', function() {
        var bar = $('.bar');
        var percent = $('.percent');
        var status = $('#status');
        
        $('#add_form').ajaxSubmit({
            beforeSend: function() {
                status.empty();
                var percentVal = '0%';
                bar.width(percentVal)
                percent.html(percentVal);
            },
            uploadProgress: function(event, position, total, percentComplete) {
                var percentVal = percentComplete + '%';
                bar.width(percentVal)
                percent.html(percentVal);
            },
            complete: function(xhr) {
                status.html(xhr.responseText);
            },
            success: function(data, statusText, xhr, $form) {
                // remove errors
                $form.find('.alert').remove();
                if (data['result'] == 'success') {
                    $('#id_text').val('');
                    //$('#Reset').click();
                    $("label[for='id_text']").html("Text: 0")
                    $form.find('.error_list').after('<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert">×</button><strong>' + data['response'] + '</strong></div>');
                
                } 
                else if (data['result'] == 'error') {
                    // display errors
                    display_form_errors(data['response'], $form);
                }
            },
            dataType: 'json'
        });
    
    });


    //*-----------------------*/

    $('#push_formimg').live('click', function() {
        var bar = $('.bar');
        var percent = $('.percent');
        var status = $('#status');
        $('#add_formimg').ajaxSubmit({
            beforeSend: function() {
                status.empty();
                var percentVal = '0%';
                bar.width(percentVal)
                percent.html(percentVal);
            },
            uploadProgress: function(event, position, total, percentComplete) {
                var percentVal = percentComplete + '%';
                bar.width(percentVal)
                percent.html(percentVal);
            },
            complete: function(xhr) {
                status.html(xhr.responseText);
            },
            success: function(data, statusText, xhr, $form) {
                // remove errors
                $form.find('.alert').remove();
                if (data['result'] == 'success') {
                    $('#id_text').val($('#id_text').val() + '<img src="..' + data['imagefileurl'] + '"class="img-polaroid" width="100" height="100" />');
                    $('#Resetimg').click();
                    $("textarea[id='id_text']").click();
                    $form.find('.error_list').after('<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert">×</button><strong>' + data['response'] + '</strong></div>');
                } 
                else if (data['result'] == 'error') {
                    // display errors
                    display_form_errors(data['response2'], $form);
                }
            },
            dataType: 'json'
        });
    });
//*-----------------------*/
}
)
