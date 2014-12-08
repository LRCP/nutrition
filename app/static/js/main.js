// http://davidstutz.github.io/bootstrap-multiselect/#further-examples
$(document).ready(function() {
    $('.multiselect').multiselect({    
        includeSelectAllOption: true, 
        onChange: function(option, checked, select) {
            var selectedOptions = $('.multiselect option:selected');
            var selected_food_groups = "";
            selectedOptions.each(function(index, selectedOption){
                selected_food_groups += $(selectedOption).val();
                selected_food_groups += ',';
            });
            console.log(selected_food_groups);
            // need to add the selected food
            $.post("/food_log/selected_food_groups?food_groups=" + selected_food_groups);

        }
    });
    var datums = [];
    var foodEnterred = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        limit: 50,
        remote: {
            url: '/queries/',
            /*filter code is saving the data as datums variable so that we can use it later.*/
            filter: function(data) {
                datums = data;
                return data;
            },
            /*replace code is adding the group codes to the query.*/
            replace: function(url, query) {
                // we got the food_group_select from the food_log.html
                var select1 = document.getElementById("food_group_select");
                    var groups_string = ".json?";
                    for (var i = 1; i < select1.length; i++) {
                        if (select1.options[i].selected ) {


                            groups_string = groups_string + "group=" + select1.options[i].value;
                            if (i != select1.length-1) {
                                groups_string = groups_string + "&";
                            }
                        }; 

                    }
               
                console.log(groups_string)  
                return url + query + groups_string


                
                }


            }
    });

    foodEnterred.initialize();
    /*find the element with the class typeahead.*/ 
    // $ is a function selects elements of my DOM
    var input = $('.typeahead');


    /*sets up typeahead*/
    input.typeahead({autoselect: true}, {
        name: 'food-enterred',
        /*displayKey should be adding the units and should tell us
        suggestion object dictionary, containing the names, 
        values, and unit_list is appended to the food_list.
        */
        displayKey: function(suggestion){
            console.log(suggestion.name);
            
            return suggestion.name;
        },
        /* need something in addition to displayKey: 'units'*/
        source: foodEnterred.ttAdapter()
    });

    input.on("typeahead:selected",function(event, suggestion, dataset) {
       $("#units").empty()
        for (var i = 0; i < suggestion.units.length; i++) {
            var unit = suggestion.units[i];
            var option = $("<option>");
            option.text(unit.name);
            option.attr("value", JSON.stringify(unit));
            $("#units").append(option);
        } 
    });

    /*The blur function cause the text to disappear if the full
    name of the food is not selected*/
    /*when the imput loses focus, run the function we pass to the blur function.*/

    /*input.on("blur", function() {})*/
    input.blur(function(engine, event) {
        /*our variable input inside the function is 
        the same as the variable outside the function.*/
        var input = $(event.target);
        /*looping over the datums, the options for the food
        we may want.*/
        for (var i = 0; i < datums.length; i++) {
            var datum = datums[i];
            /*if what we typed in is one of the options, do nothing and we are good to go*/
            if (input.val().toLowerCase() == datum.name.toLowerCase()) {           
                $("#units").prop('disabled', false);
                $("#quantity-input").prop('disabled', false);
                return;
            }
        }
        $("#units").prop('disabled', true);
        $("#quantity-input").prop('disabled', true);
        input.val("");
    }.bind(null, foodEnterred));
    var weight_ranges = $(".weight_range");
    weight_ranges.each(function(index, range){
        var range = $(range);
        var input = range.find("input");
        input.on("input change", function(event){
            var input = $(event.target);
            var kilograms = input.val();
            var pounds = kilograms * .45;
            var stones = kilograms * 6.35;
            var kilogramsSpan = range.find(".kilograms");
            var poundsSpan = range.find(".pounds");
            var stonesSpan = range.find(".stones");
            pounds = Math.round(pounds * 4) / 4;
            kilograms = parseFloat(kilograms).toFixed(1);
            stones = stones.toFixed(2);
            poundsSpan.text(pounds + " pounds");
            kilogramsSpan.text(kilograms + " kg");
            stonesSpan.text(stones + " st");
        });
    });
    /*accessing the class in profile.html*/
    var height_ranges = $(".height_range");

    /* http://api.jquery.com/each/ */
    height_ranges.each(function(index, range){
        /* jquery loops through the html elements.*/
        /* we are converting the javascript/html element into jquery javascript/html elements*/
        var range = $(range);
        var input = range.find("input");
        input.on("input change", function(event){
            var input = $(event.target);
            var meters = input.val();
            var inches = meters * 39.37;
            var feet = Math.floor(inches / 12);
            /*in javascript, use var to declare the variable for the first time.
            thereafter, do not need the var*/
            inches = Math.round(inches % 12 *4) / 4;
            meters = parseFloat(meters).toFixed(2);
            var metersSpan = range.find(".meters");
            var feetSpan = range.find(".feet");
            metersSpan.text(meters + " m");
            feetSpan.text(feet + "'" + inches + '"');
        });
    });
   var feet_input = $("#height_in_feet");
   var inches_input = $("#height_in_inches");
   var centimeters_input = $("#height_in_centimeters");
   feet_input.on("input change", function(event){
        var inches = feet_input.val() * 12;
        inches += inches_input.val();
        var centimeters = inches / 3.937;
        centimeters_input.val(Math.round(centimeters));
   });
   inches_input.on("input change", function(event){
        var inches = feet_input.val() * 12;
        inches += inches_input.val();
        var centimeters = inches / 3.937;
        centimeters_input.val(Math.round(centimeters));
   });
   centimeters_input.on("input change", function(event){
        var centimeters = centimeters_input.val();
        var meters = centimeters / 100;
        var inches = meters * 39.37;
        var feet = Math.floor(inches / 12);
        // This returns in .5 increments
        inches = Math.round(inches % 12 *2) / 2;
        feet_input.val(feet);
        inches_input.val(inches);
        
   });
});