![GMIT Logo](http://password.gmit.ie/images/logo.png "GMIT Logos")
# Data Representation

Repository for the project for the Data Representation module @ GMIT - 2021

Author: Maciej Izydorek Email: G00387873@gmit.ie Github: [mizydorek](https://github.com/mizydorek)

#

### Project Overview

Create a web application that performs the CRUD operations on the data using Flask web framework — that serves a RESTful API — MySQL/PostgreSQL database and web front-end to display data and interact with the server using Javascript to consume a RESTful API.

### Contents of repository

The repository contains:

* `README.md` file
* `actorDAO.py` — contains data access object that provides methods to retrive data from db
* `testDAO.py` — for testing methods of DAO
* `actorServer.py` — python script that contains application based on flask package 
* `dbconfigtemplate.py` — contains database config file 
* `static` — folder contains index.html page for the application
* `requirements.txt` — contains list of packages need to build the application
* `.gitignore` — contains list of files that have to be ignore
* `initdb.sql` — contains code to create db, tables and insert the data  

### Required software

The following software is required to run the notebook:

* `git` — open source software to download the repository onto computer[3]
* `Python` — Python Programming Language
* `Flask` — python web framework
* `PostgreSQL` — object-relational database

The following command will install the packages according to the configuration file

### Download the repository

At github repository [Data Representation](https://github.com/mizydorek/Data-Representation-Project) click on the green `Code` button to copy the link. Open command line(windows) or terminal(osx/linux), navigate to the selected directory and enter the command `git clone` followed copied the URL. Alternatively copy the whole command below:

```
git clone https://github.com/mizydorek/Data-Representation-Project.git
```

The whole repository will be cloned down onto current working directory.

### Set up the Virtual Environment

While you are still in current working directory you can create virtual environment by issuing the command below:

```
$ python3 -m venv my_env
```
*where you can specify the name of the virtual environment by replacing my_env*

Once created, it can now be activated with the following command:

```
$ source path_to_virtual_environment_directory/bin/activate
```
*replace the path to your virtual environment with path_to_virtual_environment_directory*


The following command will install the packages according to the configuration file:

```
$ pip install -r requirements.txt
```

### Set up PostgreSQL database

After the installation, log in to an an interactive Postgres session by using sudo and pass in the username with the -u option:

```
$ sudo -u postgres psql
```

and create database:

```
postgres=# CREATE DATABASE project;
```

Then, create user and select the password:

```
postgres=# CREATE USER user WITH PASSWORD 'password';
```

and give new user access to administrate the new database:


```
postgres=# GRANT ALL PRIVILEGES ON DATABASE project TO user;
```
*replace the database, username and password with your own*