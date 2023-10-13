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
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Continuum+Album+Art+John+Mayer.png",
        owner = "John Mayer Live",
        year = 2006,
        date_created = datetime(2023, 9, 6)
    )

    album_2 = Albums (
        user_id = 1,
        title = "The Hunting Party",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Hunting+Party+LinkinPark.jpeg",
        owner = "Linkin Park",
        year = 2011,
        date_created = datetime(2023, 9, 6)
    )

    album_3 = Albums (
        user_id = 1,
        title = "Meteora",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Meteora+LinkinPark.jpeg",
        owner = "Linkin Park",
        year = 2014,
        date_created = datetime(2023, 9, 6)
    )

    album_4 = Albums (
        user_id = 1,
        title = "Transformers: Revenge of the Fallen - The Album",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/TransformersRevengeFallen+LinkinPark.jpg",
        owner = "Linkin Park",
        year = 2013,
        date_created = datetime(2023, 9, 6)
    )

    album_5 = Albums (
        user_id = 1,
        title = "Hybrid Theory",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Hybrid+Theory+LinkinPark.jpeg",
        owner = "Linkin Park",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_6 = Albums (
        user_id = 1,
        title = "Minutes to Midnight",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/MinutesToMidnight+Linkinpark.jpg",
        owner = "Linkin Park",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_7 = Albums (
        user_id = 1,
        title = "Any Given Thursday",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Red+Album+Art+Taylor+Swift.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_8 = Albums (
        user_id = 1,
        title = "Battle Studies",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Battle+Studies+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_9 = Albums (
        user_id = 1,
        title = "Born and Raised",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Born+and+Raised+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_10 = Albums (
        user_id = 1,
        title = "Paradise Valley",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Paradise+Valley+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_11 = Albums (
        user_id = 1,
        title = "Room For Squares",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Room+For+Squares+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_12 = Albums (
        user_id = 1,
        title = "Where The Light is",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/WhereTheLightIs+JohnMayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_13 = Albums (
        user_id = 1,
        title = "Sob Rock",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Sob+Rock+John+Mayer.png",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_14 = Albums (
        user_id = 1,
        title = "The Search for Everything",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/The+Search+for+Everything+John+Mayer.jpeg",
        owner = "John Mayer",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_15 = Albums (
        user_id = 1,
        title = "Vulpeck Live",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/VulpeckLive.jpeg",
        owner = "Vulfpeck",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_16 = Albums (
        user_id = 1,
        title = "Sleep Through the Static",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/SleepThroughTheStatic+JackJackson.jpeg",
        owner = "Jack Jackson",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_17 = Albums (
        user_id = 1,
        title = "Brushfire Fairytales",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/BrushfireFairyTales+JackJackson.jpeg",
        owner = "Jack Jackson",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_18 = Albums (
        user_id = 1,
        title = "In Between Dreams",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/InBetweenDreams+JackJackson.jpeg",
        owner = "Jack Jackson",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_19 = Albums (
        user_id = 1,
        title = "On and On",
        album_photo = "",
        owner = "Jack Jackson",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_20 = Albums (
        user_id = 1,
        title = "Lover",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Lover+Taylor+Swift.jpeg",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_21 = Albums (
        user_id = 1,
        title = "Speak Now (Taylor's Version)",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Speak+Now+Taylor+Swift.png",
        owner = "Taylor Swift",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_22 = Albums (
        user_id = 1,
        title = "Call Me Irresponsible",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Call+Me+Irresponsible+Michael+Buble.jpeg",
        owner = "Vulfpeck",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_23 = Albums (
        user_id = 1,
        title = "Call Me Irresponsible (Deluxe)",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Call+Me+Irresponsible+Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_24 = Albums (
        user_id = 1,
        title = "Crazy Love",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Crazy+Love+Michael+Buble.png",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_25 = Albums (
        user_id = 1,
        title = "Love (Deluxe Edition)",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Love+Michael+Buble.jpg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_26 = Albums (
        user_id = 1,
        title = "Michael Bublé",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_27 = Albums (
        user_id = 1,
        title = "Special Delivery",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/Special+Delivery+Michael+Buble.jpg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    album_28 = Albums (
        user_id = 1,
        title = "To Be Loved",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/To+Be+Loved+Michael+Buble.jpeg",
        owner = "Michael Bublé",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    playlist_1 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/John+Mayer+Portrait.jpeg",
        title = "This is John Mayer Live",
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
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/LinkinParkCover.jpeg",
        title = "This is Linkin Park",
        date_created = datetime(2023, 9, 6)
    )

    playlist_4 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/VulfpeckCover.jpeg",
        title = "This is Vulfpeck Live",
        date_created = datetime(2023, 9, 6)
    )

    playlist_5 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/JackJacksonCover.jpeg",
        title = "This is Jack Johnson Live",
        date_created = datetime(2023, 9, 6)
    )
    
    song_1 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/02-Slow+Dancing+in+a+Burning+Room.flac",
        title = "Slow Dancing in a Burning Room",
        artist = "John Mayer",
        duration = "4:03",
        lyrics = """    
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_2 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/03-Shot+in+the+Dark.flac",
        title = "Shot in the Dark",
        artist = "John Mayer",
        duration = "6:18",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_3 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/04-Wild+Blue.flac",
        title = "Wild Blue",
        artist = "John Mayer",
        duration = "3:59",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_4 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/07-Why+Georgia.flac",
        title = "Why Georgia",
        artist = "John Mayer",
        duration = "4:28",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_5 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/08-War+of+My+Life.flac",
        title = "War of My Life",
        artist = "John Mayer",
        duration = "1:08",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_6 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/11-Neon.flac",
        title = "Neon",
        artist = "John Mayer",
        duration = "6:54",
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
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/09-Who+Says.flac",
        title = "Who Says",
        artist = "John Mayer",
        duration = "2:53",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_8 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/05-Queen+of+California.flac",
        title = "Queen of California",
        artist = "John Mayer",
        duration = "4:31",
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
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/10-Waitin'+on+the+Day.flac",
        title = "Waitin' On the Day",
        artist = "John Mayer",
        duration = "4:29",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_10 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/12-In+Your+Atmosphere.flac",
        title = "In Your Atmosphere",
        artist = "John Mayer",
        duration = "7:40",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_11 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/13-In+the+Blood.flac",
        title = "In the Blood",
        artist = "John Mayer",
        duration = "4:26",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_12 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/14-You're+Gonna+Live+Forever+in+Me.flac",
        title = "You're Gonna Live Forever in Me",
        artist = "John Mayer",
        duration = "3:24",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_13 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/15-I+Will+Be+Found+(Lost+at+Sea).flac",
        title = "I Will Be Found (Lost at Sea)",
        artist = "John Mayer",
        duration = "1:17",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_14 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/16-Changing.flac",
        title = "Changing",
        artist = "John Mayer",
        duration = "6:30",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_15 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/18-Stop+This+Train.flac",
        title = "Stop This Train",
        artist = "John Mayer",
        duration = "5:03",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_16 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/19-All+We+Ever+Do+is+Say+Goodbye.flac",
        title = "All We Ever Do is Say Goodbye",
        artist = "John Mayer",
        duration = "2:27",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_17 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/20-Man+on+the+Side.flac",
        title = "Man on the Side",
        artist = "John Mayer",
        duration = "1:44",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_18 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/21-Age+of+Worry.flac",
        title = "The Age of Worry",
        artist = "John Mayer",
        duration = "3:31",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_19 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/22-Your+Body+is+a+Wonderland.flac",
        title = "Your Body is a Wonderland",
        artist = "John Mayer",
        duration = "5:35",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_20 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/23-Walt+Grace.flac",
        title = "Walt Grace",
        artist = "John Mayer",
        duration = "5:42",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_21 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/24-If+I+Ever+Get+Around+to+Livin.flac",
        title = "If I Ever Get Around to Livin",
        artist = "John Mayer",
        duration = "7:42",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )
    
    song_22 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/25-Edge+of+Desire.flac",
        title = "Edge of Desire",
        artist = "John Mayer",
        duration = "7:31",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_23 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/26-Heart+of+Life.flac",
        title = "Heart of Life",
        artist = "John Mayer",
        duration = "4:18",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_24 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JohnMayerLive/27-Free+Fallin.flac",
        title = "Free Fallin",
        artist = "John Mayer",
        duration = "4:24",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_25 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/01+-+Keys+To+The+Kingdom.mp3",
        title = "Keys To The Kingdom",
        artist = "Linkin Park",
        duration = "3:38",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_26 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/02+-+Don't+Stay.mp3",
        title = "Don't Stay",
        artist = "Linkin Park",
        duration = "3:07",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_27 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/03+-+Somewhere+I+Belong.mp3",
        title = "Somewhere I Belong",
        artist = "Linkin Park",
        duration = "3:33",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_28 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/04+-+Lying+From+You.mp3",
        title = "Lying From You",
        artist = "Linkin Park",
        duration = "2:55",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_29 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/new+divide.mp3",
        title = "New Divide",
        artist = "Linkin Park",
        duration = "4:28",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_30 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/05+-+Hit+The+Floor.mp3",
        title = "Hit The Floor",
        artist = "Linkin Park",
        duration = "2:44",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_31 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/06+-+Easier+To+Run.mp3",
        title = "Easier To Run",
        artist = "Linkin Park",
        duration = "3:24",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_32 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/07+-+Faint.mp3",
        title = "Faint",
        artist = "Linkin Park",
        duration = "2:42",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_33 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/09+-+Breaking+The+Habit.mp3",
        title = "Breaking The Habit",
        artist = "Linkin Park",
        duration = "3:16",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_34 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/10+-+From+The+Inside.mp3",
        title = "From The Inside",
        artist = "Linkin Park", 
        duration = "2:55",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_35 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/11+-+Nobody's+Listening.mp3",
        title = "Nobody's Listening",
        artist = "Linkin Park",
        duration = "2:58",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_36 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/12+-+Session.mp3",
        title = "Session",
        artist = "Linkin Park",
        duration = "2:24",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6),
    )

    song_37 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/13+-+Numb.mp3",
        title = "Numb",
        artist = "Linkin Park",
        duration = "3:07",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_38 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/Crawling+(Official+Video)+-+Linkin+Park.mp3",
        title = "Crawling",
        artist = "Linkin Park",
        duration = "3:36",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_39 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/Linkin+Park+-+Forgotten+(Lyrics).mp3",
        title = "Forgotten",
        artist = "Linkin Park",
        duration = "3:20",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_40 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/LinkinPark-KeysToTheKingdom/linkin+park+-+what+i've+done193295486.mp3",
        title = "What I've Done",
        artist = "Linkin Park",
        duration = "3:28",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_41 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/1.1+Rollerblade.mp3",
        title = "Rollerblade",
        artist = "Vulfpeck",
        duration = "2:26",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_42 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/1.2+I'll+Still+Call.mp3",
        title = "I'll Still Call",
        artist = "Vulfpeck",
        duration = "3:04",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_43 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/1.3+Wind+Cries+Mary.mp3",
        title = "Wind Cries Mary",
        artist = "Vulfpeck",
        duration = "3:29",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_44 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/1.4+Self+Discovery.mp3",
        title = "Self Discovery",
        artist = "Vulfpeck",
        duration = "6:46",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_45 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/1.5+Bike+Ride.mp3",
        title = "Bike Ride",
        artist = "Vulfpeck",
        duration = "6:55",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_46 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.01+Speed+of+Night.mp3",
        title = "Speed of the Night",
        artist = "Vulfpeck",
        duration = "4:49",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_47 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.02+Lost+in+Translation.mp3",
        title = "Lost in Translation",
        artist = "Vulfpeck",
        duration = "3:53",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_48 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.04+United.mp3",
        title = "United",
        artist = "Vulfpeck",
        duration = "3:39",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_49 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.05+What's+Goin+On.mp3",
        title = "What's Goin On",
        artist = "Vulfpeck",
        duration = "5:49",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_50 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.06+Pleasin.mp3",
        title = "Pleasin",
        artist = "Vulfpeck",
        duration = "4:41",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_51 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.07+Bright+Light.mp3",
        title = "Bright Light",
        artist = "Vulfpeck",
        duration = "5:33",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_52 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.08+Work+It+Out.mp3",
        title = "Work It Out",
        artist = "Vulfpeck",
        duration = "3:59",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_53 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.09+Lord+Will+Make+A+Way.mp3",
        title = "Lord Will Make A Way",
        artist = "Vulfpeck",
        duration = "4:09",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_54 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.10+Simple+Step.mp3",
        title = "Simple Step",
        artist = "Vulfpeck",
        duration = "5:05",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_55 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.11+1612.mp3",
        title = "1612",
        artist = "Vulfpeck",
        duration = "3:26",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_56 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.12+Wait+for+the+Moment.mp3",
        title = "Wait for the Moment",
        artist = "Vulfpeck",
        duration = "3:51",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_57 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.13+Serve+Somebody.mp3",
        title = "Serve Somebody",
        artist = "Vulfpeck",
        duration = "6:23",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_58 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.15+You've+Got+a+Friend.mp3",
        title = "You've Got a Friend",
        artist = "Vulfpeck",
        duration = "5:47",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_59 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/AntwaunStanley-Vulfpeck/2.16+Thank+Yous.mp3",
        title = "Thank Yous",
        artist = "Vulfpeck",
        duration = "3:03",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_60 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/AllAtOnce.mp3",
        title = "All At Once",
        artist = "Jack Jackson",
        duration = "4:16",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_61 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/BananaPancakes.mp3",
        title = "Banana Pancakes",
        artist = "Jack Jackson",
        duration = "3:33",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_62 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/BetterTogether.mp3",
        title = "Better Together",
        artist = "Jack Jackson",
        duration = "4:18",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_63 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/Breakdown.mp3",
        title = "Breakdown",
        artist = "Jack Jackson",
        duration = "4:22",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_64 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/BubbleToes.mp3",
        title = "Bubble Toes",
        artist = "Jack Jackson",
        duration = "5:13",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_65 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/WastingTime.mp3",
        title = "Wasting Time",
        artist = "Jack Jackson",
        duration = "5:46",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_66 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/Constellations.mp3",
        title = "Constellation",
        artist = "Jack Jackson",
        duration = "4:01",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_67 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/Taylor.mp3",
        title = "Taylor",
        artist = "Jack Jackson",
        duration = "4:13",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_68 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/Flake.mp3",
        title = "Flake",
        artist = "Jack Jackson",
        duration = "4:48",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_69 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/GoodPeople.mp3",
        title = "Good People",
        artist = "Jack Jackson",
        duration = "3:24",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_70 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/GoOn.mp3",
        title = "Go On",
        artist = "Jack Jackson",
        duration = "5:12",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_71 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/HirozionHasBeenDefeated.mp3",
        title = "Hirozion Has Been Defeated",
        artist = "Jack Jackson",
        duration = "2:53",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_72 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/HopeYourNotAlone.mp3",
        title = "Hope Your Not Alone",
        artist = "Jack Jackson",
        duration = "4:00",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_73 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/IfIHadEyes.mp3",
        title = "If I Had Eyes",
        artist = "Jack Jackson",
        duration = "5:16",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_74 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/InaudibleMelodies.mp3",
        title = "Inuadible Melodies",
        artist = "Jack Jackson",
        duration = "3:53",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_75 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/Monsoon.mp3",
        title = "Monsoon",
        artist = "Jack Jackson",
        duration = "4:07",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_76 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/MotherandChildReunion.mp3",
        title = "Mother and Child Reunion",
        artist = "Jack Jackson",
        duration = "1:29",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_77 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/SameGirl.mp3",
        title = "Same Girl",
        artist = "Jack Jackson",
        duration = "2:28",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_78 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/SittingWaitingWishing.mp3",
        title = "Sitting Waiting Wishing",
        artist = "Jack Jackson",
        duration = "3:55",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_79 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/SleepThroughTheStatic.mp3",
        title = "Sleep Through the Static",
        artist = "Jack Jackson",
        duration = "5:12",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_80 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/JackJohnsonLive/StapleItTogether.mp3",
        title = "Staple It Together",
        artist = "Jack Jackson",
        duration = "4:07",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    # song_70 = Songs (
    #     user_id = 1,
    #     audio_url = "",
    #     title = "",
    #     artist = "Jack Jackson",
    #     duration = "",
    #     lyrics = """
    #                     """,
    #     date_created = datetime(2023, 9, 6)
    # )



    db.session.add_all([demo, bobbie])
    # db.session.add_all([marnie])
    # 30 more if I want to access all of them, should probably split them up based on different playlists
    db.session.add_all([album_1, album_2, album_3, album_4, album_5, album_6, album_7, album_8, album_9, album_10, album_11, album_12, album_13, album_14, 
                        album_15, 
                        album_16, album_17, album_18,
                        # album_19, album_20, album_21, album_22, album_23, album_24, album_25, album_26, album_27, album_28
                        ])

    db.session.add_all([playlist_1, playlist_3, playlist_4, playlist_5])
    # db.session.add_all([playlist_2])

    db.session.add_all([song_1, song_2, song_3, song_4, song_5, song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15, song_16, song_17, song_18, song_19, song_20, song_21, song_22, song_23, song_24, song_25, song_26, song_27, song_28, song_29, song_30, song_31, song_32, song_33, song_34, song_35, song_36,
                        song_37, song_38, song_39, song_40, song_41, song_42, song_43, song_44, song_45, song_46, song_47, song_48, song_49, song_50, song_51, song_52,
                        song_53, song_54, song_55, song_56, song_57, song_58, song_59, song_60, song_61, song_62, song_63, song_64, song_65, song_66, song_67, song_68, song_69, song_70,
                        song_71, song_72, song_73, song_74, song_75, song_76, song_77, song_78, song_79, song_80
                        ])


    album_1.album_songs.extend([song_1, song_9, song_15, song_23])
    
    album_2.album_songs.extend([song_25])
    album_3.album_songs.extend([song_26, song_27, song_28, song_30, song_31, song_32, song_33, song_34, song_35, song_36, song_37,   ])
    album_4.album_songs.extend([song_29])
    album_5.album_songs.extend([song_39])
    album_6.album_songs.extend([song_40])
    album_7.album_songs.extend([song_17])
    album_8.album_songs.extend([song_5, song_7, song_16])
    album_9.album_songs.extend([song_8, song_18, song_20, song_21, song_22])
    album_10.album_songs.extend([song_13])
    album_11.album_songs.extend([song_4, song_6, song_19])
    album_12.album_songs.extend([song_10, song_24])
    album_13.album_songs.extend([song_2, song_3])
    album_14.album_songs.extend([song_11, song_12, song_14])
    album_15.album_songs.extend([song_41, song_42, song_43, song_44, song_45, song_46, song_47, song_48, song_49, song_50, song_51, song_52, song_53, song_54, song_55, song_56, song_57, song_58, song_59])
    album_16.album_songs.extend([song_60, song_70, song_73, song_75, song_77, song_79 ])
    album_17.album_songs.extend([song_64, song_68, song_74])
    album_18.album_songs.extend([song_61, song_62, song_63, song_66, song_69, song_78, song_80])
    album_19.album_songs.extend([song_65, song_67, song_71])
    # album_20.album_songs.extend([])
    # album_21.album_songs.extend([])
    # album_22.album_songs.extend([])
    # album_23.album_songs.extend([])
    # album_24.album_songs.extend([])
    # album_25.album_songs.extend([])
    # album_26.album_songs.extend([])
    # album_27.album_songs.extend([])
    # album_28.album_songs.extend([])

    playlist_1.playlist_songs.extend([song_1, song_2, song_3, song_4, song_5, song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15, song_16, song_17, song_18, song_19, song_20, song_21, song_22, song_23, song_24])
    playlist_3.playlist_songs.extend([song_25, song_26, song_27, song_28, song_29, song_30, song_31, song_32, song_33, song_34, song_35, song_36, song_37, song_38, song_39, song_40])
    playlist_4.playlist_songs.extend([song_41, song_42, song_43, song_44, song_45, song_46, song_47, song_48, song_49, song_50, song_51, song_52, song_53, song_54, song_55, song_56, song_57, song_58, song_59])
    playlist_5.playlist_songs.extend([song_60, song_61, song_62, song_63, song_64, song_65, song_66, song_67, song_68, song_69, song_70,song_71, song_72, song_73, song_74, song_75, song_76, song_77, song_78, song_79, song_80])


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