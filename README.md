# Soundify

Step into Soundify, a meticulous recreation of Spotify, where users and artists connect in a familiar yet personalized space. Discover, create, enjoy – this is music made personal.

Live Link: https://soundify-render-actual.onrender.com

## Index

- Features List: https://github.com/SonQHoang/Soundify/wiki/Features-List
- Database Schema: https://github.com/SonQHoang/Soundify/wiki/Schema
- Frontend and Backend Routes:
- What's Coming Up Next: https://github.com/SonQHoang/Soundify/wiki/What's-Coming-Up-Next

Site Links

## Getting Started

1. Install dependencies

```
pipenv install -r requirements.txt
```

2. Create a .env file based on the example with proper settings for your development environment

3. Make sure the SQLite3 database connection URL is in the .env file

4. Replace the value for SCHEMA with a unique name, making sure you use the snake_case convention.

5. Get into your pipenv, migrate your database, seed your database, and run your Flask app

```
pipenv shell
flask db upgrade
flask seed all
flask run

To run the React App in development, checkout the README inside the react-app directory.
```

## Get in Touch:
- Sean Hoang: https://www.linkedin.com/in/sean-hoang/
