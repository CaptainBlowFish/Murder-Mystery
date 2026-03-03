# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mel = Character("Mel Atonin")
define mike = Character("Mike Cull")
# The game starts here.

label start:

    scene bg room

    show Mel Atonin Neutral
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
    
    default looked_at_chalk_outline = False
    default looked_at_knife = False
    defualt park_open = False
    
    call crime_scene(looked_at_chalk_outline, looked_at_knife)
    # This ends the game.
    return

label crime_scene(looked_at_chalk_outline, looked_at_knife):
    
    menu:
        "Look at Chalk Outline":
            $ looked_at_chalk_outline = True
            show Mel Atonin Neutral
            mel "So this is where Tessa died-"
            mel "Hm? There seems to be something written here."
            show Jen Estra Name Blood
            mel "Jen's name is written in blood here."

            show Mike Cull Neutral
            mike "The blood is the victim's, and there was blood found on the victim's right index finger."
            mike "This is undeniably the victim's dying message."

            narrator "Dying Message was added to the Evidence Folder."

        "Look at Knife":
            $ looked_at_knife = True
            show Mel Atonin Neutral
            mel "Is this the murder weapon?"

            show Mike Cull Neutral
            mike "Yep. The blade matches the wound, and the handle has the suspect's fingerprints- no one else's."

            narrator "Knife was added to the Evidence Folder"


    if looked_at_chalk_outline and looked_at_knife:
        show Mel Atonin Neutral
        mel "There doesn't seem to be much here, but it all seems pretty concrete."
        mel "Were there any witnesses?"
        
        show Mike Cull Neutral
        mike "Actually, yeah. The one who called it in was Pops ... Officer Ickle."
        mike "He saw the suspect leaving the scene with the body behind her."
        mike "He chased the suspect to the park, where he then arrested her."
        mike "Last I heard, he was still over there."

        if not park_open:
            $ park_open = True
            narrator "New location 'PARK' unlocked"
        
        return
    else:
        call crime_scene(looked_at_chalk_outline, looked_at_knife)
    