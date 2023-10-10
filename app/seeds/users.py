from app.models import db, User, environment, SCHEMA, Songs, Albums, Playlists
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(
        username='Demo',
        first_name = 'Demo',
        last_name = 'Tester',
        email='demo@aa.io',
        password='password'
        )
    
    marnie = User(
        username='marnie',
        first_name = "Marnie",
        last_name = "MA",
        email='marnie@aa.io',
        password='password',
        )
    
    bobbie = User(
        username='bobbie',
        first_name= "Bobbie",
        last_name = "BA",
        email='bobbie@aa.io',
        password='password'
        )
    
    album_1 = Albums (
        user_id = 1,
        title = "Continuum",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Continuum+Album+Art+John+Mayer.png",
        owner = "John Mayer",
        year = 2006,
        date_created = datetime(2023, 9, 6)
    )

    album_2 = Albums (
        user_id = 1,
        title = "+",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Plus+Album+Art+Ed+Sheeran.png",
        owner = "Ed Sheeran",
        year = 2011,
        date_created = datetime(2023, 9, 6)
    )

    album_3 = Albums (
        user_id = 1,
        title = "x",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Multiply+Album+Art+Ed+Sheeran.jpeg",
        owner = "Ed Sheeran",
        year = 2014,
        date_created = datetime(2023, 9, 6)
    )

    album_4 = Albums (
        user_id = 1,
        title = "=",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Equals+Album+Art.png",
        owner = "Ed Sheeran",
        year = 2013,
        date_created = datetime(2023, 9, 6)
    )

    album_5 = Albums (
        user_id = 1,
        title = "÷",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Divide+Album+Art+Ed+Sheeran.jpg",
        owner = "Ed Sheeran",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_6 = Albums (
        user_id = 1,
        title = "It's Time",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Its+Time+Album+Art+Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_7 = Albums (
        user_id = 1,
        title = "Red",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Red+Album+Art+Taylor+Swift.jpeg",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_8 = Albums (
        user_id = 1,
        title = "Battle Studies",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Battle+Studies+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_9 = Albums (
        user_id = 1,
        title = "Born and Raised",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Born+and+Raised+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_10 = Albums (
        user_id = 1,
        title = "Paradise Valley",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Paradise+Valley+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_11 = Albums (
        user_id = 1,
        title = "Room For Squares",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Room+For+Squares+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_12 = Albums (
        user_id = 1,
        title = "Say",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Say+John+Mayer.png",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_13 = Albums (
        user_id = 1,
        title = "Sob Rock",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Sob+Rock+John+Mayer.png",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_14 = Albums (
        user_id = 1,
        title = "The Search for Everything",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/The+Search+for+Everything+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_15 = Albums (
        user_id = 1,
        title = "XO",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/XO+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_16 = Albums (
        user_id = 1,
        title = "1989",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/1989+Taylor+Swift.webp",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_17 = Albums (
        user_id = 1,
        title = "Fearless",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Fearless+Orig+Taylor+Swift.png",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_18 = Albums (
        user_id = 1,
        title = "Fearless (Taylor's Version)",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Fearless+Taylor+Swift.png",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_19 = Albums (
        user_id = 1,
        title = "Love Story (Taylor's Version)",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Love+Story+Taylor+Swift.jpeg",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_20 = Albums (
        user_id = 1,
        title = "Lover",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Lover+Taylor+Swift.jpeg",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_21 = Albums (
        user_id = 1,
        title = "Speak Now (Taylor's Version)",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Speak+Now+Taylor+Swift.png",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_22 = Albums (
        user_id = 1,
        title = "Call Me Irresponsible",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Call+Me+Irresponsible+Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_23 = Albums (
        user_id = 1,
        title = "Call Me Irresponsible (Deluxe)",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Call+Me+Irresponsible+Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_24 = Albums (
        user_id = 1,
        title = "Crazy Love",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Crazy+Love+Michael+Buble.png",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_25 = Albums (
        user_id = 1,
        title = "It's Time",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/It's+time+Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_26 = Albums (
        user_id = 1,
        title = "Love (Deluxe Edition)",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Love+Michael+Buble.jpg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_27 = Albums (
        user_id = 1,
        title = "Michael Bublé",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_28 = Albums (
        user_id = 1,
        title = "Special Delivery",
        album_photo = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/Special+Delivery+Michael+Buble.jpg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_29 = Albums (
        user_id = 1,
        title = "To Be Loved",
        album_photo = "",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    playlist_1 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/This+is+John+Mayer.jpeg",
        title = "This is John Mayer",
        date_created = datetime(2023, 9, 6)
    )

    # playlist_2 = Playlists (
    #     user_id = 2,
    #     owner = "Marnie",
    #     title = "This is John Mayer",
    #     date_created = datetime(2023, 9, 6)
    # )

    playlist_3 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/This+is+Ed+Sheeran.jpeg",
        title = "This is Ed Sheeran",
        date_created = datetime(2023, 9, 6)
    )

    playlist_4 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/This+is+Taylor+Swift.jpeg",
        title = "This is Taylor Swift",
        date_created = datetime(2023, 9, 6)
    )

    playlist_5 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/AlbumCoverArt/This+is+Michael+Buble.jpeg",
        title = "This is Michael Bublé",
        date_created = datetime(2023, 9, 6)
    )
    
    song_1 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/05+-+John+Mayer+-+Perfectly+Lonely.mp3",
        title = "Perfectly Lonely",
        artist = "John Mayer",
        duration = "4:28",
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

    song_2 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Heartbreak+Warfare.mp3",
        title = "Heartbreak Warfare",
        artist = "John Mayer",
        duration = "4:29",
        lyrics = """
                    Lightning strikes
                    Inside my chest to keep me up at night
                    Dream of ways
                    To make you understand my pain

                    Clouds of sulfur in the air
                    Bombs are falling everywhere
                    It's heartbreak warfare
                    Once you want it to begin,
                    No one really ever wins
                    In heartbreak warfare

                    If you want more love why don't you say so?
                    If you want more love why don't you say so?

                    Drop his name
                    Push it in and twist the knife again
                    Watch my face
                    As I pretend to feel no pain, pain, pain..

                    Clouds of sulfur in the air
                    Bombs are falling everywhere
                    It's heartbreak warfare
                    Once you want it to begin,
                    No one really ever wins
                    In heartbreak warfare.

                    If you want more love why don't you say so?
                    If you want more love why don't you say so?

                    Just say so...

                    How come the only way to know how high you get me is to see how far I fall?
                    God only knows how much I'd love you if you let me but I can't break through it all.

                    It's a heart... heartbreak...

                    I don't care if we don't sleep at all tonight
                    Let's just fix this whole thing now
                    I swear to God we're gonna get it right
                    If you lay your weapon down
                    Red wine and Ambien
                    You're talking shit again, it's heartbreak warfare
                    Good to know it's all a game
                    Disappointment has a name, it's heartbreak, heartbreak.

                    It's heartbreak warfare
                    It's heartbreak warfare
                    It's heartbreak warfare
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_3 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+Wynton+Marsalis+Septet%2C+John+Mayer%2C+Wynton+Marsalis+-+I'm+Gonna+Find+Another+You.mp3",
        title = "I'm Gonna Find Another You",
        artist = "John Mayer",
        duration = "2:44",
        lyrics = """
                    It's really over
                    You made your stand
                    You got me crying
                    As was your plan
                    But when my loneliness is through
                    I'm gonna find another you
                    You take your sweaters
                    You take your time
                    You might have your reasons
                    But you will never have my rhyme
                    I'm gonna sing my way away from blue
                    I'm gonna find another you
                    When I was your lover
                    No one else would do
                    If I'm forced to find another
                    I hope she looks like you
                    Yeah, and she's nicer too
                    So go on, baby
                    Make your little getaway
                    My pride will keep me company
                    And you just gave yours all away
                    Oh, now I'm gonna dress myself for two
                    Once for me, and once for someone new
                    I'm gonna do some things you wouldn't let me do
                    I'm gonna find another you
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_4 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/08+-+John+Mayer+-+Love+Is+A+Verb.mp3",
        title = "Love is a Verb",
        artist = "John Mayer",
        duration = "2:24",
        lyrics = """
                    Love is a verb
                    It ain't a thing
                    It's not something you own
                    It's not something you scream
                    When you show me love
                    I don't need your words
                    Yeah love ain't a thing
                    Love is a verb
                    Love ain't a thing
                    Love is a verb
                    Love ain't a crutch
                    It ain't an excuse
                    No you can't get through love
                    On just a pile of I-O-Us
                    Love ain't a drug
                    Despite what you've heard
                    Yeah love ain't a thing
                    Love is a verb
                    Love ain't a thing
                    Love is a verb
                    So you gotta show, show, show me
                    Show, show, show me
                    Show, show, show me
                    That love is a verb
                    You gotta show, show, show me
                    Show, show, show me
                    Show, show, show me
                    That love is a verb
                    Love ain't a thing
                    Love is a verb
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_5 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Last+Train+Home.mp3",
        title = "Last Train Home",
        artist = "John Mayer",
        duration = "3:07",
        lyrics = """
                If you wanna roll me
                Then you gotta roll me all night long
                And if you wanna use me
                Then you gotta use me 'til I'm gone
                I'm not a fallen angel, I just fell behind
                I'm out of luck and I'm out of time
                If you don't wanna love me, let me go
                I'm runnin' for the last train
                I'm runnin' for the last train home
                If you wanna know me
                Then you gotta know me through and through
                And if you're gonna hurt me
                Then you gotta hold me next to you
                No matter how you work it, things go wrong
                I put my heart where it don't belong
                So if you're comin' with me, let me know
                Maybe you're the last train
                Maybe you're the last train home
                I'm on the last train runnin'
                I'm on the last train runnin'
                And I surrender
                And I surrender
                I'm on the last train runnin'
                I'm on the last train runnin'
                And I surrender
                And I surrender
                I'm on the last train runnin'
                I'm on the last train runnin'
                And I surrender
                And I surrender
                I'm on the last train runnin'
                I'm on the last train runnin'
                And I surrender
                And I surrender
                (Oh, yeah)
                (Ooh)
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_6 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/05+-+John+Mayer+-+Neon.mp3",
        title = "Neon",
        artist = "John Mayer",
        duration = "4:21",
        lyrics = """
            When sky blue gets dark enough
            To see the colors of the city lights
            A trail of ruby red and diamond white
            Hits her like a sunrise
            She comes and she goes
            Like no one can
            Tonight she's out to lose herself
            And find a high on Peachtree Street
            From mixed drinks to techno beats it's always
            Heavy into everything
            She comes and goes and comes and goes
            Like no one can
            She comes and goes and no one knows
            She's slipping through my hands
            She's always buzzing just like
            Neon, neon
            Neon, neon
            Who knows how long, how long, how long
            She can go before she burns away
            I can't be her angel now
            You know it's not my place to hold her down
            And it's hard for me to take a stand
            When I would take her anyway I can
            She comes and goes and comes and goes
            Like no one can
            She comes and goes and no one knows
            She's slipping through my hands
            She's always buzzing just like
            Neon, neon
            Neon, neon
            Who knows how long, how long, how long
            She can go before she burns away
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_7 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+No+Such+Thing.mp3",
        title = "No Such Thing",
        artist = "John Mayer",
        duration = "3:51",
        lyrics = """
                Welcome to the real world
                She said to me condescendingly
                Take a seat, take your life
                Plot it out in black and white
                Well, I never lived the dream of the prom kings
                And the drama queens
                I'd like to think the best of me
                Is still hiding up my sleeve
                They love to tell you
                Stay inside the lines
                But something's better
                On the other side
                I wanna run through the halls of my high school
                I wanna scream at the top of my lungs
                I just found out there's no such thing as the real world
                Just a lie you've got to rise above
                So the good boys and girls
                Take the so called right track
                Faded white hats
                Grabbing credits and maybe transfers
                They read all the books but they can't find the answers
                And all of our parents, they're getting older
                I wonder if they've wished for anything better
                While in their memories tiny tragedies
                They love to tell you
                Stay inside the lines
                But something's better
                On the other side
                I wanna run through the halls of my high school
                I wanna scream at the top of my lungs
                I just found out there's no such thing as the real world
                Just a lie you got to rise above
                I am invincible
                I am invincible
                I am invincible
                As long as I'm alive
                I wanna run through the halls of my high school
                I wanna scream at the top of my lungs
                I just found out there's no such thing as the real world
                Just a lie you've got to rise above
                I just can't wait 'til my ten year reunion
                I'm gonna bust down the double doors
                And when I stand on these tables before you
                You will know what all this time was for
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_8 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Queen+of+California.mp3",
        title = "Queen of California",
        artist = "John Mayer",
        duration = "4:10",
        lyrics = """
                Goodbye cold, goodbye rain
                Goodbye sorrow, goodbye shame
                I'm headed out west with my headphones on
                Boarded a flight with a song in the back of my soul
                And no one knows
                I just found out her ghost left town
                The Queen of California is stepping down, down
                Hello beauty, hello strange
                Hello wonder, what's your name?
                Looking for the sun that Neil Young hung
                After the gold rush of 1971
                I just found out her ghost left town
                The Queen of California is stepping down, down
                If you see her say, "Hello"
                Just don't tell me, "I told you so"
                Joni wrote Blue in her house by the sea
                I gotta believe there's another color waiting on me
                To set me free
                I just found out her ghost left town
                The Queen of California is stepping down, down
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_9 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Say.mp3",
        title = "Say",
        artist = "John Mayer",
        duration = "3:50",
        lyrics = """
                Take all of your wasted honor
                Every little past frustration
                Take all of your so-called problems
                Better put 'em in quotations

                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say

                Walking like a one man army
                Fighting with the shadows in your head
                Living out the same old moment
                Knowing you'd be better off instead
                If you could only

                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say

                Have no fear for giving in
                Have no fear for giving over
                You'd better know that in the end
                It's better to say too much
                Than never to say what you need to say again

                Even if your hands are shaking
                And your faith is broken
                Even as the eyes are closing
                Do it with a heart wide open

                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                Say what you need to say
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_10 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Still+Feel+Like+Your+Man.mp3",
        title = "Still Feel Like Your Man",
        artist = "John Mayer",
        duration = "3:55",
        lyrics = """
                I still feel like your man, oh
                I still feel like your man, ooh
                I still feel
                I still feel
                I still feel like your man
                I still feel like
                The prettiest girl in the room, she wants me
                I know because she told me so
                She says come over
                I'd like to get to know you
                But I just don't think I can
                'Cause I still feel like your man
                Still feel like your man
                Still feel like your man
                Still feel like your man
                I still feel like your man
                I still keep your shampoo in my shower
                In case you wanna wash your hair
                And I know that you probably found yourself some more, somewhere
                But I do not really care
                'Cause as long as it is there
                I still feel like your man
                Still feel like your man
                Still feel like your man
                (Oh oh, momma)
                Still feel like your man
                I still feel like your man
                Your man
                Ever since the day we met, ever since the day we met
                Still like the letters in your name and how they feel, babe
                Still think I'm never gonna find another you
                Still like to leave the party early and go home, babe
                And don't you know, babe
                I'd rather sit here on my own and be alone, babe
                'Cause I still feel like your man
                Still feel like your man
                I still feel like your man
                (Oh, honey)
                Still feel like your man
                I still feel like your man
                Still feel like your man
                Still feel like your man
                And I don't know why
                Still feel like your man
                I still feel like
                I still feel like
                I still feel like
                I still
                I still
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_11 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Waiting+On+the+World+to+Change.mp3",
        title = "Waiting On the World to Change",
        artist = "John Mayer",
        duration = "3:21",
        lyrics = """
                One, two
                One, two, three
                Me and all my friends
                We're all misunderstood
                They say we stand for nothing and
                There's no way we ever could
                Now we see everything that's going wrong
                With the world and those who lead it
                We just feel like we don't have the means
                To rise above and beat it
                So we keep waiting (waiting)
                Waiting on the world to change
                We keep on waiting (waiting)
                Waiting on the world to change
                It's hard to beat the system
                When we're standing at a distance
                So we keep waiting on (waiting)
                Waiting on the world to change
                Now if we had the power
                To bring our neighbors home from war
                They woulda never missed a Christmas
                No more ribbons on their door
                And when you trust your television
                What you get is what you got
                'Cause when they own the information, oh
                They can bend it all they want
                That's why we're waiting (waiting)
                Waiting on the world to change
                We keep on waiting (waiting)
                Waiting on the world to change
                It's not that we don't care
                We just know that the fight ain't fair
                So we keep on waiting (waiting)
                Waiting on the world to change
                And we're still waiting (waiting)
                Waiting on the world to change
                We keep on waiting (waiting)
                Waiting on the world to change
                One day our generation
                Is gonna rule the population
                So we keep on waiting (waiting)
                Waiting on the world to change
                Now I keep on waiting (waiting)
                Waiting on the world to change
                We keep on waiting (waiting)
                We're waiting on the world to change
                Waiting on the world to change
                Waiting on the world to change
                Waiting on the world to change
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_12 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Wildfire.mp3",
        title = "Wildfire",
        artist = "John Mayer",
        duration = "4:13",
        lyrics = """
                River's strong you can swim inside it
                Then we could string some lights up the hill beside it
                Tonight the moon's so bright
                You could drive with your headlights out
                'Cause a little bit of summer's what the whole year's all about
                You look fine, fine, fine
                Put your feet up next to mine
                We can watch that water line
                Get higher and higher
                Say, say, say
                Ain't it been some kind of day
                You and me been catching on
                Like a wildfire
                Don't get up just to get another
                You can drink from mine
                We can't leave each other
                But we can dance with the dead
                You can rest your head on my shoulder
                If you want to get older with me
                'Cause a little bit of summer makes a lot of history
                And you look fine, fine, fine
                Put your feet up next to mine
                We can watch that water line
                Get higher and higher
                Say, say, say
                Ain't it been some kind of day
                You and me been catchin' on
                Like a wildfire
                I got a rock from the river in my medicine bag
                Magpie feather in his medicine bag
                Say, say, say
                Ain't it been some kind of day
                You and me been catchin' on
                Like a wildfire
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_13 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+XO.mp3",
        title = "XO",
        artist = "John Mayer",
        duration = "3:33",
        lyrics = """
                Your love is bright as ever
                Even in the shadows
                Baby, kiss me
                Before they turn the lights out
                Your heart is glowing
                And I'm crashing into you
                Baby, kiss me kiss me
                Before they turn the lights out
                Before they turn the lights out
                Baby, love me lights out
                In the darkest night
                I'll search through the crowd,
                Your face is all that I see
                I'll give you everything
                Baby, love me lights out
                Baby, love me lights out
                We don't have forever
                Baby, daylight's wasting
                You better kiss me
                Before our time has run out
                Nobody sees what we see
                They're just hopelessly gazing
                Baby, take me take me
                Before they turn the lights out
                Before time has run out
                Baby, love me lights out
                In the darkest night
                I'll search through the crowd,
                Your face is all that I see
                I'll give you everything
                Baby, love me lights out
                Baby, love me lights out
                You can turn my lights out
                I love you like XO
                You love me like XO
                You kill me, girl, XO
                You love me like XO
                All that I see
                Give you everything
                Baby, love me lights out
                Baby, love me lights out
                You can turn my lights out
                In the darkest night
                I'll search through the crowd,
                Your face is all that I see
                I'll give you everything
                Baby, love me lights out
                Baby, love me lights out
                You can turn my lights out
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_14 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Dear+Marie.mp3",
        title = "Dear Marie",
        artist = "John Mayer",
        duration = "3:42",
        lyrics = """
                Dear Marie, tell me what it was I used to be
                Dear Marie, tell me what it was I used to be
                And if you're further up the road can you show me what I still can't see
                Remember me, I'm the boy you used to love when we were fifteen
                Remember me, I'm the boy you used to love when we were fifteen
                Now I wonder what you think when you see me on the magazine
                From time to time, I go looking for your photograph online
                From time to time, I go looking for your photograph online
                Some county judge in Ohio is all I ever find
                Dear Marie, tell me do you still believe in me
                Dear Marie, tell me do you still believe in me
                Yeah I've got my dream but you've got family
                Yeah I've got my dream but you've got family
                Yeah I've got my dream but I guess it got away from me
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_15 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Emoji+of+a+Wave.mp3",
        title = "Emoji of a Wave",
        artist = "John Mayer",
        duration = "3:59",
        lyrics = """
                Oh honey
                You don't have to try so hard
                To hurt me
                Don't worry
                I been thinking bout you too
                What do we do
                Your heart is where my head should be
                The dissonance is killing me
                It breaks my heart
                It breaks my heart
                Oh honey
                Oh honey
                It's just a wave
                It's just a wave and I know
                That when it comes
                I just hold on
                I just hold on
                Oh honey
                I been talking to myself
                Just to hear you
                And you're saying
                Everything I wish you would
                And it's so good
                It's raining on the mission bell
                They're draining out the wishing well
                It breaks my heart
                It breaks my heart
                Oh honey
                Oh honey
                It's just a wave
                It's just a wave and I know
                That when it comes
                I just hold on
                I just hold on
                I rose on you like morning light
                In shuttered dream we'll sleep at night
                It breaks my heart
                It takes all the love I have to say
                I know we're gonna be ok
                It breaks my heart
                It breaks my heart
                Oh honey
                Oh honey
                It's just a wave
                It's just a wave and I know
                That when it comes
                I just hold on
                Until it's gone
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_16 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+Tony+Bennett%2C+John+Mayer+-+One+for+My+Baby+(And+One+More+for+the+Road).mp3",
        title = "One for My Baby (And One More for the Road)",
        artist = "John Mayer",
        duration = "2:56",
        lyrics = """
                It's quarter to three
                There's no one in the place except you and me
                Set 'em up, Joe,
                You know John I've got a little story that you ought know
                Maybe you've heard about this
                We're drinking, my friend
                To the end of a brief episode
                (I'm telling you, this is what happened)
                Make it one for my baby
                And one more for the road
                I got the routine (Oh no, you too?)
                So drop another nickel in the machine
                Men I'm feeling so bad
                I wish you'd make the music dreamy and sad
                I Could tell you a lot (You too?)
                But you've got to be true to your code
                Make it one for my baby
                And one more for the road
                You'd never know it but buddy, I'm a kind of poet
                And I got a lot of things to say
                And when I'm gloomy
                You simply gotta listen to me
                Until it's talked away
                That's how it goes
                John I know your getting pretty anxious to close (John: You don't know me well then)
                Tony thanks for the cheer
                I hope you didn't mind my bending your ear
                'Cause this torch that I found must be drowned or it soon might explode
                Make it one for my baby
                And one more for the road
                That long, long road
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_17 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Shouldn't+Matter+but+It+Does.mp3",
        title = "Shouldn't Matter but It Does",
        artist = "John Mayer",
        duration = "3:56",
        lyrics = """
                Shoulda been open
                Shoulda done more
                Shoulda learned a lesson from the year before
                Shoulda been honest
                Shoulda just cried
                Shoulda told me there was nothing left inside
                Now the road keeps rolling on forever
                And the years keep pulling us apart
                We lost something, I still wonder what it was
                It shouldn't matter
                Shouldn't matter, but it does
                You shoulda just broken
                You shoulda come clean
                You shoulda been sad instead of being so fucking mean
                It shouldn't be easy
                But it shouldn't be hard
                You shouldn't be a stranger in your own backyard
                Now the road keeps rolling on forever
                And the years keep pulling us apart
                I know it's over, I'm just saying this because
                It shouldn't matter
                Shouldn't matter, but it does
                I shouldn't be angry
                I shouldn't hold on
                I shouldn't leave you messages in every little song
                It could have been always
                It could have been me
                We could have been busy naming baby number three
                Now the road keeps rolling on forever
                And the years keep pulling us apart
                If it's on someone, then I blame the both of us
                It shouldn't matter
                Shouldn't matter, but it
                Shouldn't matter
                Shouldn't matter, but it
                Shouldn't matter
                Shouldn't matter, but it does
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_18 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+The+Age+of+Worry.mp3",
        title = "The Age of Worry",
        artist = "John Mayer",
        duration = "2:37",
        lyrics = """
                Close your eyes and clone yourself
                Build your heart an army
                To defend your innocence
                While you do everything wrong

                Don't be scared to walk alone
                Don't be scared to like it
                There's no time that you must be home
                So sleep where darkness falls

                Alive in the age of worry
                Smile in the age of worry
                Go wild in the age of worry
                And say, "Worry, why should I care?"

                Know your fight is not with them
                Yours is with your time here
                Dream your dreams but don't pretend
                Make friends with what you are

                Give your heart then change your mind
                You're allowed to do it
                'Cause God knows it's been done to you
                And somehow you got through it

                Alive in the age of worry
                Rage in the age of worry
                Sing out in the age of worry
                And say, "Worry, why should I care?"

                Rage in the age of worry
                Act your age in the age of worry
                And say, "Worry, get out of here!"
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_19 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Why+Georgia.mp3",
        title = "Why Georgia",
        artist = "John Mayer",
        duration = "4:28",
        lyrics = """
                I am driving up 85 in the
                Kind of morning that lasts all afternoon
                I'm just stuck inside the gloom
                4 more exits to my apartment but
                I am tempted to keep the car in drive
                And leave it all behind
                'Cause I wonder sometimes
                About the outcome
                Of a still verdictless life
                Am I living it right?
                Am I living it right?
                Am I living it right?
                Why, why Georgia, why?
                I rent a room and I fill the spaces with
                Wood in places to make it feel like home
                But all I feel's alone
                It might be a quarter life crisis
                Or just the stirring in my soul
                Either way I wonder sometimes
                About the outcome
                Of a still verdictless life
                Am I living it right?
                Am I living it right?
                Am I living it right?
                Why, why Georgia, why?
                So what, so I've got a smile on
                But it's hiding the quiet superstitions in my head
                Don't believe me
                Don't believe me
                When I say I've got it down
                Everybody is just a stranger but
                That's the danger in going my own way
                I guess it's the price I have to pay
                Still "everything happens for a reason"
                Is no reason not to ask myself if I
                Am living it right?
                Am I living it right?
                Am I living it right?
                Why, tell me why,
                Why, why Georgia, why?
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_20 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/03+-+John+Mayer+-+Half+of+My+Heart.mp3",
        title = "Half of My Heart",
        artist = "John Mayer",
        duration = "4:10",
        lyrics = """
                I was born in the arms of imaginary friends
                Free to roam, made a home out of everywhere I've been
                Then you come on crashing in
                Like the realest thing
                Tried my best to understand
                All that your love can bring
                Half of my heart's got a grip on the situation
                Half of my heart takes time
                Half of my heart's got the right mind to tell you
                That I can't keep loving you
                With half of my heart
                I was made to believe I'd never love somebody else
                Made a plan, stayed the man who can only love himself
                Lonely was the song I sang
                'Til the day you came
                Showing me another way
                And all that my love can bring
                Half of my heart's got a grip on the situation
                Half of my heart takes time
                Half of my heart's got the right mind to tell you
                That I can't keep loving you
                With half of my heart
                With half of my heart
                Your faith is strong
                But I can only fall short for so long
                Down the road later on
                You will hate that I never gave more to you
                Than half of my heart
                But I can't stop loving you
                I can't stop loving you
                I can't stop loving you
                With half of my
                Half of my heart
                Half of my heart
                Half of my heart's got a real good imagination
                Half of my heart's got you
                Half of my heart's got a right mind to tell you
                That half of my heart won't do
                Half of my heart is a shotgun wedding
                To a bride with a paper ring
                And half of my heart is the part of a man
                Who's never truly loved anything
                Half of my heart
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_21 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/02+-+Ed+Sheeran+-+Castle+on+the+Hill.mp3",
        title = "Castle on the Hill",
        artist = "Ed Sheeran",
        duration = "4:21",
        lyrics = """
                When I was six years old, I broke my leg
                When I was running from my brother and his friends
                And tasted the sweet perfume of the mountain grass I rolled down
                Well, I was younger then, take me back to when
                I found my heart and broke it here
                Made friends and lost them through the years
                And I've not seen the roaring fields in so long, I know I've grown
                But I can't wait to go home
                I'm on my way
                Driving at 90 down those country lanes
                Singing to "Tiny Dancer"
                And I miss the way you make me feel, and it's real
                And we watched the sunset over the castle on the hill
                15 years old and smoking hand-rolled cigarettes
                Running from the law through the backfields
                And getting drunk with my friends
                Had my first kiss on a Friday night
                I don't reckon that I did it right
                But I was younger then, take me back to when
                We found weekend jobs, when we got paid
                We'd buy cheap spirits and drink them straight
                Me and my friends have not thrown up in so long, oh, how we've grown
                But I can't wait to go home
                I'm on my way (hoo-hoo)
                Driving at 90 down those country lanes (hoo-hoo)
                Singing to "Tiny Dancer"
                And I miss the way you make me feel, and it's real
                And we watched the sunset (hoo-hoo), over the castle on the hill
                Hoo-hoo, over the castle on the hill
                Hoo-hoo, over the castle on the hill
                One friend left to sell clothes, one works down by the coast
                One had two kids but lives alone, one's brother overdosed
                One's already on his second wife, one's just barely getting by
                But these people raised me and I can't wait to go home
                And I'm on my way
                I still remember these old country lanes
                When we did not know the answers
                And I miss the way (hoo-hoo) you make me feel, it's real
                When we watched the sunset (hoo-hoo) over the castle on the hill
                Hoo-hoo, over the castle on the hill
                Hoo-hoo, over the castle on the hill
                        """,
        date_created = datetime(2023, 9, 6)
    )
    
    song_22 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/04+-+Ed+Sheeran+-+Shape+of+You.mp3",
        title = "Shape of You",
        artist = "Ed Sheeran",
        duration = "3:53",
        lyrics = """
                The club isn't the best place to find a lover
                So the bar is where I go
                Me and my friends at the table doing shots
                Drinking fast and then we talk slow
                Come over and start up a conversation with just me
                And trust me I'll give it a chance now
                Take my hand, stop, put Van the Man on the jukebox
                And then we start to dance, and now I'm singing like
                Girl, you know I want your love
                Your love was handmade for somebody like me
                Come on now, follow my lead
                I may be crazy, don't mind me
                Say, boy, let's not talk too much
                Grab on my waist and put that body on me
                Come on now, follow my lead
                Come, come on now, follow my lead
                I'm in love with the shape of you
                We push and pull like a magnet do
                Although my heart is falling too
                I'm in love with your body
                Last night you were in my room
                And now my bedsheets smell like you
                Every day discovering something brand new
                I'm in love with your body
                (Oh-I-oh-I-oh-I-oh-I)
                I'm in love with your body
                (Oh-I-oh-I-oh-I-oh-I)
                I'm in love with your body
                (Oh-I-oh-I-oh-I-oh-I)
                I'm in love with your body
                Every day discovering something brand new
                I'm in love with the shape of you
                One week in we let the story begin
                We're going out on our first date
                You and me are thrifty, so go all you can eat
                Fill up your bag and I fill up a plate
                We talk for hours and hours about the sweet and the sour
                And how your family is doing okay
                And leave and get in a taxi, then kiss in the backseat
                Tell the driver make the radio play, and I'm singing like
                Girl, you know I want your love
                Your love was handmade for somebody like me
                Come on now, follow my lead
                I may be crazy, don't mind me
                Say, boy, let's not talk too much
                Grab on my waist and put that body on me
                Come on now, follow my lead
                Come, come on now, follow my lead
                I'm in love with the shape of you
                We push and pull like a magnet do
                Although my heart is falling too
                I'm in love with your body
                Last night you were in my room
                And now my bedsheets smell like you
                Every day discovering something brand new
                I'm in love with your body
                (Oh-I-oh-I-oh-I-oh-I)
                I'm in love with your body
                (Oh-I-oh-I-oh-I-oh-I)
                I'm in love with your body
                (Oh-I-oh-I-oh-I-oh-I)
                I'm in love with your body
                Every day discovering something brand new
                I'm in love with the shape of you
                Come on, be my baby, come on
                Come on, be my baby, come on
                Come on, be my baby, come on
                Come on, be my baby, come on
                Come on, be my baby, come on
                Come on, be my baby, come on
                Come on, be my baby, come on
                Come on, be my baby, come on
                I'm in love with the shape of you
                We push and pull like a magnet do
                Although my heart is falling too
                I'm in love with your body
                Last night you were in my room
                And now my bedsheets smell like you
                Every day discovering something brand new
                I'm in love with your body
                Come on, be my baby, come on
                Come on (I'm in love with your body), be my baby, come on
                Come on, be my baby, come on
                Come on (I'm in love with your body), be my baby, come on
                Come on, be my baby, come on
                Come on (I'm in love with your body), be my baby, come on
                Every day discovering something brand new
                I'm in love with the shape of you
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_23 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/05+-+Ed+Sheeran+-+Perfect.mp3",
        title = "Perfect",
        artist = "Ed Sheeran",
        duration = "4:23",
        lyrics = """
                I found a love, for me
                Darling, just dive right in and follow my lead
                Well, I found a girl, beautiful and sweet
                Oh, I never knew you were the someone waiting for me
                'Cause we were just kids when we fell in love
                Not knowing what it was
                I will not give you up this time
                But darling, just kiss me slow
                Your heart is all I own
                And in your eyes, you're holding mine
                Baby, I'm dancing in the dark
                With you between my arms
                Barefoot on the grass
                Listening to our favourite song
                When you said you looked a mess
                I whispered underneath my breath
                But you heard it
                Darling, you look perfect tonight
                Well, I found a woman, stronger than anyone I know
                She shares my dreams, I hope that someday I'll share her home
                I found a lover, to carry more than just my secrets
                To carry love, to carry children of our own
                We are still kids, but we're so in love
                Fighting against all odds
                I know we'll be alright this time
                Darling, just hold my hand
                Be my girl, I'll be your man
                I see my future in your eyes
                Baby, I'm dancing in the dark
                With you between my arms
                Barefoot on the grass
                Listening to our favorite song
                When I saw you in that dress, looking so beautiful
                I don't deserve this
                Darling, you look perfect tonight
                Baby, I'm dancing in the dark
                With you between my arms
                Barefoot on the grass
                Listening to our favorite song
                I have faith in what I see
                Now I know I have met an angel in person
                And she looks perfect
                I don't deserve this
                You look perfect tonight
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_24 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/06+-+Ed+Sheeran+-+Galway+Girl.mp3",
        title = "Galway Girl",
        artist = "Ed Sheeran",
        duration = "2:51",
        lyrics = """
                She played the fiddle in an Irish band
                But she fell in love with an English man
                Kissed her on the neck and then I took her by the hand
                Said, "Baby, I just want to dance"
                I met her on Grafton street right outside of the bar
                She shared a cigarette with me while her brother played the guitar
                She asked me what does it mean, the Gaelic ink on your arm?
                Said it was one of my friend's songs, do you want to drink on?
                She took Jamie as a chaser, Jack for the fun
                She got Arthur on the table with Johnny riding a shotgun
                Chatted some more, one more drink at the bar
                Then put Van on the jukebox, got up to dance
                You know, she played the fiddle in an Irish band
                But she fell in love with an English man
                Kissed her on the neck and then I took her by the hand
                Said, "Baby, I just want to dance"
                With my pretty little Galway Girl
                You're my pretty little Galway Girl
                You know she beat me at darts and then she beat me at pool
                And then she kissed me like there was nobody else in the room
                As last orders were called was when she stood on the stool
                After dancing to Cèilidh singing to trad tunes
                I never heard Carrickfergus ever sang so sweet
                A capella in the bar using her feet for a beat
                Oh, I could have that voice playing on repeat for a week
                And in this packed out room swear she was singing to me
                You know, she played the fiddle in an Irish band
                But she fell in love with an English man
                Kissed her on the neck and then I took her by the hand
                Said, "Baby, I just want to dance"
                My pretty little Galway Girl
                My, my, my, my, my, my, my Galway Girl
                My, my, my, my, my, my, my Galway Girl
                My, my, my, my, my, my, my Galway Girl
                And now we've outstayed our welcome and it's closing time
                I was holding her hand, her hand was holding mine
                Our coats both smell of smoke, whisky and wine
                As we fill up our lungs with the cold air of the night
                I walked her home then she took me inside
                To finish some Doritos and another bottle of wine
                I swear I'm gonna put you in a song that I write
                About a Galway Girl and a perfect night
                She played the fiddle in an Irish band
                But she fell in love with an English man
                Kissed her on the neck and then I took her by the hand
                Said, "Baby, I just want to dance"
                My pretty little Galway Girl
                My, my, my, my, my, my, my Galway Girl
                My, my, my, my, my, my, my Galway Girl
                My, my, my, my, my, my, my Galway Girl
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_25 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/07+-+Ed+Sheeran+-+Happier.mp3",
        title = "Happier",
        artist = "Ed Sheeran",
        duration = "3:28",
        lyrics = """
                Walking down 29th and Park
                I saw you in another's arms
                Only a month we've been apart
                You look happier
                Saw you walk inside a bar
                He said somethin' to make you laugh
                I saw that both your smiles were twice as wide as ours
                Yeah, you look happier, you do
                Ain't nobody hurt you like I hurt you
                But ain't nobody love you like I do
                Promise that I will not take it personal, baby
                If you're movin' on with someone new
                'Cause baby you look happier, you do
                My friends told me one day I'll feel it too
                And until then I'll smile to hide the truth
                But I know I was happier with you
                Sat in the corner of the room
                Everything's reminding me of you
                Nursing an empty bottle
                And telling myself you're happier, aren't you?
                (Hey, yeah, hey, yeah, hey, yeah)
                Oh, ain't nobody hurt you like I hurt you (hey, yeah, hey, yeah)
                But ain't nobody need you like I do (hey, yeah, hey, yeah)
                I know that there's others that deserve you (hey, yeah, hey, yeah)
                But my darlin', I am still in love with you
                But I guess you look happier, you do
                My friends told me one day I'll feel it too
                I could try to smile to hide the truth
                But I know I was happier with you
                Hey, yeah, hey, yeah, hey, yeah
                Hey, yeah, hey, yeah, hey, yeah
                Hey, yeah, hey, yeah, hey, yeah
                Hey, yeah, hey, yeah, hey, yeah
                'Cause baby, you look happier, you do
                I knew one day you'd fall for someone new
                But if he breaks your heart like lovers do
                Just know that I'll be waitin' here for you
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_26 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/10+-+Ed+Sheeran+-+What+Do+I+Know.mp3",
        title = "What Do I Know",
        artist = "Ed Sheeran",
        duration = "3:57",
        lyrics = """
                Ain't got a soapbox I can stand upon
                But God gave me a stage, a guitar and a song
                My daddy told me, "son, don't you get involved in
                Politics, religions or other people's quotes"
                I'll paint the picture, let me set the scene
                I know when I have children they will know what it means
                And I pass on these things my family's given to me
                Just love and understanding, positivity
                We could change this whole world with a piano
                Add a bass, some guitar, grab a beat and away we go
                I'm just a boy with a one-man show
                No university, no degree, but lord knows
                Everybody's talking 'bout exponential growth
                And the stock market crashing in their portfolios
                While I'll be sitting here with a song that I wrote
                Sing, love could change the world in a moment
                But what do I know?
                Love can change the world in a moment
                But what do I know?
                Love can change the world in a moment
                The revolution's coming, it's a minute away
                I saw people marching in the streets today
                You know we are made up of love and hate
                But both of them are balanced on a razor blade
                I'll paint the picture, let me set the scene
                I know, I'm all for people following their dreams
                Just re-remember life is more than fittin' in your jeans
                It's love and understanding, positivity
                We could change this whole world with a piano
                Add a bass, some guitar, grab a beat and away we go
                I'm just a boy with a one-man show
                No university, no degree, but lord knows
                Everybody's talking 'bout exponential growth
                And the stock market crashing in their portfolios
                While I'll be sitting here with a song I wrote
                Sing, love could change the world in a moment
                But what do I know?
                Love can change the world in a moment
                But what do I know?
                Love can change the world in a moment
                I'll paint the picture, let me set the scene
                You know, the future's in the hands of you and me
                So let's all get together, we can all be free
                Spread love and understanding, positivity
                We could change this whole world with a piano
                Add a bass, some guitar, grab a beat and away we go
                I'm just a boy with a one-man show
                No university, no degree, but lord knows
                Everybody's talking 'bout exponential growth
                And the stock market crashing in their portfolios
                While I'll be sitting here with a song I wrote
                Sing, love could change the world in a moment
                But what do I know?
                Love can change the world in a moment
                But what do I know?
                Love can change the world in a moment
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_27 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/11+-+Ed+Sheeran+-+How+Would+You+Feel+(Paean).mp3",
        title = "How Would You Feel (Paean)",
        artist = "Ed Sheeran",
        duration = "4:41",
        lyrics = """
                You are the one girl
                And you know that it's true
                I'm feeling younger
                Every time that I'm alone with you
                We were sitting in a parked car
                Stealing kisses in the front yard
                We got questions we should not ask but
                How would you feel, if I told you I loved you?
                It's just something that I want to do
                I'll be taking my time, spending my life
                Falling deeper in love with you
                So tell me that you love me too
                In the summer, as the lilacs bloom
                Love flows deeper than the river
                Every moment that I spend with you
                We were sat upon our best friend's roof
                I had both of my arms round you
                Watching the sunrise replace the moon
                How would you feel, if I told you I loved you?
                It's just something that I want to do
                I'll be taking my time, spending my life
                Falling deeper in love with you
                So tell me that you love me too
                We were sitting in a parked car
                Stealing kisses in the front yard
                We got questions we shouldn not ask
                How would you feel, if I told you I loved you?
                It's just something that I want to do
                I'll be taking my time, spending my life
                Falling deeper in love with you
                So tell me that you love me too
                Tell me that you love me too
                Tell me that you love me too
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_28 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%3D/02+-+Ed+Sheeran+-+Shivers.mp3",
        title = "Shivers",
        artist = "Ed Sheeran",
        duration = "3:28",
        lyrics = """
                I took an arrow to the heart
                I never kissed a mouth that tastes like yours
                Strawberries and somethin' more
                Ooh yeah, I want it all
                Lipstick on my guitar (ooh)
                Fill up the engine, we can drive real far
                Go dancin' underneath the stars
                Ooh yeah, I want it all
                Mm, you got me feelin' like
                I wanna be that guy, I wanna kiss your eyes
                I wanna drink that smile, I wanna feel like I'm
                Like my soul's on fire, I wanna stay up all day and all night
                Yeah, you got me singin' like
                Ooh, I love it when you do it like that
                And when you're close up, give me the shivers
                Oh baby, you wanna dance 'til the sunlight cracks
                And when they say the party's over, then we'll bring it right back
                And we'll say, ooh, I love it when you do it like that
                And when you're close up, give me the shivers
                Oh baby, you wanna dance 'til the sunlight cracks
                And when they say the party's over, then we'll bring it right back
                Into the car
                On the backseat in the moonlit dark
                Wrap me up between your legs and arms
                Ooh, I can't get enough
                You know you could tear me apart (ooh)
                Put me back together and take my heart
                I never thought that I could love this hard
                Ooh, I can't get enough
                Mm, you got me feeling like
                I wanna be that guy, I wanna kiss your eyes
                I wanna drink that smile, I wanna feel like I'm
                Like my soul's on fire, I wanna stay up all day and all night
                Yeah, you got me singin' like
                Ooh, I love it when you do it like that
                And when you're close up, give me the shivers
                Oh baby, you wanna dance 'til the sunlight cracks
                And when they say the party's over, then we'll bring it right back
                And we'll say, ooh, I love it when you do it like that
                And when you're close up, give me the shivers
                Oh baby, you wanna dance 'til the sunlight cracks
                And when they say the party's over, then we'll bring it right back
                Baby, you burn so hot
                You make me shiver with the fire you got
                This thing we started, I don't want it to stop
                You know you make me shiver-er-er
                Baby, you burn so hot
                You make me shiver with the fire you got
                This thing we started, I don't want it to stop
                You know you make me shiver
                Yeah, you got me singin' like
                Ooh, I love it when you do it like that
                And when you're close up, give me the shivers
                Oh baby, you wanna dance 'til the sunlight cracks
                And when they say the party's over, then we'll bring it right back (oh no)
                And we'll say, ooh, I love it when you do it like that
                And when you're close up, give me the shivers
                Oh baby, you wanna dance 'til the sunlight cracks
                And when they say the party's over, then we'll bring it right back, hey
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_29 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%3D/03+-+Ed+Sheeran+-+First+Times.mp3",
        title = "First Times",
        artist = "Ed Sheeran",
        duration = "3:06",
        lyrics = """
                I thought it'd feel different playing Wembley
                Eighty thousand singing with me
                It's what I've been chasing 'cause this is the dream
                When it was all over, I cleared out the room
                Grabbed a couple beers, just me and you
                Then we start talking the way that we do
                Ain't it funny how the simplest things in life can make a man?
                Little moments that pass us by
                Oh, but I remember
                The first kiss, the first night, the first song that made you cry
                The first drink, red wine, on a step in Brooklyn
                I still feel the first fight, and we both made it out alive
                And I can't wait to make a million more first times
                (Mm-hmm, mm-hmm)
                The greatest thing that I have achieved
                This four little words, down on one knee
                Said, "Darling, are you joking?"
                And I just said, "Please"
                Ain't it funny how the simplest things in life can make a man?
                Little moments that pass us by
                Oh, but I remember
                The first kiss, the first night, the first song that made you cry
                The first look in your eyes when I said, "I love you"
                I can still feel the butterflies from when we stumbled home that night
                I can't wait to make a million more first times
                (Mm-hmm, mm-hmm)
                Ain't it funny how the simplest things in life can make a man?
                Little moments that pass us by
                Oh, but I remember
                First kiss, first night, first song that made you cry
                First dance, moonlight, in your parents' garden
                I can't wait to see everything that's yet to be
                Our first child, and then a million more first times
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_30 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%3D/12+-+Ed+Sheeran+-+Visiting+Hours.mp3",
        title = "Visiting Hours",
        artist = "Ed Sheeran",
        duration = "3:36",
        lyrics = """
                I wish that heaven had visiting hours
                So I could just show up and bring the news
                That she's gettin' older and I wish that you'd met her
                The things that she'll learn from me, I got them all from you
                Can I just stay a while and we'll put all the world to rights?
                The little ones will grow and I'll still drink your favorite wine
                And soon, they're going to close, but I'll see you another day
                So much has changed since you've been away
                I wish that heaven had visiting hours
                So I could just swing by and ask your advice
                What would you do in my situation? I haven't a clue how I'd even raise them
                What would you do? 'Cause you always do what's right
                Can we just talk a while until my worries disappear?
                I'd tell you that I'm scared of turnin' out a failure
                You'd say, "Remember that the answer's in the love that we create"
                So much has changed since you've been away
                I wish that heaven had visiting hours
                And I would ask them if I could take you home
                But I know what they'd say, that it's for the best
                So I will live life the way you taught me, and make it on my own
                And I will close the door, but I will open up my heart
                And everyone I love will know exactly who you are
                'Cause this is not goodbye, it is just 'til we meet again
                So much has changed since you've been away
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_31 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/03+-+Ed+Sheeran+-+Sing.mp3",
        title = "Sing",
        artist = "Ed Sheeran",
        duration = "3:55",
        lyrics = """
                It's late in the evening
                Glass on the side
                I've been sat with you
                For most of the night
                Ignoring everybody here
                We wish they would disappear
                So maybe we could get down now
                I don't wanna know
                If you're getting ahead of the programme
                I want you to be mine, lady
                And to hold your body close
                Take another step into the no-man's land
                For the longest time, lady
                I need you, darling
                Come on, set the tone
                If you feel you're falling
                Won't you let me know?
                Oh-oh, ooh-ooh
                Oh-oh, ooh-ooh
                If you love me
                Come on, get involved
                Feel it rushing through you
                From your head to toe
                Oh-oh, ooh-ooh
                Oh-oh, ooh-ooh
                Sing!
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                Louder!
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                Sing!
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                This love is ablaze
                I saw flames from the side of the stage
                And the fire brigade comes in a couple of days
                Until then, we got nothing to say
                And nothing to know
                But something to drink and maybe something to smoke
                Let it go until our roads are changed
                Singing "we found love in a local rave", no
                I don't really know what I'm supposed to say
                But I can just figure it out, and then hope and pray
                I told her my name and said, "It's nice to meet ya"
                Then she handed me a bottle of water filled with tequila
                I already know she's a keeper
                Just from this one small act of kindness
                I'm in deep if anybody finds out
                I'm meant to drive home, but I've drunk all of it now
                Not sobering up we just sit on the couch
                One thing led to another
                Now she's kissing my mouth
                I need you, darling
                Come on, set the tone
                If you feel you're falling
                Won't you let me know?
                Oh-oh, ooh-ooh
                Oh-oh, ooh-ooh
                If you love me
                Come on, get involved
                Feel it rushing through you
                From your head to toe
                Oh-oh, ooh-ooh
                Oh-oh, ooh-ooh
                Sing!
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                Louder!
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                Sing!
                Oh-oh-oh-oh-oh-oh-oh, oh-oh-oh-oh
                Can you feel it?
                All the guys in here don't even wanna dance
                Can you feel it?
                All that I can hear is music from the back
                Can you feel it?
                I found you hiding here, so won't you take my hand, darling?
                Before the beat kicks in again
                Can you feel it?
                Can you feel it?
                Sing!
                I need you, darling
                Come on set the tone
                If you feel you're falling
                Won't you let me know?
                (Louder!) Oh-oh, ooh-ooh
                Oh-oh, ooh-ooh
                If you love me
                Come on, get involved
                Feel it rushing through you
                From your head to toe
                (Louder!) Oh-oh, ooh-ooh
                Oh-oh, ooh-ooh
                Sing!
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_32 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/04+-+Ed+Sheeran+-+Don't.mp3",
        title = "Don't",
        artist = "Ed Sheeran",
        duration = "3:40",
        lyrics = """
                Don't, don't play with her, don't be dishonest (Ayy)
                Still not understandin' this logic (Ayy)
                I'm back and I'm better (And I'm better)
                I want you bad as ever
                Don't let me just let up
                I wanna give you better
                Baby, it's whatever
                Somebody gotta step up
                Girl, I'm that somebody, so I'm next up
                Be damned if I let him catch up
                It's easy to see that you're fed up
                I am on a whole 'nother level
                Girl, he only fucked you over 'cause you let him
                Fuck him, girl, I guess he didn't know any better
                Girl, that man didn't show any effort
                Do all I can just to show you you're special
                Certain it's your love that holds me together
                Lately you say he been killin' the vibe
                Gotta be sick of this guy
                Pull up, skrr, get in the ride
                Left hand is steerin' the other is grippin' your thigh
                Light up a spliff and get high
                Shawty, you deserve what you've been missin'
                Lookin' at you I'm thinkin' he must be trippin'
                Play this song for him, tell him, "Just listen"
                Don't
                Don't
                Girl, said he keeps on playin' games
                And his lovin' ain't the same
                I don't know what to say, but
                What a shame
                If you were mine you would not get the same
                If you were mine you would top everything
                Suicide in the drop switchin' lanes
                And that thing so fire, baby, no propane
                Got good pussy, girl, can I be frank?
                To keep it 100, girl, I ain't no saint
                But he the only reason that I'm feelin' this way
                Givin' you the world, baby, when you get space
                Pen game get me laid, baby, that's penetrate
                Oh, baby
                Don't
                H-Town got a nigga so throwed
                Pour up, we can party some more
                Yeah, got this drank in my cup
                Got a young nigga feelin' so throwed
                Spit fire in a world so cold
                Young money got a nigga feelin' old
                Spit fire in a world so cold
                H-Town got me feelin' so throwed
                H-Town got me feelin' so throwed
                Ride paint and we sip 'til we fold
                H-Town got me feelin' so throwed
                Spit fire in a world so cold
                H-Town got a nigga so throwed
                Don't
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_33 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/06+-+Ed+Sheeran+-+Photograph.mp3",
        title = "Photograph",
        artist = "Ed Sheeran",
        duration = "4:19",
        lyrics = """
                Loving can hurt, loving can hurt sometimes
                But it's the only thing that I know
                When it gets hard, you know it can get hard sometimes
                It is the only thing makes us feel alive
                We keep this love in a photograph
                We made these memories for ourselves
                Where our eyes are never closing
                Hearts are never broken
                And time's forever frozen, still
                So you can keep me
                Inside the pocket of your ripped jeans
                Holding me closer 'til our eyes meet
                You won't ever be alone, wait for me to come home
                Loving can heal, loving can mend your soul
                And it's the only thing that I know, know
                I swear it will get easier
                Remember that with every piece of ya
                Hmm, and it's the only thing we take with us when we die
                Hmm, we keep this love in a photograph
                We made these memories for ourselves
                Where our eyes are never closing
                Hearts were never broken
                And time's forever frozen, still
                So you can keep me
                Inside the pocket of your ripped jeans
                Holding me closer 'til our eyes meet
                You won't ever be alone
                And if you hurt me
                That's okay, baby, only words bleed
                Inside these pages, you just hold me
                And I won't ever let you go
                Wait for me to come home
                Wait for me to come home
                Wait for me to come home
                Wait for me to come home
                Oh, you can fit me
                Inside the necklace you got when you were sixteen
                Next to your heartbeat where I should be
                Keep it deep within your soul
                And if you hurt me
                Well, that's okay, baby, only words bleed
                Inside these pages, you just hold me
                And I won't ever let you go
                When I'm away, I will remember how you kissed me
                Under the lamppost back on Sixth street
                Hearing you whisper through the phone
                "Wait for me to come home"
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_34 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/11+-+Ed+Sheeran+-+Thinking+out+Loud.mp3",
        title = "Thinking Out Loud",
        artist = "Ed Sheeran",
        duration = "4:18",
        lyrics = """
                When your legs don't work like they used to before
                And I can't sweep you off of your feet
                Will your mouth still remember the taste of my love
                Will your eyes still smile from your cheeks
                And darling I will be loving you 'til we're 70
                And baby my heart could still fall as hard at 23
                And I'm thinking 'bout how people fall in love in mysterious ways
                Maybe just the touch of a hand
                Oh me I fall in love with you every single day
                And I just wanna tell you I am
                So honey now
                Take me into your loving arms
                Kiss me under the light of a thousand stars
                Place your head on my beating heart
                I'm thinking out loud
                Maybe we found love right where we are
                When my hair's all but gone and my memory fades
                And the crowds don't remember my name
                When my hands don't play the strings the same way, mm
                I know you will still love me the same
                'Cause honey your soul can never grow old, it's evergreen
                Baby your smile's forever in my mind and memory
                I'm thinking 'bout how people fall in love in mysterious ways
                Maybe it's all part of a plan
                I'll just keep on making the same mistakes
                Hoping that you'll understand
                But baby now
                Take me into your loving arms
                Kiss me under the light of a thousand stars
                Place your head on my beating heart
                I'm thinking out loud
                That maybe we found love right where we are, oh
                So baby now
                Take me into your loving arms
                Kiss me under the light of a thousand stars
                Oh darling, place your head on my beating heart
                I'm thinking out loud
                That maybe we found love right where we are
                Oh baby, we found love right where we are (maybe)
                And we found love right where we are
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_35 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%2B/01+-+Ed+Sheeran+-+The+A+Team.mp3",
        title = "The A Team",
        artist = "Ed Sheeran",
        duration = "4:42",
        lyrics = """
                White lips, pale face
                Breathing in snowflakes
                Burnt lungs, sour taste
                Light's gone, day's end
                Struggling to pay rent
                Long nights, strange men

                And they say
                She's in the Class A Team
                Stuck in her daydream
                Been this way since eighteen
                But lately her face seems
                Slowly sinking, wasting
                Crumbling like pastries
                And they scream
                The worst things in life come free to us
                'Cause we're just under the upper hand
                And go mad for a couple grams
                And she don't want to go outside tonight
                And in a pipe she flies to the Motherland
                Or sells love to another man
                It's too cold outside
                For angels to fly
                Angels to fly

                Ripped gloves, raincoat
                Tried to swim and stay afloat
                Dry house, wet clothes
                Loose change, bank notes
                Weary-eyed, dry throat
                Call girl, no phone

                And they say
                She's in the Class A Team
                Stuck in her daydream
                Been this way since eighteen
                But lately her face seems
                Slowly sinking, wasting
                Crumbling like pastries
                And they scream
                The worst things in life come free to us
                'Cause we're just under the upper hand
                And go mad for a couple grams
                And she don't want to go outside tonight
                And in a pipe she flies to the Motherland
                Or sells love to another man
                It's too cold outside
                For angels to fly
                An angel will die
                Covered in white
                Closed eye
                And hoping for a better life
                This time, we'll fade out tonight
                Straight down the line

                And they say
                She's in the Class A Team
                Stuck in her daydream
                Been this way since eighteen
                But lately her face seems
                Slowly sinking, wasting
                Crumbling like pastries
                They scream
                The worst things in life come free to us
                And we're all under the upper hand
                Go mad for a couple grams
                And we don't want to go outside tonight
                And in a pipe we fly to the Motherland
                Or sell love to another man
                It's too cold outside
                For angels to fly
                Angels to fly
                To fly, fly
                For angels to fly, to fly, to fly
                For angels to die
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_36 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%2B/09+-+Ed+Sheeran+-+Lego+House.mp3",
        title = "Lego House",
        artist = "Ed Sheeran",
        duration = "3:05",
        lyrics = """
                I'm gonna pick up the pieces
                And build a Lego house
                When things go wrong we can knock it down
                My three words have two meanings
                There's one thing on my mind, it's all for you
                And it's dark in a cold December
                But I've got ya to keep me warm
                And if you're broken I'll mend ya
                And I keep you sheltered from the storm
                That's raging on now
                I'm out of touch, I'm out of love
                I'll pick you up when you're getting down
                And out of all these things I've done
                I think I love you better now
                I'm out of sight, I'm out of mind
                I'll do it all for you in time
                And out of all these things I've done
                I think I love you better now, now
                I'm gonna paint you by numbers and color you in
                If things go right we can frame it
                And put you on a wall
                And it's so hard to say it but I've been here before
                Now I'll surrender up my heart and swap it for yours
                I'm out of touch, I'm out of love
                I'll pick you up when you're getting down
                And out of all these things I've done
                I think I love you better now
                I'm out of sight, I'm out of mind
                I'll do it all for you in time
                And out of all these things I've done
                I think I love you better now
                Don't hold me down
                I think my braces are breaking
                And it's more than I can take
                And it's dark in a cold December
                But I've got ya to keep me warm
                If you're broken I will mend ya
                And I keep you sheltered from the storm
                That's raging on now
                I'm out of touch, I'm out of love
                I'll pick you up when you're getting down
                And out of all these things I've done
                I think I love you better now
                I'm out of sight, I'm out of mind
                I'll do it all for you in time
                And out of all these things I've done
                I think I love you better now
                I'm out of touch, I'm out of love
                I'll pick you up when you're getting down
                And out of all these things I've done
                I will love you better now
                        """,
        date_created = datetime(2023, 9, 6),
    )

    song_37 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+1989/02+-+Taylor+Swift+-+Blank+Space.mp3",
        title = "Blank Space",
        artist = "Taylor Swift",
        duration = "3:51",
        lyrics = """
                Nice to meet you, where you been?
                I could show you incredible things
                Magic, madness, heaven, sin
                Saw you there and I thought
                "Oh, my God, look at that face
                You look like my next mistake
                Love's a game, wanna play?" Ay
                New money, suit and tie
                I can read you like a magazine
                Ain't it funny? Rumors fly
                And I know you heard about me
                So hey, let's be friends
                I'm dying to see how this one ends
                Grab your passport and my hand
                I can make the bad guys good for a weekend
                So it's gonna be forever
                Or it's gonna go down in flames
                You can tell me when it's over, mm
                If the high was worth the pain
                Got a long list of ex-lovers
                They'll tell you I'm insane
                'Cause you know I love the players
                And you love the game
                'Cause we're young, and we're reckless
                We'll take this way too far
                It'll leave you breathless, mm
                Or with a nasty scar
                Got a long list of ex-lovers
                They'll tell you I'm insane
                But I've got a blank space, baby
                And I'll write your name
                Cherry lips, crystal skies
                I could show you incredible things
                Stolen kisses, pretty lies
                You're the King, baby, I'm your Queen
                Find out what you want
                Be that girl for a month
                Wait, the worst is yet to come, oh, no
                Screaming, crying, perfect storms
                I can make all the tables turn
                Rose garden filled with thorns
                Keep you second guessing like
                "Oh, my God, who is she?"
                I get drunk on jealousy
                But you'll come back each time you leave
                'Cause, darling, I'm a nightmare dressed like a daydream
                So it's gonna be forever
                Or it's gonna go down in flames
                You can tell me when it's over, mm
                If the high was worth the pain
                Got a long list of ex-lovers
                They'll tell you I'm insane
                'Cause you know I love the players
                And you love the game
                'Cause we're young, and we're reckless (oh)
                We'll take this way too far
                It'll leave you breathless, mm (oh)
                Or with a nasty scar
                Got a long list of ex-lovers
                They'll tell you I'm insane (insane)
                But I've got a blank space, baby
                And I'll write your name
                Boys only want love if it's torture
                Don't say I didn't, say I didn't warn ya
                Boys only want love if it's torture
                Don't say I didn't, say I didn't warn ya
                So it's gonna be forever
                Or it's gonna go down in flames
                You can tell me when it's over (over)
                If the high was worth the pain
                Got a long list of ex-lovers
                They'll tell you I'm insane (I'm insane)
                'Cause you know I love the players
                And you love the game
                'Cause we're young, and we're reckless
                We'll take this way too far (ooh)
                It'll leave you breathless, mm
                Or with a nasty scar (leave a nasty scar)
                Got a long list of ex-lovers
                They'll tell you I'm insane
                But I've got a blank space, baby
                And I'll write your name
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_38 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+1989/06+-+Taylor+Swift+-+Shake+It+Off.mp3",
        title = "Shake It Off",
        artist = "Taylor Swift",
        duration = "3:39",
        lyrics = """
                I stay out too late
                Got nothing in my brain
                That's what people say, mmm-mmm
                That's what people say, mmm-mmm

                I go on too many dates
                But I can't make them stay
                At least that's what people say, mmm-mmm
                That's what people say, mmm-mmm

                But I keep cruising
                Can't stop, won't stop moving
                It's like I got this music
                In my mind
                Saying, "It's gonna be alright."

                'Cause the players gonna play, play, play, play, play
                And the haters gonna hate, hate, hate, hate, hate
                Baby, I'm just gonna shake, shake, shake, shake, shake
                I shake it off, I shake it off
                Heart-breakers gonna break, break, break, break, break
                And the fakers gonna fake, fake, fake, fake, fake
                Baby, I'm just gonna shake, shake, shake, shake, shake
                I shake it off, I shake it off

                I never miss a beat
                I'm lightning on my feet
                And that's what they don't see, mmm-mmm
                That's what they don't see, mmm-mmm

                I'm dancing on my own (dancing on my own)
                I make the moves up as I go (moves up as I go)
                And that's what they don't know, mmm-mmm
                That's what they don't know, mmm-mmm

                But I keep cruising
                Can't stop, won't stop grooving
                It's like I got this music
                In my mind
                Saying, "It's gonna be alright."

                'Cause the players gonna play, play, play, play, play
                And the haters gonna hate, hate, hate, hate, hate
                Baby, I'm just gonna shake, shake, shake, shake, shake
                I shake it off, I shake it off
                Heart-breakers gonna break, break, break, break, break
                And the fakers gonna fake, fake, fake, fake, fake
                Baby, I'm just gonna shake, shake, shake, shake, shake
                I shake it off, I shake it off

                Shake it off, I shake it off,
                I, I, I shake it off, I shake it off,
                I, I, I shake it off, I shake it off,
                I, I, I shake it off, I shake it off

                Hey, hey, hey
                Just think while you've been getting down and out about the liars and the dirty, dirty cheats of the world,
                You could've been getting down to this sick beat.

                My ex-man brought his new girlfriend
                She's like "Oh, my God!" but I'm just gonna shake.
                And to the fella over there with the hella good hair
                Won't you come on over, baby? We can shake, shake, shake

                Yeah ohhh

                'Cause the players gonna play, play, play, play, play
                And the haters gonna hate, hate, hate, hate, hate (haters gonna hate)
                I'm just gonna shake, shake, shake, shake, shake
                I shake it off, I shake it off
                Heart-breakers gonna break, break, break, break, break (mmmm)
                And the fakers gonna fake, fake, fake, fake, fake (and fake, and fake, and fake)
                Baby, I'm just gonna shake, shake, shake, shake, shake
                I shake it off, I shake it off

                Shake it off, I shake it off,
                I, I, I shake it off, I shake it off,
                I, I, I shake it off, I shake it off
                I, I, I shake it off, I shake it off

                Shake it off, I shake it off,
                I, I, I shake it off, I shake it off,
                I, I, I shake it off, I shake it off,
                I, I, I shake it off, I shake it off

                Shake it off, I shake it off,
                I, I, I shake it off, I shake it off (you've got to),
                I, I, I shake it off, I shake it off,
                I, I, I shake it off, I shake it off
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_39 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Fearless+(Taylor%E2%80%99s+Version)+The+I+Remember+What+You+Said+Last+Night+Chapter/01+-+Taylor+Swift+-+You+Belong+With+Me+(Taylor%E2%80%99s+Version).mp3",
        title = "You Belong With Me (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "3:51",
        lyrics = """
                You're on the phone with your girlfriend, she's upset
                She's going off about something that you said
                'Cause she doesn't get your humor like I do
                I'm in the room, it's a typical Tuesday night
                I'm listening to the kind of music she doesn't like
                And she'll never know your story like I do
                But she wears short skirts
                I wear T-shirts
                She's Cheer Captain, and I'm on the bleachers
                Dreaming about the day when you wake up and find
                That what you're looking for has been here the whole time
                If you could see that I'm the one
                Who understands you
                Been here all along
                So, why can't you see?
                You belong with me
                You belong with me
                Walk in the streets with you in your worn-out jeans
                I can't help thinking this is how it ought to be
                Laughing on a park bench thinking to myself
                Hey, isn't this easy?
                And you've got a smile
                That can light up this whole town
                I haven't seen it in a while
                Since she brought you down
                You say you're fine, I know you better than that
                Hey, what you doing with a girl like that?
                She wears high heels
                I wear sneakers
                She's Cheer Captain, and I'm on the bleachers
                Dreaming about the day when you wake up and find
                That what you're looking for has been here the whole time
                If you could see that I'm the one
                Who understands you
                Been here all along
                So, why can't you see?
                You belong with me
                Standing by and waiting at your backdoor
                All this time how could you not know, baby?
                You belong with me
                You belong with me
                Oh, I remember you driving to my house
                In the middle of the night
                I'm the one who makes you laugh
                When you know you're 'bout to cry
                And I know your favorite songs
                And you tell me 'bout your dreams
                Think I know where you belong
                Think I know it's with me
                Can't you see that I'm the one
                Who understands you?
                Been here all along
                So, why can't you see?
                You belong with me
                Standing by and waiting at your backdoor
                All this time how could you not know, baby?
                You belong with me
                You belong with me
                You belong with me
                Have you ever thought just maybe
                You belong with me?
                You belong with me
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_40 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Fearless/02+-+Taylor+Swift+-+Fifteen.mp3",
        title = "Fifteen",
        artist = "Taylor Swift",
        duration = "4:54",
        lyrics = """
                You take a deep breath
                And you walk through the doors
                It's the morning of your very first day
                You say hi to your friends you ain't seen in awhile
                Try and stay out of everybody's way
                It's your freshman year
                And you're gonna be here for the next four years
                In this town
                Hoping one of those senior boys
                Will wink at you and say, "you know I haven't seen you around, before"
                'Cause when you're fifteen,
                Somebody tells you they love you
                You're gonna believe them
                And when you're fifteen
                Feeling like there's nothing to figure out
                Count to ten
                Take it in
                This is life before you know who you're gonna be
                At fifteen
                You sit in class next to a red-head named Abigail
                And soon enough you're best friends
                Laughing at the other girls
                Who they think they're so cool
                We'll be out of here as soon as we can
                And then you're on your very first date
                And he's got a car
                And you're feeling like flying
                And you're mama's waiting up
                And you're thinking he's the one
                And you're dancing around the room when the night ends
                When the night ends
                'Cause when you're fifteen,
                Somebody tells you they love you
                You're gonna believe them
                And when you're fifteen
                And your first kiss makes your head spin around
                But in your life you'll do things
                Greater than dating the boy on the football team
                But I didn't know it at fifteen
                When all you wanted
                Was to be wanted
                Wish you could go back
                And tell yourself what you know now
                Back then I swore I was gonna marry him someday
                But I realized some bigger dreams of mine
                And Abigail gave everything she had
                To a boy who changed his mind
                And we both cried
                'Cause when you're fifteen,
                Somebody tells you they love you
                You're gonna believe them
                And when you're fifteen
                Don't forget to look before you fall
                I've found time can heal most anything
                And you just might find who you're supposed to be
                I didn't know who I was supposed to be
                At fifteen
                La la la la la
                Your very first day
                Take a deep breath girl
                And take a deep breath as you walk through the doors
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_41 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Love+Story+(Taylor%E2%80%99s+Version)/01+-+Taylor+Swift+-+Love+Story+(Taylor%E2%80%99s+Version).mp3",
        title = "Love Story (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "3:55",
        lyrics = """
                We were both young when I first saw you
                I close my eyes and the flashback starts
                I'm standin' there
                On a balcony in summer air
                See the lights, see the party, the ball gowns
                See you make your way through the crowd
                And say, "Hello"
                Little did I know
                That you were Romeo, you were throwin' pebbles
                And my daddy said, "Stay away from Juliet"
                And I was cryin' on the staircase
                Beggin' you, "Please don't go, " and I said
                Romeo, take me somewhere we can be alone
                I'll be waiting, all there's left to do is run
                You'll be the prince and I'll be the princess
                It's a love story, baby, just say, "Yes"
                So I sneak out to the garden to see you
                We keep quiet, 'cause we're dead if they knew
                So close your eyes
                Escape this town for a little while, oh oh
                'Cause you were Romeo, I was a scarlet letter
                And my daddy said, "Stay away from Juliet"
                But you were everything to me
                I was beggin' you, "Please don't go, " and I said
                Romeo, take me somewhere we can be alone
                I'll be waiting, all there's left to do is run
                You'll be the prince and I'll be the princess
                It's a love story, baby, just say, "Yes"
                Romeo, save me, they're tryna tell me how to feel
                This love is difficult, but it's real
                Don't be afraid, we'll make it out of this mess
                It's a love story, baby, just say, "Yes"
                Oh, oh
                I got tired of waiting
                Wonderin' if you were ever comin' around
                My faith in you was fading
                When I met you on the outskirts of town, and I said
                Romeo, save me, I've been feeling so alone
                I keep waiting for you, but you never come
                Is this in my head? I don't know what to think
                He knelt to the ground and pulled out a ring
                And said, "Marry me, Juliet
                You'll never have to be alone
                I love you and that's all I really know
                I talked to your dad, go pick out a white dress
                It's a love story, baby, just say, "Yes"
                Oh, oh, oh
                Oh, oh, oh, oh
                'Cause we were both young when I first saw you
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_42 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Lover/16+-+Taylor+Swift%2C+Brendon+Urie%2C+Panic!+At+The+Disco+-+ME!+(feat.+Brendon+Urie+of+Panic!+At+The+Disco).mp3",
        title = "ME! (feat. Brendon Urie of Panic! At The Disco)",
        artist = "Taylor Swift",
        duration = "3:13",
        lyrics = """
                I promise that you'll never find another like me
                I know that I'm a handful, baby, uh
                I know I never think before I jump
                And you're the kind of guy the ladies want
                (And there's a lot of cool chicks out there)
                I know that I went psycho on the phone
                I never leave well enough alone
                And trouble's gonna follow where I go
                (And there's a lot of cool chicks out there)
                But one of these things is not like the others
                Like a rainbow with all of the colors
                Baby doll, when it comes to a lover
                I promise that you'll never find another like
                Me-e-e, ooh-ooh-ooh-ooh
                I'm the only one of me
                Baby, that's the fun of me
                Eeh-eeh-eeh, ooh-ooh-ooh-ooh
                You're the only one of you
                Baby, that's the fun of you
                And I promise that nobody's gonna love you like me-e-e
                I know I tend to make it about me
                I know you never get just what you see
                But I will never bore you, baby
                (And there's a lot of lame guys out there)
                And when we had that fight out in the rain
                You ran after me and called my name
                I never wanna see you walk away
                (And there's a lot of lame guys out there)
                'Cause one of these things is not like the others
                Livin' in winter, I am your summer
                Baby doll, when it comes to a lover
                I promise that you'll never find another like
                Me-e-e, ooh-ooh-ooh-ooh
                I'm the only one of me
                Let me keep you company
                Eeh-eeh-eeh, ooh-ooh-ooh-ooh
                You're the only one of you
                Baby, that's the fun of you
                And I promise that nobody's gonna love you like me-e-e
                Hey, kids!
                Spelling is fun!
                Girl, there ain't no I in "team"
                But you know there is a "me"
                Strike the band up, one, two, three
                I promise that you'll never find another like me
                Girl, there ain't no I in "team"
                But you know there is a "me"
                And you can't spell "awesome" without "me"
                I promise that you'll never find another like
                Me-e-e (yeah), ooh-ooh-ooh-ooh (and I won't stop, baby)
                I'm the only one of me (I'm the only one of me)
                Baby, that's the fun of me (baby, that's the fun of me)
                Eeh-eeh-eeh, ooh-ooh-ooh-ooh (oh)
                You're the only one of you (oh)
                Baby, that's the fun of you
                And I promise that nobody's gonna love you like me-e-e
                Girl, there ain't no I in "team" (ooh-ooh-ooh-ooh)
                But you know there is a "me"
                I'm the only one of me (oh-oh)
                Baby, that's the fun of me
                (Eeh-eeh-eeh, ooh-ooh-ooh-ooh)
                Strike the band up, one, two, three
                You can't spell "awesome" without "me"
                You're the only one of you
                Baby, that's the fun of you
                And I promise that nobody's gonna love you like me-e-e
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_43 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Red+(Taylor's+Version)/04+-+Taylor+Swift+-+I+Knew+You+Were+Trouble+(Taylor's+Version).mp3",
        title = "I Knew You Were Trouble (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "3:39",
        lyrics = """
                Once upon a time
                A few mistakes ago
                I was in your sights
                You got me alone
                You found me
                You found me
                You found me
                I guess you didn't care
                And I guess I liked that
                And when I fell hard
                You took a step back
                Without me
                Without me
                Without me
                And he's long gone
                When he's next to me
                And I realize
                The blame is on me
                'Cause I knew you were trouble when you walked in
                So shame on me now
                Flew me to places I'd never been
                'Til you put me down, oh
                I knew you were trouble when you walked in
                So, shame on me now
                Flew me to places I'd never been
                Now I'm lyin' on the cold hard ground
                Oh, oh
                Trouble, trouble, trouble
                Oh, oh
                Trouble, trouble, trouble
                No apologies
                He'll never see you cry
                Pretends he doesn't know
                That he's the reason why
                You're drowning
                You're drowning
                You're drowning
                And I heard you moved on
                From whispers on the street
                A new notch in your belt
                Is all I'll ever be
                And now I see
                Now I see
                Now I see
                He was long gone
                When he met me
                And I realize
                The joke is on me, hey
                I knew you were trouble when you walked in (oh)
                So shame on me now
                Flew me to places I'd never been
                'Til you put me down, oh
                I knew you were trouble when you walked in
                So shame on me now
                Flew me to places I'd never been, yeah
                Now I'm lyin' on the cold hard ground
                Oh, oh (yeah)
                Trouble, trouble, trouble
                Oh, oh
                Trouble, trouble, trouble
                And the saddest fear
                Comes creepin' in
                That you never loved me
                Or her
                Or anyone
                Or anything
                Yeah
                I knew you were trouble when you walked in
                So shame on me now
                Flew me to places I'd never been (never been)
                'Til you put me down, oh
                I knew you were trouble when you walked in (knew it right there)
                So shame on me now (knew it right there)
                Flew me to places I'd never been
                (Ooh) now I'm lyin' on the cold hard ground
                Oh, oh
                Trouble, trouble, trouble (oh)
                Oh, oh
                Trouble, trouble, trouble
                I knew you were trouble when you walked in
                Trouble, trouble, trouble
                I knew you were trouble when you walked in
                Trouble, trouble, trouble
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_44 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Red+(Taylor's+Version)/06+-+Taylor+Swift+-+22+(Taylor's+Version).mp3",
        title = "22 (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "3:51",
        lyrics = """
                It feels like a perfect night
                To dress up like hipsters
                And make fun of our exes
                Ah-ah, ah-ah
                It feels like a perfect night
                For breakfast at midnight
                To fall in love with strangers
                Ah-ah, ah-ah
                Yeah, we're happy, free, confused, and lonely at the same time
                It's miserable and magical, oh yeah
                Tonight's the night when we forget about the deadlines
                It's time, oh-oh
                I don't know about you, but I'm feeling 22
                Everything will be alright if you keep me next to you
                You don't know about me, but I'll bet you want to
                Everything will be alright if we just keep dancing like we're 22
                22
                It seems like one of those nights
                This place is too crowded
                Too many cool kids
                Ah ah, ah ah ("Who's Taylor Swift anyway? Ew")
                It seems like one of those nights
                We ditched the whole scene
                And end up dreaming, instead of sleeping
                Yeah, we're happy, free, confused, and lonely in the best way
                It's miserable and magical, oh yeah
                Tonight's the night when we forget about the heartbreaks
                It's time, oh-oh
                I don't know about you, but I'm feeling 22
                Everything will be alright if you keep me next to you
                You don't know about me, but I'll bet you want to
                Everything will be alright (alright) if we just keep dancing like we're 22
                (Oh, oh, oh, oh, oh)
                22 (I don't know about you)
                22
                22
                We ditched the whole scene
                (It feels like one of those nights)
                We won't be sleeping
                (It feels like one of those nights)
                You look like bad news
                I gotta have you
                I gotta have you
                Oh, oh, oh, oh, yeah
                but I'm feeling 22
                Everything will be alright if you keep me next to you
                You don't know about me (you don't know about me) but I'll bet you want to
                Everything will be alright if we just keep dancing like we're 22
                Oh-whoa, oh, oh, oh
                22 (dancing like)
                22 (yeah, yeah)
                22 (yeah, yeah, yeah)
                We ditched the whole scene
                (It feels like one of those nights)
                We won't be sleeping
                (It feels like one of those nights)
                You look like bad news
                I gotta have you
                I gotta have you
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_45 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Red+(Taylor's+Version)/08+-+Taylor+Swift+-+We+Are+Never+Ever+Getting+Back+Together+(Taylor's+Version).mp3",
        title = "We Are Never Ever Getting Back Together (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "3:13",
        lyrics = """
                I remember when we broke up the first time
                Saying, "This is it, I've had enough," 'cause like
                We hadn't seen each other in a month
                When you said you needed space. (What?)
                Then you come around again and say
                "Baby, I miss you and I swear I'm gonna change, trust me."
                Remember how that lasted for a day?
                I say, "I hate you," we break up, you call me, "I love you."

                Ooh, we called it off again last night
                But ooh, this time I'm telling you, I'm telling you

                We are never ever ever getting back together
                We are never ever ever getting back together
                You go talk to your friends, talk to my friends, talk to me
                But we are never ever ever ever getting back together

                Like, ever

                I'm really gonna miss you picking fights
                And me falling for it screaming that I'm right
                And you would hide away and find your peace of mind
                With some indie record that's much cooler than mine

                Ooh, you called me up again tonight
                But ooh, this time I'm telling you, I'm telling you

                We are never, ever, ever getting back together
                We are never, ever, ever getting back together
                You go talk to your friends, talk to my friends, talk to me (talk to me)
                But we are never ever ever ever getting back together

                Ooh, yeah, ooh yeah, ooh yeah
                Oh oh oh

                I used to think that we were forever ever
                And I used to say, "Never say never..."
                Uggg... so he calls me up and he's like, "I still love you,"
                And I'm like... "I just... I mean this is exhausting, you know, like
                We are never getting back together. Like, ever"

                No!

                We are never ever ever getting back together
                We are never ever ever getting back together
                You go talk to your friends, talk to my friends, talk to me
                But we are never ever ever ever getting back together

                We, ooh, getting back together, ohhh
                We, ooh, getting back together

                You go talk to your friends, talk to my friends, talk to me (talk to me)
                But we are never ever ever ever getting back together
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_46 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Red+(Taylor's+Version)/22+-+Taylor+Swift+-+Better+Man+(Taylor's+Version)+(From+The+Vault).mp3",
        title = "Better Man (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "4:57",
        lyrics = """
                I know I'm probably better off on my own
                Than lovin' a man who didn't know
                What he had when he had it
                And I see the permanent damage you did to me
                Never again, I just wish I could forget when it was magic
                I wish it wasn't 4am, standing in the mirror
                Saying to myself, you know you had to do it
                I know the bravest thing I ever did was run

                Sometimes, in the middle of the night, I can feel you again
                But I just miss you, and I just wish you were a better man
                And I know why we had to say goodbye like the back of my hand
                But I just miss you, and I just wish you were a better man
                A better man

                I know I'm probably better off all alone
                Than needing a man who could change his mind at any given minute
                And it was always on your terms
                I waited on every careless word
                Hoping it might turn sweet again
                Like it was in the beginning
                But your jealousy, oh, I can hear it now
                You're talking down to me like I'll always be around
                You push my love away like it was some kind of loaded gun
                Oh, you never thought I'd run

                Sometimes, in the middle of the night, I can feel you again
                But I just miss you, and I just wish you were a better man
                I know why we had to say goodbye like the back of my hand
                And I just miss you, and I just wish you were a better man
                A better man

                I hold onto this pride because these days it's all I have
                And I gave to you my best and we both know you can't say that

                I wish you were a better man
                I wonder what we would've become
                If you were a better man
                We might still be in love
                If you were a better man
                You would've been the one
                If you were a better man
                Yeah, yeah

                Sometimes, in the middle of the night, I can feel you again
                But I just miss you, and I just wish you were a better man
                I know why we had to say goodbye like the back of my hand
                But I just miss you and I just wish you were a better man
                A better man

                Sometimes, in the middle of the night, I can feel you again
                (We might still be in love, if you were a better man)
                But I just miss you, and I just wish you were a better man
                I know why we had to say goodbye
                Like the back of my hand
                But I just miss you and I just wish you were a better man
                A better man
                We might still be in love, if you were a better man
                You would've been the one
                If you were a better man
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_47 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Red+(Taylor's+Version)/26+-+Taylor+Swift%2C+Chris+Stapleton+-+I+Bet+You+Think+About+Me+(feat.+Chris+Stapleton)+(Taylor%E2%80%99s+Version)+(From+The+Vault).mp3",
        title = "I Bet You Think About Me (feat. Chris Stapleton) (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "4:45",
        lyrics = """
                3 a.m. and I'm still awake, I'll bet you're just fine
                Fast asleep in your city that's better than mine
                And the girl in your bed has a fine pedigree
                And I'll bet your friends tell you she's better than me, huh
                Well, I tried to fit in with your upper-crust circles
                Yeah, they let me sit in back when we were in love
                Oh, they sit around talkin' 'bout the meaning of life
                And the book that just saved 'em that I hadn't heard of
                But now that we're done and it's over
                I bet you couldn't believe
                When you realized I'm harder to forget than I was to leave
                And I bet you think about me
                You grew up in a silver-spoon, gated community
                Glamorous, shiny, bright Beverly Hills
                I was raised on a farm, no, it wasn't a mansion
                Just livin' room dancin' and kitchen table bills
                But you know what they say, you can't help who you fall for
                And you and I fell like an early spring snow
                But reality crept in, you said we're too different
                You laughed at my dreams, rolled your eyes at my jokes
                Mr. Superior Thinkin'
                Do you have all the space that you need?
                I don't have to be your shrink to know that you'll never be happy
                And I bet you think about me
                I bet you think about me
                Yes, I bet you think about me
                Oh, block it all out
                The voices so loud sayin', "Why did you let her go?"
                Does it make you feel sad
                That the love that you're lookin' for
                Is the love that you had?
                Now you're out in the world, searchin' for your soul
                Scared not to be hip, scared to get old
                Chasing make-believe status, last time you felt free
                Was when none of that shit mattered 'cause you were with me
                But now that we're done, and it's over
                I bet it's hard to believe
                But it turned out I'm harder to forget than I was to leave
                Then, yeah, I bet you think about me
                I bet you think about me
                Yes, I bet you think about me
                I bet you think about me when you're out
                At your cool indie music concerts every week
                I bet you think about me in your house
                With your organic shoes and your million-dollar couch
                I bet you think about me when you say
                "Oh my God, she's insane, she wrote a song about me"
                I bet you think about me
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_48 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Speak+Now+(Taylor's+Version)/03+-+Taylor+Swift+-+Back+To+December+(Taylor's+Version).mp3",
        title = "Back To Decemeber (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "4:54",
        lyrics = """
                I'm so glad you made time to see me
                How's life? Tell me, how's your family?
                I haven't seen them in a while
                You've been good, busier than ever
                We small talk, work and the weather
                Your guard is up and I know why
                Because the last time you saw me
                Is still burned in the back of your mind
                You gave me roses and I left them there to die
                So this is me swallowin' my pride
                Standin' in front of you sayin' I'm sorry for that night
                And I go back to December all the time
                It turns out freedom ain't nothin' but missin' you
                Wishin' I'd realized what I had when you were mine
                I'd go back to December, turn around and make it alright
                I go back to December all the time
                These days, I haven't been sleepin'
                Stayin' up playin' back myself leavin'
                When your birthday passed and I didn't call
                Then I think about summer, all the beautiful times
                I watched you laughin' from the passenger's side
                And realized I loved you in the fall
                And then the cold came, the dark days
                When fear crept into my mind
                You gave me all your love and all I gave you was goodbye
                So this is me swallowin' my pride
                Standin' in front of you sayin' I'm sorry for that night
                And I go back to December all the time
                It turns out freedom ain't nothin' but missin' you
                Wishin' I'd realized what I had when you were mine
                I'd go back to December, turn around and change my own mind
                I go back to December all the time
                I miss your tan skin, your sweet smile
                So good to me, so right
                And how you held me in your arms that September night
                The first time you ever saw me cry
                Maybe this is wishful thinkin'
                Probably mindless dreamin'
                But if we loved again, I swear I'd love you right
                I'd go back in time and change it, but I can't
                So if the chain is on your door, I understand
                But this is me swallowin' my pride
                Standin' in front of you sayin' I'm sorry for that night
                And I go back to December
                It turns out freedom ain't nothin' but missin' you
                Wishin' I'd realized what I had when you were mine
                I'd go back to December, turn around and make it alright
                I'd go back to December, turn around and change my own mind
                I go back to December all the time
                All the time
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_49 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Speak+Now+(Taylor's+Version)/05+-+Taylor+Swift+-+Dear+John+(Taylor's+Version).mp3",
        title = "Dear John (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "6:45",
        lyrics = """
                Long were the nights when
                My days once revolved around you
                Counting my footsteps
                Praying the floor won't fall through again
                And my mother accused me of losing my mind
                But I swore I was fine
                You paint me a blue sky
                And go back and turn it to rain
                And I lived in your chess game
                But you changed the rules every day
                Wondering which version of you I might get on the phone tonight
                Well, I stopped picking up and this song is to let you know why
                Dear John, I see it all now that you're gone
                Don't you think I was too young to be messed with?
                The girl in the dress, cried the whole way home
                I should've known
                Well, maybe it's me
                And my blind optimism to blame
                Or maybe it's you and your sick need
                To give love then take it away
                And you'll add my name to your long list of traitors
                Who don't understand
                And I'll look back and regret how I ignored when they said
                "Run as fast as you can"
                Dear John, I see it all now that you're gone
                Don't you think I was too young to be messed with?
                The girl in the dress, cried the whole way home
                Dear John, I see it all now, it was wrong
                Don't you think nineteen's too young
                To be played by your dark, twisted games when I loved you so?
                I should've known
                You are an expert at sorry and keeping the lines blurry
                Never impressed by me acing your tests
                All the girls that you've run dry have tired lifeless eyes
                'Cause you burned them out
                But I took your matches before fire could catch me
                So don't look now
                I'm shining like fireworks over your sad empty town
                Oh, oh
                Dear John, I see it all now that you're gone
                Don't you think I was too young to be messed with?
                The girl in the dress, cried the whole way home
                I see it all now that you're gone
                Don't you think I was too young to be messed with?
                The girl in the dress wrote you a song
                You should've known
                You should've known
                Don't you think I was too young?
                You should've known
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_50 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/TaylorSwiftMp3/Taylor+Swift+-+Speak+Now+(Taylor's+Version)/09+-+Taylor+Swift+-+Enchanted+(Taylor's+Version).mp3",
        title = "Enchanted (Taylor's Version)",
        artist = "Taylor Swift",
        duration = "5:53",
        lyrics = """
                There I was again tonight
                Forcing laughter, faking smiles
                Same old tired, lonely place
                Walls of insincerity, shifting eyes and vacancy
                Vanished when I saw your face
                All I can say is, it was enchanting to meet you
                Your eyes whispered, "Have we met?"
                'Cross the room your silhouette
                Starts to make its way to me
                The playful conversation starts
                Counter all your quick remarks
                Like passing notes in secrecy
                And it was enchanting to meet you
                All I can say is, I was enchanted to meet you
                This night is sparkling, don't you let it go
                I'm wonderstruck, blushing all the way home
                I'll spend forever wondering if you knew
                I was enchanted to meet you
                The lingering question kept me up
                2 AM, who do you love?
                I wonder 'til I'm wide awake
                And now I'm pacing back and forth
                Wishing you were at my door
                I'd open up and you would say, "Hey"
                It was enchanting to meet you
                All I know is, I was enchanted to meet you
                This night is sparkling, don't you let it go
                I'm wonderstruck, blushing all the way home
                I'll spend forever wondering if you knew
                That this night is flawless, don't you let it go
                I'm wonderstruck, dancing around all alone
                I'll spend forever wondering if you knew
                I was enchanted to meet you
                This is me praying that
                This was the very first page
                Not where the story line ends
                My thoughts will echo your name, until I see you again
                These are the words I held back, as I was leaving too soon
                I was enchanted to meet you
                Please don't be in love with someone else
                Please don't have somebody waiting on you
                Please don't be in love with someone else
                Please don't have somebody waiting on you
                This night is sparkling, don't you let it go
                I'm wonderstruck, blushing all the way home
                I'll spend forever wondering if you knew
                This night is flawless, don't you let it go
                I'm wonderstruck, dancing around all alone
                I'll spend forever wondering if you knew
                I was enchanted to meet you
                Please don't be in love with someone else
                Please don't have somebody waiting on you
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_51 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/03+-+John+Mayer+-+New+Light.mp3",
        title = "New Light",
        artist = "John Mayer",
        duration = "3:37",
        lyrics = """
                I'm the boy in your other phone
                Lighting up inside your drawer at home all alone
                Pushing 40 in the friend zone
                We talk and then you walk away every day
                Oh you don't think twice bout me
                And maybe you're right to doubt me but
                But if you give me just one night
                You're gonna see me in a new light
                Yeah if you give me just one night
                To meet you underneath the moonlight
                Oh I want a take two
                I wanna break through
                I wanna know the real thing about you
                So I can see you in a new light
                Take a ride up to Malibu
                I just wanna sit and look at you, look at you
                What would it matter if your friends knew
                Who cares what other people say anyway
                Oh we can go far from here
                And make a new world together babe
                'Cause if you give me just one night
                You're gonna see me in a new light
                Yeah, if you give me just one night
                To meet you underneath the moonlight
                Oh I want a take two
                I wanna break through
                I wanna know the real thing about you
                So I can see you in a new light
                Yeah if you give me just one night
                You're gonna see me in a new light
                Yeah if you give me just one night
                To meet you underneath the moonlight
                What do I do with all this
                What do I do with all this
                This love that's running through my veins for you
                What do I do with all this
                What do I do with all this
                This love that's running through my veins for you
                What do I do with all this
                What do I do with all this
                This love that's running through my veins for you
                What do I do with all this
                What do I do with all this, oooh
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_52 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Call+Me+Irresponsible+(Deluxe)/14+-+Michael+Bubl%C3%A9+-+L+O+V+E.mp3",
        title = "L O V E",
        artist = "Michael Bublé",
        duration = "2:50",
        lyrics = """
                L is for the way you look at me
                O is for the only one I see
                V is very, very extraordinary
                E is even more than anyone that you adore
                And love is all that I can give to you
                Love is more than just a game for two
                Two in love can make it
                Take my heart but please don't break it
                Love was made for me and you
                L is for the way you look at me
                O is for the only one I see
                V is very, very extraordinary
                E is even more than anyone that you adore
                And love is all that I can give to you
                Love, love, love is more than just a game for two
                Two in love can make it
                Take my heart but please don't break it
                'Cause love was made for me and you
                I said love was made for me and you
                You know that love was made for me and you
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_53 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Call+Me+Irresponsible/09+-+Michael+Bubl%C3%A9+-+Everything.mp3",
        title = "Everything",
        artist = "Michael Bublé",
        duration = "3:32",
        lyrics = """
                You're a falling star, you're the get away car
                You're the line in the sand when I go too far
                You're the swimming pool, on an August day
                And you're the perfect thing to say
                And you play it coy, but it's kinda cute
                Oh, when you smile at me you know exactly what you do
                Baby don't pretend, that you don't know it's true
                'Cause you can see it when I look at you
                And in this crazy life, and through these crazy times
                It's you, it's you, you make me sing
                You're every line, you're every word, you're everything
                You're a carousel, you're a wishing well
                And you light me up, when you ring my bell
                You're a mystery, you're from outer space
                You're every minute of my everyday
                And I can't believe, uh that I'm your man
                And I get to kiss you baby just because I can
                Whatever comes our way, oh we'll see it through
                And you know that's what our love can do
                And in this crazy life, and through these crazy times
                It's you, it's you, you make me sing
                You're every line, you're every word, you're everything
                So, la, la, la, la, la, la, la
                So, la, la, la, la, la, la, la
                And in this crazy life, and through these crazy times
                It's you, it's you, you make me sing
                You're every line, you're every word, you're everything
                You're every song, and I sing along
                'Cause you're my everything
                Yeah, yeah
                So, la, la, la, la, la, la, la
                So, la, la, la, la, la, la, la, la, la, la, la
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_54 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Crazy+Love/05+-+Michael+Bubl%C3%A9+-+Haven't+Met+You+Yet.mp3",
        title = "Haven't Met You Yet",
        artist = "Michael Bublé",
        duration = "4:03",
        lyrics = """
                I'm not surprised, not everything lasts
                I've broken my heart so many times I stopped keeping track
                Talk myself in, I talk myself out
                I get all worked up then I let myself down

                I tried so very hard not to lose it
                I came up with a million excuses
                I thought, I thought of every possibility

                And I know some day that it'll all turn out
                You'll make me work so we can work to work it out
                And I promise you kid that I'll give so much more than I get
                I just haven't met you yet

                Hmm... hmm

                I might have to wait, I'll never give up
                I guess it's half timing and the other half's luck
                Wherever you are, whenever it's right
                You'll come out of nowhere and into my life

                And I know that we can be so amazing
                And baby your love is gonna change me
                And now I can see every possibility

                Somehow I know that it'll all turn out
                You'll make me work so we can work to work it out
                And promise you kid I'll give so much more than I get
                I just haven't met you yet

                They say all's fair in love and war
                But I won't need to fight it
                We'll get it right and we'll be united

                And I know that we can be so amazing
                And being in your life is gonna change me
                And now I can see every single possibility

                And someday I know it'll all turn out
                And I'll work to work it out
                Promise you kid I'll give more than I get, than I get, than I get, than I get

                Oh you know it'll all turn out
                And you'll make me work so we can work to work it out
                And promise you kid to give so much more than I get yeah
                I just haven't met you yet

                I just haven't met you yet
                Oh promise you kid to give so much more than I get
                I said love love love love love love love
                I just haven't met you yet
                Yeah, I just haven't met you yet
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_55 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+It's+Time/01+-+Michael+Bubl%C3%A9+-+Feeling+Good.mp3",
        title = "Feeling Good",
        artist = "Michael Bublé",
        duration = "3:56",
        lyrics = """
                Birds flying high
                You know how I feel
                Sun in the sky
                You know how I feel
                Breeze driftin' on by
                You know how I feel
                It's a new dawn
                It's a new day
                It's a new life
                For me
                And I'm feeling good
                I'm feeling good
                Fish in the sea
                You know how I feel
                River running free
                You know how I feel
                Blossom on a tree
                You know how I feel
                It's a new dawn
                It's a new day
                It's a new life
                For me
                And I'm feeling good
                Dragonfly out in the sun, you know what I mean, don't you know
                Butterflies all havin' fun, you know what I mean
                Sleep in peace when day is done, that's what I mean
                And this old world is a new world
                And a bold world
                For me
                For me
                Stars when you shine
                You know how I feel
                Scent of the pine
                You know how I feel
                Oh, freedom is mine
                And I know how I feel
                It's a new dawn
                It's a new day
                It's a new life
                It's a new dawn
                It's a new day
                It's a new life
                It's a new dawn
                It's a new day
                It's a new life
                It's a new life
                For me
                And I'm feeling good
                I'm feeling good
                I feel so good
                I feel so good
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_56 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+It's+Time/05+-+Michael+Bubl%C3%A9+-+Home.mp3",
        title = "Home",
        artist = "Michael Bublé",
        duration = "3:45",
        lyrics = """
                Another summer day
                Has come and gone away
                In Paris and Rome
                But I wanna go home, mmm
                May be surrounded by
                A million people I
                Still feel all alone
                Just wanna go home
                Oh, I miss you, you know
                And I've been keeping all the letters
                That I wrote to you
                Each one a line or two
                I'm fine baby, how are you?
                Well I would send them but I know
                That it's just not enough
                My words were cold and flat
                And you deserve more than that
                Another airplane
                Another sunny place
                I'm lucky I know
                But I wanna go home
                Mmm, I got to go home
                Let me go home
                I'm just too far
                From where you are
                I wanna come home
                And I feel just like
                I'm living someone else's life
                It's like I just stepped outside
                When everything was going right
                And I know just why you could not
                Come along with me
                That this was not your dream
                But you always believed in me
                Another winter day
                Has come and gone away
                In even Paris and Rome
                And I wanna go home
                Let me go home
                And I'm surrounded by
                A million people I
                I still feel alone
                Oh, let me go home
                Oh, I miss you, you know
                Let me go home
                I've had my run
                Baby, I'm done
                I gotta go home
                Let me go home
                It'll all be all right
                I'll be home tonight
                I'm coming back home
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_57 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+It's+Time/08+-+Michael+Bubl%C3%A9+-+Save+the+Last+Dance+for+Me.mp3",
        title = "Save The Last Dance For Me",
        artist = "Michael Bublé",
        duration = "3:37",
        lyrics = """
                Now you can dance every dance with the guy
                Who gives you the eye, let him hold you tight
                And you can smile every smile for the man
                Who held your hand beneath the pale moon light
                But don't forget who's takin' you home
                And in whose arms you're gonna be
                So darling, save the last dance for me
                Oh, I know that the music's fine
                Like sparklin' wine, go and have your fun
                Laugh and sing, but while we're apart
                Don't give your heart to anyone
                And don't forget who's takin' you home
                And in whose arms you're gonna be
                So darling, save the last dance for me
                Baby, don't you know I love you so
                Can't you feel it when we touch
                I will never, never let you go
                I love you oh, so much
                You can dance, go and carry on
                'Til the night is gone
                And it's time to go
                If he asks if you're all alone
                Can he walk you home, you must tell him no
                'Cause don't forget who's taking you home
                And in whose arms you're gonna be
                Save the last dance for me
                Oh, I know that the music's fine
                Like sparklin' wine, go and have your fun
                Laugh and sing, but while we're apart
                Don't give your heart to anyone
                And don't forget who's taking you home
                And in whose arms you're gonna be
                So darling, save the last dance for me
                So don't forget who's taking you home
                Or in whose arms you're gonna be
                So darling, save the last dance for me
                Oh baby, won't you save the last dance for me
                Ooh, you make a promise
                That you'll save the last dance for me
                Save the last dance
                The very last dance
                For me
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_58 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+love+(Deluxe+Edition)/03+-+Michael+Bubl%C3%A9+-+Love+You+Anymore.mp3",
        title = "Love You Anymore",
        artist = "Michael Bublé",
        duration = "3:02",
        lyrics = """
                Just because I wander 'round the places we would go
                Hoping that I'd run into you one last time
                Just because I never took your picture off my phone
                Doesn't mean that you're still on my mind

                Just because I accidentally slip and say your name
                When I hear our song, it makes me insecure
                Just because I know I'll never ever feel the same
                Doesn't mean I love you anymore

                Am I lying to myself again
                When I say you're not the best I've ever had
                Am I lying to myself again
                When I say that I'm not missing you so bad

                Just because I'm on my knees and swearing I will change
                And I'd do anything to hear you say "I'm yours"
                Just because I know I'll never ever feel the same
                Doesn't mean I love you anymore

                Am I lying to myself again
                When I say you're not the best I've ever had
                Am I lying to myself again
                When I say that I'm not missing you so bad

                Just because I'm on my knees and swearing I will change
                And do anything to hear you say "I'm yours"
                Just because I know I'll never ever feel the same
                Doesn't mean I love you anymore, more
                Doesn't mean I love you anymore (anymore, anymore)
                Doesn't mean I love you anymore
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_59 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Michael+Bubl%C3%A9/04+-+Michael+Bubl%C3%A9+-+For+Once+in+My+Life.mp3",
        title = "For Once in My Life",
        artist = "Michael Bublé",
        duration = "2:33",
        lyrics = """
                For once in my life, I've got someone who needs me
                Someone I've needed so long
                For once unafraid, I can go where life leads me
                And somehow I know I'll be strong
                For once I can touch what my heart used to dream of
                Long before I knew someone warm like you
                Could make my dreams come true
                For once in my life, I won't let sorrow hurt me
                Not like it's hurt me before
                For once I have someone I know won't desert me
                I'm not alone anymore
                For once I can say, "This is mine, you can't take it
                Long as I know I've got love, I can make it"
                For once in my life, I've got someone who needs me
                At least for once I can say, "This is mine, you can't take it
                Long as I know I've got love, I can make it"
                For once in my life, I've got someone
                For once in my life, I found someone
                For once in my life, I've got someone who needs me
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_37 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Michael+Bubl%C3%A9/10+-+Michael+Bubl%C3%A9+-+Sway.mp3",
        title = "Sway",
        artist = "Michael Bublé",
        duration = "3:08",
        lyrics = """
                When marimba rhythms start to play
                Dance with me, make me sway
                Like a lazy ocean hugs the shore
                Hold me close, sway me more
                Like a flower bending in the breeze
                Bend with me, sway with ease
                When we dance, you have a way with me
                Stay with me, sway with me
                Other dancers may be on the floor
                Dear, but my eyes will see only you
                Only you have that magic technique
                When we sway, I go weak
                I can hear the sounds of violins
                Long before it begins
                Make me thrill as only you know how
                Sway me smooth, sway me now
                Other dancers may be on the floor
                Dear, but my eyes will see only you
                Only you have that magic technique
                When we sway, I go weak
                I can hear the sounds of violins
                Long before it begins
                Make me thrill as only you know how
                Sway me smooth, sway me now
                When marimba rhythms start to play
                Dance with me, make me sway
                Like a lazy ocean hugs the shore
                Hold me close, sway me more
                Like a flower bending in the breeze
                Bend with me, sway with ease
                When we dance you have a way with me
                Stay with me, sway with me
                When marimbas start to play
                Hold me close, make me sway
                Like a lazy ocean hugs the shore
                Hold me close, sway me more
                Like a flower bending in the breeze
                Bend with me, sway with ease
                When we dance, you have a way with me
                Stay with me, sway with me
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_60 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Michael+Bubl%C3%A9/11+-+Michael+Bubl%C3%A9+-+The+Way+You+Look+Tonight.mp3",
        title = "The Way You Look Tonight",
        artist = "Michael Bublé",
        duration = "4:39",
        lyrics = """
                Someday when I'm awfully low
                When the world is cold
                I will feel a glow just thinking of you
                And the way you look tonight
                You're lovely, with your smile so warm
                And your cheeks, so soft
                There is nothing for me but to love you
                And the way you look tonight
                With each word, your tenderness grows
                Tearing my fears apart
                And that laugh that wrinkles your nose
                It touches my foolish heart, hmm
                Lovely, never ever change
                Keep that breathless charm
                Won't you please arrange it? 'Cause I love you
                Just the way you look tonight
                With each word, your tenderness grows
                Tearing my fears apart
                And that laugh that wrinkles your nose
                It touches my foolish heart
                Lovely, don't you ever change
                Keep that breathless charm
                Won't you please arrange it? 'Cause I love you
                Just the way you look tonight
                Ooh, tonight
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_61 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Michael+Bubl%C3%A9/12+-+Michael+Bubl%C3%A9+-+Come+Fly+with+Me.mp3",
        title = "Come Fly with Me",
        artist = "Michael Bublé",
        duration = "3:18",
        lyrics = """
                Come fly with me, let's fly, let's fly away
                If you can use some exotic booze
                There's a bar in far Bombay
                Come fly with me
                Let's fly, let's fly away
                Come fly with me, let's float down to Peru
                In lama land, there's a one man band
                And he'll toot his flute for you
                Come fly with me, let's take off in the blue
                Once I get you up there
                Where the air is rarefied
                We'll just glide
                Starry eyed
                Once I get you up there
                I'll be holding you so near
                You may hear the angels cheer
                Because we're together
                Weather wise it's such a lovely day
                Just say the words and we'll beat those birds
                Down to Acapulco bay
                It's perfect, for a flying honeymoon, they say
                So come fly with me
                Let's fly, let's fly away
                (Oh, come on and fly)
                Once I get you up there
                Where the air is rarefied
                We'll just glide
                Starry eyed
                Once I get you up there
                I'll be holding you so near
                You may hear all the angels cheer
                Because we're together
                Weather wise it's such a lovely day
                You just say those words and we'll beat those birds
                Down to Acapulco bay
                It's so perfect, for a flying honeymoon, they say
                Come fly with me
                Let's fly, let's fly
                Pack up, let's fly away
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_62 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+Special+Delivery/03+-+Michael+Bubl%C3%A9+-+Dream+a+Little+Dream+of+Me.mp3",
        title = "Dream a Little Dream of Me",
        artist = "Michael Bublé",
        duration = "3:07",
        lyrics = """
                Stars shining bright above you
                Night breezes seem to whisper, "I love you"
                Birds singing in the sycamore tree
                Dream a little dream of me
                Say "nighty-night" and kiss me
                Just hold me tight and tell me you'll miss me
                While I'm alone and blue as can be
                Dream a little dream of me
                Stars fading, but I linger on, dear
                Still craving your kiss
                I'm longing to linger 'til dawn, dear
                Just saying this
                Sweet dreams 'til sunbeams find you
                Sweet dreams that leave all worries behind you
                But in your dreams, whatever they be
                Dream a little dream of me
                Stars fading, but I linger on, dear
                Still craving your kiss
                I'm longing to linger 'til dawn, dear
                Just saying this
                Sweet dreams 'til sunbeams find you
                Sweet dreams that leave all worries behind you
                But in your dreams, whatever they be
                Dream a little dream of
                Dream a little dream of
                Dream a little dream of me
                Of me
                Dream a little dream of me
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_63 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+To+Be+Loved/02+-+Michael+Bubl%C3%A9+-+It's+a+Beautiful+Day.mp3",
        title = "It's a Beautiful Day",
        artist = "Michael Bublé",
        duration = "3:18",
        lyrics = """
                I don't know why
                You think that you could hold me
                When you couldn't get by by yourself
                And I don't know who
                Would ever want to tear the seam of someone's dream
                Baby, it's fine, you said that we should just be friends
                While I came up with that line and I'm sure
                That it's for the best
                If you ever change your mind, don't hold your breath
                'Cause you may not believe
                That baby, I'm relieved, hmm
                When you said goodbye, my whole world shines
                Hey hey hey
                It's a beautiful day and I can't stop myself from smiling
                If we're drinking, then I'm buying
                And I know there's no denying
                It's a beautiful day, the sun is up, the music's playing
                And even if it started raining
                You won't hear this boy complaining
                'Cause I'm glad that you're the one who got away
                It's a beautiful day
                It's my turn to fly, so girls, get in line
                'Cause I'm easy, no playing this guy like a fool
                Now I'm alright
                Might've had me caged before, but not tonight
                And you may not believe, hmm
                That baby, I'm relieved
                This fire inside, it burns too bright
                I don't want to say "So long", I just want to say "Goodbye"
                It's a beautiful day and I can't stop myself from smiling
                If we're drinking, then I'm buying
                And I know there's no denying
                That it's a beautiful day, the sun is up, the music's playing
                And even if it started raining
                You won't hear this boy complaining
                'Cause I'm glad that you're the one who got away, hmm
                'Cause if you ever think I'll take up
                My time with thinking of our break-up
                Then, you've got another thing coming your way
                'Cause it's a beautiful day
                Beautiful day
                Oh, baby, any day that you're gone away
                It's a beautiful day
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_64 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/MichaelBubleMp3/Michael+Bubl%C3%A9+-+To+Be+Loved/09+-+Michael+Bubl%C3%A9%2C+Naturally+7+-+Have+I+Told+You+Lately+That+I+Love+You+(with+Naturally+7).mp3",
        title = "Have I Told You Lately That I Love You (with Naturally 7)",
        artist = "Michael Bublé",
        duration = "3:25",
        lyrics = """
                Have I told you lately that I love you?
                Can I tell you once again somehow?
                Have I told with all my heart and soul how I adore you?
                Well darlin', I'm tellin' you now
                Have I told you lately when I'm sleepin'
                Every dream I dream is you somehow?
                Have I told you why the nights are long when you're not with me?
                Well darlin', I'm telling you now
                My heart would break in two if I should loose you
                It's no good without you anyhow
                Have I told you lately that I love you?
                Well my darling, I'm telling you now
                Have I told you how the nights are long
                When you're not with me?
                Well darling, I'm telling you now
                My heart would break in two if I should loose you
                It's no good without you anyhow
                Oh, have I told you lately that I love you?
                Well darling, I'm telling you now
                My sweet darling, I'm telling you now
                Darling, I'm telling you now
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_65 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/04+-+John+Mayer+-+Gravity.mp3",
        title = "Gravity",
        artist = "John Mayer",
        duration = "4:05",
        lyrics = """
                Gravity is working against me
                And gravity wants to bring me down
                Oh, I'll never know
                What makes this man, with all the love that his heart can stand
                Dream of ways to throw it all away
                Whoa, whoa
                Gravity is working against me
                And gravity wants to bring me down
                Oh, twice as much ain't twice as good
                And can't sustain like one half could
                It's wanting more that's gonna send me to my knees
                Oh, twice as much ain't twice as good
                And can't sustain like one half could
                It's wanting more that's gonna send me to my knees
                Whoa, whoa
                Gravity, stay the hell away from me
                Whoa, whoa
                Gravity has taken better men than me
                Now how can that be?
                Just keep me where the light is
                Just keep me where the light is
                Just keep me where the light is
                Come on, keep me where the light is
                Come on, keep me where the light is
                Come on, keep me where, now, keep me where the light is
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_66 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/05+-+John+Mayer+-+The+Heart+of+Life.mp3",
        title = "The Heart of Life",
        artist = "John Mayer",
        duration = "3:18",
        lyrics = """
                I hate to see you cry
                Lying there in that position
                There's things you need to hear
                So turn off your tears and listen
                Pain throws your heart to the ground
                Love turns the whole thing around
                No, it won't all go the way it should
                But I know the heart of life is good
                You know it's nothing new
                Bad news never had good timing
                But then the circle of your friends
                Will defend the silver lining
                Pain throws your heart to the ground
                Love turns the whole thing around
                No, it won't all go the way it should
                But I know the heart of life is good
                Pain throws your heart to the ground
                Love turns the whole thing around
                Fear is a friend who's misunderstood
                But I know the heart of life is good
                I know it's good
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_67 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/07+-+John+Mayer+-+Stop+This+Train.mp3",
        title = "Stop This Train",
        artist = "John Mayer",
        duration = "4:45",
        lyrics = """
                No, I'm not colorblind
                I know the world is black and white
                I try to keep an open mind
                But I just can't sleep on this tonight
                Stop this train
                I want to get off and go home again
                I can't take the speed it's moving in
                I know I can't
                But honestly, won't someone stop this train?
                Don't know how else to say it
                Don't want to see my parents go
                I'm one generation's length away
                From fighting life out on my own
                Oh, come on, stop this train
                I want to get off and go home again
                I can't take the speed it's moving in
                I know I can't
                But honestly, won't someone stop this train?
                I'm so scared of getting older
                I'm only good at being young
                So I play the numbers game
                To find a way to say my life has just begun
                Had a talk with my old man
                Said, "Help me understand"
                He said "Turn 68, oh, you'll re-negotiate"
                "Don't stop this train
                Don't for a minute change the place you're in
                And don't think I couldn't ever understand
                I tried my hand
                John, honestly we'll never stop this train"
                Oh, now, once in a while, when it's good
                It'll feel like it should
                And they're all still around
                And you're still safe and sound
                And you don't miss a thing
                'Til you cry
                When you're driving away in the dark, yeah
                Singing
                Stop this train
                I want to get off and go back home again
                I can't take the speed this thing moving in
                I know I can't
                'Cause now I see, I'm never gonna stop this train
                Never gonna stop this train
                Oh, I'm never gonna stop this train
                Oh, I'm never gonna stop this train
                Oh, I'm never gonna stop this train
                Thank you
                How you feel tonight? You ready to hear alot of music
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_68 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/08+-+John+Mayer+-+Slow+Dancing+in+a+Burning+Room.mp3",
        title = "Slow Dancing in a Burning Room",
        artist = "John Mayer",
        duration = "4:02",
        lyrics = """
                It's not a silly little moment
                It's not the storm before the calm
                This is the deep and dying breath of
                This love that we've been working on
                Can't seem to hold you like I want to
                So I can feel you in my arms
                Nobody's gonna come and save you
                We pulled too many false alarms
                We're going down
                And you can see it too
                We're going down
                And you know that we're doomed
                My dear
                We're slow dancing in a burning room
                I was the one you always dreamed of
                You were the one I tried to draw
                How dare you say it's nothing to me?
                Baby, you're the only light I ever saw
                I'll make the most of all the sadness
                You'll be a bitch because you can
                You try to hit me just to hurt me
                So you leave me feeling dirty
                'Cause you can't understand
                We're going down
                And you can see it too
                We're going down
                And you know that we're doomed
                My dear
                We're slow dancing in a burning room
                Go cry about it, why don't you?
                Go cry about it, why don't you?
                Go cry about it, why don't you?
                My dear, we're slow dancing in a burning room
                Burning room
                Burning room
                Don't you think we oughta know by now?
                Don't you think we should have learned somehow?
                Dont you think we oughta know by now?
                Dont you think we should have learned somehow?
                Don't you think we oughta know by now?
                Don't you think we should have learned somehow?
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_69 = Songs (
        user_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/10+-+John+Mayer+-+Dreaming+with+a+Broken+Heart.mp3",
        title = "Dreaming with a Broken Heart",
        artist = "John Mayer",
        duration = "4:05",
        lyrics = """
                It's not a silly little moment
                It's not the storm before the calm
                This is the deep and dying breath of
                This love that we've been working on
                Can't seem to hold you like I want to
                So I can feel you in my arms
                Nobody's gonna come and save you
                We pulled too many false alarms
                We're going down
                And you can see it too
                We're going down
                And you know that we're doomed
                My dear
                We're slow dancing in a burning room
                I was the one you always dreamed of
                You were the one I tried to draw
                How dare you say it's nothing to me?
                Baby, you're the only light I ever saw
                I'll make the most of all the sadness
                You'll be a bitch because you can
                You try to hit me just to hurt me
                So you leave me feeling dirty
                'Cause you can't understand
                We're going down
                And you can see it too
                We're going down
                And you know that we're doomed
                My dear
                We're slow dancing in a burning room
                Go cry about it, why don't you?
                Go cry about it, why don't you?
                Go cry about it, why don't you?
                My dear, we're slow dancing in a burning room
                Burning room
                Burning room
                Don't you think we oughta know by now?
                Don't you think we should have learned somehow?
                Dont you think we oughta know by now?
                Dont you think we should have learned somehow?
                Don't you think we oughta know by now?
                Don't you think we should have learned somehow?
                        """,
        date_created = datetime(2023, 9, 6)
    )



    db.session.add_all([demo, bobbie])
    # db.session.add_all([marnie])
    # 30 more if I want to access all of them, should probably split them up based on different playlists
    db.session.add_all([album_1, album_2, album_3, album_4, album_5, album_6, album_7])

    db.session.add_all([playlist_1, playlist_3, playlist_4, playlist_5])
    # db.session.add_all([playlist_2])

    db.session.add_all([song_1, song_2, song_3, song_4, song_5, song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15, song_16, song_17, song_18, song_19, song_20, song_21, song_22, song_23, song_24, song_25, song_26, song_27, song_28, song_29, song_30, song_31, song_32, song_33, song_34, song_35, song_36,
                        song_37, song_38, song_39, song_40, song_41, song_42, song_43, song_44, song_45, song_46, song_47, song_48, song_49, song_50, song_51, song_52,
                        song_53, song_54, song_55, song_56, song_57, song_58, song_59, song_60, song_61, song_62, song_63, song_64, song_65, song_66])


    album_1.album_songs.extend([song_11,song_65, song_66, song_67, song_68, song_69])
    album_2.album_songs.extend([song_35, song_36])
    album_3.album_songs.extend([song_31, song_32, song_33, song_34])
    album_4.album_songs.extend([song_28, song_29, song_30])
    album_5.album_songs.extend([song_21, song_22, song_23, song_24, song_25, song_26, song_27])
    album_6.album_songs.extend([song_55, song_56, song_57])
    album_7.album_songs.extend([song_43, song_44, song_45, song_46, song_47])
    album_8.album_songs.extend([song_1, song_2, song_20])
    album_9.album_songs.extend([song_4, song_8, song_18])
    album_10.album_songs.extend([song_12, song_14])
    album_11.album_songs.extend([song_6, song_7, song_19])
    album_12.album_songs.extend([song_9])
    album_13.album_songs.extend([song_5, song_17, song_51])
    album_14.album_songs.extend([song_10, song_15])
    album_15.album_songs.extend([song_13])
    album_16.album_songs.extend([song_37, song_38])
    album_17.album_songs.extend([song_40])
    album_18.album_songs.extend([song_39])
    album_19.album_songs.extend([song_41])
    album_20.album_songs.extend([song_42])
    album_21.album_songs.extend([song_48,song_49,song_50])
    album_22.album_songs.extend([song_53])
    album_23.album_songs.extend([song_52])
    album_24.album_songs.extend([song_54])
    album_25.album_songs.extend([song_55, song_56, song_57, ])
    album_26.album_songs.extend([song_58])
    album_27.album_songs.extend([song_37, song_59, song_60, song_61])
    album_28.album_songs.extend([song_62])
    album_29.album_songs.extend([song_63, song_64])

    playlist_1.playlist_songs.extend([song_1, song_2, song_3, song_4, song_5, song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15, song_16, song_17, song_18, song_19, song_20, song_51, song_65, song_66, song_67, song_68, song_69])
    playlist_3.playlist_songs.extend([song_21, song_22, song_23, song_24, song_25, song_26, song_27, song_28, song_29, song_30, song_31, song_32, song_33, song_34, song_35, song_36])
    playlist_4.playlist_songs.extend([song_38, song_39, song_40, song_41, song_42, song_43, song_44, song_45, song_46, song_47, song_48, song_49, song_50])
    playlist_5.playlist_songs.extend([song_37, song_52, song_53, song_54, song_55, song_56, song_57, song_58, song_59, song_60, song_61, song_62, song_63, song_64])


    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        # db.session.execute(f"TRUNCATE table {SCHEMA}.album_likes RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.song_likes RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlist_songs RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.album_songs RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")

    else:
        db.session.execute(text("DELETE FROM playlist_songs"))
        db.session.execute(text("DELETE FROM album_songs"))
        db.session.execute(text("DELETE FROM playlists"))
        db.session.execute(text("DELETE FROM songs"))
        db.session.execute(text("DELETE FROM albums"))
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()