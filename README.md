# Soundify

Step into Soundify, a meticulous recreation of Spotify, where users and artists connect in a familiar yet personalized space. Discover, create, enjoy – this is music made personal.

Live Link: https://soundify-render-actual.onrender.com

## Index

- Features List: https://github.com/SonQHoang/Soundify/wiki/Features-List
- Database Schema: https://github.com/SonQHoang/Soundify/wiki/Schema
- Frontend and Backend Routes:
- What's Coming Up Next: https://github.com/SonQHoang/Soundify/wiki/What's-Coming-Up-Next
  
<img width="1407" alt="Screenshot 2023-10-16 at 8 39 45 AM" src="https://github.com/SonQHoang/Soundify/assets/116997524/fc2f926b-7165-4b4b-90ab-5eebe42e14e0">
<img width="1425" alt="Screenshot 2023-10-16 at 8 39 59 AM" src="https://github.com/SonQHoang/Soundify/assets/116997524/a51b2358-c07e-4179-8291-59068a1c64d9">
<img width="1420" alt="Screenshot 2023-10-16 at 8 42 35 AM" src="https://github.com/SonQHoang/Soundify/assets/116997524/7e5fa1a1-9c5d-462d-83ce-ffd18fb661cd">
<img width="1419" alt="Screenshot 2023-10-16 at 8 42 44 AM" src="https://github.com/SonQHoang/Soundify/assets/116997524/515f85e5-a7f3-45f4-839d-1a126d4a5abe">


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
