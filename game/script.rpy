# The script of the game goes in this file.

# declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("mindy")
define a = Character("ashleigh")
define d = Character("dan")
define j = Character("Principal Joe")
define p = Character("megaphone")
default danPoints = 0
default ashleighPoints = 0

# The game starts here.

label start:

    play music "audio/Tune.mp3"
    jump Opening

label Opening:

    scene classroom
    "First day of School: august 13th"
    p "mindy to the Principal's office"
    "mindy gets up from her chair, wondering what Principal Joe wants this time."

    scene hallway
    #show Joe

    j "Good morning mindy!  How was your vacation?"
    m "It was nice, but I'm glad to be back.  did you need my help with something?"
    j "Since you're class president, I was hoping you could show a new student around the school."
    j "Try to make him feel welcome."
    j "dan, come on in."

    #show abominationdan

    d "..."
    m "Hi I'm min-did you just move in next door?"
    d "What?"
    m "I think I saw you moving in yesterday!  The blue house on Elm Street?"
    d "Oh yhea.  That's me."
    j "..."
    j "alright mindy, please show him around the school."
    m "Where are you from?"
    d "doesn’t matter."
    "mindy was taken aback. What’s this kid’s problem? I’m just trying to help him out…"
    m "Let me show you around then. Here’s the bathroom and here’s the cafeteria."
    d "How’s the food?"
    # danpoints
    menu:
        "Ew! It’s disgusting!":
            jump continueOpening
        "It’s okay I guess.":
            jump continueOpening


label continueOpening:

d "Well, it’s probably better than at home."
m "Oh..."
m "and here’s our class."
m "do you have any questions?"
d "Nope. Thanks."

label ClassroomIntroducingashleigh:
    scene classroom
    a "Hey mindy!"

    show Happyashleigh

    a "Who’s that hot guy you were with?"

    show Heartashleigh

    a "Where is he from?"
    a "Is he in our grade?"
    a "doyoureallythinkhelikesthecafeteriafood?"

    show Happyashleigh

    a "Tell. me. Everything."
    "Typical ashleigh. I’ve known her forever and of course she would ask me about any guy she saw me with."
    m "His name is dan. He’s new here and apparently he’s my neighbor."
    a "OmG he moved in right next to you? That’s just like a movie!"
    a "So what do you think? do you like him?"

menu:
    "I’ve only talked to him once, ashleigh.":
        jump continuedAshleigh
    "I dunno - he seems okay I guess.":
        jump continuedAshleigh


label continuedAshleigh:
    show annoyedashleigh
    a "Ugh...this is why you’ve never had a boyfriend."

    show defaultashleigh
    a "Well, since you’re neighbors and all...why don’t you ask him to walk to school with you tomorrow? maybe you can get to know him a little more?"

    menu: #ashpoints
        "That’s actually a good idea. I’ll try that.":
            jump idea
        "I guess it’s not like he has any other friends. Sure, why not?":
            jump idea

    label idea:
    show Heartashleigh
    a "I can’t believe you finally listened to me! Good luck!"

    jump Outroashleigh

    label friends:
show Happyashleigh
a "That’s my girl. Go get him!"
jump Outroashleigh

label Outroashleigh:
"Well. I guess I’m walking him to school tomorrow."
show BlackScreen
"ding-a-ling! Class is over!"

label WalkingdanToClass:
    "September 2nd."
    scene Outside
    "dan keeps refusing to walk to school with me.  But today is the day, determination will get me through!"

    show abominationdan

    m "Hey dan I noticed you haven’t joined a club yet.  I have a brochure, let’s walk and talk."
    d "..."
    d "..."
    d "...what kind of clubs?"
m "Well...there’s book club, crochet club, astronomy club - oh! There’s debate team. I’m captain of that one."
d "..."
"maybe he doesn’t like the brainy ones. Let’s try sports."
m "We have football, swim team, ice hockey, basketball-"
d "do you like sports?"

menu: #danpoints
    "Sometimes I watch basketball with my dad.":
        $ basketball = true
        jump basketball
    "That’s not really my thing.":
        jump thing

label basketball:
show dan
d "me too. It’s been hard to keep up lately with the move and all though."
jump ashleighSprint

label thing:
d "Oh. Figures."

jump ashleighSpring

show Heartashleigh
a "OmG I cannot believe you two are together!"
"ashley… why…"
m "Oh, dan, this is ashleigh. We’ve been friends since elementary school."
show dan
d "Oh, hi. mindy, I’ll see you around."

show defaultashleigh
a "So what were you two talking about? You two seemed pretty chummy."
a "mindy spills the details."
if basketball:
    m "He likes basketball. I guess we have that in common."
    m "He didn’t really say much"
    a "Homecoming’s coming up."
    a "You know, He doesn’t talk to anyone else but you. Why don’t you ask him to go to the dance with you?"
    "man ashleigh is pushy recently"

scene BlackScreen
"ding-a-ling! Get those asses in those classes!"


label Homecoming: # October 27th
    scene Homecoming
show dan
d "Hey, mindy. did you catch the season opening?"
m "Of course! That was such an upset. did you see that bankshot? I had to stay up late to finish my chemistry homework because I couldn’t take my eyes off the game."
d "Bankshot? Talk about that last minute three! That’s so unlike you to stay up watching basketball miss Class President."
m  "Speaking of staying up late...Homecoming is coming up soon."
"It is October 22nd, and homecoming is this weekend…"
d "Isn’t it this weekend?"

menu:
        "How about we continue this conversation at the dance?":
            jump danceballs
        "Yeah, I’m going with ashleigh. I know you hate those types of things.":
            jump BreakingBad

label BreakingBad:
    show abominationdan

    d "Oh okay. I’m going with Jessica. I guess I’ll see you around the neighborhood."
m "Okay, see you around."

scene BlackScreen
"mindy has fun at the homecoming dance and has a successful career. dan eventually drops out of school, and mindy loses contact with him."
return

label danceballs:
    d "are you sure? I’m sure there’s plenty of people who would want to go with you..."
    m "Oh, I’m sure. You’re not getting out of it now."

    show dan

    d "...Sure, I’d like to."

    show Smilingdan
    "Wow...I’ve never seen him smile like that."
    scene BlackScreen
    "ding-a-ling! Homecoming Bonecoming!"



label LifeOnHolidays: # december 17th
    scene Outside
    "december 17th."
    show Heartashleigh

    a "Oh mY GOd, you have been glued to dan since homecoming. You’re practically inseparable."
    a "I can’t believe it’s the holidays already. Woo hoo!  We can hangout during the break"
    show Happyashleigh
    a "Tell me how you and dan are celebrating. I want to live vicariously through you."
    m "Well, I was thinking we wou- Oh, hey dan."
    show dan
    show Normalashleigh
    d "Hey, you two. What are your plans for the holidays?"
    a "Well, I know mindy has some plans for you."
    "Oh no, I have to shut her up. This is so embarrassing, ashleigh…"
    m "Oh, I have a lot of studying to do…"
    a "Girl, could you be more boring? I’m going holiday shopping, and you’re coming with me."
    show Heartashleigh
a "We’ll see you later, dan!"

scene BlackScreen
menu: #danpoints #ashleighpoints
        "Buy a present for ashleigh.":
            jump ashleighPresent
        "Buy a present for dan.":
            jump danPresent
        "Buy a present for Both.":
            jump BothPresents

label ashleighPresent:
scene outside
show Heartashleigh
a "Oh. my. GOd. I saw you buy that, and I was SO hoping it was for me."
scene BlackScreen
"Ring-a-ding! 5 Golden Rings!"
jump Valentines

label danPresent:
scene outside
show dan
d "Oh. You didn’t have to do that. Thanks."
scene BlackScreen
"Ring-a-ding! 5 Golden Rings!"
jump Valentines

label BothPresents:
scene outside
show Smilingdan
show Heartashleigh
d "Oh. You didn’t have to do that. Thanks."
a "Oh. my. GOd. I saw you buy that, and I was SO hoping it was for me."
scene BlackScreen
"Ring-a-ding! 5 Golden Rings!"
jump Valentines

label Valentines: # February 14th
    "February 13th. One day before Valentine’s day."
scene Hallway
"Oh god, it’s almost Valentine’s day, what should I do?"
m "I’ve heard that making your own chocolates is better than buying them."
m "Can’t be that difficult, I’m class president after all"
"BOOm…CRaSH....BURN"
m "...oh no…"
m "I have to clean this up now. at least the chocolates are done. I think they’re safe enough to eat...technically."
"Who should I give these to?"
    menu:
        "Give chocolate to ashleigh.":
            jump ashleighChocolate
        "Give chocolate to dan.":
            jump danChocolate

    label ashleighChocolate
    show Happyashleigh
    m "Here, ashleigh. I know this is kind of out of the blue, but I made these for you."
    a "are you kidding me? Raspberry chocolates?? Oh, mindy, you know me so well!"
    a "actually...I made some for you too. dark chocolate, of course. I know sweet isn’t your style."
    show Heartashleigh
    a "do you like them?"
    m "Honestly, I love them, but not as much as I love you. I hope that’s okay."
    a "It’s more than okay."
    "ashleigh winks at mindy. mindy smiles. She will never forget this moment."
    scene BlackScreen
#    mindy pursues her dream of becoming a neurosurgeon, but her favorite part is that she does so with ashleigh at her side. ashleigh stays with their two dogs, Butch and dan 2.0. Every year they make chocolate for each other.



    label danChocolate
    show abominationdan
    "dan should appreciate these, I hope."
    m "Hey dan, I hope you like chocolate. I made these for you."
    show dan
    d "Wow, thank you. I tried to make some for you actually...but I accidentally burnt them. and our kitchen. "
    m "Oh, dan, so that’s what that alarm was. You know you can’t cook. I hope you didn’t get in trouble."
    d "It’s not like my parents are around enough to notice that kind of thing."
d "But seriously, these are great. No one’s ever given me chocolate before."
m "maybe I’ll cook more for you sometime."
    scene BlackScreen
    "ding-a-ling! Kissing leads to dinging!"

label BigTest #march 28th
    "march 28th."
    scene Classroom
    show dan
    d "Hey, how do you feel about the big test coming up?"
    m "I’ll be fine of course. But do you want to study together beforehand?"
    d "are you sure? Somehow I doubt we’re at the same level."
    m "I can get you up to speed. don’t worry about it."
    d "Oh cool. Thanks!"
    "He sure did need the help."
    d "I think you’d make a great teacher. Isn’t that what you wanted to go to college for?"
    m "It’s been a dream of mine for awhile. I just think I could really make a difference, you know?"
    d "Well, you’ve already made a difference in one life."
        menu: #danpoints
         "What do you mean?" :
            jump errands
         "Not enough..." :
            jump danLife

label danLife
show abominationdan
d "What do you mean "not enough?"
m "I feel like I could do more."
d "But you’ve already done so much for me."
m "There’s still a little time before graduation."
"He has no idea how great he can be."

        label Errands
        m "all I do right now is study and run errands for the principal.
        d "mindy, you’re constantly helping people. Hell, you’re still here with me after all this time."
        m "I never thought of it as a chore."
        m "You know, you’re actually a great listener. You might make a good therapist one day."
        d "Well, actually, I was thinking of being a therapist one day. I know it’s silly, but…"
        m "It’s not silly at all."
        "He’ll definitely become a great therapist one day. He’s certainly got the patience for it."

label Why #april 1st
    "april 1st."
scene Hallway
    m "...and then, ashleigh asked me to go to Jake’s party. I keep telling her I don’t want to go. Every time she drinks she clings to me and then pukes."
    m "I’m always the designated driver. It get so annoy-"
    show abominationdan
    d "mindy, why are you with me?"
    menu: #danpoint
        m "Is this a prank?" :
            jump Why #why
        m "What do you mean?" :
            jump meaning
        m "are you sure you want to know?" :
            jump Knowledge
label meaning:
    show abominationdan
d "You’re going to college. You know what you’re going to do with your life. I’m nothing to you."
m "You’re something to me. Yes, I’m going to college, but I care about you, dan."
show dan
d "I feel like this can’t last. I can’t keep up with you."
m "I like you exactly as you are."
"Like..? Is it more than that?"
if
    jump ashleighFinal

label Knowledge:
d "Just give it to me straight, mindy."
m "Fine...When I first saw you I knew you were broken."
d "Broken?
m "You think I didn’t notice the comment about the cafeteria food, dan? I can hear your parents arguing every night. I wanted to help you...fix you."
d "Fix me? FIX mE? What am I, some broken toy?"
m "dan, I-"
d "I’m not some plaything."
m "dan…"
"I watched him walk away. He started avoiding me at school."
    if
jump

label ashleighSupportive
    scene Outside
    "may 5th."
    show defaultashleigh
a "Oh. my. God. I cannot believe we are finally in our last week of school."
    m "me either! What a long strange journey it’s been."
    a "You’re leaving me so soon! I don’t know what I’m going to do without you."
    m "I’m so so sorry about that. You know it’s always been my dream and girl, you have to follow your dream."
    show Cryingashleigh
    a "I know… it just hurts."
    a "Will I see you at the graduation party?
    menu:
        "Wouldn’t miss it for the world." :
         "Sure! See you there?":
    show Heartashleigh
    a "See if dan will dance with you again like he did at Homecoming."
    m "I think we both know how that’ll go."
    "ding-a-ling! This job doesn’t pay enough."

label ashleighCatty
    scene Outside
    "may 5th."
    show Normalashleigh
a "Oh. my. God. I cannot believe we are finally in our last week of school."
    m "me either! What a long strange journey it’s been."
    a "You’re leaving me so soon! I don’t know what I’m going to do without you."
    m "I’m so so sorry about that. You know it’s always been my dream and girl, you have to follow your dream."
    show annoyedashleigh
    a "I know… it just hurts."
    a "Will I see you at the graduation party?"
    menu:
        "Wouldn’t miss it for the world." :
         "Sure! See you there?":
    a "See if dan will dance with you again like he did at Homecoming."
    m "I think we both know how that’ll go."
    "ding-a-ling! This job doesn’t pay enough."

label Party #may 20th
    scene Classroom
    show dan
    d "I can’t believe I’m actually looking forward to a party."
    m "me either. Ever since I finished my college applications, I’ve felt like I was on the moon."
    d "You’ll get in for sure. You deserve it. I’m still waiting for mine too, but I have a good feeling about this one."
    menu:
        "So...how did the big talk go?":
        "I hope it didn’t get lost in the post. I’m sure it’s fine though.":
    d "Oh, I talked with my parents. I think I got through to my mom, but my dad might take more work."
    d "If I’m being honest, I don’t know if I can get through to him anytime soon."
    d "do you think it’s worth pursuing?"
    menu:
        "You can do anything, dan. If you keep talking to him, he’s bound to listen at some point.":
        "You’ll be out of that house before you know it. You have so many awesome things to look forward to with or without him.":
    d "You always know just what to say."
    m "It’s a talent of mine."
    d "do you think we’ll keep in touch?"
    menu:
        "anything could happen.":
        "I’m here whenever you need me. ":
    show BlackScreen
"dan and mindy leave the classroom for the last time, ready to receive their diplomas. The after party is held at ashleigh’s house later that night."

    "ding-a-ling!"


label Ending
    scene NightTime
    "The party is booming in ashleigh’s backyard. She always knew how to throw a good party. mindy"








label BidenSecret:

    scene Classroom
    "Enter Principal Biden."
    j "Hello kids."
    j "You know poor kids can be just as skilled and talented as white kids."
    "Joe Biden creeps closer."
    "He leans in to sniff your hair."
    j "ahhhh…."
    j "You know a thug walked up to me when I was your age.  I called him corn pop, then apologized for being racist, but told him I would beat him in a push-up contest."
    m "Joe… I always wanted to fix him. I just didn’t realize him means you."
