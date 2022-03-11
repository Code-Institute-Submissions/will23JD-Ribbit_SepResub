# Ribbit online Discussion forum

[View the live project here.](https://ribbit-2022.herokuapp.com/)



![View of website on different screen sizes.]()

## User Experience (UX)

### As a site user:
* I want to be able to ready discussion and comments
* I want to be able to filter by a catagory

### As a registered site user:
* I want to be able to create my own discussions
* I want to be able to comment on other discussions
* I want to be able to edit my discussions
* I want to be able to delete my discussions
* I want to be able to edit or delete my comments

### As the site admin in need to:
* Be able to manage all discussions and comments
* Be able to update discussions, comments and categories
* Be able to add futher categories
* Be able to delete discussions, comments, categories and users


* ## Design 

    * ### Imagery
        * As images are able to be uploaded, by registered users, 
        there is no theme, or stlye however if a user doesn't choose an images\
        a basic frog is displayed to fill the space.

    * ### Colour Scheme
        * I used a mix of green throughout the page to stick with the theme
        of a frog(Hence the name Ribbit)

        ![Color scheme](documentation/screenshots/colorPallet.png)

    * ### Typography 
        * For my body and p elements, I used: [Montserrat](https://fonts.google.com/specimen/Montserrat)
        with a weight of 500. As this is a clean and easie to read font

        * For the head emelents, I used: [Raleway](https://fonts.google.com/specimen/Raleway) with a 
        weight of 400 as this again was a clean font.

* ## Wireframes 


## Features

### Navigation:

#### Nav
![Image of the nav bar](documentation/screenshots/Navbar.png)
* On the Nav bar you are able to go back to the home page, view by category and if you are signed in you can:
    * Create a new discussion and logout.
* If you aren't singed in you can login or sign up for an account.

#### Footer
![Image of the footer](documentation/screenshots/footer.png)
* The footer doesn't change based on if you are signed or not, and contains links to social platforms and copyright.


### Home page (index.html):

#### Discussion cards
![Image of a discussion card](documentation/screenshots/card.png)
* The card is general information about the discussion, which contains:
    * featured image
    * title and exserpt
    * auhtor and category
    * date of creation and up and down votes
* The aim of the card is do give users an idea about the discussion before they click
on it.

#### Pagination
![Image of a pagination](documentation/screenshots/card.png)
* The page paginate a 12 cards to stop user having to scroll for a long time.

### Opened discussion
![Image of a an open discussion](documentation/screenshots/open-discussion.png)
* At the top of the page is the title of the discussion
* Following this is is the feature image, if the user doesn't us a picture nothing will be displayed.
* After this is the generall information about the post like: author, creation, up and down votes.
* Next is the body/main area for the discussion.
* Last is the comment section, where you can read other peoples comments and comment your self.

### Your discussions
* Having a separate page for all your discussion makes it easier to find, edit and delete 
them, this is important because a user doesn't want to have to scroll though other 
discussion in order to get the theirs.

### Editing and deleting your comments and discussions
![Image of edit and delete](documentation/screenshots/edit-delete.png)
![Image of editing a discussion](documentation/screenshots/delete.png)
![Image of deleting a discussion](documentation/screenshots/edit.png)
* Being able to edit or delete a discussion or comment is important as a user 
may need to update a discussion to contain new/ correct information.

### Adding a discussion
![Image of adding a discussion](documentation/screenshots/add-discussion.png)
* As a Login user If want to make a discussion I should have a clean simple way to do so.
thats why adding a discussion is right on the nav bar and, open a simple form for users to create there discussion about what ever they want.

### login/out and sign up
![Image of signing up](documentation/screenshots/sign-up.png)
* The sign up and and other pages have a simple clean look in order to keep it easy to get logged in or sign up.


###  Features Left to Implement

## Testing

### Web browers
* When testing in different browers I wanted to make sure all feature and style look and functioned the same. This is important so that the user can have the same expeerience on any different brower. I tested that the page opens and works in browsers: Chrome, Edge, Firefox,and Bing. To test the different browsers I used my computer to test Chrome, Edge, Firefox, and bing

### Responsiveness
* By using bootstrap I was able to make sure, the content was view able on all screen sizes with out stretching or overflow.

### Validator Testing

* HTML
    * No errors were found when passing through the [official W3C validator](https://validator.w3.org/#validate_by_input).

    ![HTML validator]()

* CSS
    * No errors were found when passing through the [official (Jigsaw) validator](https://jigsaw.w3.org/css-validator/#validate_by_input).

    ![CSS validator]()

* Javascript
    * No errors were found when passing through the [JSHint validator](https://jshint.com/).

    ![Javascript validator]()

* Accessibility
    * I used lighthouse to confirm the site accessibility was 100%.

    ![Lighthouse results]()


### Fixed Bugs 


### Unfixed Bugs


## Technologies Used

### Languages Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### Framework, Libraries and Programs used
* [Django](https://www.djangoproject.com/)

* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

* [Gunicorn](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/gunicorn/)
* [Cloudinary](https://cloudinary.com/home-3722)

* [Summernote](https://summernote.org/)

* [Balsamiq](https://balsamiq.com/wireframes/):

* [Google Fonts](https://fonts.google.com/):
 
* [Font Awesome](https://fontawesome.com/):



## Deployment

### Heroku App

### Forking the GitHub Repository

Forking the repository allows us to have a copy of the original repository to view and make changes on our GitHub account with affecting to original work. Forking a repository can be done with the following steps.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top right of the repository above settings, find and click the fork button. 
3. You will now have a copy in your account.

## Credits

### Code 
* 
* [W3Schools](https://www.w3schools.com/) use for help with audio sounds.

### Acknowledgements

* My Mentor for feedback throughout the project.
* Friends and family for help with testing and feedback