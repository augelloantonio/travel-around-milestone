// Materialize Customiztions

// Add the collapse to the navbar button
$(".button-collapse").sideNav();

// Add the tooltip
$(document).ready(function() {
    $('.tooltipped').tooltip();
});


// Add select function
$(document).ready(function() {
    $('select').toggle();
});

$('.carousel.carousel-slider').carousel({
    fullWidth: true
});


// Matezialize box
$(document).ready(function() {
    $('.materialboxed').materialbox();
});

// Materialize Modal
$(document).ready(function() {
    $('.modal').modal();
});