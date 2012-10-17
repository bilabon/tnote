$(function() {
    $("textarea[id='id_text']").keyup(function count(){
    number = $("textarea[id='id_text']").val().length;
    $("label[for='id_text']").html("Text("+number+"): ")
        ;})
        ;})
