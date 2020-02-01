# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Mindy")
define a = Character("Ashleigh")


# The game starts here.

label start:
    jump classroomIntroducingAshleigh

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hall

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show couple happy at left

    # These display lines of dialogue.
    play sound "audio/FemaleGasp.mp3"
    a "Ash, meet my new man. He is totally not a Chad, his name is Dan"

    show crying friend at right
    play sound "audio/FemaleCrying.mp3"
    a "He is so broken & BEAUTFIUL!"

label classroomIntroducingAshleigh:

    scene classroom

    show ashleigh open arms at left
    a "Hey, Mindy"

    show ashleigh shocked at right with dissolve
    a "Who is the beefcake?"

    show ashleigh intrigued at left
    a "Where is he from?"
    a "Is he in our grade?"
    a "Doyoureallythinkhelikesthecafeteriafood?"


    # This ends the game.

    return
