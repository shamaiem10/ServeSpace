# ServeSpace  
**ServeSpace** is a volunteer management system built using Django. It enables organizations to efficiently manage their volunteers by providing features like profile management, scheduling, and participation tracking.  


## 🧑‍💻 User Roles & Features

ServeSpace has three primary user roles, each with distinct features and capabilities:

### 1. **Admin**
The Admin role has full control over the application and can manage all users and settings. Features for Admin:
- **User Management**: Admin can delete, and view all users, including volunteers and organizations.
- **Dashboard Access**: Access to the overall dashboard, where Admin can view activity reports, registration statistics, and system logs.
- **Data Overview**: Admin has access to all the data in the system, including volunteer hours, organization progress, and completed projects.

### 2. **Organization (Org)**
Organizations can manage volunteers and oversee projects or campaigns. Features for Organizations:
- **Volunteer Management**: Org users can view, accept, or reject volunteers for specific tasks or projects.
- **Project Management**: Create and manage volunteer opportunities or events, track their progress, and assign tasks to volunteers.
- **Communicate with Volunteers**: Send messages or updates to volunteers working on specific projects.

### 3. **Volunteer**
Volunteers can register, view, and participate in projects, but have limited access compared to Admin and Organizations. Features for Volunteers:
- **Profile Management**: Volunteers can update their personal information, contact details, and preferences.
- **Browse Volunteer Opportunities**: Volunteers can view available projects and events in the organization, and register for the ones they are interested in.
- **Notifications**: Receive updates and notifications about project changes, upcoming events, and organizational news.
  
### 4. **Leaderboard**
The **Leaderboard** feature ranks volunteers based on their contribution, allowing a competitive and rewarding environment. Features for Leaderboard:
- **Volunteer Ranking**: Volunteers are ranked based on the total hours worked, number of projects completed, or other criteria defined by the organization.
- **Top Performers**: Display the top volunteers with the most hours or significant contributions, fostering a sense of achievement and encouraging more participation.
- **Leaderboard Display**: The leaderboard is displayed on the volunteer dashboard, showing the rankings for top contributors.

### Additional Features:
- **User Authentication**: Secure login and registration system for all user types.
- **Volunteer Hours Tracking**: A feature that allows volunteers to log their hours and track participation.
- **Real-time Notifications**: Volunteers and Organizations are notified in real-time for any project or registration updates.



---

## Tech Stack  
- **Backend**: Python, Django  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: MySQL  

---
## Project Structure
The project is organized into different folders and files. Here's a breakdown:

# Main Folder: ServeSpace/
### ServeSpace/: This is the main folder for the project, which contains all the core files.
**settings.py:** Contains the configuration settings for the project.
**urls.py:** Handles the routing of URLs for the project.
**wsgi.py and asgi.py:** These files are for deployment purposes, helping run the project on a server.
**__init__.py:** A special Python file that indicates this folder is a Python package.
### App Folder: volunteers/
### volunteers/: This folder holds the files related to the app named volunteers (the core functionality of the project).
### migrations/: This folder contains files related to the database schema changes (like adding new tables).
### static/: This folder stores static files (like images, CSS, and JavaScript).
### css/: Holds the CSS files for styling the web pages.
### js/: Contains JavaScript files to add interactivity to the website.
### images/: Stores image files used in the project.
### templates/: This folder contains the HTML files used to structure the web pages.
### volunteers/: Stores the HTML files specific to the volunteers app.
**models.py:** Defines the database structure (like the tables and fields).
**views.py:** Contains the code that defines what happens when a user requests a page.
**admin.py:** Allows the creation of an admin interface to manage the database.
**apps.py:** Configures the app settings.
**__init__.py:** Similar to the one in the main folder, it marks this folder as a Python package.
tests.py: Holds the test cases to check if the app is working correctly.
# Other Files:
**manage.py:** A command-line tool used to manage and run the project (like starting the server or creating database migrations).
**db.sqlite3:** The database file where the project's data is stored (only if using SQLite).


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
2. **Set up Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate     # For Windows
4. **Install Dependencies**
   ```bash
   pip install django mysqlclient
*Note: mysqlclient is required to connect Django with MySQL. If you encounter installation issues with mysqlclient, refer to the installation guide.*
4.**Create MySQL Database**
  `
   CREATE DATABASE servespace;
`


5.**Configure the Database**


   Open ServeSpace/settings.py and update the DATABASES setting as follows:
  ` DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'servespace',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
`

6.**Run Migrations**
`
   python manage.py makemigrations
   python manage.py migrate
`


7.**Start the Development Server**
`
   python manage.py runserver
`


8.Visit `http://127.0.0.1:8000` in your browser.

## Usage
**Setting Up the App**
1.**Create a Django project named ServeSpaceProject** 

`django-admin startproject ServeSpace`


2.**Create an app named 'volunteers'**
`python manage.py startapp volunteers`


**Static & Template files**
- Place all images in the static/images/ folder.
- Use the templates/volunteers/ folder for all HTML files.
- Include CSS and JavaScript files in static/css/ and static/js/ respectively.
## My Contributions

- **[Shamaiem](https://github.com/shamaiem10)**:
  - Frontend Coding.
  - Developed the backend logic for volunteer.
  - Configured and integrated the database (MySQL) for storing project data.
  - Designed and structured the project’s directory, including the static and templates folders.
    
## 🤝 Collaborators

- **[Minahil](https://github.com/Minahil-Rauf)**:
  - Database Design.
  - Developed Backend logic for organization.

- **[Maryam](https://github.com/maryam)**:
  - Canva UI design.
  - Developed Backend logic for admin.
  - Database Design.



