## Akins API
**Brief description:**
The name of this API comes from an Egyptian name which means: "brave".
This first version it is designed to provide an esential back-end service to build a web page to register a new drone. Whenever a new drone arrives to the company.

Akins has a lot of things to fix in the future. 

See you in the next versions...

## What do I need to run this app? 

## To start:

Create a new folder.

If you're on Windows and have git installed, right-click and select "Git Bash Here" from the menu context.

Execute the command: git clone https://github.com/evinyhotmail/akins.git

Exit from the git console.

In your terminal, cd into the **akins** directory.

A directory called **akins** must been have created on your computer, enter it.

Run: “python manage.py runserver”  to start up the Django web server.

To check all parameters accepted by the API, open your browser and go to: http://127.0.0.1:8000/api/

**Note:** Remember that some python packets need to be installed. For more information check requirements.txt file.

**Important note:** This API was builded under Python 3.8.5, so when you install Django 4.0.3 it will be automatically installed the library: backports.zoneinfo==0.2.1.

If your Python version is 3.9.x you can simply comment out the line: backports.zoneinfo==0.2.1. into the file requirements.txt, in order to prevent installation errors.

For more details, you can go to the following link: https://docs.djangoproject.com/id/4.0/releases/4.0/ from the official Django documentation.

## More things you should know
- To list all drones, the API can be accessed by any user. For the rest of methods (POST, PUT or DELETE) you need to provide some user credentials due to is protected for unauthorized users.

**Note:** If you feel confortable using Postman, I recomended it to test the API.


3 users already configured: 
	
	- support(Support Team user), password=Zaq12wsx!
	- user1(Standard user), password=Zaq12wsx!
	- localadmin-a(superuser) , password=Zaq12wsx! (It is only used to enter the Django admin panel.)
  

**Note**: The distribution code contains a preload information:

- Database: (db.sqlite3) 


## Specifications to cover:

- A web page to register a new drone, whenever a new drone arrives to the company. Someone from the support team will use the feature to register it by adding all the needed data. This should include at least: name, brand, serial number, different types of supported cameras (ex: phantom, DJI, x4303,hero3). The camera’s main parameters are the model, megapixel number and the brand (ex: hero3, 12MP,gopro).
- A web page to see the list of drones registered. In this page, it could also help to have some kind of filtering (e.g. by name, brand, camera megapixel, etc) as well as the ability to change the order of the results.
- All users can read the list of drones but only the members from the support team can add, new drones to the list.

**Important**:
As part of improvement, to Add, Modify, or Delete any Drone you need to provide user credentials.


## Last important things:
- Be aware that I used Python 3.8.5, so don't had been tested on higher or lower versions.
- The version of the django framework is: 4.0.3, so don't had been tested on higher or lower versions.
- The CRUD is just implemented for a Drone model.



