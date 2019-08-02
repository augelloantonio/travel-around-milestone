//Function to display my search form on click

$(document).ready(function() {
    $('#search_icon').click(function() {
        $('#search_form').toggle();
    });
});


// Materialize Customiztions
$(".button-collapse").sideNav();

$(document).ready(function() {
    $('.tooltipped').tooltip();
});

$(document).ready(function() {
    $('#search_cities').collapsible();
});

$(document).ready(function() {
    $('.carousel').carousel();
});
