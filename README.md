
# udado

Udacity nano degree project

## Setup Guide

### Creating the .env File for Docker

The .env file stores environment variables for Docker containers. It should be in the same directory as the docker-compose.yml file.

Steps to Create and Configure the .env File

Create a new file named .env.
Add Environment Variables:

.env

        POSTGRES_DB: Name of your default database.
        POSTGRES_USER: Database username.
        POSTGRES_PASSWORD: Database password (choose a strong one).

Save the File:

Save the .env file in the same directory as your docker-compose.yml.
Security Note:

Include .env in .gitignore to prevent it from being committed to version control.
Connecting to PostgreSQL using pgAdmin in a Browser
After setting up Docker containers, connect to PostgreSQL through pgAdmin using a web browser.

### Steps to Access and Connect via pgAdmin

#### Access pgAdmin:

Open a web browser.
Navigate to http://localhost:5050.

#### Log into pgAdmin:

Use the email and password set in Docker (PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD).
Add a New Server in pgAdmin:

Click 'Add New Server'.
In 'Create - Server' dialog:
General tab:
Name: udado DB.
Connection tab:
Host name/address: udado-db.
Port: 5432.
Maintenance database: udado or postgres.
Username: udado (from .env file).
Password: Password (from .env file).
Click 'Save'.
Connect and Use:



