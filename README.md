# CodeDeejay Blog
Code-Deejay.com is my personal blog focused on helping and informing coders of all skill levels.  It also serves as a portfolio site to provide a central location with links 
to each project (as well as being a part of the portfolio itself). Feel free to check it out at https://www.code-deejay.com!  This is the same repo that is used for the production version of the blog with the exception of a 
few local changes that are present in the deployment environment.  It's a work in progress but it in it's current state it is very usable as a basic blog engine.

- [Features](#features)
- [Setup](#setup)
- [Built With](#built-width)

## Features

### Blog
  * Posts can be created via the Django admin site
  * You can edit the raw HTML of the post from it's page on the site (requires you to be logged in as a superuser)
  * Tagging system that allows you to tag each post with relative words
  * The sidebar contains a list of all of the tags available, clicking one will take you to a list of posts with the specified tag
  * Sidebar also contains a list of popular posts on the site (currently these are manually chosen)
  
### Portfolio
  * Projects can be added to the portfolio via the admin site and given a specified order on the page
  * Each project will give a link to the Github repo and project website when hovered over
  
### About & Contact
  * About page and Contact page that can be edited be via the admin site
  * Contact page allows site visitors to send me an email to my personal Gmail address (without revealing the address)
  
## Setup
Placeholder for local setup guide

## Built With

- [Django](https://www.djangoproject.com/start/overview/) - for the webserver and backend database 
- [Taggit](https://django-taggit.readthedocs.io/en/latest/) - for the tag system
- [Skeleton.css](http://getskeleton.com/) - very lightweight CSS framework (very lightly utilized)
- [PythonAnywhere](https://www.pythonanywhere.com) - for deployment
