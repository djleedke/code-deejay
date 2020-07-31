# CodeDeejay Blog

Code-Deejay.com is my personal blog focused on helping and informing coders of all skill levels.  It also serves as a portfolio site to provide a central location with links 
to each project (as well as being a part of the portfolio itself). Feel free to check it out at https://www.code-deejay.com!  This is the same repo that is used for the production version of the blog with the exception of a 
few local changes that are present in the deployment environment.  It's a work in progress but it in it's current state it is very usable as a basic blog engine.

## Contents

- [Features](#features)
- [Setup](#setup)
- [Built With](#built-with)

## Features

### Blog
* Posts can be created via the Django admin site.
* You can edit the raw HTML of the post from it's page on the site (requires you to be logged in as a superuser).
* Tagging system that allows you to tag each post with relative words.
* The sidebar contains a list of all of the tags available, clicking one will take you to a list of posts with the specified tag.
* Sidebar also contains a list of popular posts on the site (currently these are manually chosen).
  
### Portfolio
* Projects can be added to the portfolio via the admin site and given a specified order on the page.
* Each project will give a link to the Github repo and project website when hovered over.

### About & Contact
* About page and Contact page that can be edited be via the admin site.
* Contact page allows site visitors to send me an email to my personal Gmail address (without revealing the address).

### Responsive
* It's responsive!
  
## Setup

If you'd like to get the project running locally start by setting up .git in a new folder:
```
git init
```

Pull the repo into the folder:
```
git pull https://github.com/djleedke/code-deejay-blog.git
```

Install virtualenv if you don't have it already and set up the environment (in the root folder still): 
```
pip install virtualenv
```
```
python -m virtualenv venv
```

Activate the virtual environment:
```
venv\scripts\activate
```

Now install the requirements.txt packages:
```
pip install -r requirements.txt
```

Now the fun starts, there are a few things that need to be setup prior to getting the server up and running.  These are related to getting the contact page's email address setup.  Everything is configured to utilize a [Gmail](https://mail.google.com/) account so if you want to use something else you will need to tweak a few other things not mentioned here.  

First we need to create a config.py file in the ```\blog``` folder.  Place the following in it:
```
EMAIL = 'email@gmail.com'
```

Once this is done go to the ```\code_deejay``` folder and create a ```local_settings.py``` file with the following:
```
EMAIL_HOST_USER = 'email@gmail.com'
EMAIL_HOST_PASSWORD = 'PASSWORD HERE'
```

Next, in ```\code_deejay\settings.py``` you will need to ensure that local host has been added to the ```ALLOWED_HOSTS``` list:
```
ALLOWED_HOSTS = [
    '127.0.0.1'
]
```

Now to initialize the database we will need to perform the first migration:
```
python manage.py migrate
```

At this point if you head to 127.0.0.1:8000 in your browser the blog page should be working now.  You will find that the other pages are not working yet.  We need to add a few entries into the database that the pages are looking for. (I know this can be a cleaner process and it will be fixed eventually):

Create your superuser account:
```
python manage.py createsuperuser
```

Now we need to get the server up and running:
```
python manage.py runserver
```

Navigate to http://127.0.0.1:8000/admin/ and login using the credentials you just made.  From here click on "Contents" and then add 3 content objects with the titles "About", "Contact", and "Portfolio".  Case is important here.  Your contents page should look like this:

![image](https://user-images.githubusercontent.com/33850990/89080438-7447e500-d34e-11ea-8339-d5d564e8d6b6.png)

Feel free to edit the content to whatever you would like but the title needs to stay the same for the pages to work.

The final step is to head over to the "Images" page and add any image with the title of "Me" this will be the image that appears on the About page of the site:

![image](https://user-images.githubusercontent.com/33850990/89080462-84f85b00-d34e-11ea-870a-29e141a8361b.png)

At this point the site should run normally!  Posts & projects can be added via the Django admin site to start filling it with content.  Again, this process can definitely still be streamlined a bit but for now this is how it works.

Let me know if you have any questions. Enjoy!

## Built With

- [Django](https://www.djangoproject.com/start/overview/) - for the webserver and backend database 
- [Taggit](https://django-taggit.readthedocs.io/en/latest/) - for the tag system
- [Skeleton.css](http://getskeleton.com/) - very lightweight CSS framework (very lightly utilized)
- [PythonAnywhere](https://www.pythonanywhere.com) - for deployment
