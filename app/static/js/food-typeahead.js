$(document).ready(function() {
    //https://github.com/twitter/typeahead.js/blob/master/src/bloodhound/options_parser.js
    //bloodhound is a typeahead.js user suggestion engine.
    //bloodhound makes get request to the server to best match to what we typed.
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
            /*function prepareByReplace(query, settings) {
      settings.url = replace(settings.url, query);
      return settings;
    }*/
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
                /*Tells what url we are going to.*/
                return url + query + groups_string


                
                }


            }
    });
    //created the variable foodEnterred. 
    //initialize function initializes the engine.
    foodEnterred.initialize();

    //typeahead user interface section.
    /*find the element with the class typeahead.*/ 
    // $ is a function selects elements of my DOM
    var input = $('.food-typeahead');


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
            option.text(unit.amount + " " + unit.name + " (" + unit.Gm_Wgt + "g)");
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
                /*$("#units").prop('disabled', false);
                $("#quantity-input").prop('disabled', false);*/
                return;
            }
        }
        /*$("#units").prop('disabled', true);
        $("#quantity-input").prop('disabled', true);*/
        input.val("");
    }.bind(null, foodEnterred));
});
