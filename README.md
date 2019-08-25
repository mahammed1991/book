
# Contact Book
###################################################################################################

# Project's README
Python 3.6.8 (default, Jan 14 2019, 11:02:34)

A simple Application to store Contacts, Delete contact, Update
###################################################################################################

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Recipe-Suggestion

Backend **:**

	Python Framwork Django 2.X, and Python3

Front End **:**
	HTML,CSS 
	  
Database **:**
	Django Defualt (While Developing sqlite3 was default selected, You can Choose any DB / 
	Dont change DB as of now Keep sqlite3 as it is to check working flow of the app)

Run recipe-suggestion:

1) Create Virtual environment and activate it
	virtualenv {{environment name}}
	source bin/activate

2) Install requirements (all the library and django version is mentioned inside this file)
	pip install -r requirements.txt

3) CD(Change Directory/Folder) TO magical_project where manage.py file exist
	
	python manage.py makemigrations
	python manage.py migrate

4) Run the app 
	python manage.py runserver 0.0.0.0:8000

5) Access the app at URL http://127.0.0.1:8000/  #Using Browser

6) Log in Admin (Where You can add Information)
	http://127.0.0.1:8000/admin

  to log in admin user need to create superuser from backend using below command and fallow the instruction
  python manage.py createsuperuser (In terminal where manage.py file exist in project)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Project Description 

A simple django application for storing the details of the Contacts (Phone Number And Email)

After succefully running the app, 

User will be landed on Authentication page , where we have two options.
- Sign Up
- Log in 

Sign Up is based on Email and password After Successfull Sign Up, User will be
redirected to same Authentication page where he can log-in using same email and password

On Successfull Login user will get the Home page
where we have different Tabs/Links such as 

- Add contact(Link) **:**
a simple django form , where we will be adding Name, Phone No and Email

- View Contatcs(Link) **:**
On click of this tab it will redirect to a page where we can see all list of contacts
- Under this section we have 
  **a)** Edit action (Editing of any contact) 
  **b)** Delete Action (Deleting of on confirmation)
- Pagination 
  I have implimeted pagination Based view , contact list will be 
  showing 10 rows per page, you can navigate towards forward and 
  backword or you can jump to last page or first page,

- Search Contact(Link) **:**
On click of search tab we you will be landed on search page where you can type 
searching key words in search input, search is based on Name and email pattren,
here also if result is more than 10 rows you will get pagination option.

- Logout (Link) **:**
On click of this link , User will be asked for confirmation for signout, on clean exist 
user will be shown again login authentication page. 

