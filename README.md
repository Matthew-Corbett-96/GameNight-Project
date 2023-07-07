# Your Project Title

## Project Description

This is a full-stack application that provides a platform for managing game nights. It allows users to manage games, game nights, and announcements for game nights. It also provides attendance management features. The backend of the application is built using Flask, and the frontend is built with Vue.js.

## Tech Stack

This project uses several key technologies:

- [Flask](https://flask.palletsprojects.com/en/2.0.x/): A lightweight backend framework for Python.
- [Vue.js](https://vuejs.org/): A progressive framework for building user interfaces.
- [Docker](https://www.docker.com/): A platform to develop, ship, and run applications inside containers.
- [PostgreSQL](https://www.postgresql.org/): A powerful, open-source relational database.
- [pgAdmin](https://www.pgadmin.org/): An open-source administration and management tool for the PostgreSQL database.
- [Docker Compose](https://docs.docker.com/compose/): A tool for defining and managing multi-container Docker applications.

## Running the Docker Compose Setup Locally

To run this project locally, follow these steps:

1. Install Docker and Docker Compose on your machine.
2. Clone this repository to your local machine.
3. Navigate to the directory where you have cloned the repository.
4. Run `docker-compose up` in your terminal.

This will start all the services defined in the `docker-compose.yml` file:

- The Vue.js frontend will be accessible at `http://localhost:3000`
- The Flask backend will be accessible at `http://localhost:5000`
- The PostgreSQL database will be accessible at `localhost:5432`
- The pgAdmin interface will be accessible at `http://localhost:5050`

Remember to stop the services when you're done by running `docker-compose down`.

## Notes

- Make sure the port numbers provided above aren't being used by other services on your machine. If necessary, you can change the port numbers in the `docker-compose.yml` file.
- Replace the placeholders for `POSTGRES_USERNAME`, `POSTGRES_PASSWORD`, `PGADMIN_DEFAULT_EMAIL`, and `PGADMIN_DEFAULT_PASSWORD` in the `docker-compose.yml` file with your actual details.

## Flask-Migrate Instructions

### Set Up the Environment

Before running migrations, make sure your environment is correctly set up. This often means activating your virtual environment and setting any necessary environment variables. This can vary depending on your specific setup. Here's an example:

```bash
   source venv/bin/activate  # Activate your virtual environment
   export FLASK_APP=app.py   # Point Flask to your application
```

### Initialize Flask-Migrate

If you haven't already done so, you need to initialize Flask-Migrate. This creates a migrations directory which stores your migration scripts.

```bash
   flask db init
```

Note: You only need to run this command once.

### Generate a Migration Script

When your models change, you'll need to create a new migration script. This script contains instructions for how to update your database schema to match your models.

```bash
   flask db migrate -m "Description of the changes"
```

*Be sure to replace "Description of the changes" with a brief description of what changes the migration script should make.*

### Apply the Migrations

Once you've generated a migration script, you can apply the changes to your database with the following command:

```bash
   flask db upgrade
```

### Rollback (if necessary)

If you need to undo the last migration, you can use the downgrade command:

```bash
   flask db downgrade
```

### Things to Consider

Remember to include these migrations as part of your deployment process when you're ready to deploy your application.

Also, be sure to maintain good practices by testing your migrations in a separate testing environment before applying them to your production database.
