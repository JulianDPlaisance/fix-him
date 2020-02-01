# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Mindy")
define bestie = Character("Ashleigh")


# The game starts here.

label start:

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
    f "Ash, meet my new man. He is totally not a Chad, his name is Dan"

    show crying friend at right
    play sound "audio/FemaleCrying.mp3"
    bestie "He is so broken & BEAUTFIUL!"

    # This ends the game.

    return
