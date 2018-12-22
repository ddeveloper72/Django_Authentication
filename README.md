# Django Authorization
## An introduction to Authorization with Django...
## The Mini-Walk Through Tutorial
#### *A part of Full Stack Development*


Welcome to my Django introduction tutorial on VSCode  

The tutorial was taught by the
[Code Institute](https://courses.codeinstitute.net/)

This tutorial focused on creating a Django mini app which at its heart, lets a user
perform CRUD operations on a simple local sqlite3 database. The data is user login details,
a name, a password and an email address.  The user can cerate a simple profile which is managed
by the Django admin panel.

In the ecommerce tutorial, also by Code Institute, the auth app created in this tutorial was
incorporated into the working online [Django E-Commerce Mini-Project](https://ddeveloper72-ecommerce.herokuapp.com).
Check it out after you are happy with what you ahve read below about how the app is constructed.

In this tutorial, we crate a *user login form* and a *user registration form*.

We also create a password reset system that utilizes the built in Django facility to email a
password reset link.

Remember, CRUD -> ```Create, Read, Update, Delete```

The Learning Outcomes Are:

## 1 Learning about the MVT (Model View Template)

   * The Template being the HTML or the presentation layer, 
   * The View layer contains the logic, that the end user will be interacting with.
    
## 2 Getting data through different models

   * manipulation of data in the view,
   * presenting the data to the user,
   * taking data from the html, passing it to the view and adding to the database.

## 3 Setting up included url patterns

### The url pattern Structure:

````
├── index/
├── admin/
│   ├── logout
│   ├── login
│   ├── register
│   ├── profile
│   └── password-reset
└── accounts
````
   * The main app will include url patterns from other apps.

````python
from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(accounts_urls))  
]
````

   * setup the default url pattern,

````python
urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
````

   * include url_reset patterns from urls_reset.py

````python
urlpatterns = [
    url('^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url('^complete/$', password_reset_complete, name='password_reset_complete')
]
````

## 4 Useful development tips and lessons learned:

   * As usual, just when you think one is getting to grips with Python and Django,
   there is always that  bug that is sent your way to test you.
   Indentation/ nesting or lack of nesting can have interesting effects.
   Effects where the code may still run fault free but with an unexpected outcome.
   It does exactly what its told.
   In this tutorial, I discovered that I was able to use the same email address for
   multiple applicants registering on my site.  I had not nested my `def clean_email(self):`
   function inside of the `class UserRegistrationForm(UserCreationForm):`

   * This is a learning mistake that took a few minutes to discover after running numerous test, adding
   mew users to my User model and then consulting with colleagues on [#Slack](https://slack.com/) for ideas.  The value gained from understanding the error is enormous.

## 5 Setting up email interface in Django and VSCode tie-in

### From settings.py in Django

#### Setting up the allowed hosts for VSCode and Cloud 9

````python
ALLOWED_HOSTS = [
    os.environ.get('C9_HOSTNAME'),
    os.environ.get('localhost', '127.0.0.1')
]
````

#### Setting up the requirements for the email interface

````python
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587
````

### From .vscode settings.json
The reason why I'm showing this, is because one of the most challenging aspects that I have while learning coding, had been learning to use the development software and configuring environments.  Learning to Understanding ones tools for coding is as essential as the projects themselves.

````javascript
"terminal.integrated.env.windows": {
        "DEVELOPMENT": "true",
        "SECRET_KEY": "<my_secret_key>",
        "DATABASE_URL": "",
        "ADMIN": "admin pass",
        "DJANGO_SETTINGS_MODULE": "django_auth.settings",
        "EMAIL_ADDRESS": "<my_email_address>",
        "EMAIL_PASSWORD": "<my_email_password>"
        }

````
