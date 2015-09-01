//select the 


$(document).ready(function() {
   
    var add_saved_meals_btn = $("#add_saved_meals_btn");

    add_saved_meals_btn.click(function(){
        var meal_name = $('input[name=meal_name]').val();
        console.log(meal_name);
        $.post("/food_log/add_saved_meal?meal_name=" + meal_name, function( data )
            {
                $("#food_log_table").append(data)
            });
       
    });
});