# ==============================================================================
# Story - Day 3
# ==============================================================================

label morning_classroom_scene:

    scene classroom_day
    with fade

    play music morning_casual fadein 1.5

    n "The next morning feels normal."

    pause 0.5

    n "Or at least… it tries to."

    pause 0.8

    show aira neutral at left:
        yalign -1.0
    with dissolve

    a "You look tired."

    mc "I slept late."

    a "Reading again?"

    pause 0.5

    menu:
        "Yeah":

            mc "Yeah."

            show aira pout

            a "…Wow."

            a "You really are changing."

        "Couldn’t sleep":
            mc "Couldn’t really sleep."

            a "You should stop thinking so much then."

        "Maybe":
            mc "…Maybe."

            a "That means yes."

    pause 0.7

    a "You’ve been staying in the library a lot lately."

    mc "Not that much."

    show aira pout

    a "It’s enough that I noticed."

    pause 0.8

    n "Someone passes by the classroom door."

    pause 0.5

    n "Black hair."

    n "A familiar face."

    pause 0.7

    show kuroha normal2 at right:
        yalign -1.0
    with dissolve

    n "Kuroha glances inside for a second."

    pause 0.5

    n "Then notices me."

    pause 0.8

    show kuroha sweetSmile

    k "…Morning."

    pause 1.0

    mc "Morning."

    pause 0.7

    n "Aira looks between us."

    pause 0.7

    show aira neutral

    a "…Do you know her?"

    menu:
        "Not really":
            $ aira_affection += 1

            mc "Not really."

            pause 0.5

            k "…"

            pause 0.5

            show kuroha sad

            k "I see."

        "We talked yesterday":
            $ kuroha_affection += 1

            mc "We talked yesterday."

            pause 0.7

            show aira pout

            a "Huh."

            a "You meet a lot of people lately."

        "Why do you care?":
            $ aira_affection -= 1

            mc "Why do you care?"

            pause 0.5

            show aira pout

            a "I was just asking."

    pause 0.8

    show kuroha normal

    k "…I should go."

    pause 0.5

    hide kuroha
    with dissolve

    n "She leaves quietly."

    pause 0.8

    a "…She’s kinda weird."

    mc "You noticed fast."

    a "I’m serious."

    pause 0.5

    show aira pout

    a "She looked at you too much."

    pause 0.8

    mc "You say that like it’s a crime."

    a "Maybe it is."

    pause 0.7

    n "She says it lightly."

    n "But not completely joking."

    stop music fadeout 2.0

label lunch_free_choice:

    scene classroom_day
    with fade

    play music classroom_casual fadein 1.5

    n "Classes pass slower than usual."

    n "The sound of chalk against the board starts blending together after a while."

    pause 0.6

    n "At some point, I stop paying attention completely."

    pause 0.7

    n "Not that I was doing a great job before."

    pause 0.8

    scene classroom_day
    with dissolve

    n "Eventually…"

    n "The lunch bell rings."

    pause 0.8

    n "Almost immediately, the classroom changes."

    n "Chairs move."

    n "People start talking louder."

    n "Someone near the window laughs too hard at something probably not funny."

    pause 0.8

    n "Normal."

    pause 0.7

    show aira neutral at left:
        yalign -1.0
    with dissolve

    a "So?"

    pause 0.5

    a "What’re you doing for lunch today?"

    pause 0.7

    mc "Not sure yet."

    show aira pout

    a "That means you forgot to plan again."

    mc "Maybe."

    pause 0.5

    a "You’re hopeless."

    pause 0.8

    n "Aira rests her chin on my desk for a second."

    n "Like she already expects my answer."

    pause 0.8

    show aira neutral

    a "Well…"

    a "Don’t take too long deciding."

    pause 0.6

    hide aira
    with dissolve

    n "She walks off toward her friends."

    pause 0.8

    n "The classroom slowly empties."

    pause 0.7

    n "Somewhere outside the hallway…"

    n "I catch a glimpse of black hair passing by."

    pause 0.7

    n "Kuroha."

    pause 0.8

    n "At the same time…"

    n "I remember the unfinished conversation from the library yesterday."

    pause 0.8

    mc "…"

    pause 1.0

    menu:
        "Eat lunch with Aira":
            $ aira_affection += 2
            $ free_choice = "aira"
            jump aira_lunch2

        "Go to the library":
            $ reina_affection += 2
            $ free_choice = "reina"
            jump reina_scene4

        "Walk around the school":
            $ kuroha_affection += 2
            $ free_choice = "kuroha"
            jump kuroha_scene2

label aira_lunch2:

    scene rooftop_day:
        zoom 1.5
    with fade

    play music boku_yaba_best  fadein 1.5

    n "The rooftop door clicks shut behind us."

    pause 0.6

    n "Warm air brushes past lightly."

    n "The sky’s clearer than yesterday."

    pause 0.7

    show aira happy at center:
        yalign -1.0
    with dissolve

    a "See?"

    a "I knew you’d end up coming with me."

    mc "You sound really confident about that."

    show aira pout

    a "Because I know you."

    pause 0.5

    a "If I leave you alone during lunch…"

    a "you’ll either forget to eat or stare out a window for thirty minutes."

    mc "That only happened once."

    pause 0.5

    show aira happy

    a "Twice."

    mc "…"

    a "Three times, actually."

    pause 0.8

    n "She sits down near the fence."

    pause 0.7

    scene aira_rooftop:
        zoom  1.5
    with fade
    a "Here."

    n "She places a drink beside me before opening her lunch."

    mc "You brought extra again?"

    a "Obviously."

    pause 0.5

    a "You think I’d trust you to survive on your own?"

    mc "That bad?"

    a "Worse."

    pause 0.7

    n "I laugh quietly."

    pause 0.5

    n "Aira pauses for a second."

    n "Then smiles a little too."

    pause 0.8

    a "…There."

    mc "What?"

    a "You laughed."

    mc "People do that sometimes."

    a "Not you lately."

    pause 0.8

    n "The way she says it is light."

    n "But careful too."

    pause 0.8

    mc "Have I really been that weird?"

    a "A little."

    pause 0.5

    a "You’ve been thinking too much."

    a "And staying around other people more."

    mc "That second part sounds personal."

    pause 0.5

    scene rooftop_day:
        zoom 1.5
    with fade

    show aira pout at center:
        yalign -1.0
    with dissolve

    a "Maybe it is."

    pause 0.7

    menu:
        "Jealous?":
            $ aira_affection += 1

            mc "Jealous?"

            pause 0.5

            show aira embarrassed

            a "Wha— no."

            mc "That reaction says otherwise."

            a "You’re annoying today."

            pause 0.5

            show aira pout

            a "Maybe a little."

        "You still have priority":
            $ aira_affection += 2

            mc "You still have priority, don’t worry."

            pause 1.0

            show aira full_blush

            a "…You can’t just say things like that casually."

            mc "Why not?"

            pause 0.5

            a "Because it sounds unfairly nice."

        "You’re overthinking":
            mc "You’re overthinking."

            show aira pout

            a "I learned from you."

    pause 0.8

    n "A soft breeze passes across the rooftop."

    n "For a moment, neither of us says anything."

    pause 0.7

    a "…Hey."

    mc "Hm?"

    pause 0.5

    show aira neutral

    a "Do you remember when we used to eat lunch behind the gym?"

    mc "Back in middle school?"

    a "Yeah."

    pause 0.5

    a "You dropped your drink all over yourself."

    mc "You still remember that?"

    show aira happy

    a "Of course I do."

    a "You looked genuinely devastated."

    mc "It was my last drink."

    a "You stared at the empty carton like your life ended."

    pause 0.7

    mc "You laughed for ten minutes."

    a "Because it was funny."

    pause 0.8

    n "She’s laughing again now."

    n "The same way she used to."

    pause 0.8

    n "Comfortable."

    n "Easy."

    pause 0.7

    show aira neutral

    a "Things feel different lately though."

    mc "Different how?"

    pause 0.5

    a "…I dunno."

    a "Like you’re slowly walking somewhere."

    pause 0.5

    a "And I’m trying to keep up."

    pause 0.9

    mc "That sounds dramatic."

    show aira pout

    a "I’m serious."

    pause 0.8

    n "The bell rings in the distance."

    pause 0.6

    show aira pout

    a "Already?"

    a "That’s annoying."

    mc "You say that every lunch."

    a "Because lunch is too short every day."

    pause 0.7

    n "She stands up slowly."

    n "Then waits for me instead of walking ahead."

    pause 0.8

    show aira happy

    a "Come on."

    a "If we’re late, I’m blaming you."

    mc "Naturally."

    pause 0.8

    n "We head back downstairs together."

    n "Like we always do."

    stop music fadeout 1.5

    jump afternoon_transition

label reina_scene4:

    scene library_day
    with fade

    play music dangers_in_my_heart fadein 1.5

    n "The library’s quieter than usual during lunch."

    n "Only the sound of pages turning and the faint hum of the ceiling fan remain."

    pause 0.7

    n "I walk between the shelves automatically now."

    n "At some point, this place stopped feeling unfamiliar."

    pause 0.8

    n "The seat near the window is occupied."

    pause 0.7

    scene reina_sleep_cg:
        zoom 1.5
    with fade

    n "Reina’s asleep on the bench."

    pause 0.8

    n "One arm rests under her head."

    n "An open book lies against her lap."

    pause 0.7

    n "She looks… different like this."

    n "Less guarded."

    pause 0.8

    mc "…"

    n "I end up staring a little longer than I should."

    pause 1.0

    r "…Don’t stare too much."

    pause 0.8

    mc "You’re awake?"

    r "Mm."

    pause 0.5

    r "It’s embarrassing."

    pause 0.7

    mc "Then why say it with your eyes closed?"

    pause 0.5

    r "Because opening them makes it worse."

    pause 0.8

    n "I laugh quietly."

    pause 0.6

    n "Reina slowly sits up."

    scene library_evening
    with fade

    show reina embarrassed at center:
        yalign -1.0
    with dissolve

    r "What time is it…?"

    mc "Lunch break."

    pause 0.5

    show reina curiosity

    r "…Already?"

    mc "Rough night?"

    pause 0.6

    show reina normal

    r "I finished a book."

    mc "That explains absolutely nothing."

    r "It was long."

    mc "That explains slightly more."

    pause 0.8

    n "She fixes her hair a little before noticing the book in my hand."

    pause 0.6

    show reina curiosity

    r "…You brought it."

    mc "You recommended it."

    pause 0.5

    r "Most people don’t actually read the books I recommend."

    mc "That bad?"

    show reina embarrassed

    r "Apparently."

    pause 0.7

    mc "I’m starting to think you intentionally pick the slowest books possible."

    show reina slight_smile

    r "Maybe I do."

    mc "Why?"

    pause 0.8

    r "Because people rush through everything."

    pause 0.5

    r "Slow books force you to stay with them longer."

    pause 0.8

    mc "That sounds like something only you would say."

    pause 0.6

    show reina normal

    r "Did you hate it?"

    mc "…Not really."

    pause 0.5

    mc "The beginning was rough though."

    show reina slight_smile

    r "I knew it."

    mc "You say that like you were waiting for me to complain."

    r "I was."

    pause 0.7

    n "There’s a small smile on her face now."

    n "Not obvious."

    n "But definitely there."

    pause 0.8

    mc "You seem happier than usual."

    pause 0.7

    show reina embarrassed

    r "Do I?"

    mc "A little."

    pause 0.5

    r "…I just wasn’t expecting someone to actually finish it."

    pause 0.8

    mc "You make it sound tragic."

    r "You’d be surprised."

    pause 0.6

    r "Most people stop halfway."

    pause 0.5

    r "Or say it’s boring."

    mc "It WAS boring sometimes."

    show reina pout

    r "That’s rude."

    mc "You literally fell asleep reading."

    pause 0.8

    show reina embarrassed

    r "That’s different."

    mc "How?"

    pause 0.5

    r "…I already know the ending."

    pause 0.8

    n "That answer somehow makes sense."

    pause 0.7

    mc "So what now?"

    mc "You gonna keep giving me emotionally exhausting book recommendations?"

    show reina slight_smile

    r "Probably."

    pause 0.5

    r "You actually read them."

    pause 0.8

    n "She says it quietly."

    n "But there’s something honest underneath it."

    pause 0.7

    mc "That sounds dangerous."

    r "For you maybe."

    pause 0.8

    n "The sunlight near the window shifts slightly."

    n "For a moment, the library feels warmer than usual."

    pause 0.7

    show reina normal

    r "…You can sit if you want."

    mc "You sure?"

    r "Mm."

    pause 0.5

    r "Just don’t stare again."

    mc "No promises."

    pause 0.7

    menu:
        "Keep teasing her":
            $ reina_affection += 1

            mc "You know, for someone recommending books all the time…"

            mc "you falling asleep while reading is kinda convincing me not to trust your taste."

            show reina pout

            r "That’s unfair."

            mc "You were literally unconscious."

            r "I already read that one three times."

            mc "That somehow makes it worse."

            pause 0.6

            show reina slight_smile

            r "…You still finished the book though."

        "Sit beside her":
            $ reina_affection += 2

            n "I sit down beside the bench."

            pause 0.5

            n "Reina glances at me briefly before looking back at the book in her lap."

            pause 0.7

            r "…Usually people leave after returning books."

            mc "You sound disappointed about that."

            pause 0.6

            show reina embarrassed

            r "I didn’t say that."

            mc "You didn’t have to."

            pause 0.8

            n "She quietly hides part of her face behind the book."

        "Ask what she was reading":
            $ reina_affection += 1

            mc "So what book made you pass out like that?"

            pause 0.5

            show reina normal

            r "A collection of short stories."

            mc "That sounds suspiciously boring."

            r "It is."

            mc "At least you’re honest."

            pause 0.6

            r "…I like quiet stories."

            mc "I noticed."

            pause 0.7

            r "You still read them anyway."

            pause 0.8

    show reina embarrassed

    r "…Annoying."

    pause 0.8

    n "But she’s smiling when she says it."

    n "The silence after that feels comfortable."

    n "Not empty."

    n "Just quiet."

    pause 0.8

    r "…Lunch break’s almost over."

    mc "Yeah."

    pause 0.5

    n "Reina closes the book on her lap carefully."

    pause 0.5

    show reina normal

    r "You should go before you’re late."

    mc "You too."

    r "I still have library duty."

    mc "Right."

    pause 0.7

    n "I stand up slowly."

    n "For a second, it feels like I forgot something."

    pause 0.6

    mc "Hey."

    show reina curiosity

    r "…?"

    mc "Recommend something less painful next time."

    pause 0.7

    show reina slight_smile

    r "No."

    mc "Figured."

    pause 0.8

    r "…See you later, Ren."

    pause 0.7

    mc "Yeah."

    mc "Later."

    pause 0.8

    n "I leave the library quietly."

    n "But this time…"

    n "it doesn’t feel as distant as before."

    stop music fadeout 1.5

    jump afternoon_transition

label kuroha_scene2:

    scene corridor_day
    with fade

    play music boku_yaba_best fadein 1.5

    n "Lunch break gets noisy fast."

    n "Too noisy."

    pause 0.6

    n "So I leave the classroom before anyone tries to drag me into a hollow conversation."

    pause 0.7

    n "My feet carry me around the back of the school without thinking."

    pause 0.8

    scene back_shool_day:
        zoom 1.5
    with fade

    n "There’s an old bench behind the storage building."

    n "Mostly hidden by trees."

    pause 0.6

    n "Almost nobody comes here."

    pause 0.8

    mc "…"

    n "Someone’s already sitting there."

    pause 0.7

    scene kuroha_backschool:
        zoom 1.5
    with fade

    n "Kuroha."

    pause 0.8

    mc "You again."

    pause 0.5

    k "Mm."

    pause 0.7

    n "She shifts slightly on the bench, pulling her skirt down tight."

    n "Like she was already adjusting herself to make space before I even turned the corner."

    pause 0.8

    mc "What are you doing back here?"

    pause 0.6

    k "Eating lunch."

    mc "Alone?"

    k "Usually."

    pause 0.7

    mc "This place is pretty well hidden."

    pause 0.5

    k "That’s why I chose it."

    pause 0.8

    n "There’s a small convenience store sandwich resting beside her."

    n "Completely untouched."

    pause 0.6

    mc "You haven’t even unwrapped it yet."

    k "I was waiting."

    pause 0.8

    mc "…Waiting for what?"

    pause 0.6

    k "For you."

    pause 1.0

    mc "That’s a little concerning."

    k "Sorry."

    mc "You always say sorry after saying something that catches me off guard."

    pause 0.7

    k "Because I don't want to startle you away. But I'm just telling the truth."

    pause 0.8

    n "I take a seat on the opposite end of the bench."

    pause 0.5

    n "Kuroha glances at the gap left between us."

    pause 0.6

    k "…You sat far away today."

    mc "There’s literally space for a whole person between us."

    k "Mm."

    pause 0.7

    n "Her voice has a flat, quiet disappointment to it that makes me feel strangely exposed."

    pause 0.8

    mc "Did you actually know I’d come back here?"

    pause 0.6

    scene backschool_day:
        zoom 1.5
    with fade

    show kuroha normal at center:
        yalign -1.0
    with dissolve

    k "I was sure of it."

    mc "How?"

    pause 0.5

    k "Whenever the classroom gets too loud, your left shoulder tenses up. Then you look down at your desk, count to three, and leave."

    pause 0.9

    mc "…"

    mc "You notice some terrifyingly specific things."

    pause 0.6

    k "Only when it comes to you."

    pause 1.0

    mc "That does NOT make it feel any safer, Kuroha."

    pause 0.7

    show kuroha genuine_smile

    n "Kuroha smiles faintly."

    n "A gentle, soft expression, but her eyes stay completely locked onto mine."

    pause 0.8

    mc "So what? Have you just been secretly watching me all this time?"

    pause 0.7

    k "Not secretly."

    mc "Kuroha."

    k "…Mostly secretly. Until you started looking back."

    pause 0.8

    n "I almost let out a dry laugh. Her honesty is incredibly unsettling."

    pause 0.6

    mc "You admit to things that should probably make me run away."

    pause 0.7

    k "But you aren't running."

    mc "Should I be?"

    pause 0.8

    k "…I’d prefer if you stayed right where you are."

    pause 0.9

    n "There’s an intense, heavy gravity behind that soft whisper."

    pause 0.7

    menu:
        "Move a little closer":
            $ kuroha_affection += 2

            n "I shift slightly closer on the wooden bench, closing half the distance."

            pause 0.6

            n "Kuroha’s eyes widen just a fraction as she notices."

            show kuroha s_blush

            k "…"

            mc "What? You were the one complaining about the space."

            pause 0.5

            k "Nothing. My chest just... felt very tight for a second."

            pause 0.5

        "Ask why she notices you so much":
            $ kuroha_affection += 1

            mc "Seriously though. Out of everyone in this school... why me?"

            pause 0.7

            k "I will tell you one day, but for now, it's a secret."

            k "I only needed to see you once to realize it."

            k "You looked... entirely separate from everyone else. Like you belonged somewhere quiet."

            pause 0.5

            k "Once I realized that, I couldn't stop looking."

            pause 0.9

            mc "That sounds dangerously close to an obsession."

            show kuroha s_blush

            k "…Maybe. But is it wrong to protect what comforts you?"

        "Tease her":
            $ kuroha_affection += 1

            mc "You talk like a stray cat that silently decided I'm its property."

            pause 0.7

            show kuroha sweetSmile

            k "…"

            pause 0.5

            k "That’s not completely wrong. Except cats can lose interest."

            pause 1.0

            mc "You admitted that way too easily. Should I be worried?"

            show kuroha slight_smile
            k "Only if you try to leave me behind."

    pause 0.8

    n "The wind moves softly through the branches above us, filtering the afternoon light."

    pause 0.6

    n "She quietly cracks open the plastic wrap of her sandwich, her movements slow and deliberate."

    pause 0.5

    n "Then she stops, looking down at the ground."

    pause 0.7

    k "…You were talking to Aira before fifth period yesterday."

    mc "You were matching the hallways then, too?"

    pause 0.5

    k "Mm."

    mc "Kuroha..."

    pause 0.8

    show kuroha s_blush

    k "She was laughing at something you said. She touched your arm."

    mc "She’s just being loud, like usual. It’s normal for her."

    pause 0.7

    k "I didn’t like it."

    pause 0.8

    n "She says it without an ounce of anger in her tone. It’s a completely level statement."

    n "And somehow, that absolute calm makes it sound much worse."

    pause 0.9

    mc "It was just a normal conversation."

    pause 0.7

    k "I know."

    pause 0.5

    k "But it feels like people keep trying to crowd around you lately."

    pause 0.5

    k "Aira."

    pause 0.5

    k "And that girl from the library. Reina."

    pause 0.8

    k "Every time I look, someone else is trying to take up your thoughts."

    pause 0.7

    show kuroha sad

    k "I realized... if I kept waiting in the background..."

    pause 0.6

    k "they would take every piece of your time until you had nothing left for me."

    pause 1.2

    mc "…"

    n "Her voice drops to a faint whisper, drifting off into the wind."

    pause 0.8

    mc "So you decided to suddenly approach me because you felt rushed?"

    pause 0.6

    show kuroha genuine_smile

    k "Mm. I had to let you know I was here."

    mc "That’s a little wild, you know."

    pause 0.5

    k "Perhaps."

    pause 0.8

    n "There is an unsettling warmth in her expression, like she's entirely satisfied with her logic."

    pause 0.9

    mc "You tell me these deeply heavy things with a completely straight face."

    pause 0.5

    k "…?"

    show kuroha sweetSmile

    k "Would it make you feel safer if I smiled through it?"

    pause 0.8

    mc "No, that definitely makes it feel a lot more threatening."

    pause 0.7

    n "Kuroha lets out a soft, airy laugh under her breath."

    n "It sounds completely innocent, which only makes the whiplash deeper."

    pause 0.9

    k "…Ren?"

    mc "Yeah?"

    pause 0.5

    k "Come back to this bench tomorrow."

    pause 0.9

    mc "Are you just assuming I will?"

    pause 0.6

    k "You will get tired of the noise again. You always do."

    pause 0.5

    k "So I’ll be sitting right here, waiting for you to find me."

    pause 1.0

    mc "Sounds like you're trapping me."

    pause 0.5

    k "No."

    pause 0.6

    k "I’m just making sure you have a place to return to."

    pause 1.0

    n "The lunch bell cuts through the air, signaling the end of the break."

    mc "I should get back to class..."

    k "Go ahead. I'll see you tomorrow, Ren."

    jump afternoon_transition

label afternoon_transition:

    stop music fadeout 2.0
    scene black with fade
    pause 1.0

    n "The rest of the afternoon passes in a blur of monotone lectures and the scraping of chalk."

    pause 0.5

    n "I try to focus on the blackboard."

    n "But can't"
    pause 0.8

    scene classroom_afternoon:
        zoom 1.0
    with fade

    n "When the final chime rings, signaling the end of classes, the room immediately fills with the rustle of packing bags."

    pause 0.5

    n "I don't wait around for the chatter to start."

    pause 0.6

    n "I grab my things, slide my chair in, and walk out into the hallway alone."

    pause 0.8

    scene black with fade
    pause 1.0

    jump home_night_scene  

label home_night_scene:

    scene mc_room_night:
        zoom 1.5
    with fade

    play music library fadein 1.5

    n "By the time I get home…"

    n "the sky is completely dark."

    pause 0.7

    n "I drop my bag near the desk."

    pause 0.6

    n "The room feels quiet."

    n "Too quiet after an entire day at school."

    pause 0.8

    mc "…"

    pause 0.7

    n "I change clothes and fall onto the bed for a moment."

    pause 0.8

    n "My body feels heavier than usual."

    pause 0.7

    mc "Maybe I should sleep early today."

    pause 0.8

    n "..."
    
    n "I stare up at the ceiling, watching the shadows from the window stretch across the plaster."
    
    stop music fadeout 2.0
    play sound "sfx_phone_buzz" 
    pause 0.5
    
    mc "An alert...?"
    
    n "My phone screen lights up the dark room, casting a pale blue glow over my face."
    
    nvl clear
    
    menu:
        "Check messages from Aira" if aira_affection >= 2 and free_choice == "aira":
            n "It's a text from Aira."
            a_nvl "Hey, you made it home alright?"
            a_nvl "You looked like a zombie during lunch today. Seriously, don't forget to eat dinner."
            mc_nvl "I'm fine. Just tired."
            a_nvl "Mhm. Sure. Don't be late tomorrow morning or I'm leaving you."
            nvl clear
            
        "Check messages from Reina" if reina_affection >= 3 and free_choice == "reina":
            n "A notification from an unknown number... no, it's signed at the bottom."
            r_nvl "You left your bookmark at the counter."
            r_nvl "Don't lose your place in the book tomorrow."
            mc_nvl "Thanks. I'll make sure to get it."
            r_nvl "Good night, Ren."
            nvl clear
            
        "Check the unknown notification" if kuroha_affection >= 3 and free_choice == "kuroha":
            $ kuroha_affection += 1
            n "It's an unknown contact. No name. No number."
            
            k_nvl "You're still awake, Ren."
            k_nvl "You shouldn't stay up too late. It makes the mornings harder for you."
            mc_nvl "Who is this? Wait... Kuroha? How did you even get my number?"
            k_nvl "You left your student handbook on your desk during second period yesterday when you went to the restroom."
            k_nvl "Your emergency contact sheet was right in the front pocket. It only took me a few seconds to write it down."
            mc_nvl "You went through my things...?"
            k_nvl "I just didn't want to lose a way to reach you. Close your eyes, Ren. Sleep well."
            nvl clear

    n "I set the phone back down on the nightstand, its screen slowly fading back to black."
    
    if free_choice == "kuroha":
        play music creepy fadein 3.0
        n "My heart beats a little faster against my chest, a cold weight settling in my stomach."
        n "I slowly glance toward the window."
        n "The streetlamp outside flickers once, casting long, still shadows across the floor."
        n "She isn't outside. The glass is locked. The room is completely secure."
        n "But knowing she was standing over my desk, going through my personal belongings while I was gone for just a few minutes..."
        n "The realization makes the air in my own room feel suddenly thin."
        mc "…"
        mc "Tomorrow… I need to figure out what she's planning."
    else:
        play music sad1 fadein 2.0
        n "The comfort of the sheets does little to ease the strange tightness in my chest."
        n "The room is perfectly quiet, completely normal."
        n "But the boundaries of that normalcy are beginning to fray, leaving a phantom chill on the back of my neck."
        mc "Tomorrow..."
        
    pause 1.0
    scene black with fade
    pause 1.5
    
    n "And just like that, another day slips away into the dark."
    
    jump day3_morning

# Placeholder / Ending until Day 4 is implemented
label day3_morning:
    scene black with fade
    n "To be continued..."
    return
