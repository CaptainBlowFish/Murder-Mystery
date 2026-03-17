# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mel = Character("Mel Atonin")
define mike = Character("Mike Cull")
define pops = Character("Officer Ickle")

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
    
    $ looked_at_chalk_outline = False
    $ looked_at_knife = False
    
    $ park_open = False
    $ asked_what_you_saw = False
    $ asked_when_you_call_it_in = False
    
    $ pops_introduced = False

    $ police_station_open = False

    $ choosed_autopsy_report = False
    $ choosed_dying_message = False
    $ choosed_kife = False
    $ choosed_pops_testimony = False
    $ first_contradiction = False

    call crime_scene(looked_at_chalk_outline, looked_at_knife)

    call park(asked_what_you_saw, asked_when_you_call_it_in)

    call police_station()

    return

label crime_scene(looked_at_chalk_outline=False, looked_at_knife=False):
    scene Alley
    
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
    else:
        call crime_scene(looked_at_chalk_outline, looked_at_knife)
    
    return

label park(asked_what_you_saw=False, asked_when_you_call_it_in=False):
    scene park

    if not pops_introduced:
        $ pops_introduced = True   
        show Mel Atonin Interested
        mel "Would you happen to be Officer Ickle?"
        mel "Would you mind answering some questions for me?"

        show Pops Ickle Neutral
        pops "Sure thang, but you can just call me 'Pops.'"

        show Mel Atonin
        mel "Alright then, Pops."

    menu:
        "What did you see?":
            $ asked_what_you_saw = True
            show Pops Ickle Neutral
            pops "Well, Mike here asked me to patrol the area 'tween the park and station 'round 4:00am. Said he had a lead on some kinda case 'round 'ere or sumthin'."
            pops "When l got near the park, I saw that Jen lady standing over a woman's corpse in an alley."
            pops "I called out to 'er. She seemed pretty shaken, but when she saw me, she turned n' ran 'ere."
            pops "I caught 'er - arrested 'er on the spot, too. Can't be too sure she didn't get rid of nuttin' 'fore I caught 'er, though."
        
        "When did you call it in?":
            $ asked_when_you_call_it_in = True
            show Pops Ickle Neutral
            pops "I called it in as soon as I saw that Jen lady runnin'."
            pops "It was pretty early, prolly 'round 5 in tha mornin'."
    

    if asked_what_you_saw and asked_when_you_call_it_in:
        show Mel Atonin Neutral
        mel "(I feel like I should note this testimony for later)"
        narrator "Pops' Testimony was added to the Evidence Folder."
        mel "Well, there's not too much to build off of, but let's head back to the station and see what we can piece together based on what we have so far."
        
        if not police_station_open:
            $ police_station_open = True
            narrator "New location 'POLICE STATION' unlocked"
    else:
        call park(asked_what_you_saw, asked_when_you_call_it_in) 

    return

label police_station():
    scene Police Station
    mel "Let's see what I can piece together on the corkboard. Something about this doesn't feel right, but I'm not quite sure what for now."
    $ first_contradiction = False

    label .loop:
        call evidence_folder()
        if choosed_autopsy_report or choosed_pops_testimony:
            mel "Yeah, something is pretty off about this."
            mel "It's right in front of me..."
        else:
            mel "It doesen't seem like anything's off about this piece of evidence for now."
            jump .loop

    call discrepency()

    call discrepency2()

    return

label evidence_folder():
    scene Evidence Folder

    # I'm going to KILL myself if this doesn't work...
    $ choosed_autopsy_report = False
    $ choosed_dying_message = False
    $ choosed_kife = False
    $ choosed_pops_testimony = False

    menu:
        "Autopsy report":
            show Autopsy Report
            narrator "Autopsy Report"
            narrator "Name: Tessa Tarone"
            narrator "Cause of Death: Single stab wound to the back of ribs."
            narrator "Location of Death: Alley a block from the Park."
            narrator "Time of Death: Februrary 19, 20XX, ~3:00am."

            $ choosed_autopsy_report = True
        
        "Dying Message":
            show Dying Message
            narrator "The suspect's name is written in the victim's blood. The victim's blood was also found on her right index finger."

            $ choosed_dying_message = True

        "Knife":
            show Knife
            narrator "The knife useed to kill the victim. The same knie was used in an armed robbery a few years prior."
            narrator "... Shouldn't this still be in evidence?"

            $ choosed_kife = True

        "Pops' Testimony":
            show Testimony
            narrator "The suspect was seen at the scene of the crime around 5:00am before leaving to the park. Was asked to patrol the area by Detective Cull at around 4:00am."

            $ choosed_pops_testimony = True

    return 

label discrepency():
    label .loop:
        menu:
            "Time of Death":
                mel "According to the autopsy report, Tessa was killed at around 3:00am."
                mel "According to Officer Ickle's Testimony, Jen was at the scene at 5:00am."
                mel "What was Jen doing for that time? And does that call into question another piece of evidence?"
            "Cause of Death":
                mel "The cause of death seems right."
                jump .loop
            "Location of Death":
                mel "The Location seems right."
                jump .loop


    return

label discrepency2():
    label .loop:
        call evidence_folder()
        if choosed_autopsy_report:
            show Mel Atonin Neutral
            mel "I already know that is wrong"
            jump .loop
        elif choosed_dying_message:
            show Mel Atonin Confused
            mel "Wouldn't Jen have noticed either Tessa writing the dying message or the message itself?"
            mel "She apparently had 2 hours with the body. She could have hidden everything better."

            show Mike Cull Relaxed
            mike "Maybe it was panic? A dissociative or psychotic episode? Dosen't matter to me. All that matters is that the suspect still being there led to her being caught."

            show Mel Atonin Confused
            mel "No..."
            show Mel Atonin Worried 
            mel "That is what led to her being caught"
            jump .loop
        elif choosed_pops_testimony:
            show Mel Atonin Determined
            mel "You asked Officer Ickle to patrol the area of the murder!"
            mel "Tell me, Detective Cull, what was this case that was so important that an officer had to be deployed from the station to patrol?"

            show Mike Cull Excited
            mike "Let me be frank, Detective Jake Atonin- that's non eof your business."

            show Mel Atonin Sad
            mel "You..!"

            show Mike Cull Excited
            mike "This isn't even your case. You're just a consultant."
            mike "If you wish to do nothing but point out the obvious and spout nonsense, I'll have you removed."
            mike "Now, be a good boy and finish what I brought you here for:"
            mike "Deduce why an armed robber would kill their partner years after committing the crime."

            show Mel Atonin Worried
            mel "(What the hell is wrong with this guy..? Wait, that's it! The armed robbery!)"
            mel "I finally get it. That's how the robbery ties to this case."

            show Mike Cull Worried
            mike "Have you gone mental, now?"

            show Mel Atonin Excited
            mel "This is how the robbery connects to the murder!"
            return

            
    return

label discrepency3():
    label .loop:
        call evidence_folder()
        if choosed_kife:
            show Mel Atonin Neutral
            mel "The knife from the robbery is the same as the one used in this murder!"

            show Mike Cull Worried
            mike "Again, if you’re just going to point out the obvious, you can just leave."

            show Mel Atonin Neutral
            mel "You don’t get it, do you? That knife was still stored in evidence up until the murder. You’d need our clearance or higher to so much as look at it!"

            show Mike Cull Worried
            mike "Now just hold on, what do you think you're implying here?"

show Mel Atonin Neutral
mel "The one who instructed Officer Ickle to patrol the scene of the murder, along with the one that took the knife from evidence…"
It was you, wasn’t it?! You’re the one that killed Tessa Tarone!

Mike: You think you’re so clever, huh? Don’t forget, evidence is king, and you don’t seem to have anything more than circumstantial!

Mel: You’d think that, wouldn’t you?

Mike: The logs…


Narrator: Mike, in a panic, runs out of the room…

[Play clothesline noises]

Pops: I heard everything. I was able to find sumthin’ pretty incriminating while I was at it, too. Detective Cull, yer under arrest for murder.

            return
        else:
            jump .loop

    
    return