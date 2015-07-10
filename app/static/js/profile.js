$(document).ready(function() {
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
        //$ in javascript is a query to find a subset of a DOM, or object. Usually a class or an id.
        //"$" gives us html elements.
        //to query for anelement, 
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