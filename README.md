# Ribbit online Discussion forum

[View the live project here.](https://ribbit-2022.herokuapp.com/)



![View of website](documentation/screenshots/view.png)

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
* Home page

    ![Color scheme](documentation/screenshots/home-page.png)

* Opened discussion

    ![Color scheme](documentation/screenshots/opened.png)

* View on phones and tables

    ![Color scheme](documentation/screenshots/phone.png)

* Sign in page

    ![Color scheme](documentation/screenshots/signin.png)

### Flow chart

![Flow chart](documentation/screenshots/Flow-chart.png)
* How the user can use the site if the are signed it or not

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
![Image of a pagination](documentation/screenshots/next-pag.png)![Image of a pagination](documentation/screenshots/pev-pag.png)
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

![Image of editing a discussion](documentation/screenshots/edit.png)

![Image of deleting a discussion](documentation/screenshots/delete.png)
* Being able to edit or delete a discussion or comment is important as a user 
may need to update a discussion to contain new/ correct information.

### Adding a discussion
![Image of adding a discussion](documentation/screenshots/add-discussion.png)
* As a Login user If want to make a discussion I should have a clean simple way to do so.
thats why adding a discussion is right on the nav bar and, open a simple form for users to create there discussion about what ever they want.

### login/out and sign up
![Image of signing up](documentation/screenshots/sign-up.png)
* The sign up and and other pages have a simple clean look in order to keep it easy to get logged in or sign up.


### Potential Features
* More filters such as:
    * Number of votes
    * Discussions you have liked
* A search box to look for a specific Disussion
* User profile page

## Testing

### Web browers
* When testing in different browers I wanted to make sure all feature and style look and functioned the same. This is important so that the user can have the same expeerience on any different brower. I tested that the page opens and works in browsers: Chrome, Edge, Firefox,and Bing. To test the different browsers I used my computer to test Chrome, Edge, Firefox, and bing

### Responsiveness
* By using bootstrap I was able to make sure, the content was view able on all screen sizes with out stretching or overflow.

### Validator Testing

* HTML
    * No errors were found when passing through the [official W3C validator](https://validator.w3.org/#validate_by_input).

* CSS
    * No errors were found when passing through the [official (Jigsaw) validator](https://jigsaw.w3.org/css-validator/#validate_by_input).

* Javascript
    * No errors were found when passing through the [JSHint validator](https://jshint.com/).

* Python 
    * No errors were found when passing through the [JSHint validator](http://pep8online.com/).

* Accessibility
    * I used lighthouse to confirm the site accessibility 100% or very close to.



### Fixed Bugs 
* When Adding an email to the sign up form it would cause a 500 error.
    * Fixed by adding: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
                      ACCOUNT_EMAIL_VERIFICATION = "none"
    to settings.py
* Delete modal would cause padding to be added to the right side of the screen.
    * Fixed by adding: padding-right: 0 !important to styles.css

### Unfixed Bugs
* None

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

* [Balsamiq](https://balsamiq.com/wireframes/)

* [Lucidchart](https://www.lucidchart.com/)

* [Google Fonts](https://fonts.google.com/)
 
* [Font Awesome](https://fontawesome.com/)



## Deployment

### Django and suporting libaries
1. In a new workspace in the terminal type: pip3 install django gunicorn
2. Libaries need for PostgreSQL: pip3 install dj_database_url psycopg2
3. Create requirments.txt: pip3 freeze --local > requirments.txt
4. Create a new django project: django-admin startproject pojectname .
5. Create a new django app: python3 manage.py startapp appname
6. Add your new app the the projects installed apps: projectname > settings.py > scroll to INSTALLED_APPS > add 'appname', to the list
7. save the file
8. Now back to the terminal to migrate the changes: python3 manage.py migrate
9. Run your project: python3 manage.py runsever
10. And you're up and running just like that!
### Heroku App
1. Create a new app on heroku
2. Head to the resources tab on your new heroku app
3. In the add-ons box search: Heroku Postgress and add it to your project
4. Now head to your settings tab and click on Reveal Config Vars
4. Copy the DATABASE_URL and head back over to your project
5. In the same level as your project create an env.py file (Remeber to add this to your .gitignore)
6. In env.py import os
7. Then: os.environ["DATABASE_URL"] = "Your copied DATABASE_URL"
8. After that create your secret key: os.environ["SECRET_KEY"] = "Your random secret key"
9. Save the file and then copy the secret key
10. Back at your heroku app Config Vars add the key: SECRET_KEY and the value: Your copied secret key
11. Back in your projects settings.py file under the first import
12. import os, import dj_database_url
13. The add the if statement: if os.path.isfile('env.py'):
                                    import env
14. Now just under that replace the insercure key and replace it with = os.environ.get('SECRET_KEY')
### postgreSQL
1. In setting.py file scroll down to the Database section and comment it out
2. Then type: DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
3. Now back to the terminal and run the migrate again:(python3 manage.py migrate)
### Cloudinary
1. Create a Cloudiary account(if you dont have one all ready)
2. Copy your API Environment variable:
3. Now back to your env.py file:
os.environ["CLOUDINARY_URL"] = "copied API key"(make sure you remove the CLOUDINARY_URL from that start of the key)
4. Copy the key again and head back over to your heroku app
5. Add a new Config Var: key= CLOUDINARY_URL value=copied api key
6. Add new another Config Var: key=DISABLE_COLLECTSTATIC value=1 (This is to get the project deploying as we dont have any static files yet)
7. Back to the settings.py file, INSTALLED_APPS add: 'cloudinary_storage'(just above 'django.contrib.staticfiles'), 'cloudinary'
8. Now near the bottom of the file under STATIC_URL = '/static/' add:
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
### Templates
1. Back at the top of the settings.py file under BASE_DIR add:
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
2. Then in the middle of the file in TEMPLATES change the 'DIRS':[TEMPLATES_DIR],
### Allowed hosts
1. In the settings.py file in ALLOWED_HOSTS and ['your heruko appname.herukoapp.com', 'localhost']
2. Now on the top level of your project create 3 folder: media, static and templates
3. Then create a file named Procfile
4. In the Procfile add the line: web: gunicorn ribbit.wsgi
### Deploy 
1. First In your terminal: git add .
                           git commit -m 'Deploy'
                           git push
2. Now back to heroku and click on the deploy tab
3. Deployment method: GitHub (Connect you account id you haven't already)
4. Search for you project repo and connect it
5. Scroll to the bottom of the page and click deploy.
6. Then click on open app and you're Done! 

### Forking the GitHub Repository

Forking the repository allows us to have a copy of the original repository to view and make changes on our GitHub account with affecting to original work. Forking a repository can be done with the following steps.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top right of the repository above settings, find and click the fork button. 
3. You will now have a copy in your account.

## Credits

### Code 
* [Codemy](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw)
    * Help with displaying discussion, custom forms and add discussion page.
* [CodeInstitue](https://codeinstitute.net/)
    * Help from think before I blog walk through: Setting django app up, deploy to
    heroku, cloudinary, basic stlyes and allauth.
* [Stack overflow](https://stackoverflow.com/)
    * Help with various bugs

### Acknowledgements

* My Mentor for feedback throughout the project.
* Friends and family for help with testing and feedback