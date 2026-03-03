# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mel = Character("Mel Atonin")
define mike = Character("Mike Cull")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Mel Atonin Neutral

    # These display lines of dialogue.

    mel "My name is Mel. I work as a detective in Old Bay City."
    mel "While not as big as it used to be, crime still runs rampant here."
    mel "It's my job as a detective to try to bring some semblance of peace to the people of this town, even if they don't seem to respect me as a person…"
    mel "This new case that I've gotten, though…"
    show Mel Atonin Worried
    mel "I have a bad feeling about it."

    scene Alley

    narrator "Februrary 19, 20XX, 2:27pm."
    
    show Mike Cull Excited
    mike "Hey, Mel! Er, sorry, Detective Atonin."

    narrator "This is Mike Cull, an old friend of Mel's from high school and a fellow detective on the force."

    show Mel Atonin Relaxed
    mel "No worries, Detective Cull."
    show Mel Altonin Interested
    mel "Can you give me an overview of what happened here?"

    show Mike Cull Neutral
    mike "Sure! The victim is Tessa Tarone, age 29, previously arrested and convicted on charges of armed robbery alongside her partner."
    mike "The victim died just this morning."
    mike "The cause of death was a single stab wound to the back."
    mike "Our current suspect is the victim's partner, Jen Estra, age 27. "

    narrator "Autopsy Report was added to the Evidence Folder."

    show Mel Atonin Confused
    mel "It seems pretty cut-and-dry from what you're saying. Why'd you ask to bring me on, then?"

    show Mike Cull Worried
    mike "Well, I'm struggling to put together a motive for the suspect, and was hoping you could help establish one."

    show Mel Atonin Determined
    mel "Alright, let's get to investigating."
    
    # This ends the game.
    return
