$(document).ready(function() {
   
    var date_input = $("#date");

    date_input.change(function(){
        var date = date_input.val();
        date = date.replace(/-/g, "/")
        console.log(date) 
        window.location = "/food_log/" + date   
    });
});