from app.models import db, User, environment, SCHEMA, Songs, Albums, Playlists
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(
        username='Demo',
        first_name = 'Demo',
        last_name = 'Tester',
        bio="First User",
        email='demo@aa.io',
        password='password'
        )
    
    marnie = User(
        username='marnie',
        first_name = "Marnie",
        last_name = "MA",
        bio="Second User",
        email='marnie@aa.io',
        password='password',
        )
    
    bobbie = User(
        username='bobbie',
        first_name= "Bobbie",
        last_name = "BA",
        bio="Third User",
        email='bobbie@aa.io',
        password='password'
        )
    
    album_1 = Albums (
        user_id = 1,
        title = "Gravity",
        year = 2013,
        date_created = datetime(2023, 9, 6)
    )

    playlist_1 = Playlists (
        user_id = 1,
        song_id = 1,
        title = "This is John Mayer",
        date_created = datetime(2023, 9, 6)
    )
    
    song_1 = Songs (
        user_id = 1,
        album_id = 1,
        # playlist_id = 1,
        title = "Perfectly Lonely",
        lyrics = """    
                    Had a little love
                    But I spread it thin
                    Falling in her arms and out again
                    I made a bad name for my game 'round town
                    Tore out my heart and shut it down
                    Nothing to do
                    Nowhere to be
                    A simple little a kind of free
                    Nothing to do
                    No one but me
                    And that's all I need
                    I'm perfectly lonely
                    I'm perfectly lonely
                    I'm perfectly lonely
                    Yeah
                    Cause I don't belong to anyone
                    And nobody belongs to me
                    I see my friends around from time to time
                    When the ladies let us slip away
                    And when they ask me how I'm doing with mine
                    This is always what I say
                    Nothing to do
                    Nowhere to be
                    A simple little kind of free
                    Nothing to do
                    No one to be
                    Is it really hard to see?
                    I'm perfectly lonely
                    I'm perfectly lonely
                    I'm perfectly lonely
                    Yeah
                    Cause I don't belong to anyone
                    And nobody belongs to me
                    And this is not to say
                    There never comes a day
                    I'll take my chances and start again
                    And when I look behind
                    On all my younger times
                    I have to thank the wrongs
                    That led me to a love so strong
                    I'm perfectly lonely
                    I'm perfectly lonely
                    I'm perfectly lonely
                    Yeah
                    Cause I don't belong to anyone
                    And nobody belongs to me
                    That's the way
                    That's the way
                    That's the way
                    That I want it
                    That's the way
                    That's the way
                    That's the way
                    That I want it
                    That's the way
                    That's the way
                    That's the way
                    That I want it
                    That's the way
                    That's the way
                    That's the way
                    That I want it
                    That's the way
                    That's the way
                    That's the way
                    That I want it
                    That's the way
                    That's the way
                    That's the way
                    That I want it
                    That's the way
                    That's the way
                    That's the way
                    That I want it
                    That's the way
                    That's the way
                    That's the way
                    That I want it 
                        """,
        date_created = datetime(2023, 9, 6)
    )

    db.session.add_all([demo, marnie, bobbie])
    db.session.add_all([album_1])
    db.session.add_all([playlist_1])
    db.session.add_all([song_1])

    db.session.commit()

    # playlist_song_association = playlist_songs.insert().values(
    #     playlist_id=playlist_1.id,
    #     song_id=song_1.id
    # )

    # db.session.execute(playlist_song_association)
    # db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()