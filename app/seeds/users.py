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
        owner = "Demo",
        title = "This is John Mayer",
        date_created = datetime(2023, 9, 6)
    )

    playlist_2 = Playlists (
        user_id = 2,
        song_id = 1,
        owner = "Marnie",
        title = "This is John Mayer",
        date_created = datetime(2023, 9, 6)
    )
    
    song_1 = Songs (
        user_id = 1,
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/05+-+John+Mayer+-+Perfectly+Lonely.mp3",
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

    song_2 = Songs (
        user_id = 1,
        album_id = 1,
        audio_url = "https://soundify-audio-files.s3.us-west-1.amazonaws.com/This+Is+John+Mayer/01+-+John+Mayer+-+Heartbreak+Warfare.mp3",
        title = "Heartbreak Warfare",
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
        album_id = 1,
        audio_url = "https://file-examples.com/storage/fe235481fb64f1ca49a92b5/2017/11/file_example_MP3_5MG.mp3",
        title = "Test",
        lyrics = """
                I was born in the arms of imaginary friends
                        """,
        date_created = datetime(2023, 9, 6)
    )


    db.session.add_all([demo, marnie, bobbie])
    db.session.add_all([album_1])
    # 30 more if I want to access all of them, should probably split them up based on different playlists
    db.session.add_all([song_1, song_2, song_3, song_4, song_5, song_6, song_7, song_8, song_9, song_10, song_11, song_12, song_13, song_14, song_15, song_16, song_17, song_18, song_19, song_20, song_21])
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