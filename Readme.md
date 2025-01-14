<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Personnel_App</h1>


<div align="center">
  <h3>
    <a href="https://umit8100.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="https://umit8100.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

![screenshot](project_screenshot/Flight_App_1.gif)

---

![screenshot](project_screenshot/Flight_App_2.gif)

---

![screenshot](project_screenshot/user_register.png)

---

![screenshot](project_screenshot/user_detail.png)

---

![screenshot](project_screenshot/user_login.png)

---

![screenshot](project_screenshot/user_logout.png)

---

![screenshot](Personnel_App.jpg)

---

## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Djago Rest Framework
- Swagger
- Debug Toolbar
- Logging
- Redoc
- PostgreSQL

## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Proj_Django_Temp_Blog_App_CH-8) 

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin. 

```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Project_Django_Rest_Framawork_Personnel_App_CH-12.git

# Install dependencies
    $ python -m venv env
    $ python3.10 -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...

# for development(dev) environments
DEBUG =True

# for product(prod) environments
SQL_DATABASE={DB_NAME}
SQL_USER={DB_USER_NAME}
SQL_PASSWORD={DB_PASSWORD}
SQL_HOST=localhost
SQL_PORT=5432

# for choices environment
ENV_NAME =dev
# ENV_NAME =prod

DJANGO_LOG_LEVEL=INFO
"""

# Run the app
    $ python manage.py runserver
```

## About This Project
- Personnel registration/management system API service.
- dj-rest-auth for User Authentication..
- super_user/staff_user (CRUD), user (DETAIL, UPDATE for own Profile objects)..
- Creating a Profile for each user by expanding the Default User model.
- permissions definitions between super_user, staff_user, user;
   (Only the staff_user or super_user who created a created user can update it. Only super_user can delete.)
- Separate environment settings for production and development.
- Using Postgresql database in production environment.

<hr>

- Personel kayıt/yönetim sistemi API servisi.
- User Authentication için dj-rest-auth..
- super_user/staff_user (CRUD), user (Kendi Profile objeleri için DETAİL, UPDATE)..
- Default User modelini genişleterek her user için bir Profile oluşturulması..
- super_user, staff_user, user arasında permissions tanımlamaları;
   (create edilen bir user'ı sadece create eden staff_user veya super_user update edebilsin. 
    Sadece super_user delete edebilsin.) 
- Production ve development için ayrı ortam ayarları.
- Production ortamında postgresql database kullanımı.

## Acknowledgements
- [Logging](https://docs.djangoproject.com/en/5.1/topics/logging/) - System logging modul
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation) - Environment and document modul 
- [Debug_Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - Debug Toolbar modul 

## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
