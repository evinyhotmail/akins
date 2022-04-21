## Akins API
**Brief description:**
The name of this API,  comes from an Egyptian name, which means: "brave"
This first version, it is designed to provide an esential back-end service, to build a web page to register a new drone. Whenever a new drone arrives to the company.

Akins has a lot of things to fix in the future. 

See you in the next versions...

## What do I need to run this app? 

## To start:

Create a new folder, right-click, and choose Git Bash Here

If you're on windows and have git installed, right-click and select "Git Bash Here" from the menu context.

execute the command : git clone https://github.com/evinyhotmail/akins.git

exit from Git Bash Here

In your terminal, cd into the **akins** directory.

A directory called **akins** must been have created on your computer, enter it.

Run: “python manage.py  runserver”  to start up the Django web server and visit the website in your browser.

To check all parameters accepted by the API open your brower and go to: http://127.0.0.1:8000/api/

**Note:** Remember that some python packet need to be installed, for more information check requirements.txt file.


**Important note:** Due to the development of this API was under Python 3.8.5, when you install Diango 4.0.3, it will automatically install the library: backports.zoneinfo==0.2.1.

If your Python version is 3.9.x, you can simply comment out the line: backports.zoneinfo==0.2.1. into the file requirements.txt,  you need to do this in order to prevent installation errors.

For more details,  you can go to the following link: https://docs.djangoproject.com/id/4.0/releases/4.0/ from the official Django documentation.

## More things you should know
- The view to show all Drones, can be consumed for any users, but the rest of views for POST, GET, PUT or DELETE are protected for unauthorized users, this means that you need to provide some user credencial.

**Note:** If you feel confortable using Postman, I recomended it to test the API.


3 users already configured: 
	
	- support(Support Team user), password=Zaq12wsx!
	- user1(Standard user), password=Zaq12wsx!
	- localadmin-a(superuser) , password=Zaq12wsx! (It is only used to enter the Django admin panel.)
  

**Note**: the distribution code contains a preload information:

- Database: (db.sqlite3) 


## Specifications to cover:

- A web page to register a new drone. Whenever a new drone arrives to the company, someone from the support team will use the feature to register it by adding all the needed data. This should include at least: name, brand, serial number, different type of supported cameras (ex: phantom, DJI, x4303,hero3). The camera’s main parameters are the model, megapixel number and the brand (ex: hero3, 12MP,gopro).
- A web page to see the list of drones registered. In this page, it could also help to have some kind of filtering (e.g. by name, brand, camera megapixel, etc) as well as the ability to change the order of the results.
- All users can read the list of drones but only the members from the support team can add, new drones to the list.

**Important**:
As part of improvement, to Add, Modify, or delete any Drone you to to provide users credentials.


## Last important things:
- Be aware that I used Python 3.8.5 so not tested on higher or lower versions.
- The version of the django framework is: 4.0.3, so not tested on higher or lower versions.
- The CRUD is just implemente for a Drone model



