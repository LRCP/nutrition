$(document).ready(function() {
    //The dollar sign is a jquery element selector.
    //In this part of the code, the selector is selecting the class multiselect allows us to 
    //select the food groups
    
    
    
    
    
    
    

    var food_row = $(".food_row");
    //console. log is similar to print in python used for debugging.
    //console.log(food_row)
    // $ searches for an element on the page, reutrns it to javascript
    // and lets me use it. alert is a function built into javascipt.
    // alert will pop up a message.
    food_row.click(function() {
        $( this ).toggleClass( "highlight");
        
    });
    //select btn
    //create the btn variables to correspond to the html button.
    var save_meal_btn = $("#save_meal_btn");
    var save_changes_btn = $("#save_changes_btn");

    //do something when you click on the btn
    //create a variable for selected_food_rows
    save_meal_btn.click(function(){
        var selected_food_rows = $(".food_row.highlight");
         //if food_rows are highlighted, then open the save_meal modal.
        if (selected_food_rows.length !== 0){
            $('#save_meal').modal();
            
        }
        //else if no food_rows are highlighted, then open the error_meal modal.
        else {
            $('#error_meal').modal();
            
        }
       

    });
    save_changes_btn.click(function(){
        //selects the foods rows that have been highlighted
        var selected_food_rows = $(".food_row.highlight");

        
        var selected_foods = "";
        selected_food_rows.each(function(index, selected_food_row){
            selected_foods += $(selected_food_row).data("association-id");
                selected_foods += ',';
        });
        

        //un-highlight selected_foods_rows
        selected_food_rows.removeClass("highlight")

        //console.log is a debugging technique
        //console.log(selected_foods)
        //post request to the url food_log/saved_meal
        // post connects the front end, browser, to the back end, python code
        // the query string matches up to the request.args.get('selected_foods')
        //selected_foods is a list of ids for the selected foods.
        //javascrit makes a posting request to python/terminal
        //to return or get the value of the element, 
        //or what has been typed in as save_meal, use .val()
        var meal_name_input = $('div#save_meal [name="meal"]');

        //meal_name is a copy of the immutable string returned by meal_name_input.val()
        var meal_name = meal_name_input.val() 
        //console.log(meal_name)


        //we are making a post request for 2 pieces of information to other server.
        //meal_name is a string
        //selected_foods are integers of the id of the food in the food_log_food_association
        $.post("/food_log/saved_meal?meal_name=" + meal_name + "&selected_foods=" + selected_foods);
        //changing meal_name_input.val() won't change meal_name and visa-versa.
        meal_name_input.val("")
    });



    
});
