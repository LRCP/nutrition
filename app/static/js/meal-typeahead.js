$(document).ready(function() {
    //bloodhound is a typeahead.js user suggestion engine.
    //bloodhound makes get request to the server to best match to what we typed.
    var datums = [];
    var mealEnterred = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        limit: 50,
        remote: {
            //this is the route to retrieve info in the saved_meals function
            //url: '/saved_meals/SPAM.json',
            url: "saved_meals.json?q=SPAM",
            //change app.route to @app.route("saved_meals.json")
            //then type into browser url:"/saved_meals.json?=SPAM",
            'cache': false,

            /*filter code is saving the data as datums variable so that we can use it later.*/
            filter: function(data) {
                datums = data;
                //to debug console.log("Data", data);
                return data;
            },
            //The word "SPAM" becomes what the user is searching for.
            //https://github.com/twitter/typeahead.js/blob/master/doc/bloodhound.md
            wildcard: "SPAM"

            
        }
    });
    //created the variable foodEnterred. 
    //initialize function initializes the engine.
    mealEnterred.initialize();
    //to debug:console.log(mealEnterred)
    
    //typeahead user interface section.
    //the variable input is tied to the element with the class meal-typeahead.*/ 
    // $ is a function selects elements of my DOM
    var input = $('.meal-typeahead');
    //to debug console.log("saved meal", input)


    /*sets up typeahead*/
    input.typeahead({autoselect: true}, {
        name: 'meal-enterred',
        /*displayKey will display the value associated with the name key.
        The name key is part of the suggestion object reurned from the server.
        */
        displayKey: function(suggestion){
            //to debug console.log("name", suggestion.name);
            
            return suggestion.name;
        },
        /* need something in addition to displayKey: 'units'*/
        source: mealEnterred.ttAdapter()
    });

    

    /*The blur function cause the text to disappear if the full
    name of the food is not selected*/
    /*when the imput loses focus, run the function we pass to the blur function.*/

    /*input.on("blur", function() {})
    THe argument event is passes into input.blur*/
    input.blur(function(event) {
        /*our variable input inside the function is 
        the same as the variable outside the function.*/
        var input = $(event.target);
        /*looping over the datums, the options for the food
        we may want.
        similar to for datum in datums
        daturm refers to the aray Datums at the index.*/
        for (var i = 0; i < datums.length; i++) {
            var datum = datums[i];
            /*if what we typed in is one of the options, do nothing and we are good to go
            input.val()is a jquery function*/
            if (input.val().toLowerCase() == datum.name.toLowerCase()) {           
                /*We are not returning anything*/
                return;
            }
        }
        /*This sets the iput.val to an empty string.*/
        input.val("");
    
    });
});