# Data Centric Developement Milestone Project

# [Travel Around](https://travelaroundmilestone.herokuapp.com/)

![Page Logo](https://github.com/gello94/second-milestone-antonio/blob/master/assets/img/pagelogo.jpg)

This Website was developed as Milestone Project for Code Institute's Data Centric Developement.


![Moqup](/wireframes/moqup.jpg)

As a travellers myself I know how usefull is to find information and tips from people that have already been in a place without promotional intent or sponsirized locations.

Travel Around has the goal to buil a community of people who love to travel and share their trip tips based on their personal experience, to help other travellers to have a better travel experience.
The user will also have a personal profile shared with the community in wich will be possible to show the cities that the user has made, the cities that the user would like to visit, the cities visited and the preferite cities.


## UX

The website is accessible to everyone, all ages, and is direct expecially to who like to travel, but everyone can explore cities and start travelling from Travel Around.

### Scope
The scope of the website had changed during the developement of same.

The starting idea was based on the "Recept Milestone" suggestion provided by CodeInstitute as milestone project, to build a responsive Web App with collection of data and demonstration of the use of the method **CRUD**:

```
C = Create 
R = Read 
U = Update 
D = Delete
```

Once reached this I had few more ideas and I did more upgrades and I still have more ideas to implement in future upgrades. 
The idea is to launch this app in the future, in the next module we are going to approach with Django and it will be implemented, once learned, to this project to have a better management of the database and made faster the app.
Other than only having this web site as a web app I would like to made a mobile app for same and I am already looking for solutions as [Kivy](https://kivy.org/#home).

### Moq Ups
The starting design drafts were done on [Moqups.com](https://moqups.com/).

The wireframe of the startig idea can be found divided for desktop ad mobile devices at the following link:

- Desktop Devices(/wireframes/desktop)
- Mobile Devices(/wireframes/mobile)

The final design is bit different from the starting idea, multiple changes were applied to the website following ideas and improvements and the features implemented while developing the Web App.

## Scenarios

##### 1. New visitor:

What a new visitor would like to do is to understand what a web site is for. Since the visitor access to the wesite it is clear that it is a travelling website.
By clicking on the city card the user can easly access to the city information page and already from the homepage the user can see how many interaction people have done. By clicking on the social icons the user will be directed to a page showing all the benefits to be a registered user.


##### 2. User looking to organize a trip:

As someone that is organizing a trip I would like to find clear lists of places that I can see when visiting a city, but as well I know how precious are tips from other people that have been already in that place. On Travel Around all these info are easy accessible and there are only tips shared by travellers for travellers.


## Users
The website can be seen by all the users without the need to be registered. As following the 3 different users type explained.

#### Visitors
A visitor can navigate trought the web site and explore cities info, but can't interact with the website.

#### Registered user
The registered are divided in three sub-categories, divided by permissions:

- user
- admin

#### 1. User
A registered user can interact with the website, it can:
- Add a new city
- Edit an existing city
- Add a city to the "city to visit"
- Add a city to the "visited list"
- Add a city to the "preferred list"
- Manage is own account
- Delete is own account
- View other users account and relative lists

#### 2. Admin
As admin, other to have the "user" features, it is possible to acces to the admin area where it will be possible to see a list of all the user registered sorted by username, what permitt does the user have and the email address of that user.

Another important option that only an admin user can do it is delete a city. 

#### 3. Owner
The owner is the user with grather permitts, he can access, other than access to all the admin option, as well to the user rights and can change the user permitts on the website. 

## Database Structure

To collect data and made a database of objects I used [MongoDB](https://www.mongodb.com), hoted by [Atlas](https://www.mongodb.com/cloud/atlas) as I learned during the Data Centric Module Lessons provided by [CodeInstitute](https://codeinstitute.net).

### Collection and Data Storage 

The collections used for this project are:

#### 1. Cities

| Title        | Key           | Data Type  |
| ------------- |:-------------:| -----:|
| City ID      | _id | ObjectId |
| City Name      | city_name      |  string  |
| City Country | city_country     |    string |
| City Region | city_region     |    string |
| City Population | city_population     |    string |
| City Language | city_language     |    string |
| City Description | city_description     |    string |
| City Category | city_category     |    string |
| City Must See | city_must_see     |    array |
| City Tips | city_tips     |    array |
| City To Avoid | city_to_avoid    |    array |
| City Image Url | city_image     |    string |
| City Visited By | city_visited_by     |    array |
| City Preferred By | city_preferred_by     |    array |
| City To Be Visited By | city_to_visit_by     |    array |
| City Added date | added_time     |    string |

#### 2. User

| Title        | Key           | Data Type  |
| ------------- |:-------------:| -----:|
| User ID      | _id | ObjectId |
| Username      | username      |  string  |
| Password | [hashed]password     |    string |
| Email | email     |    string |
| City Author | city_author     |    string |
| user Permitt | right     |    string |
| Cities to Visit | city_to_visit     |    array |
| Cities Visited | city_visited     |    array |
| Cities Made | cities_made     |    array |


#### 3. Regions

| Title        | Key           | Data Type  |
| ------------- |:-------------:| -----:|
| Region ID      | _id | ObjectId |
| Region Name      | city_name      |  string  |
| Cities in Region | cities_in_region     |    string |


### Local JSON collection

A **JSON** collection is used and stored locally for this project.

The collection **Countries** was imported from https://gist.github.com/keeguon/2310008 with the command `` wget ``.

This collection contain a list of countries and is used in my project to made a list of Countries in the "Add City Page".


## Feature

The structure is very simple and intuitive, this is essential to made the web site accessible to everyone. 

It follows the Mobile First principles and both on Mobile and Desktop devices the navigation is simple and easy to access.

The **Navigation Bar** and the **Footer** are static and the same in all the website.


#### Navigation Bar

The navigation bar is the same in every page of the website.

The Navigation Bar for Desktop Devices is divided into two section, divided by the logo. 

**1. Left**

 If user is not logged:
 - Home.

If user is logged:
- Home;
- User List;
- Settings.


**2. Right**

If user is not logged:
- Search button, on click will how the text input on the navbar, inline with same;
- Log In;
- Register; 
- Log Out.

If user is logged:
- Search button, as above;
- Add a city;
- User Page;
- Log Out.

For Mobile Devices there is a Collapsible Navigation Bar, containing a search input field and relative search button and as a list all the element contained as above.
As a plus in the Mobile Navigation Bar are contained the social links.

### Footer

The footer contains either Mobile or Desktop version the Travel Around Logo, a briefh about the website goal, the social links and the copyright info.



### Home Page

As first in the home page is is possible to see a text header "Where are you going next?" With a carousel showing six cities sorted by name, that will give the idea of what is the web site for.

Srolling the home page tere are six Regions:
- Europe
- North America & Canada
- Asia
- Central America & South America
- Australia & New Zeland
- Africa & The Middle East

In each region are showed 8 card containing the city image and the city name, all card are pointed this way the user will understand that can click on the card to be redirected to the city page.

At the end of each region area there is a button link that redirect to a city list page with the cities containing that region name filter.

For each card there are action that a registered user can perform as:
- Add to "To Visit List"
- Add to "To Visited List"
- Add to "To Preferite List"

When the user click on this action that city will be added to the chosen category and the counter on the card will increase.

This made the web site more social and interesting, the users can interact as well other than just add cities or info and all of these info will be displayed on the User Page accessible by all the registered user.

### City Page for Regions

As mentioned above this web page contain all the cities card that are in that region.

The cities are listed alphabetically. 

### City Page

Clicking on one of the cards the user will be redirected to the city page, this contain all the info about the city.

The city name is the header, after this there is a row containing the image on the left occuping 8 column on medium and above size screen according to [Materialize Grid](https://materializecss.com/grid.html) of the row size and the other 4 column are occupied by the city basical info as:
- Region
- Country	
- Population
- Category	 
- Language	
- Added by	
- Date Added

On mobile screen these will be displayed as full row.

Scrolling the page there is the section "City Description", in which the user can add a short description about the city.

More info are set as three column (s4 size on medium devices screen and above):
- City Must See
- City Tips
- To Avoid

The registered user can add more tips or info sharing the personal experience to the entire community.

If the user is registered a button edit will be added on the page floating on the bottom right position of the screen.

If the user has the permission as "admin" beside the "edit" button a delete button will be added.
To prevent an accidental delete action by clicking on this button will appear a confirmation form where to proceed it need to type "delete" on the provided input area. If the input is "delete" then the buttons "Go Back" and "Delete" will appear to the user and by clicking to "Delete" the city will be deleted from the database. If the user doesn't perform any action within 3 sec the modal will redirect the user again to the confirmation form.
This action is performed using a function in JavaScript as follow:

```
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
```


### User Page
After the Log In for registered user or after the registration for new user, he will be redirect to the User Page.

It is possible to access to the same as well by clicking on he User Page button present on the Navigatio Bar that appear only to logged in users.

This page contain an internal Navigation Bar for users containing the following list of categories:

- Made
- To Visit
- Visited
- Preferite

Clicking on one of these categories the user will be able to see cities contained in that particular category. When the user click on one of the category the navigation section will have a grey color style to allow the user see in which category is.

The default category when the user access to the user page is "Made".

This action is performed with the use of the css ``display: none`` applied to the relative div.
With the use of JavaScript and jQuery then with an onClick action on the navigation bar the user will call the function that show the relative div of that section and hide the others.

On the top left side of each card there is a floating button action where the user can easily access to settings functions as:

- Edit 
- Remove to "To Visit List"
- Remove to "To visited List"
- Remove to "To Preferite List"

Each button is in the relative category.

Another action that the user can perform is Delete is own account, by clicking on the "Delete Account" button positioned floating on the bottom right side of the page.

To delete the account, as for to delete a city, the user has to confirm by a confirmation form the action.

### Other Users Profile

The structure of other users profile is the same of the Personal User Profile. 

The user however will not be able to see the action buttons on this page.

If the user has right as "admin" a "Delete Account" button positioned floating on the bottom right side of the page will be displayed. The admin can delete other users accounts.


### Add and Edit City 

Add and Edit City have the same layout and the info that the user can add or modify are:
- City Name
- City Country
- City region
- City Population
- City Language
- City Category
- City Image (by pasting a link of an image)
- City Description
- City Must see
- City Tips
- To Avoid

Other info will be added by adding a city that can not be modded as:
- City Author
- Time Added 

### 404 Page

If the user goes in a page that doesn't exist it will be redirect to a personal 404 error page that contain a 404 logo designed following Travel Around logo design.

To test the 404 error page go to the following link - https://travelaroundmilestone.herokuapp.com/error

### Permission Required Page

When the user click on the actions of the home page it will be redirect to a page where it will be acked to register to perform that action and that explain all the advantage to be a registered user of Travel Around.

### Admin Settings 
This page is only for user with right as "admin" and for the "owner".

In this page the admin can see a list of all the user registered sorted by username, what permitt does the user have and the email address of that user.

The owner can also change the users right, by clicking on the button "change user permitt" it is possible to manage it an change it.

## Features Left to Implement

- Allow users to set private profile;
- Allow user to personalize user profile image;
- When user will be able to personalize profile image add it on user profile;
- Add new sections to city page like "Suggested Food";
- Add filtered search for country and description;
- Add a privacy policy page declarations according to GDPR (General Data Protection Regulation) for the launch.



## Technologies Used

For this project I used:

- [AWS Cloud9](https://aws.amazon.com/it/cloud9/)
    - Used as Ide to develop the code.

- [HTML5]( https://en.wikipedia.org/wiki/HTML5)
    - The project uses **HTML5** to structure the content in line with modern semantic HTML5.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
    - The project uses **CSS3** to style the html content.

- [SCSS/SASS](https://sass-lang.com)
    - The project uses **SCSS**.

- [JavaScript](https://it.wikipedia.org/wiki/JavaScript)
    - The project uses **JavaScript** to manupulate the frontend.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to control toggle features.

- [Python](https://www.python.org)
    - The project uses **Python** as developing langauge to build Travel Around and as a server side/back-end language.

- [MongoDB](https://www.mongodb.com/)
    - The project uses **MongoDB** to create and manage a database.

- [JSON ](https://www.json.org/)
    - The project uses **JSON** to manage my local collection.

- [Flask](https://palletsprojects.com/p/flask/)
    - The project uses **Flask Framework** to render the templates.

- [Materialize 0.100.2](http://archives.materializecss.com/0.100.2/)
    - The project uses **Materialize 0.100.2** to Layout the html content.

- [FontAwesome](https://fontawesome.com/)
    - The project uses **FontAwesome** to add icons for social media and contact forms.

- [GoogleFonts](https://fonts.google.com/)
    - The project uses **GoogleFonts** to add the font Roboto and Alfa Slab One importing same in my CSS.

- [Google Images](https://www.google.com/imghp?hl=en)
    - I used **Google Images** to find the icons for account, research done using the filter to find images with the permit to be used.

- [Stackoverflow](https://stackoverflow.com)
    - For the project I used **stackoverflow** community to help building the app searching for scripts and explanations and to ask explanation about python.


## Testing

Cross Web Testing done on the following Browsers:

#### Mobile Browsers
* Chrome
* Safari
* Internet Samsung 

#### Desktop Browsers
* Chrome
* Firefox
* Edge

#### Devices
* Hp Laptop
* Asus Laptop
* Acer Laptop
* Samsung S8
* iPhone X
* Vernee Thor
* 42" Screen Desktop PC

During the testing I used Chrome Developer tools to test the responsive design on different size and the features of the page on different width.

I also used Firefox Developer tools when I discovered that my card were not following the grid on other browsers other than Chrome.

The site was developed following the Grid System and the same was tested to ensure that all the elements are responsive on the following resolutions on each page:

- Width ≥1200px 
- Width between 1200px and 768px
- Width ≥≤ 768px 
- width ≤450px (this to prevent card and text to be too big on smaller size screen)

Some TDD (Test Driven Developement) have be done while developing the python code and can be found in my test.py. For this test I used UnitTest, running my test.py file in the console with the command ```python3 test.py``` i get 8 test done and an **OK** status that means that all my code passed.

More testing on my JavaSvript have be done by manually checking if my code was called at the right action, using the ```console.log('funcion called')``` code in the function i wanted to check.

I did several manual testing to the code as well by testing the various feaures of my website like:

- Register
- Log in
- Log Out
- Add a city to one of the list and check if are in the list in the user page
- Try to search a city
- Delete a city
- Delete an account
- Change user permitt

### During development

During the developement I had iussue with the Grid System on Firefox and Edge, same fixed adding to the div i needed the following code: 

```
.flex {
  display: flex;
  flex-wrap: wrap; }

.content {
  flex: 1 0 auto; }
  ```
  
On Edge at the moment the span it is still not having a light grey background like on the other browsers.

It seem as there are no other bugs at the moment.

To test the if the SEO guidelines are followed I used [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) as Google Chrome extension that give me 100% of result.

### Validation Testings

For HTML validation testing I used ["W3 Validator"](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelaroundmilestone.herokuapp.com%2F) which shows few error in duplicate ID that are made by my function to repeat the carousel images for each city in the list. For the search button it is to save adding more code to definy a second search form in python, the second search button will anyway be displayed only on mobile size and is always going to be unique.

For CSS validation testing I used ["W3 CSS Validator"](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fcloud9%2Fide%2Ff5cc4af3f817467b952808358ab6cfef&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=it) which shows no errors on my main.css style sheet.

For JavaScript validation testing I used ["JSHint"](https://gello94.github.io/second-milestone-antonio/) with whom I checked the presence of unused variable and code errors.

## Deployment
The web site has been deployed on Heroku for hosting and on GitHub.

### Heroku
This page has been deployed to ["Heroku"](https://travelaroundmilestone.herokuapp.com/).

These steps were followed to Deploy the project on Heroku:
- Database and Tables were created in an Atlas MongoDB account
- Project workspace was created in AWS Cloud 9. 
- Framework needed were installed with the command ```$ sudo pip3 install 'framework-name' ```
- Created an instance of flask ``` app = flask(__name__) ```
- Host set as follow:
```
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT")),
            debug=False)
```
- Created a new Heroku App - unique name and EU Server
- In cloud 9 login to Heroku by the code ```$ heroku login --interactive```
- Provided username and password
Created a git repository in AWS Cloud9 as follow:
```>$ git init
>$ git add 
>$ git commit -m "Initial Commit"
```
- Connected AWS cloud9 to Heroku using the code ```$ heroku git remote -a travelaroundmilestone
- Created requirements.txt file with the code ```$ sudo pip3 freeze --local > requirements.txt```
- Created the Procfile with the code ```$ echo web:python app.py>Procfile```
- Then added and Commited to Git Repository:
```
>$ git add . 
>$ git commit -m "initial commit"
```
- Push to Heroku with the code ```$ git push heroku master```
- Setted in Heroku in the repository settings the 'COnfig Vars' including IP, Port, Mongo_DB and Mongo_URI and Secret Key


### GitHub
This page has been deployed to ["Github Pages"](https://gello94.github.io/second-milestone-antonio/).

GitHub is used to host the code and publish the pages.

A new repository was created in GitHub called: travel-around-milestone.

The repository has been pushed following these commands

```
>$git remote add origin https://github.com/gello94/travel-around-milestone.git
>$ git push -u origin master
```

After a final Git Add and Git commit

```
>$git add .
>$git commit -m "final commit"
```

The pages were pushed to the GitHub repository

```
>$ git push -u origin master
>$Username
>$Password
```

### Run my project locally
To run this project you can follow one of the follwing way:

#### 1. Deployment through Cloud9
- Create a blank workspace in your Cloud9 dashboard.
- Get all files from github using 'git clone https://github.com/**mylinkhere**' command in the C9 CLI
- install Python dependies with following command: 'pip3 install -r requirements.txt'
- Run app with following command: 'python3 app.py'.
- Click on preview >> preview running application and get link
- Open up Link in browser of choice

#### 2. Deployment through Heroku
- Copy Github repository
- Make sure Procfile and requirements.txt for dependencies are correct.
- Create new heroku app and set environment variables (IP, PORT & MONGO_URI)
- Connect Github repository to Heroku App through 'Deployment Method' in Heroku - App Dashboard
- Deploy Branch through Manual Deploy' in Heroku App Dashboard

## Credits

Thanks to CodeInstitute Slack Community helping me to find extra material to study to improve my knowledges to develop this web app.

Thanks to the tutor Ali Ashik that has been always available to help me to understand and clarify areas of this project that were difficult to me.

### Media

- The icons used for the user are taken from ["Google Images"](https://www.google.com/imghp?hl=en), found using the filter "re-use rights".
- The Logo used is made by me with Adobe Photoshop, all credits reserved.
- The 404 Image is made by me with Adobe Photoshop, all credits reserved.


## Extra Sources

More info were taken from the following documentation files:

- [Jinja2 - Templates](https://jinja.palletsprojects.com/en/2.10.x/templates/)
- [Python - Timezone](https://docs.python.org/3/library/time.html#time.timezone)
- [Flask - Testing](https://flask.palletsprojects.com/en/1.1.x/testing/#the-first-test)
-  [Lazy Loader](https://imagekit.io/blog/lazy-loading-images-complete-guide/)

