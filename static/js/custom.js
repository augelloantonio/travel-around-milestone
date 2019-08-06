//Function to display my search form on click

// 
$(document).ready(function() {
    $('#search_icon').click(function() {
        $('#search_form').toggle();
    });
});


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
$(document).ready(function(){
    $('.materialboxed').materialbox();
  });