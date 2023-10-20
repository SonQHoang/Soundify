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
        title = "Music For The Sleepy Traveler",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/MusicForTheSleepyTraveler.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "SalmonLikeTheFish",
        year = 2018,
        date_created = datetime(2018, 1, 18)
    )

    album_2 = Albums (
        user_id = 1,
        title = "srs",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/srsAlbumCover.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "eddy",
        year = 2018,
        date_created = datetime(2018, 8, 18)
    )

    album_3 = Albums (
        user_id = 1,
        title = "2 Damn Loud",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/2DamnLoudAlbuMCover.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "eddy",
        year = 2018,
        date_created = datetime(2018, 9, 19)
    )

    album_4 = Albums (
        user_id = 1,
        title = "Jazz Night",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/JazzMlodastClubCover.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "Jazz at Mladost Club",
        year = 2010,
        date_created = datetime(2010, 5, 25)
    )

    album_5 = Albums (
        user_id = 1,
        title = "Beethoven's Sonata No. 13 in E Flat Major",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/DanielVeeseyCoverArt.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "Daniel Veesey",
        year = 2009,
        date_created = datetime(2009, 4, 23)
    )

    album_6 = Albums (
        user_id = 1,
        title = "Beethoven's Sonata No. 19 in G Minor",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/DanielVeeseyCoverArt.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "Daniel Veesey",
        year = 2009,
        date_created = datetime(2009, 4, 23)
    )

    album_7 = Albums (
        user_id = 1,
        title = "Beethoven's Sonata No. 20 in G Major",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/DanielVeeseyCoverArt.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "Daniel Veesey",
        year = 2009,
        date_created = datetime(2009, 4, 30)
    )

    album_8 = Albums (
        user_id = 1,
        title = "Beethoven's Sonata No. 22 in F Major",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/DanielVeeseyCoverArt.jpeg",
        album_description = """
        Source: Free Music 
        Archive License: CC BY-NC""",
        owner = "Daniel Veesey",
        year = 2009,
        date_created = datetime(2009, 4, 30)
    )

    album_9 = Albums (
        user_id = 1,
        title = "Beethoven's Sonata No. 8 in C Minor Pathetique",
        album_photo = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/DanielVeeseyCoverArt.jpeg",
        album_description = "Source: Free Music Archive License: CC BY-NC",
        owner = "Daniel Veesey",
        year = 2009,
        date_created = datetime(2009, 4, 23)
    )

    # album_10 = Albums (
    #     user_id = 1,
    #     title = "",
    #     album_photo = "",
    #     owner = "",
    #     year = 2021,
    #     date_created = datetime(2023, 9, 6)
    # )

    playlist_1 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/JonSalmon.jpeg",
        title = "This is SalmonLikeTheFish",
        playlist_description = "Music composed, performed, and produced by Jon Salmon. Philadelphia PA.",
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
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/eddyArtist.jpeg",
        title = "This is eddy",
        date_created = datetime(2023, 9, 6)
    )

    playlist_4 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/JazzMlodastClubCover.jpeg",
        title = "This is Jazz at Mladost Club",
        playlist_description = "VA from Subotica, Serbia playing jazz standards at Mladost Club, Subotica.",
        date_created = datetime(2023, 9, 6)
    )

    playlist_5 = Playlists (
        user_id = 1,
        owner = "Demo",
        image = "https://d47mwstkaud3p.cloudfront.net/AlbumCoverArt/DanielVeeseyArtistPhoto.jpeg",
        title = "This is Daniel Veesey",
        playlist_description = "Daniel Veesey is a pianist, mainly playing classical music.",
        date_created = datetime(2023, 9, 6)
    )
    
    song_1 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/SalmonLikeTheFish+-+Music+for+the+Sleepy+Traveler/01+SalmonLikeTheFish+-+Zion.mp3",
        title = "Zion",
        artist = "SalmonLikeTheFish",
        duration = "6:23",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_2 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/SalmonLikeTheFish+-+Music+for+the+Sleepy+Traveler/02+SalmonLikeTheFish+-+Yellowstone.mp3",
        title = "Yellowstone",
        artist = "SalmonLikeTheFish",
        duration = "6:47",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_3 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/SalmonLikeTheFish+-+Music+for+the+Sleepy+Traveler/03+SalmonLikeTheFish+-+Glacier.mp3",
        title = "Glacier",
        artist = "SalmonLikeTheFish",
        duration = "7:23",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_4 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/SalmonLikeTheFish+-+Music+for+the+Sleepy+Traveler/04+SalmonLikeTheFish+-+Sequoia.mp3",
        title = "Sequoia",
        artist = "SalmonLikeTheFish",
        duration = "5:14",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_5 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/SalmonLikeTheFish+-+Music+for+the+Sleepy+Traveler/05+SalmonLikeTheFish+-+Shenandoah.mp3",
        title = "Shenandoah",
        artist = "SalmonLikeTheFish",
        duration = "4:43",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_6 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+srs/01+eddy+-+Though+the+Tunnels.mp3",
        title = "Through the Tunnels",
        artist = "eddy",
        duration = "2:28",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_7 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+srs/02+eddy+-+Spy.mp3",
        title = "Spy",
        artist = "eddy",
        duration = "1:14",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_8 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+srs/03+eddy+-+Building+Tension.mp3",
        title = "Building Tension",
        artist = "eddy",
        duration = "1:23",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_9 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+srs/04+eddy+-+Coming+Up.mp3",
        title = "Coming Up",
        artist = "eddy",
        duration = "0:36",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_10 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+srs/05+eddy+-+Sorrow.mp3",
        title = "Sorrow",
        artist = "eddy",
        duration = "2:47",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_11 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+srs/06+eddy+-+The+Moment.mp3",
        title = "The Moment",
        artist = "eddy",
        duration = "1:00",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_12 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+2+Damn+Loud/01+eddy+-+Pure+Adrenaline.mp3",
        title = "Pure Adrenaline",
        artist = "eddy",
        duration = "0:33",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_13 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+2+Damn+Loud/02+eddy+-+Ruff.mp3",
        title = "Ruff",
        artist = "eddy",
        duration = "0:46",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_14 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+2+Damn+Loud/02+eddy+-+Ruff.mp3",
        title = "All The Way Up",
        artist = "eddy",
        duration = "2:41",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_15 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/eddy+-+2+Damn+Loud/04+eddy+-+Machinery.mp3",
        title = "Machinery",
        artist = "eddy",
        duration = "3:41",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_16 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/01+Jazz+at+Mladost+Club+-+No+More+Blues.mp3",
        title = "No More Blues",
        artist = "Jack Jackson",
        duration = "5:02",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_17 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/02+Jazz+at+Mladost+Club+-+Avenue+B.mp3",
        title = "Avenue B",
        artist = "Jazz at Mladost Club",
        duration = "7:12",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_18 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/03+Jazz+at+Mladost+Club+-+Blue+Monk.mp3",
        title = "Blue Monk",
        artist = "Jazz at Mladost Club",
        duration = "10:58",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_19 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/04+Jazz+at+Mladost+Club+-+Caravan.mp3",
        title = "Caravan",
        artist = "Jazz at Mladost Club",
        duration = "14:37",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_20 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/05+Jazz+at+Mladost+Club+-+Balkan+improvisation.mp3",
        title = "Balkan Improvisation",
        artist = "Jazz at Mladost Club",
        duration = "15:10",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_21 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/06+Jazz+at+Mladost+Club+-+Blue+bossa.mp3",
        title = "Blue Bossa",
        artist = "Jazz at Mladost Club",
        duration = "8:01",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_22 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/07+Jazz+at+Mladost+Club+-+Maiden+voyage.mp3",
        title = "Maiden Voyage",
        artist = "Jazz at Mladost Club",
        duration = "13:22",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_23 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/08+Jazz+at+Mladost+Club+-+C-mol+blues.mp3",
        title = "C-mol blues",
        artist = "Jazz at Mladost Club",
        duration = "10:25",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_24 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/09+Jazz+at+Mladost+Club+-+Kurina+blues.mp3",
        title = "Kurina Blues",
        artist = "Jazz at Mladost Club",
        duration = "14:45",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_25 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/10+Jazz+at+Mladost+Club+-+Song+for+Bilbao.mp3",
        title = "Song For Bilbao",
        artist = "Jazz at Mladost Club",
        duration = "9:16",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_26 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/11+Jazz+at+Mladost+Club+-+Konflikt.mp3",
        title = "Konflict",
        artist = "Jazz at Mladost Club",
        duration = "7:56",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_27 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/12+Jazz+at+Mladost+Club+-+Arana.mp3",
        title = "Arana",
        artist = "Jazz at Mladost Club",
        duration = "6:57",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_28 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+13+in+E+Flat+Major/01+Daniel+Veesey+-+Sonata+No.+13+in+E+Flat+Major%2C+Op.+27+No.+1+-+III.+Adagio+con+espressione.mp3",
        title = "Sonata No. 13 in E Flat Major, Op. 27 No. 1 - III. Adagio con espressione",
        artist = "Daniel Veesey",
        duration = "3:28",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_29 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+13+in+E+Flat+Major/02+Daniel+Veesey+-+Sonata+No.+13+in+E+Flat+Major%2C+Op.+27+No.+1+-+II.+Allegro+molto+e+vivace.mp3",
        title = "Sonata No. 13 in E Flat Major, Op. 27 No. 1 - II. Allegro molto e vivace",
        artist = "Daniel Veesey",
        duration = "2:14",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_30 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+13+in+E+Flat+Major/03+Daniel+Veesey+-+Sonata+No.+13+in+E+Flat+Major%2C+Op.+27+No.+1+-+I.+Andante+-+Allegro+-+Tempo+I.mp3",
        title = "Sonata No. 13 in E Flat Major, Op. 27 No. 1 - I. Andante - Allegro - Tempo I",
        artist = "Daniel Veesey",
        duration = "6:00",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_31 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+13+in+E+Flat+Major/04+Daniel+Veesey+-+Sonata+No.+13+in+E+Flat+Major%2C+Op.+27+No.+1+-+IV.+Allegro+vivace+-+Tempo+I+-+Presto.mp3",
        title = "Sonata No. 13 in E Flat Major, Op. 27 No. 1 - IV. Allegro vivace - Tempo I - Presto",
        artist = "Daniel Veesey",
        duration = "5:41",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_32 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+19+in+G+Minor/01+Daniel+Veesey+-+Sonata+No.+19+in+G+Minor%2C+Op.+49+No.+1+-+I.+Andante.mp3",
        title = "Sonata No. 19 in G Minor, Op. 49 No. 1 - I. Andante",
        artist = "Daniel Veesey",
        duration = "4:36",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_33 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+19+in+G+Minor/02+Daniel+Veesey+-+Sonata+No.+19+in+G+Minor%2C+Op.+49+No.+1+-+II.+Rondo++Allegro.mp3",
        title = "Sonata No. 19 in G Minor, Op. 49 No. 1 - II. Rondo Allegro",
        artist = "Daniel Veesey",
        duration = "3:41",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_34 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+20+in+G+Major/01+Daniel+Veesey+-+Sonata+No.+20+in+G+Major%2C+Op.+49+No.+2+-+II.+Tempo+di+menuetto.mp3",
        title = "Sonata No. 20 in G Major, Op. 49 No. 2 - II. Tempo di menuetto",
        artist = "Daniel Veesey",
        duration = "3:56",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_35 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+20+in+G+Major/02+Daniel+Veesey+-+Sonata+No.+20+in+G+Major%2C+Op.+49+No.+2+-+I.+Allegro+ma+non+troppo.mp3",
        title = "Sonata No. 20 in G Major, Op. 49 No. 2 - I. Allegro ma non troppo",
        artist = "Daniel Veesey",
        duration = "4:58",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_36 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+22+in+F+Major/01+Daniel+Veesey+-+Sonata+No.+22+in+F+Major%2C+Op.+54+-+II.+Allegretto.mp3",
        title = "Sonata No. 22 in F Major, Op. 54 - II. Allegretto",
        artist = "Daniel Veesey",
        duration = "6:21",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_37 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+22+in+F+Major/02+Daniel+Veesey+-+Sonata+No.+22+in+F+Major%2C+Op.+54+-+I.+In+tempo+dun+Menuetto.mp3",
        title = "Sonata No. 22 in F Major, Op. 54 - I. In tempo dun Menuetto",
        artist = "Daniel Veesey",
        duration = "6:14",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_38 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+8+in+C+Minor+Pathetique/01+Daniel+Veesey+-+Sonata+8%2C+'Pathetique'+-+I.+Grave+-+Allegro+di+molto+e+con+brio.mp3",
        title = "Sonata 8, 'Pathetique' - I. Grave - Allegro di molto e con brio",
        artist = "Daniel Veesey",
        duration = "9:03",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_39 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+8+in+C+Minor+Pathetique/02+Daniel+Veesey+-+Sonata+8%2C+'Pathetique'+-+II.+Adagio+cantabile.mp3",
        title = "Sonata 8, 'Pathetique' - II. Adagio cantabile",
        artist = "Daniel Veesey",
        duration = "6:20",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_40 = Songs (
        user_id = 1,
        audio_url = "https://d47mwstkaud3p.cloudfront.net/Jazz+at+Mladost+Club+-+Jazz+Night/Daniel+Veesey+-+Beethoven's+Sonata+No.+8+in+C+Minor+Pathetique/03+Daniel+Veesey+-+Sonata+8%2C+'Pathetique'+-+III.+Rondo+Allegro.mp3",
        title = "Sonata 8, 'Pathetique' - III. Rondo Allegro",
        artist = "Daniel Veesey",
        duration = "4:29",
        lyrics = """
                        """,
        date_created = datetime(2023, 9, 6)
    )

    # song_1 = Songs (
    #     user_id = 1,
    #     audio_url = "",
    #     title = "",
    #     artist = "Daniel Veesey",
    #     duration = "",
    #     lyrics = """
    #                     """,
    #     date_created = datetime(2023, 9, 6)
    # )



    db.session.add_all([demo, bobbie])
    # db.session.add_all([marnie])
    # 30 more if I want to access all of them, should probably split them up based on different playlists
    db.session.add_all([album_1, album_2, album_3, album_4, album_5, album_6, album_7, album_8, album_9])

    db.session.add_all([playlist_1, playlist_3, playlist_4, playlist_5])
    # db.session.add_all([playlist_2])

    db.session.add_all([song_1, song_2, song_3, song_4, song_5, song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15, song_16, song_17, song_18, song_19, song_20, song_21, song_22, song_23, song_24, song_25, song_26, song_27, song_28, song_29, song_30, song_31, song_32, song_33, song_34, song_35, song_36,
                        song_37, song_38, song_39, song_40
                        ])


    album_1.album_songs.extend([song_1, song_2, song_3, song_4, song_5])
    album_2.album_songs.extend([song_6, song_7, song_8, song_9, song_10, song_11])
    album_3.album_songs.extend([song_12, song_13, song_14, song_15])
    album_4.album_songs.extend([song_16, song_17, song_18, song_19, song_20, song_21, song_22, song_23, song_24, song_25, song_26, song_27])
    album_5.album_songs.extend([song_28, song_29, song_30, song_31])
    album_6.album_songs.extend([song_32, song_33])
    album_7.album_songs.extend([song_34, song_35])
    album_8.album_songs.extend([song_36, song_37])
    album_9.album_songs.extend([song_38, song_39, song_40])



    playlist_1.playlist_songs.extend([song_1, song_2, song_3, song_4, song_5])
    playlist_3.playlist_songs.extend([song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15])
    playlist_4.playlist_songs.extend([song_16, song_17, song_18, song_19, song_20, song_21, song_22, song_23, song_24, song_25, song_26, song_27])
    playlist_5.playlist_songs.extend([song_28, song_29, song_30, song_31, song_32, song_33, song_34, song_35, song_36, song_37, song_38, song_39, song_40])


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