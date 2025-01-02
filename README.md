# ServeSpace  
**ServeSpace** is a volunteer management system built using Django. It enables organizations to efficiently manage their volunteers by providing features like profile management, scheduling, and participation tracking.  

## Features  
- **Volunteer Profiles**: Add, update, and manage volunteer details.  
- **Schedules**: Create and manage events and schedules for volunteers.  
- **Interactive UI**: User-friendly interface built with HTML, CSS, and JavaScript.  
- **Dynamic Content**: Seamless integration of backend and frontend using Django.  

---

## Tech Stack  
- **Backend**: Python, Django  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: MySQL  

---

## Project Structure  
Here’s an overview of the project structure:  
ServeSpace/ ├── ServeSpace/ # Main project folder │ ├── init.py │ ├── settings.py # Project settings │ ├── urls.py # URL routing │ ├── wsgi.py │ └── asgi.py ├── volunteers/ # App folder │ ├── migrations/ # Database migrations │ ├── static/ # Static files folder │ │ ├── css/ # CSS files │ │ ├── js/ # JavaScript files │ │ └── images/ # Images for the application │ ├── templates/ # Templates folder │ │ └── volunteers/ # HTML files for the app │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py # Models for the database │ ├── tests.py │ └── views.py # View functions for the app ├── manage.py # Django management script └── db.sqlite3 # SQLite database file (optional if using MySQL)

---

## Getting Started  

### Prerequisites  
- Python 3.x installed  
- Virtual Environment (recommended)  
- Django 4.x (or latest version)  
- MySQL Server running on your machine  

### Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/username/ServeSpace.git
   cd ServeSpace
2. **Set up Virtual Environment*8
   python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows
3. **Install Dependencies**
   pip install django mysqlclient
Note: mysqlclient is required to connect Django with MySQL. If you encounter installation issues with mysqlclient, refer to the installation guide.
4.**Create MySQL Database**
   CREATE DATABASE servespace;
5.**Configure the Database**
   Open ServeSpace/settings.py and update the DATABASES setting as follows:
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'servespace',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
6.**Run Migrations**
   python manage.py makemigrations
python manage.py migrate
7.**Start the Development Server**
   python manage.py runserver
8.Visit http://127.0.0.1:8000 in your browser.

##Usage
**Setting Up the App**
1.**Create a Django project named ServeSpaceProject**
django-admin startproject ServeSpace
2.**Create an app named 'volunteers'
python manage.py startapp volunteers
**Static & Template files**
Place all images in the static/images/ folder.
Use the templates/volunteers/ folder for all HTML files.
Include CSS and JavaScript files in static/css/ and static/js/ respectively.
