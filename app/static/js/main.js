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
                var selected1 = [];
                    for (var i = 1; i < select1.length; i++) {
                        if (select1.options[i].selected) {selected1.push(select1.options[i].value)};                            
                    }
                console.log(selected1);
                    /*here create a for loop to loop over each element in selected1[]and add it to the string
                    .json?*/
                /* var selected1Length = selected1.length;
                 for (var i = 0; i < selected1Length, i++) }
                    return url + query + ".json?group=" + selected1[i] + ".group=selected1[selected1.length]"*/

                return url + query + ".json?group=1100&group=400"
                /*$("select.multiselect")[0].options [list of indices ranging from 1 thru 26*/
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