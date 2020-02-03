# The script of the game goes in this file.

# declare characters used by this game. The color argument colorizes the
# name of the character.
define gui.choice_button_text_idle_color = '#0000FF'
define gui.idle_color = '#FFaa00'
define gui.choice_button_text_hover_color = '#33FF99'

define m = Character("Mindy", color="#0101aa")
define a = Character("Ashleigh", color="#10ff10")
define d = Character("Dan", color="#BF0101")
define j = Character("Principal Joe", color="#01d01d")
define p = Character("Student on Intercom", color="#fafafa")
default danPoints = 6
default ashleighPoints = 0
default basketball = False
default bidenPoints = 0


# The game starts here.

label start:

    play music "audio/Tune.mp3"
    jump Opening

label Opening:

    scene classroom
    "First day of School: August 13th."
    p "Mindy to the Principal's office."
    "Mindy gets up from her chair, wondering what Principal Joe wants this time."

    scene hall

    j "Good morning Mindy! How was your vacation?"
    m "It was nice, but I’m glad to be back. Did you need my help with something?"
    j "Since you’re class president, I was hoping you could show a new student around the school. Try to make him feel welcome."
    j "Dan, come on in."

    show dan abom at left

    d "..."
    m "Hi I'm min-did you just move in next door?"
    d "What?"
    m "I think I saw you moving in yesterday!  The blue house on Elm Street?"
    d "Oh yeah.  That's me."
    j "..."
    j "Alright Mindy, please show him around the school."
    m "Where are you from?"
    d "doesn’t matter."
    "Mindy was taken aback. What’s this kid’s problem? I’m just trying to help him out…"
    m "Let me show you around then. Here’s the bathroom and here’s the cafeteria."
    d "How’s the food?"
    # danpoints
    menu:
        "Ew! It’s disgusting!":
            $ danPoints -= 1
            jump continueOpening
        "It’s okay I guess.":
            jump continueOpening


label continueOpening:

d "Well, it’s probably better than at home."
m "Oh..."
m "...and here’s our class."
m "Do you have any questions?"
d "Nope. Thanks."

label ClassroomIntroducingashleigh:
    scene classroom
    a "Hey Mindy!"

    show ashleigh intrigued at right

    a "Who’s that hot guy you were with?"
    hide ashleigh intrigued
    show ashleigh shocked at left

    a "Where is he from?"
    a "Is he in our grade?"
    a "doyoureallythinkhelikesthecafeteriafood?"
    hide ashleigh shocked
    show ashleigh intrigued at right

    a "Tell. me. Everything."
    "Typical ashleigh. I’ve known her forever and of course she would ask me about any guy she saw me with."
    m "His name is Dan. He’s new here and apparently he’s my neighbor."
    a "O.M.G. he moved in right next to you? That’s just like a movie!"
    a "So what do you think? do you like him?"

menu:
    "I’ve only talked to him once, ashleigh.":
        jump continuedAshleigh
    "I dunno - he seems okay I guess.":
        jump continuedAshleigh


label continuedAshleigh:
    hide ashleigh intrigued
    show ashleigh apathetic at center
    a "Ugh...this is why you’ve never had a boyfriend."
    hide ashleigh apathetic
    show ashleigh open arms at center
    a "Well, since you’re neighbors and all...why don’t you ask him to walk to school with you tomorrow? Maybe you can get to know him a little more?"

    menu: #ashpoints
        "That’s actually a good idea. I’ll try that.":
            $ ashleighPoints += 1
            jump idea
        "I guess it’s not like he has any other friends. Sure, why not?":
            $ ashleighPoints -= 1
            jump idea

    label idea:
    hide ashleigh open arms
    show ashleigh shocked at right
    a "I can’t believe you finally listened to me! Good luck!"
    hide ashleigh shocked
    jump Outroashleigh

    label friends:
hide ashleigh open arms
show ashleigh open arms at right
a "That’s my girl. Go get him!"
hide ashleigh open arms
jump Outroashleigh

label Outroashleigh:

"Well. I guess I’m walking him to school tomorrow."
show Blackscreen
"Ding-a-ling! Class is over! Go home you!"

label WalkingdanToClass:
    "September 2nd."
    scene Outside
    "Dan keeps refusing to walk to school with me.  But today is the day, determination will get me through!"

    show dan abom at left

    m "Hey Dan I noticed you haven’t joined a club yet.  I have a brochure, let’s walk and talk."
    d "..."
    d "..."
    d "...what kind of clubs?"
m "Well...there’s book club, crochet club, astronomy club - oh! There’s debate team. I’m captain of that one."
d "..."
"Maybe he doesn’t like the brainy ones. Let’s try sports."
m "We have football, swim team, ice hockey, basketball-"
d "Do you like sports?"

menu: #danpoints
    "Sometimes I watch basketball with my dad.":
        $ basketball = True
        jump basketball
    "That’s not really my thing.":
        $ danPoints -= 1
        jump thing

label basketball:
hide dan abom
show dan at left
d "Me too. It’s been hard to keep up lately with the move and all though."
jump ashleighSpring

label thing:
    d "Oh. Figures."
    jump ashleighSpring

label ashleighSpring:
show ashleigh shocked at center
a "OMG I cannot believe you two are together!"
"ashley… why…"
m "Oh, Dan, this is Ashleigh. We’ve been friends since elementary school."
hide dan
hide ashleigh shocked
show dan
d "Oh, hi. Mindy, I’ll see you around."
hide dan
show ashleigh open arms at right
a "So what were you two talking about? You two seemed pretty chummy."
"Mindy spills the details."
if basketball:
    m "He likes basketball. I guess we have that in common."
    m "He didn’t really say much"
    a "Homecoming’s coming up."
    a "You know, He doesn’t talk to anyone else but you. Why don’t you ask him to go to the dance with you?"
    "Man, Ashleigh is pushy recently."
hide ashleigh open arms
scene Blackscreen
p "Ding-a-ling! Get those asses in those classes!"


label Homecoming: # October 27th
scene partyclass
show dan at left
d "Hey, Mindy. Did you catch the season opening?"
m "Of course! That was such an upset. Did you see that bankshot? I had to stay up late to finish my chemistry homework because I couldn’t take my eyes off the game."
d "Bankshot? Talk about that last minute three! That’s so unlike you to stay up watching basketball Miss Class President."
m  "Speaking of staying up late...Homecoming is coming up soon."
"It is October 22nd, and homecoming is this weekend…"
d "Isn’t it this weekend?"

menu:
        "How about we continue this conversation at the dance?":
            jump danceballs
        "Yeah, I’m going with ashleigh. I know you hate those types of things.":
            jump BreakingBad

label BreakingBad:
    hide dan
    show dan abom at right

    d "Oh okay. I’m going with Jessica. I guess I’ll see you around the neighborhood."
    m "Okay, see you around."
hide dan abom
scene Blackscreen
"Mindy has fun at the homecoming dance and has a successful career. Dan eventually drops out of school, and Mindy loses contact with him."

".:. Early Ending."
return

label danceballs:
    d "Are you sure? I’m sure there’s plenty of people who would want to go with you..."
    m "Oh, I’m sure. You’re not getting out of it now."

    show dan at left

    d "...Sure, I’d like to."
    hide dan
    show Smilingdan at center
    "Wow...I’ve never seen him smile like that."
    scene Blackscreen
    p "Ding-a-ling! Homecoming Bonecoming!"
    hide Smilingdan


label LifeOnHolidays: # december 17th
    scene Outside
    "December 17th."
    show ashleigh shocked at right

    a "Oh My God, you have been glued to dan since homecoming. You’re practically inseparable."
    a "I can’t believe it’s the holidays already. Woo hoo!  We can hangout during the break"
    hide ashleigh shocked
    show ashleigh intrigued at center
    a "Tell me how you and Dan are celebrating. I want to live vicariously through you."
    m "Well, I was thinking we wou- Oh, hey dan."
    hide ashleigh intrigued
    show dan at left
    show ashleigh open arms at right
    d "Hey, you two. What are your plans for the holidays?"
    a "Well, I know Mindy has some plans for you."
    "Oh no, I have to shut her up. This is so embarrassing, ashleigh…"
    m "Oh, I have a lot of studying to do…"
    hide ashleigh open arms
    show ashleigh shocked at center
    a "Girl, could you be more boring? I’m going holiday shopping, and you’re coming with me."
    a "We’ll see you later, dan!"
    hide ashleigh shocked
scene Blackscreen
menu: #danpoints #ashleighpoints
        "Buy a present for Ashleigh.":
            $ ashleighPoints += 1
            jump ashleighPresent
        "Buy a present for Dan.":
            $ ashleighPoints -= 1
            $ danPoints += 1
            jump danPresent
        "Buy a present for Both.":
            $ ashleighPoints += 1
            $ danPoints += 1
            jump BothPresents

label ashleighPresent:
scene outside
show ashleigh shocked at center
a "Oh. my. GOd. I saw you buy that, and I was SO hoping it was for me."
hide ashleigh shocked
scene Blackscreen
p "Ring-a-ding! Ring-a-ding! Ring-a-ding! Ring-a-ding! Ring-a-ding! 5 Golden Rings!"
jump Valentines

label danPresent:
scene outside
show dan at center
d "Oh. You didn’t have to do that. Thanks."
hide dan
scene Blackscreen
p "Ring-a-ding! Ring-a-ding! Ring-a-ding! Ring-a-ding! Ring-a-ding! 5 Golden Rings!"
jump Valentines

label BothPresents:
scene outside
show Smilingdan at left
show ashleigh shocked at right
d "Oh. You didn’t have to do that. Thanks."
a "Oh. my. GOd. I saw you buy that, and I was SO hoping it was for me."
hide Smilingdan
hide ashleigh shocked
scene Blackscreen
p "Ring-a-ding! Ring-a-ding! Ring-a-ding! Ring-a-ding! Ring-a-ding! 5 Golden Rings!"
jump Valentines

label Valentines: # February 14th
    "February 13th. One day before Valentine’s day."
scene hall
"Oh god, it’s almost Valentine’s day. What should I do?"
m "I’ve heard that making your own chocolates is better than buying them."
m "Can’t be that difficult, I’m class president after all"
"BOOm…CRaSH....BURN"
m "...oh no…"
m "I have to clean this up now. at least the chocolates are done. I think they’re safe enough to eat...technically."
"Who should I give these to?"
menu:
    "Give chocolate to Ashleigh.":
        jump ashleighChocolate
    "Give chocolate to Dan.":
        jump danChocolate

label ashleighChocolate:
"February 14th.  Valentine's day"
show ashleigh intrigued at left
m "Here, Ashleigh. I know this is kind of out of the blue, but I made these for you."
a "Are you kidding me? Raspberry chocolates?? Oh, Mindy, you know me so well!"
a "Actually...I made some for you too. dark chocolate, of course. I know sweet isn’t your style."
hide ashleigh intrigued
show ashleigh shocked at center
a "Do you like them?"
hide ashleigh shocked
show ashleigh shocked at right
m "Honestly, I love them, but not as much as I love you. I hope that’s okay."
a "It’s more than okay."
hide ashleigh shocked
show ashleigh open arms at center
"Ashleigh winks at mindy. mindy smiles. She will never forget this moment."
p "Ding-a-ling! Kissing leads to dinging!"
scene Blackscreen
"Mindy pursues her dream of becoming a neurosurgeon, but her favorite part is that she does so with ashleigh at her side. Ashleigh stays with their two dogs, Butch and Dan 2.0. Every year they make chocolate for each other."

".:. Ashleigh Ending."
return


label danChocolate:
"February 14th.  Valentine's day"
show dan abom at left
"Dan should appreciate these, I hope."
m "Hey Dan, I hope you like chocolate. I made these for you."
hide dan abom
show dan at left
d "Wow, thank you. I tried to make some for you actually...but I accidentally burnt them. and our kitchen. "
m "Oh, Dan, so that’s what that alarm was. You know you can’t cook. I hope you didn’t get in trouble."
d "It’s not like my parents are around enough to notice that kind of thing."
d "But seriously, these are great. No one’s ever given me chocolate before."
m "maybe I’ll cook more for you sometime."
hide dan
scene Blackscreen
p "Ding-a-ling! Kissing leads to dinging!"

label BigTest: #march 28th
    "march 28th."
    scene classroom
    show dan at left
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
        "What do you mean?":
            jump errands
        "Not enough...":
            $ danPoints -= 1
            jump danLife

label danLife:
hide dan
show dan abom at left
d "What do you mean 'not enough?'"
m "I feel like I could do more."
d "But you’ve already done so much for me."
m "There’s still a little time before graduation."
"He has no idea how great he can be."
hide dan abom
jump Why

label errands:
m "All I do right now is study and run errands for the principal."
d "Mindy, you’re constantly helping people. Hell, you’re still here with me after all this time."
m "I never thought of it as a chore."
m "You know, you’re actually a great listener. You might make a good therapist one day."
d "Well, actually, I was thinking of being a therapist one day. I know it’s silly, but…"
m "It’s not silly at all."
"He’ll definitely become a great therapist one day. He’s certainly got the patience for it."
hide dan
jump Why

label Why: #april 1st
    "April 1st."
scene hall
m "...and then, ashleigh asked me to go to Jake’s party. I keep telling her I don’t want to go. Every time she drinks she clings to me and then pukes."
m "I’m always the designated driver. It get so annoy-"
show dan abom at center
d "Mindy, why are you with me?"
menu: #danpoint
    "Is this a prank?":
        $ bidenPoints += 1
        if bidenPoints < 5:
            jump Why #why
        else:
            jump BidenSecret
    "What do you mean?":

        jump meaning
    "are you sure you want to know?":
        $ danPoints -= 1
        jump Knowledge
label meaning:
    hide dan abom
    show dan abom at left
d "You’re going to college. You know what you’re going to do with your life. I’m nothing to you."
m "You’re something to me. Yes, I’m going to college, but I care about you, Dan."
hide dan abom
show dan at center
d "I feel like this can’t last. I can’t keep up with you."
m "I like you exactly as you are."
"Like..? Is it more than that?"
#if
jump ashleighFinal

label Knowledge:
d "Just give it to me straight, Mindy."
m "Fine...When I first saw you I knew you were broken."
d "Broken?"
m "You think I didn’t notice the comment about the cafeteria food, dan? I can hear your parents arguing every night. I wanted to help you...fix you."
d "Fix me? FIX mE? What am I, some broken toy?"
m "Dan, I-"
hide dan abom
d "I’m not some plaything."
m "Dan…"
"I watched him walk away. He started avoiding me at school."
#    if
#jump
label ashleighFinal:
if ashleighPoints>0:
    jump ashleighSupportive
else:
    jump ashleighCatty

label ashleighSupportive:
    scene Outside
    "May 5th."
    show ashleigh open arms at right
a "Oh. my. God. I cannot believe we are finally in our last week of school."
m "Me either! What a long strange journey it’s been."
a "You’re leaving me so soon! I don’t know what I’m going to do without you."
m "I’m so so sorry about that. You know it’s always been my dream and girl, you have to follow your dream."
hide ashleigh open arms
show ashleigh sobbing at center
a "I know… it just hurts."
a "Will I see you at the graduation party?"
menu:
    "Wouldn’t miss it for the world.":
        jump ashsupportcont
    "Sure! See you there?":
        jump ashsupportcont

label ashsupportcont:
    hide ashleigh sobbing
    show ashleigh shocked at left
    a "See if dan will dance with you again like he did at Homecoming."
    m "I think we both know how that’ll go."
    "Ding-a-ling! This job doesn’t pay enough."
    hide ashleigh shocked
    jump Party

label ashleighCatty:
    scene Outside
    "may 5th."
    show ashleigh apathetic at right
a "Oh. my. God. I cannot believe we are finally in our last week of school."
m "Me either! What a long strange journey it’s been."
a "You’re leaving me so soon! I don’t know what I’m going to do without you."
m "I’m so so sorry about that. You know it’s always been my dream and girl, you have to follow your dream."
hide ashleigh apathetic
show ashleigh intrigued at center
a "I know… it just hurts."
a "Will I see you at the graduation party?"
menu:
    "Wouldn’t miss it for the world.":
        jump cattycontinue
    "Sure! See you there?":
        jump cattycontinue

label cattycontinue:
hide ashleigh intrigued
show ashleigh apathetic at left
a "See if dan will dance with you again like he did at Homecoming."
m "I think we both know how that’ll go."
"Ding-a-ling! This job doesn’t pay enough."
hide ashleigh apathetic
jump Party

label Party: #may 20th
    scene classroom
    show dan at center
    d "I can’t believe I’m actually looking forward to a party."
    m "Me either. Ever since I finished my college applications, I’ve felt like I was on the moon. I hope we both get in"
    d "You’ll get in for sure. You deserve it. I’m still waiting for mine too, but I have a good feeling about this one."
    d "We’ll get in together, I’m sure of it."

    menu:
        "So...how did the big talk go?":
            jump party11
        "I hope it didn’t get lost in the post. I’m sure it’s fine though.":
            jump party11

label party11:
    d "Oh, I talked with my parents. I think I got through to my mom, but my dad might take more work."
    d "If I’m being honest, I don’t know if I can get through to him anytime soon."
    d "do you think it’s worth pursuing?"
    menu:
        "You can do anything, dan. If you keep talking to him, he’s bound to listen at some point.":
            $ danPoints -= 1
            jump party12
        "You’ll be out of that house before you know it. You have so many awesome things to look forward to with or without him.":
            jump party12

label party12:
    d "You always know just what to say."
    m "It’s a talent of mine."
    d "Do you think we’ll keep in touch?"
    menu:
        "Anything could happen.":
            jump party13
        "I’m here whenever you need me. ":
            jump party13

label party13:
    show Blackscreen
"Dan and Mindy leave the classroom for the last time, ready to receive their diplomas. The after party is held at ashleigh’s house later that night."

p "Ding-a-ling! Ring my bell tonight at the party!!!"


label Ending:
    scene partyclass
    "The party is booming in Ashleigh’s backyard. There’s dancing, booze, and plenty of food to keep the recent graduates busy."
    "If anyone was born to throw a wild party, it’s Ashleigh. Mindy spots her near the pool and decides to say hello."

    if danPoints == 1:
        jump WorstEnding
    elif danPoints == 6:
        jump BestEnding
    elif danPoints > 4:
        jump GoodEnding
    elif danPoints < 4:
        jump BadEnding
    elif danPoints == 4:
        jump SecretEnding


label BadEnding:
    "Mindy starts toward Ashleigh, but when Dan enters the backyard, Mindy immediately changes her path to talk to him first."
    m "Dan! I’m glad we made it through that long ceremony."
    m "I thought Principal Joe would drone on for forever!"
    "But something was wrong. Dan wasn’t smiling back."
    show dan abom at left
    d "Mindy, we need to talk."
    m "Talk? I just wanted to have fun tonight. This is supposed to be the night we go crazy before college!"
    m "What’s that serious face for?"
    m "Has something happened?"
    d "Mindy…"
    d "I didn’t get into college."
    d "I know that might disappoint you..."
    "Mindy was lost for words"
    m "…"
    d "Mindy?"
    m "I thought I had fixed you…helped you enough to get your foot in the door."
    d "What do you mean by that? You mean like college?"
    m "That was the whole idea. I fix you, make you a perfect boyfriend, and I get to keep you forever!"
    m "We would go to the same college, get married, and grow old together! But you messed it all up!"
    d "What the fuck?!"
    d "That’s so messed up! Keep me forever? That’s stalker talk, Mindy!"
    m "I know how it might sound, but I just… I care about you so much."
    m "I wanted you to succeed so badly, but you just didn’t live up to my expectations."
    d "Fuck you and your obsession with perfection, Mindy! I gave you everything I had! What more could I have done!?"
    d "Fuck this- I don’t need college, and I don’t need you!"
    hide dan abom
    "Dan turns his back on Mindy, walking out the door and back home."
    scene Blackscreen
    "After their argument, Dan avoids Mindy until she leaves for college. She drops out after obtaining her first C her sophomore year. The pressure to be perfect was just too much..."
    ".:. Bad Ending."
    return



return

label WorstEnding:
    "Mindy starts toward Ashleigh, but when Dan enters the backyard, Mindy immediately changes her path to talk to him first."
    m "Dan! I’m glad we made it through that long ceremony."
    m "I thought Principal Joe would drone on for forever!"
    "But something was wrong. Dan wasn’t smiling back."
    show dan abom at right
    d "Mindy, we need to talk."
    m "Talk? I just wanted to have fun tonight. This is supposed to be the night we go crazy before college!"
    m "What’s that serious face for?"
    m "Has something happened?"
    d "Mindy…"
    d "I didn’t get into college."
    d "I know that might disappoint you..."
    "Mindy was lost for words"
    m "…"
    d "Mindy?"
    m "I thought I had fixed you…helped you enough to get your foot in the door."
    d "What do you mean by that? You mean like college?"
    m "That was the whole idea. I fix you, make you a perfect boyfriend, and I get to keep you forever!"
    m "We would go to the same college, get married, and grow old together! But you messed it all up!"
    d "What the fuck?!"
    d "That’s so messed up! Keep me forever? That’s stalker talk, Mindy!"
    m "I know how it might sound, but I just… I care about you so much."
    m "I wanted you to succeed so badly, but you just didn’t live up to my expectations."
    d "Fuck you and your obsession with perfection, Mindy! I gave you everything I had! What more could I have done!?"
    d "Fuck this- I don’t need college, and I don’t need you!"
    hide dan abom
    "Dan turns his back on Mindy, walking out the door and back home."
    scene Blackscreen
    "After their argument, Mindy can’t help but chug the drink in her hand. That night became a blur of music, booze, dancing and more booze. She gets into a car...flashing lights...it- everything hurts…"
    "It hurts so much... "
    show ashleigh sobbing at right
    show dan abom at left
    a "I can’t believe she’s gone...I can’t-"
    d "..."
    hide ashleigh sobbing
    hide dan abom
    ".:. Worst Ending."
    return

label GoodEnding:
"Mindy arrives at the graduation party and tries to find Ashleigh. She starts walking towards the kitchen, but she spots Dan on the way and decides to speak with him first."
m "Dan! I’m so glad we made it on time after that long ceremony. I thought principal Joe would never stop talking!"
show Smilingdan at center
d "Me too! Ashleigh sure knows how to throw a sick party, doesn’t she?"
"The party is kicking around them as other graduates drink and dance to the loud music booming throughout the house."
"Both Mindy and Dan raise their voices to hear each other over the noise."
m "Ashleigh’s parties are always killer! She should major in event planning at college!"
m "Speaking of college, how did sending in your application go? Has the reply come in the mail yet?"
d "Oh, it came back, but...I didn’t get in. But it’s not too bad! I think I’ll stay in town and go to the local community college."
"Mindy, knowing his situation, is glad he is still pursuing his goals and isn’t crushed by the rejection."
"But, Mindy had received her acceptance letter. She was hoping that she and Dan could have gone there together."
"She knows what’s coming, but doesn’t know how to phrase it…"
d "Hey, Mindy. It’s okay. I know.."
"Dan must have noticed her worrying. He reaches over to put a hand on her shoulder, not sure if she’d accept a hug."
d "But let’s have one more great night together with all our friends! Plus we can still see each other over the summer. I’d love to listen to the woes of college life and stories of new friends."
"Mindy sniffles, feeling the sting of tears in her eyes that she chokes down. She pulls him down for a hug."
m "Dan, you really are great. Thank you so much...for everything. This year wouldn’t have been the same if you hadn’t been in it."
"Dan lightly squeezes Mindy then lets go. They smile at each other, content in their decision to part ways. As they begin to talk more about the coming months, Ashleigh shows up, beer in hand."
show ashleigh shocked at right
a "Hey guys! Don’t think I didn’t see that hug! Bring it in!"
hide ashleigh shocked
show ashleigh open arms at left
"They all group hug and Ashleigh laughs."
hide ashleigh open arms
show ashleigh intrigued at right
a "Let’s all live it up tonight!"
d "Yeah!"
m "Yeah!"
hide Smilingdan
hide ashley intrigued
scene Blackscreen
"Mindy and Dan enjoy their last night as a couple having fun, dancing with Ashleigh, and enjoying each other's company."
"They had a night that even 20 years from now they can look back on as a night they can never forget. That night was the culmination of a year together that had made a difference in both their lives."

".:. Good Ending."
return

label BestEnding:
    "By the time Mindy gets to Ashleigh’s house, the graduation party is well underway. Loud music blares from inside and everyone is dancing and having a good time. Mindy enters the house and starts walking toward Ashleigh, who is in the kitchen, but a gentle tap on the shoulder stops her in her tracks."
show Smilingdan at center
d "Hey, you finally made it!"
m "I would have been here earlier if the traffic wasn’t so bad, but I’m here now so it doesn’t matter. Let’s party!"
d "I’m so glad I got here before that crash blocked the roads!"
"Dan holds up his drink in a toast and hands a filled cup to Mindy."
"Cheers for the college students!"
"Mindy goes to take a sip but stops suddenly, looking at Dan with wide eyes."
m "...Does that mean what I think it means?"
"She watches as Dan’s smile gets even wider."
hide Smilingdan
show dan awkward at center
d "I got in!!"
m "Oh my god! Why didn’t you tell me sooner!? I’m so proud of you!!!"
d "I wanted it to be a surprise!"
"Mindy and Dan, excited to be going to the same college together, toast their drinks."
"Just as Mindy starts heading towards the kitchen for a refill she hears her name being shouted over the music."
show ashleigh shocked at right
"Ashleigh looks a little tipsy but seems to be standing well enough."
a "I’m so glad I found you! I’ve been looking around foreeeever!"
m "Oh. My. God. Ashleigh you won’t believe it!"
a "What is it?!"
d "Dan and I got into the same college!"
a "I am so happy for both of you! Now you can finally pursue your dream! AND you get to have a boyfriend?? I’m so jealous!"
m "Ashleigh..."
a "Oh don’t worry about me, I’ll be fine! We can worry about the future tomorrow. Let’s all live it up tonight!"
m "Yeah, let’s have a good time tonight!"
d "Yeah, let’s dance!"
hide ashleigh shocked
scene Blackscreen
"After going through the ups and downs of college and grad school together, Mindy and Dan got married. Spending those years together, helping to fix and bolster each other, strengthened their resolve and they decided that it was time to help fix others. Dan eventually became a therapist for troubled youths while Mindy became a neurosurgeon."
hide dan awkward
".:. Best Ending."
return

label SecretEnding:
    "Mindy finally arrives at the party after a long wait in traffic. As she approaches the house she spots Dan in the front yard. Making her way over, Mindy realizes that her boyfriend’s attention was already occupied by someone else."
    m "Hey, Dan- oh..."
    "I guess I’ll come back later... Wait. Is that Ashleigh?"
    "Mindy watches as the person Dan was talking to is revealed to be Ashleigh. He spots Mindy and walks over to her, Ashleigh in tow, but something about him seems off."
    "Wait… what?!"
    show ashleigh dan at center
    d "It’s about time you showed up."
    "What’s with that annoyed tone? And what is Ashleigh doing hanging all over Dan!?"
    a "Oh, hey Mindy."
    "Mindy wants to slap the shit-eating grin off Ashleigh’s face right now."
    a "Isn’t he just the cutest?"
    d "Not as cute as you, Ash."
    "Ashleigh giggles and squeezes Dan’s arm tighter, her pointed gaze boring directly into Mindy’s."
    a "You’re too much, babe! I hope you’re not drunk when you say that."
    d "The only drug I need is you, Ash. You make me feel like flying high all the time."
    "Dan leans in and gives Ashleigh a kiss for good measure. Mindy looks on, horrified at the realization that Ashleigh and Dan are an item."
    a "So yeah, Mindy. This is how it is. Sorry, but we got close over the break and well...you know these things tend to happen."
    "It was clear that Ashleigh had planned on stealing Dan if not from the start of the year, by sometime between then and graduation."
    "Dan grunts and whispers something into Ashleigh’s ear. Ash laughs and smiles at Mindy with a positively evil grin on her face."
    a "I wasn’t gonna spill the beans, but Dan wants full disclosure... We’ve been sleeping together for the past month, you know."
    a "You tried so hard for so long. Sorry he slipped through your fingers but I could tell you didn’t actually love him like I do."
    a "You just wanted a cookie-cutter boyfriend. You weren’t interested in HIM at all! Well, now I have him."
    a "Better luck next time..."
    scene Blackscreen
    "After storming out of the party, Mindy never spoke to Dan or Ashleigh ever again. She couldn't even stand to look at them. After all she had done for them? She had fixed Ashleigh years ago, or so she had thought... and she wasted a whole year trying to fix Dan."
    "Mindy went to college and eventually became a teacher. She always retells that story to her classes."
    m "Never- and I repeat! NEVER get into a relationship trying to fix someone...I learned that the hard way."
    ".:. Secret Ending."
    return



label BidenSecret:

    scene classroom
    show joe
    "Enter Principal Biden."
    j "Hello kids."
    j "You know poor kids can be just as skilled and talented as white kids."
    "Joe Biden creeps closer."
    "He leans in to sniff your hair."
    j "ahhhh…."
    j "You know a thug walked up to me when I was your age.  I called him corn pop, then apologized for being racist, but told him I would beat him in a push-up contest."
    m "Joe… I always wanted to fix him. I just didn’t realize him means you."

    return
