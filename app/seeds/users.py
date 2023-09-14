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
        owner = "John Mayer",
        year = 2006,
        date_created = datetime(2023, 9, 6)
    )

    album_2 = Albums (
        user_id = 1,
        title = "+",
        owner = "Ed Sheeran",
        year = 2011,
        date_created = datetime(2023, 9, 6)
    )

    album_3 = Albums (
        user_id = 1,
        title = "x",
        owner = "Ed Sheeran",
        year = 2014,
        date_created = datetime(2023, 9, 6)
    )

    album_4 = Albums (
        user_id = 1,
        title = "=",
        owner = "Ed Sheeran",
        year = 2013,
        date_created = datetime(2023, 9, 6)
    )

    album_5 = Albums (
        user_id = 1,
        title = "÷",
        owner = "Ed Sheeran",
        year = 2021,
        date_created = datetime(2023, 9, 6)
    )

    playlist_1 = Playlists (
        user_id = 1,
        owner = "Demo",
        title = "This is John Mayer",
        date_created = datetime(2023, 9, 6)
    )

    playlist_2 = Playlists (
        user_id = 2,
        owner = "Marnie",
        title = "This is John Mayer",
        date_created = datetime(2023, 9, 6)
    )
    
    song_1 = Songs (
        user_id = 1,
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/05+-+John+Mayer+-+Perfectly+Lonely.mp3",
        title = "Perfectly Lonely",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Heartbreak+Warfare.mp3",
        title = "Heartbreak Warfare",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+Wynton+Marsalis+Septet%2C+John+Mayer%2C+Wynton+Marsalis+-+I'm+Gonna+Find+Another+You.mp3",
        title = "I'm Gonna Find Another You",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+Leon+Bridges%2C+John+Mayer+-+Inside+Friend+(feat.+John+Mayer).mp3",
        title = "Inside Friend (feat. John Mayer)",
        duration = "2:55",
        lyrics = """
                    You can be my inside friend
                    You can be my inside friend
                    Slide through when you want
                    You know I want to put you on
                    It's evil out there
                    Let's keep it at home
                    So come on
                    I wanna see you slide across the kitchen floor
                    Can't give you more but
                    You can be my inside friend
                    You can be my inside friend
                    My inside friend
                    Won't you be my inside friend?
                    Come through with your hair still wet
                    Yoga pants, sweatshirt on the bed
                    Heart heavy and your week been crazy
                    We can be lazy, baby, embrace me
                    In this feeling so right
                    Don't think about leaving anytime tonight
                    You can just slide across my kitchen floor
                    And tell me goodbye
                    And just see yourself right out my door
                    Come back through when you want to
                    If you do
                    You never call me anymore
                    That's what inside friends are for
                    You can be my inside friend
                    You can be my inside friend
                    My inside friend
                    Won't you be my inside friend?
                    (Don't you wanna be, don't you wanna be, don't you wanna be my)
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_5 = Songs (
        user_id = 1,
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Last+Train+Home.mp3",
        title = "Last Train Home",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+Jacob+Collier%2C+Lizzy+McAlpine%2C+John+Mayer+-+Never+Gonna+Be+Alone+(feat.+Lizzy+McAlpine+%26+John+Mayer).mp3",
        title = "Never Gonna Be Alone (feat. Lizzy McAlpine & John Mayer)",
        duration = "4:10",
        lyrics = """
                There's a patch of sunlight in my room
                On the carpet where I held you for a moment in June
                There was something so sweet about it, never been so unguarded
                And it made me fall for you
                There's a tree that looks up at the moon
                In the garden, where I held you for a moment in the gloom
                There was something so sweet about it, I'm holding onto this moment
                'Cause it made me fall for you
                Made me fall for you
                Take me back to the window, take me back to the door
                You'll be right where I left you sittin' on the floor
                Now I'm never gonna be alone, mm, mm
                Take me back to the window, take me back to the door
                You'll be right where I left you sittin' on the floor
                Now I'm never gonna be alone
                And I know, I know
                There's so much I want to say to you
                Even though I know
                Nothing's gonna change
                But I'll always find my way back here to you
                Take me back to the window, take me back to the door
                You'll be right where I left you sittin' on the floor
                Now I'm never gonna be alone
                (Never gonna be alone, never gonna be alone, be alone, be alone)
                Take me back to the window, take me back to the door
                You'll be right where I left you sittin' on the floor
                Now I'm never gonna be alone (be alone)
                There's a patch of sunlight in my room
                On the carpet where I held you for a moment
                        """,
        date_created = datetime(2023, 9, 6)
    )

    song_7 = Songs (
        user_id = 1,
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+No+Such+Thing.mp3",
        title = "No Such Thing",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Queen+of+California.mp3",
        title = "Queen of California",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Say.mp3",
        title = "Say",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Still+Feel+Like+Your+Man.mp3",
        title = "Still Feel Like Your Man",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Waiting+On+the+World+to+Change.mp3",
        title = "Waiting On the World to Change",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Wildfire.mp3",
        title = "Wildfire",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+XO.mp3",
        title = "XO",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Dear+Marie.mp3",
        title = "Dear Marie",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Emoji+of+a+Wave.mp3",
        title = "Emoji of a Wave",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+Tony+Bennett%2C+John+Mayer+-+One+for+My+Baby+(And+One+More+for+the+Road).mp3",
        title = "One for My Baby (And One More for the Road)",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Shouldn't+Matter+but+It+Does.mp3",
        title = "Shouldn't Matter but It Does",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+The+Age+of+Worry.mp3",
        title = "The Age of Worry",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/02+-+John+Mayer+-+Why+Georgia.mp3",
        title = "Why Georgia",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/03+-+John+Mayer+-+Half+of+My+Heart.mp3",
        title = "Half of My Heart",
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
        album_id = 5,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/02+-+Ed+Sheeran+-+Castle+on+the+Hill.mp3",
        title = "Castle on the Hill",
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
        album_id = 5,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/04+-+Ed+Sheeran+-+Shape+of+You.mp3",
        title = "Shape of You",
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
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/05+-+Ed+Sheeran+-+Perfect.mp3",
        title = "Perfect",
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
        album_id = 5,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/06+-+Ed+Sheeran+-+Galway+Girl.mp3",
        title = "Galway Girl",
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
        album_id = 5,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/07+-+Ed+Sheeran+-+Happier.mp3",
        title = "Happier",
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
        album_id = 5,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/10+-+Ed+Sheeran+-+What+Do+I+Know.mp3",
        title = "What Do I Know",
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
        album_id = 5,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%C3%B7+(Deluxe)/11+-+Ed+Sheeran+-+How+Would+You+Feel+(Paean).mp3",
        title = "How Would You Feel (Paean)",
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
        album_id = 4,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%3D/02+-+Ed+Sheeran+-+Shivers.mp3",
        title = "Shivers",
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
        album_id = 4,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%3D/03+-+Ed+Sheeran+-+First+Times.mp3",
        title = "First Times",
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
        album_id = 4,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%3D/12+-+Ed+Sheeran+-+Visiting+Hours.mp3",
        title = "Visiting Hours",
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
        album_id = 3,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/03+-+Ed+Sheeran+-+Sing.mp3",
        title = "Sing",
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
        album_id = 3,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/03+-+Ed+Sheeran+-+Sing.mp3",
        title = "Don't",
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
        album_id = 3,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/06+-+Ed+Sheeran+-+Photograph.mp3",
        title = "Photograph",
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
        album_id = 3,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+x+(Deluxe+Edition)/11+-+Ed+Sheeran+-+Thinking+out+Loud.mp3",
        title = "Thinking Out Loud",
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
        album_id = 2,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%2B/01+-+Ed+Sheeran+-+The+A+Team.mp3",
        title = "The A Team",
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
        album_id = 2,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/EdSheeranMp3/Ed+Sheeran+-+%2B/09+-+Ed+Sheeran+-+Lego+House.mp3",
        title = "Lego House",
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
        date_created = datetime(2023, 9, 6)
    )




    db.session.add_all([demo, marnie, bobbie])
    # 30 more if I want to access all of them, should probably split them up based on different playlists
    db.session.add_all([song_1, song_2, song_3, song_4, song_5, song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15, song_16, song_17, song_18, song_19, song_20, song_21, song_22, song_23, song_24, song_25, song_26, song_27, song_28, song_29, song_30, song_31, song_32, song_33, song_34, song_35, song_36])
    db.session.add_all([playlist_1])
    db.session.add_all([playlist_2])

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
        # db.session.execute(f"TRUNCATE table {SCHEMA}.album_likes RESTART IDENTITY CASCADE;")
        # db.session.execute(f"TRUNCATE table {SCHEMA}.song_likes RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")

    else:

        db.session.execute(text("DELETE FROM playlists"))
        db.session.execute(text("DELETE FROM songs"))
        db.session.execute(text("DELETE FROM albums"))
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()