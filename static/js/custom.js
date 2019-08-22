/**
 * Function that will remove my hidden class to the html to let the page show only when fully charged
 * to prevent to show any not charged css and elements - this fix the bug that my personal style.css
 * font and styling is not fully charged at the load of the page
 */

function retard_loading() {
    $(window).on('load', function() {
        $('#loading').hide();
        autoplay();
    });
     $(document).ready(function() {
        document.getElementsByTagName("html")[0].style.visibility = "visible";
    });
}

//Function to display my search form on click
$(document).ready(function() {
    $('#search_icon').click(function() {
        $('#search_form').toggle();
    });
});


//Function to hide password from the form
function hide_password() {
    var password = document.getElementById("password");
    if (password === "password") {
        password = "text";
    }
    else {
        password = "password";
    }
}


// Function to add a new line to add and remove a new must see in my database
function addMustSee() {
    var addMustSee = '<textarea name="city_must_see" id="city_must_see" class="materialize-textarea new_mustSee" required> </textarea>'
    $("#add_new_must_see").before(addMustSee)
}

function removeMustSee() {
    $(".new_mustSee").last().remove()
}


// Function to add a new line to add a new tip in my database
function addTips() {
    var addTips = '<textarea name="city_tips" id="city_tips" class="materialize-textarea new_tips" required></textarea>'
    $("#add_new_tips").before(addTips)
}

function removeTips() {
    $(".new_tips").last().remove()
}

// Function to add a new line to add a new to avoid tips in my database
function addToAvoid() {
    var addToAvoid = '<textarea name="city_to_avoid" id="city_to_avoid" class="materialize-textarea new_to_avoid" required></textarea>'
    $("#add_new_to_avoid").before(addToAvoid)
}

function removeToAvoid() {
    $(".new_to_avoid").last().remove()
}


/**
 * Display only the section choose by the user in the User Persona Page
 * Using jQuery to hide or show clicking on the navbar the selected section
 * And on click the class of the selected nav will be added or removed to
 * help the user to see in which section it is
 */

function change_contents_made() {
    $("#to_visit").hide();
    $("#visited").hide();
    $("#made").show();
    $("#preferite").hide();
    $("#made_li").addClass("made_selected")
    $("#visited_li").removeClass("visited_selected")
    $("#to_visit_li").removeClass("to_visit_selected")
    $("#preferite_li").removeClass("preferite_selected")

}

function change_contents_to_visit() {
    $("#made").hide();
    $("#visited").hide();
    $("#to_visit").show();
    $("#preferite").hide();
    $("#made_li").removeClass("made_selected")
    $("#visited_li").removeClass("visited_selected")
    $("#to_visit_li").addClass("to_visit_selected")
    $("#preferite_li").removeClass("preferite_selected")
}

function change_contents_visited() {
    $("#visited").show();
    $("#to_visit").hide();
    $("#made").hide();
    $("#preferite").hide();
    $("#made_li").removeClass("made_selected")
    $("#visited_li").addClass("visited_selected")
    $("#to_visit_li").removeClass("to_visit_selected")
    $("#preferite_li").removeClass("preferite_selected")
}

function change_contents_preferite() {
    $("#preferite").show();
    $("#visited").hide();
    $("#to_visit").hide();
    $("#made").hide();
    $("#made_li").removeClass("made_selected")
    $("#visited_li").removeClass("visited_selected")
    $("#to_visit_li").removeClass("to_visit_selected")
    $("#preferite_li").addClass("preferite_selected")
}


// Let carousel self slide
function autoplay() {
    setTimeout()
    $('.carousel').carousel('next');
    setTimeout(autoplay, 4500);
}


/**
 * Function to verify that the user want to delete the account
 * typing 'delete'the delete button will appear
 * 
 * **/

function verification_form() {
    let input_delete = document.getElementById('confirm_delete_account')
    if (input_delete.value == "delete") {
        $('#delete_input').hide()
        $('#hidden_delete_btn').show()
        setTimeout(function() {
            $('#delete_input').show()
            $('#hidden_delete_btn').hide()
        }, 3000);
    }
}


// Calling my functions
retard_loading();
autoplay();
hide_password();
