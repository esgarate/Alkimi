# Alkimi
Django project with an app “Crud” where you can add, update, delete and list posts. Every Post has a Tittle and a message. Login and logout and users permissions options. 
Start page: http://127.0.0.1:8000/accounts/login/


DETAILS

Environment SETUP

•    Create a virtual environment and actívate it
•    Install Django( pip install Django) and  the library widget-teaks ( pip install django-widget-tweaks)
•    Make the migrations:
  o    python manage.py makemigrations
  o    python manage.py migrateMigrate 
•    Start the project
  o    python manage.py runserver

Description of the APP

The name of the APP is “Crud” is a system of posts where you can add, list, update and delete posts. Every Post has a Tittle and a message. 
Start page  http://127.0.0.1:8000/accounts/login/
App page  http://127.0.0.1:8000/Crud/ 
 Once you login to the initial page it redirects you to the app page where you can do all the CRUD actions over the posts and logout. 

Restrictions over the fields
Both fields, Tittle and Text must be filled otherwise the action is not completed and it redirects you to the main page.

Flash messages
These are the flash messages show after  every action:
  Register  inserted successfully
  Register not inserted successfully
  Register updated successfully
  Register deleted successfully



Login/logout and Admin/staff
In Django there is a module (registration) to manage users and permisión and the login/logout system.
The admin is: esther/esther
I have registered two teams with different permissions and two users for each one. 
Team1 usuario1, usuario2
Team2  usuario3, usuario4 
(usuarioX/contraseñaX)
This can be managed in the page http://127.0.0.1:8000/admin/
