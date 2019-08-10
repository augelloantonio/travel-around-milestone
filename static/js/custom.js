//Function to display my search form on click

// 
$(document).ready(function() {
    $('#search_icon').click(function() {
        $('#search_form').toggle();
    });
});


// Function to add a new line to add a new must see in my database
function addMustSee() {
    var addMustSee = '<textarea name="city_must_see" id="city_must_see" class="materialize-textarea" required> </textarea>'
    $("#add_new_must_see").before(addMustSee)
}


// Function to add a new line to add a new tip in my database
function addTips() {
    var addTips = '<textarea name="city_tips" id="city_tips" class="materialize-textarea" required></textarea>'
    $("#add_new_tips").before(addTips)
}




// Materialize Customiztions

// Add the collapse to the navbar button
$(".button-collapse").sideNav();

// Add the tooltip
$(document).ready(function() {
    $('.tooltipped').tooltip();
});

// Add the collpase to the search box
$(document).ready(function() {
    $('#search_cities').collapsible();
});

// Add select function
$(document).ready(function() {
    $('select').toggle();
});

// Add carousel function
$(document).ready(function() {
    $('.carousel').carousel();
});

// Matezialize box
$(document).ready(function() {
    $('.materialboxed').materialbox();
});
