if (document.getElementById){
    $(function() {
        $("textarea[id='id_text']").click();
        $("label[for='id_text']").html("<b>Text:</b> " + $("textarea[id='id_text']").val().length);
        $("textarea[id='id_text']").bind('change click keyup', function count(){
        number = $("textarea[id='id_text']").val().length;
        $("label[for='id_text']").html("<b>Text:</b> "+number);
        })
    })
}
