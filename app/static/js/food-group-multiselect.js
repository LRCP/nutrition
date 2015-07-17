//http://davidstutz.github.io/bootstrap-multiselect/#further-examples
//https://github.com/twitter/typeahead.js/blob/master/src/bloodhound/options_parser.js

$(document).ready(function() {
    //The dollar sign is a jquery element selector.
    //In this part of the code, the selector is selecting the class multiselect allows us to 
    //select the food groups
    $('.multiselect').multiselect({    
        includeSelectAllOption: true,
        numberDisplayed: 0,
        onChange: function(option, checked, select) {
            //selecting the cild option of parent class multiselect, 
            //and only chosing the selected.
            var selectedOptions = $('.multiselect option:selected');
            var selected_food_groups = "";
            selectedOptions.each(function(index, selectedOption){
                //.val() is used to get values from form )inputs, dropdowns) elements
                var value = $(selectedOption).val();
                if (value != "multiselect-all"){
                    selected_food_groups += value;
                    selected_food_groups += ',';
                }
            });
            console.log(selected_food_groups);
            // need to add the selected food
            $.post("/food_log/selected_food_groups?food_groups=" + selected_food_groups);

        }
    });
});