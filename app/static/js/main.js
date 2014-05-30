$(document).ready(function() {
    $('.multiselect').multiselect({    
        includeSelectAllOption: true, 
        enableFiltering: true, 
        filterBehavior: 'both', 
        enableCaseInsensitiveFiltering: true
    });
    var datums = [];
    var foodEnterred = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
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

        var input = $('.typeahead');



        input.typeahead({autoselect: true}, {
            name: 'food-enterred',
            displayKey: 'value',
            source: foodEnterred.ttAdapter()
        });
        /*The blur function cause the text to disappear if the full
        name of the food is not selected*/
        
        input.blur(function(engine, event) {
            var input = $(event.target);
            
 
            for (var i = 0; i < datums.length; i++) {
                var datum = datums[i];
                if (input.val().toLowerCase() == datum.value.toLowerCase()) {
                    return;
                }
            }
            input.val("");
        }.bind(null, foodEnterred));
       
    })