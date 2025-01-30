<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Personnel_App</h1>


<!-- <div align="center">
  <h3>
    <a href="https://umit8100.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="https://umit8100.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div> -->

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [API Documentation](#api-documentation)
- [API Testing](#api-testing)
- [Overview](#overview)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## API Documentation

You can access the detailed API documentation of the project from the links below:

- [Swagger Documentation](https://umit8100.pythonanywhere.com/swagger/)
<!-- ![Swagger_Arayüzü](project_screenshot/Swagger_Dokümantasyonu_Görseli.png) -->
<img src="project_screenshot/Swagger_Dokümantasyonu_Görseli.png" alt="Swagger Arayüzü" width="400"/>
➡ Interface that allows you to easily test API endpoints.

  
- [Redoc Documentation](https://umit8100.pythonanywhere.com/redoc/)
<!-- ![Redoc_Arayüzü](project_screenshot/Redoc_Dokümantasyonu_Görseli.png) -->
<img src="project_screenshot/Redoc_Dokümantasyonu_Görseli.png" alt="Redoc Arayüzü" width="400"/>
➡ Documentation tool that presents the API structure in a detailed and organized way.

---

<!-- - Bu dokümantasyonlar sayesinde API endpoint'lerini kolayca test edebilir ve yapılarını inceleyebilirsiniz. -->
**Notes:** You can access Swagger and Redoc documentation without any user login.

**Not:** Swagger ve Redoc dokümantasyonlarına herhangi bir kullanıcı girişi yapmadan erişebilirsiniz.

- Along with Swagger and Redoc documentation, you can use our Postman collection to test APIs.
 [Personnel App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9af7bfff-e9be-4aae-b6d4-e6f60eb56aed?action=share&creator=17531143)

## API Testing

To test APIs via Postman, you can follow the steps below:

1. Install Postman (if not installed): [Download Postman](https://www.postman.com/downloads/).
2. This [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9af7bfff-e9be-4aae-b6d4-e6f60eb56aed?action=share&creator=17531143) Download and import.
3. Start testing APIs via Postman.

**Postman Collection Link:**  
[Personnel App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9af7bfff-e9be-4aae-b6d4-e6f60eb56aed?action=share&creator=17531143)


## Overview
- Project Swagger and Redoc Documentation Visual
<!-- ![screenshot](project_screenshot/personnel_swagger.gif) -->
<img src="project_screenshot/personnel_swagger.gif" alt="Project Swagger and Redoc Documentation Visual" width="400"/>
➡ Interface that allows you to easily test API endpoints.

---

- User/Authentication app testing on Postman
<!-- ![screenshot](project_screenshot/user_authentication.gif) -->
<img src="project_screenshot/user_authentication.gif" alt="User/Authentication app testing on Postman" width="400"/>
➡ User verification and authorization test screen.

---

- Personnel app testing on Postman
<!-- ![screenshot](project_screenshot/personnel_app.gif) -->
<img src="project_screenshot/personnel_app.gif" alt="Personnel app testing on Postman" width="400"/>
➡ Screen for testing personnel app with Postman.

---
- Project ER Diagram
<!-- ![screenshot](project_erd.png) -->
<img src="project_erd.png" alt="Project ER Diagram" width="400"/>
➡ ERD diagram showing the application's data model relationships.

---

- API documentation is detailed with Swagger and Redoc. You can access the relevant links via [Swagger](https://umit8100.pythonanywhere.com/swagger/) and [Redoc](https://umit8100.pythonanywhere.com/redoc/).

- Personnel App is a modern backend application developed for users to manage the stock system and provide easy integration with API documentation.
- Provides CRUD operations specific to users and staff roles.
- Swagger and Redoc were used for API documentation.



## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- [Django Rest Framework](https://www.django-rest-framework.org/) - A powerful framework for developing REST APIs.
- [Swagger And Redoc](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation) - API documentation and testing tools. 
- [Debug_Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - A powerful tool for debugging operations.
- [Logging](https://docs.djangoproject.com/en/5.1/topics/logging/) - System logging modul
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - User authentication and authorization. 
- [django-filter](https://django-filter.readthedocs.io/en/stable/) - To facilitate data filtering operations.
- PostgreSQL - High performance database for production environment.


## How To Use

<!-- This is an example, please update according to your application -->

- For online demo: You can take a look at the [Swagger](https://umit8100.pythonanywhere.com/swagger/) and [Redoc](https://umit8100.pythonanywhere.com/redoc/) interfaces.

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Rest_Framawork_Personnel_App_CH-12.git) 

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

- Çevrimiçi demo için: [Swagger](https://umit8100.pythonanywhere.com/swagger/) veya [Redoc](https://umit8100.pythonanywhere.com/redoc/) arayüzlerine göz atabilirsiniz.

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
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Logging](https://docs.djangoproject.com/en/5.1/topics/logging/) - System logging modul
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation) - Environment and document modul 
- [Debug_Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - Debug Toolbar modul 
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - for authentication


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
