# django
Python V 3.7

1. Install django:
  pip install django
  
2. Install django rest framework:
  pip install djangorestframework
  
3. Instal django filter:
  pip install django-filter
  
4. Open project folder: 
  cd test_

5. Run server:
  python manage.py runserver

6. Open http://127.0.0.1:8000/ and see page with all users:
 - click on 'Filters' button
 - write RegistrationDate in YYYY-MM-DD format
 - click on 'Submit' button
 - select 'openapi-json' in 'Format' list 
 
7. Open http://127.0.0.1:8000/admin/ and see admin page:
 - login with user name: 'admin', password: '12345678'
 - click on 'Userss' in 'Orders' block
 - click on 'Upload from csv file' button
 - click on 'Choose a file' button
 - select file
 - click 'open'
 - click 'Upload' button

8. Open http://127.0.0.1:8000/ and see page with uploaded users
