<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Personnel_App</h1>

<p align="center"><strong>👥 A modern backend application that provides personnel management and authentication processes 👥<strong></p>

<!-- <p align="center">👥 Personel yönetimi ve kimlik doğrulama işlemlerini sağlayan modern bir backend uygulaması 👥</p> -->


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
  - [Project Swagger and Redoc Documentation Visual](#project-swagger-and-redoc-documentation-visual)
  - [User Authentication and Authorization](#user-authentication-and-authorization)
  - [Personnel Management Test](#personnel-management-test)
  - [Project ER Diagram](#project-er-diagram)
- [Built With](#built-with)
- [How To Use](#how-to-use)
  - [How to Install and Run](#how-to-install-and-run)
  - [Test User Information](#test-user-information)
- [Key Features](#key-features)
- [Contact](#contact)

## API Documentation

You can access the detailed API documentation of the project from the links below:

- [Swagger Documentation](https://umit8100.pythonanywhere.com/swagger/)
<!-- ![Swagger_Arayüzü](project_screenshot/Swagger_Dokümantasyonu_Görseli.png) -->
<img src="project_screenshot/Swagger_Dokümantasyonu_Görseli.png" alt="Swagger Arayüzü" width="400"/>

➡ Interface where you can easily test API endpoints.

---
  
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

Personnel App is a modern backend application where users can manage personnel records and perform authorization-based transactions. Key features of the application:

- **User Authorization:** Different authorization levels for staff, superuser and normal user.
- **Personnel Management:** Personnel adding, updating, deleting and listing operations.
- **Extended Profile Management:** Profile creation and editing for each user.
- **Swagger and Redoc Support:** Easy testing and integration with API documentation.
- **PostgreSQL Support:** Reliable database management in the production environment.
- **Environment Settings:** Separate environment settings management for production and development.

---

Personnel App, kullanıcıların personel kayıtlarını yönetebileceği ve yetki bazlı işlemler yapabileceği modern bir backend uygulamasıdır. Uygulamanın temel özellikleri:

- **Kullanıcı Yetkilendirme:** staff, süper kullanıcı ve normal kullanıcı için farklı yetki seviyeleri.
- **Personel Yönetimi:** Personel ekleme, güncelleme, silme ve listeleme işlemleri.
- **Genişletilmiş Profil Yönetimi:** Her kullanıcı için profil oluşturulması ve düzenleme işlemleri.
- **Swagger ve Redoc Desteği:** API dokümantasyonu ile kolay test ve entegrasyon.
- **PostgreSQL Desteği:** Production ortamında güvenilir veritabanı yönetimi.
- **Environment Settings:** Production ve development için ayrı ortam ayarlarları yönetimi


### Project Swagger and Redoc Documentation Visual
<!-- ![screenshot](project_screenshot/personnel_swagger.gif) -->
<img src="project_screenshot/personnel_swagger.gif" alt="Project Swagger and Redoc Documentation Visual" width="400"/>

➡ Interface that allows you to easily test API endpoints.

---

### User Authentication and Authorization
<!-- ![screenshot](project_screenshot/user_authentication.gif) -->
<img src="project_screenshot/user_authentication.gif" alt="User/Authentication app testing on Postman" width="400"/>

➡ Testing user authentication and authorization processes with Postman.

---

### Personnel Management Test
<!-- ![screenshot](project_screenshot/personnel_app.gif) -->
<img src="project_screenshot/personnel_app.gif" alt="Personnel app testing on Postman" width="400"/>

➡ Screen for testing personnel management operations with Postman.

---

### Project ER Diagram
<!-- ![screenshot](project_erd.png) -->
<img src="project_erd.png" alt="Project ER Diagram" width="400"/>

➡ ERD diagram showing the application's data model relationships.

---

- API documentation detailed with Swagger and Redoc. You can access the documentation via the links below:  
  - [Swagger](https://umit8100.pythonanywhere.com/swagger/)  
  - [Redoc](https://umit8100.pythonanywhere.com/redoc/)

- Personnel App is a modern backend application developed for users to register and manage personnel.
- Provides CRUD operations specific to user and staff roles.
- Supports more detailed editing of user information with extended profile management.
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

### How to Install and Run

1. **clone the repository:**
    ```bash
    git clone https://github.com/Umit8098/Project_Django_Rest_Framawork_Personnel_App_CH-12.git
    ```

2. **Create and Activate Virtual Environment:**
    ```bash
    python -m venv env
    env/Scripts/activate (Windows)
    source env/bin/activate (macOS/Linux)
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Update Database with Migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create the .env File:**  
   Add the necessary settings:
    ```
    SECRET_KEY = "your_secret_key_here"
    ENV = development
    # PostgreSQL
    SQL_DATABASE = your_database_name
    SQL_USER = your_database_user
    SQL_PASSWORD = your_database_password
    SQL_HOST = localhost
    SQL_PORT = 5432
    
    # Logging level
    DJANGO_LOG_LEVEL = WARNING
    ```

6. **Run the Application:**
    ```bash
    python manage.py runserver
    ```

Now your application will run at `http://127.0.0.1:8000/`.

### Test User Information

For the live demo, you can use the following test user information:
- **Username:** testuser  
- **Password:** testpassword123  
- **Email:** testuser@gmail.com  

This user can only view inventory and add tasks.


## Key Features

- **Personnel Management:** Adding, updating and deleting personnel information.
- **Authorization:** Different authorization levels for super user, staff and normal user.
- **User Profiles:** Extended profile management for each user.
- **API Documentation:** Extensive documentation with Swagger and Redoc.
- **Data Filtering:** Advanced querying opportunity with django-filter.
- **PostgreSQL Support:** Strong database support in the production environment.

---

- **Personel Yönetimi:** Personel bilgilerini ekleme, güncelleme ve silme işlemleri.
- **Yetkilendirme:** Süper kullanıcı, staff ve normal kullanıcı için farklı yetki seviyeleri.
- **Kullanıcı Profilleri:** Her kullanıcı için genişletilmiş profil yönetimi.
- **API Dokümantasyonu:** Swagger ve Redoc ile kapsamlı dokümantasyon.
- **Veri Filtreleme:** django-filter ile gelişmiş sorgulama imkanı.
- **PostgreSQL Desteği:** Production ortamında güçlü veritabanı desteği.


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
