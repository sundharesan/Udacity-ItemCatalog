# Udacity Item Catalog - Sundharesan

A simple web application that provides a list of items in categories that is integrated with third party user registration and authentication(Google and Facebook). Authenticated users can post, edit, and delete their own items.

## Set Up

1. Clone the project from respository.

2. Launch the Vagrant VM from inside the *vagrant* folder with:

``` vagrant up```

3. Then access the shell with:

``` vagrant ssh```

4. Then move inside the catalog folder:

`cd /vagrant/Udacity-ItemCatalog-4`

5. Then run the database configuration using below command (to load with default values):

`python sampleitems.py`

6. Then run the application:

`python application.py`

7. After the last command you are able to browse the application at this URL:

`http://localhost:8000/`