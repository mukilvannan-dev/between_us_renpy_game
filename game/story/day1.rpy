# ==============================================================================
# Story - Day 1 & Prologue
# ==============================================================================

label start:
    scene black
    with fade

    play music bgm_rain fadein 2.0 loop

    n "There’s a place… I end up in sometimes."
    pause 0.5

    n "Not home. Not school. Somewhere in between."
    pause 0.6

    n "I don’t think it has a name… or maybe it does, just not one people use."
    pause 0.6

    n "I call it… The Quiet Crossing."

    scene quiet_crossing:
        zoom 1.5
    with fade

    n "Not because anything crosses here, but because something always feels like it’s about to."
    pause 0.7

    n "The bench is still wet from the rain, but I sit anyway."
    pause 0.6

    n "Cold… but not uncomfortable."
    pause 0.7

    n "It’s quiet. Not the normal kind the kind where even your thoughts feel out of place."
    pause 0.8

    n "There’s always something slightly off."
    pause 0.5

    n "Today… the wind isn’t moving the trees."
    pause 0.6

    n "I noticed that before anything else. That’s the problem with noticing things you don’t get to ignore them."
    pause 0.8

    n "People say I’m clumsy. They’re not wrong."
    pause 0.5

    n "I trip. I drop things. I miss what’s right in front of me."
    pause 0.7

    n "But I don’t miss… people."
    pause 0.9

    n "The way they smile when they don’t mean it. The way they hesitate before telling the truth."
    pause 0.7

    n "The way they look at you… when they think you’re not looking."
    pause 1.0

    n "Like right now."
    pause 1.0

    n "I’m not alone."

label aira_intro:

    play music bgm_rain fadein 2.0 loop

    scene quiet_crossing:
        zoom 1.5
    pause 0.8

    n "Rainwater drips quietly from the crossing lights."

    n "Footsteps approach from behind me."

    show aira neutral at center:
        yalign -1.0
    with dissolve

    a "There you are."

    a "You seriously walked ahead without me?"

    mc "You were late."

    show aira pout at center:
        yalign -1.0

    a "By one minute."

    a "One."

    mc "That’s still late."

    n "She lets out an annoyed sigh."

    a "Wow."

    a "What an amazing childhood friend you are."

label aira_scene1:

    a "And why were you standing here alone like some depressed main character?"

    mc "Maybe I am one."

    show aira happy at center:
        yalign -1.0

    a "Nope."

    a "You’re not cool enough for that."

    n "…Rude."

    a "Come on, let’s go before we’re actually late."

    hide aira
    with dissolve

    stop music fadeout 1.0

    scene school_road:
        zoom 1.5
    with fade

    play music morning_casual fadein 2.0

    show aira neutral at left:
        yalign -1.0
    with dissolve

    n "We fall into step beside each other, the same rhythm we've had for years."

    a "So? Be honest."

    a "Did you almost trip over your own shoelaces on the way here?"

    menu:
        "I was contemplating the universe, actually.":
            $ aira_affection += 1
            show aira happy at left:
                yalign -1.0
            a "Ah yes, the deep philosophical mysteries of staring into rain puddles."

            mc "It takes profound intellect. You wouldn't understand."

            show aira pout at left:
                yalign -1.0
            a "Keep talking like that and I'll push you into the next puddle."

        "Only because someone took forever getting ready.":
            show aira pout at left:
                yalign -1.0
            a "I told you, it was one minute!"

            a "A girl needs time to make sure she doesn't look like a walking disaster."

            mc "Could've fooled me."

            show aira happy at left:
                yalign -1.0
            a "Hey! Watch it, or I won't share my notes with you later."

        "My balance has actually improved.":
            show aira happy at left:
                yalign -1.0
            a "Right. Is that why you nearly walked headfirst into a street sign back there?"

            mc "I was testing its structural integrity."

            a "Sure you were."

    show aira neutral at left:
        yalign -1.0

    n "The easy back-and-forth clears up the morning fog in my head."

    n "No awkward pauses. No need to watch what I say."

    a "It is nice walking like this again, though."

    mc "Yeah. Feels normal."

    show aira happy at left:
        yalign -1.0

    a "Good. Don't go getting used to peace and quiet when I'm around."

label aira_arrival:

    scene school_gate:
        zoom 1.5
    with fade

    show aira happy at left:
        yalign -1.0
    with dissolve

    n "We reach the school gate as the morning crowd thickens."

    a "See? Perfect timing. You'd definitely still be wandering around the neighborhood if I wasn't here to steer you."

    mc "I know the way to school, Aira."

    show aira pout at left:
        yalign -1.0

    a "Knowing the way and actually arriving on time are two completely different skills for you."

    n "Students stream past us laughing, rushing, half-asleep."

    n "A familiar morning."

    show aira neutral at center:
        yalign -1.0

    a "Come on, slowpoke. Let's get inside before the halls get jammed."

    n "She marches ahead toward the shoe lockers, energetic as always."

    n "And without thinking, I follow beside her."

label classroom_scene:

    scene classroom_day
    with fade

    show aira neutral at left:
        yalign -1.0
    with dissolve

    n "We enter the classroom. Same noise, same routine."

    a "You go sit. I’ll be back."

    hide aira
    with dissolve

    n "I sit down. People talking, chairs moving—nothing unusual."

    pause 0.5

    n "Time passes."


label lunch_scene:

    scene classroom_day
    with fade

    show aira neutral at center:
        yalign -1.0
    with dissolve

    n "The noon bell rings, instantly breaking the quiet of the classroom."

    n "Desks slide across the floor as groups form, chatter rising all at once."

    n "Aira pulls her chair up to my desk, dropping her bento down with a deliberate thud."

    a "Let me guess."

    a "You forgot lunch again."

    mc "…I remembered it in spirit."

    show aira pout at center:
        yalign -1.0

    a "Your spirit isn't going to stop your stomach from growling during fifth period."

    mc "A minor detail."

    a "A very loud detail."

    show aira happy at center:
        yalign -1.0

    n "She pops the lid off her box, revealing an extra set of rolled omelet and rice balls."

    a "Lucky for you, my mom made way too much this morning. Or maybe she just knew you'd be hopeless."

    menu:
        "You’re a lifesaver, Aira.":
            $ aira_affection += 1
            show aira happy at center:
                yalign -1.0
            a "Naturally! Remember this the next time I need someone to carry my bags."

            mc "There's always a price with you."

            a "Nothing in life is free, Ren. Especially not homemade food."

        "Are you sure this isn't a test batch? Am I the poison tester?":
            show aira pout at center:
                yalign -1.0
            a "Hey! My cooking skills—and my mom's—are five-star compared to the convenience store junk you eat."

            mc "Alright, alright, fair point."

            show aira happy at center:
                yalign -1.0
            a "Eat it before I change my mind and eat it all myself."

        "I could’ve survived on water until dinner.":
            show aira pout at center:
                yalign -1.0
            a "Right. And then you'd pass out during gym class and embarrass us both."

            a "Just take a bite, idiot."

    show aira neutral at center:
        yalign -1.0

    n "I take one of the tamagoyaki. It's warm, slightly sweet, and surprisingly good."

    mc "It’s really good."

    show aira happy at center:
        yalign -1.0

    a "Told you."

    show aira neutral at center:
        yalign -1.0

    pause 0.4

    n "For a split second… a strange prickle hits the back of my neck."

    pause 0.3

    n "Like someone is watching."

    pause 0.4

    n "I glance toward the classroom door, but there's only students wandering through the hall."

    n "Nothing unusual."

    show aira pout at center:
        yalign -1.0

    a "Earth to Ren? Don't tell me you're spacing out in the middle of eating."

    mc "Just thinking."

    show aira happy at center:
        yalign -1.0

    a "Careful, don't strain your brain. Finish up before the bell rings."

    n "She digs into her own lunch, humming softly to herself."

    n "Whatever that feeling was… it fades away."

label class_skip:

    scene classroom_day
    with fade

    n "Classes start. The usual routine."

    n "Teacher talking, chalk on the board, pages turning."

    mc "…"

    n "I try to pay attention."

    mc "Try."

    n "It lasts for a few minutes, then I lose track somewhere in between."

    pause 0.5

    n "Aira’s a few seats away. She looks focused… or at least better than me."

    mc "Not hard."

    pause 0.5

    n "Someone drops a pen. Someone laughs quietly. Nothing unusual."

    pause 0.5

    n "Time moves slowly… until it suddenly doesn’t."

    pause 0.8

    scene classroom_afternoon
    with fade

    n "Before I notice, classes are over."

label library_reina_intro:

    scene library_evening
    with fade

    play music uncertainity fadein 1.5

    n "The library is almost empty. Most people have already left, and only a few lights are still on."

    mc "…Quiet."

    n "I place the book I borrowed on the table."

    mc "I should return it."

    pause 0.5

    n "…But I don’t. Instead, I sit down—just for a bit."

    mc "I’ll finish a few pages."

    n "That was the plan. It doesn’t really happen."

    pause 0.5

    n "My attention drifts, like always. So I close it."

    mc "Maybe something else."

    n "I walk toward the shelves. One book stands out not because it looks special, just… familiar."

    mc "…"

    n "I take it and go back to my seat. I open it."

    pause 0.5

    r "…You’re reading that one?"

    pause 0.5

    scene reina_cg_library:
        zoom 1.5
    with fade

    n "I didn’t notice her earlier. She’s standing nearby."

    mc "Yeah. Why?"

    r "No reason… just people don’t usually pick it."

    mc "That bad?"

    r "No. Just ignored."

    pause 0.5

    n "She looks at the book on the table the one I didn’t finish."

    r "You didn’t finish that one."

    mc "…Not yet."

    r "You stopped halfway."

    mc "It got a bit slow."

    pause 0.5

    r "You always stop when it gets slow?"

    mc "Not always."

    r "…Then you won’t like this one."

    mc "…Why?"

    r "It’s slower."

    pause 0.5

    n "I look at the book in my hand."

    mc "…Seriously?"

    r "Yes."

    pause 0.5

    r "If you can’t finish that one… you won’t finish this either."

    pause 0.7

    mc "…"

    n "I glance at the unfinished book, then back at her."

    mc "You’ve read both?"

    r "Yes."

    mc "And?"

    r "The first one matters more."

    pause 0.5

    r "The second only makes sense if you finish it."

    pause 0.7


    menu:
        "Go back to the old book":
            $ reina_affection += 2

            mc "…Fine. I’ll finish it."

            r "Good."

            n "I sit back down and open the old book again."

            n "This time… I don’t stop."

        "Ask why she cares":
            $ reina_affection += 1

            mc "Why do you care so much?"

            pause 0.5

            r "…"

            r "Because people give up too fast."

            mc "On books?"

            r "On everything."

            pause 0.5

            n "Her eyes drift toward the shelves."

            r "Some things only become meaningful later."

            mc "That sounds oddly personal."

            pause 0.5

            show reina shy

            r "…Maybe."

            pause 0.5

            mc "Alright. I’ll give it another chance."

            show reina normal

            r "Good."

        "Ignore her and continue":
            mc "I’ll try this one anyway."

            r "…You won’t finish it."

            pause 0.5

            n "I keep reading, but the words don’t stick."

            n "After a few minutes… I close it."

            pause 0.5

            mc "…"

            n "She was right."

    pause 0.8

    scene library_evening
    with fade

    show reina normal at center:
        yalign -1.0
    with dissolve

    r "…Take your time. No one’s rushing you."

    pause 0.5

    mc "You work here?"

    r "Library duty."

    mc "That explains it."

    pause 0.5

    r "You come here often?"

    menu:
        "Tell her the truth":
            $ reina_affection += 1

            mc "Mostly when I want somewhere quiet."

            pause 0.5

            r "…I understand that."

            n "Her voice softens slightly."

        "Keep it vague":
            mc "Sometimes."

    pause 0.5

    r "…I’ve seen you."

    pause 0.5

    mc "…Have you?"

    r "Yes."

    pause 0.5

    n "She says it simply, like it’s obvious."

    pause 0.8

    mc "…Thanks."

    r "For what?"

    mc "Stopping me from picking the wrong book."

    pause 0.5

    show reina smile

    r "…Finish it first. Then decide."

    pause 0.8

    n "I nod and go back to reading."

    n "This time… I don’t get distracted."

    stop music fadeout 1.5
    
label aira_scene3:

    scene school_gate_evening:
        zoom 1.5
    with fade

    play music morning_casual fadein 1.5

    n "By the time I leave the building, the afternoon sky is streaked with amber and dull orange."

    n "Most of the courtyard is empty, the breeze chilling down."

    pause 0.5

    show aira neutral at left:
        yalign -1.0
    with dissolve

    a "Finally."

    a "Do you know how long I’ve been waiting here?"

    mc "Five minutes?"

    show aira pout at left:
        yalign -1.0

    a "…Seven."

    mc "That’s basically five."

    a "That’s not how numbers work, Ren."

    a "Class ended twenty minutes ago. What were you doing in there, taking a nap?"

    mc "I was in the library."

    show aira neutral at left:
        yalign -1.0

    a "…The library?"

    a "You? Voluntarily?"

    mc "Why does everyone react like I confessed to a crime?"

    show aira happy at left:
        yalign -1.0

    a "Because you once used an encyclopedia as a pillow."

    mc "That was one time."

    a "Three times! One of them had your drool on page forty."

    mc "That was a bookmark."

    show aira pout at left:
        yalign -1.0

    a "Gross."

    n "We step past the school gates and start our usual walk back."

    scene corner_evening:
        zoom 1.5
    with fade

    show aira neutral at left:
        yalign -1.0
    with dissolve

    n "The amber glow of the setting sun stretches our shadows along the asphalt."

    a "So what were you actually doing in there?"

    menu:
        "I'm trying to become an intellectual.":
            $ aira_affection += 1
            show aira happy at left:
                yalign -1.0
            a "Terrifying. If you actually start getting good grades, the universe might break."

            mc "Have a little faith in me."

            a "I have faith in your ability to sleep through an earthquake. That’s about it."

        "Someone actually recommended a book to me.":
            show aira pout at left:
                yalign -1.0
            a "Wait, seriously? Who? Don't tell me you actually talked to someone?"

            mc "I can talk to people, Aira."

            a "Debatable. Who was it anyway?"

            mc "Just the girl on library duty."

            show aira neutral at left:
                yalign -1.0
            a "Hmm. Suspicious. But I’ll let you off the hook for now."

        "It was just quiet. Wanted some fresh air for my brain.":
            show aira neutral at left:
                yalign -1.0
            a "Well, fair enough. But next time give me a heads-up so I don’t freeze waiting by the gate."

            mc "You could have walked home without me."

            show aira pout at left:
                yalign -1.0
            a "And miss the chance to complain at you? Never."

    show aira happy at left:
        yalign -1.0

    a "Besides, who else am I supposed to bully on the walk back?"

    mc "So I’m just your daily entertainment."

    a "Top-tier entertainment. And completely free."

    mc "I feel valued."

    a "As you should."

    pause 0.5

    n "We keep walking side by side."

    n "Like we always do."

    stop music fadeout 1.5
    pause 0.5

label kuroha_intro:

    scene to_the_house_road
    with fade

    n "Aira leaves at the usual turn."

    hide aira
    with dissolve

    n "Same as always."

    n "I keep walking."

    pause 0.5

    n "It’s quieter now. No voices. No footsteps."

    n "Just the sound of the road."

    play music creepy fadein 2.0

    mc "…"

    n "For a second… I feel like I missed something."

    pause 0.7

    n "Like someone was there… and isn’t anymore."

    pause 0.8

    n "I stop."

    mc "…?"

    pause 0.5

    show kuroha normal at right:
        yalign -1.0
    with dissolve

    n "Someone is standing a little ahead."

    n "I don’t remember seeing her before."

    pause 0.5

    mc "…Do you need something?"

    pause 0.5

    none "No."

    pause 0.5

    none "I was just… passing by."

    pause 0.5

    n "She doesn’t move. Not immediately."

    pause 0.5

    mc "…Right."

    pause 0.5

    n "I step forward. She steps aside just enough to let me pass."

    pause 0.7

    n "Her eyes follow me… only for a moment."

    pause 0.8

    none "You walk this way every day."

    pause 0.8

    mc "…Do I?"

    none "Yes."

    pause 0.5

    none "Around this time."

    pause 0.7

    n "She says it like it’s normal. Like anyone would know that."

    pause 0.8

    mc "…I guess."

    pause 0.5

    n "I keep walking."

    pause 0.5

    none "You were late today."

    pause 1.0

    menu:
        "Turn around and ask who she is":
            $ kuroha_affection += 1
            mc "…Who are you? How do you even know that?"

            pause 0.6

            show kuroha blush

            none "…I just pay attention to you, Ren."

            pause 0.7

            mc "…How do you know my name?"

            none "Get home safe."

        "Call out without looking back":
            mc "…I was just at the library."

            pause 0.6

            none "…I know."

            show kuroha blush

            none "Good night, Ren."

        "Say nothing and keep walking":
            mc "…"

            n "I don’t turn back."

            pause 0.8

            show kuroha blush

            n "But I can still feel it… like she’s still standing there."

    pause 1.0

    stop music fadeout 2.0

label home_scene:

    scene mc_room_night:
        zoom 1.5
    with fade

    play music homework fadein 1.5

    n "By the time I get home…"

    n "It’s already dark."

    mc "…"

    n "Nothing unusual."

    n "Same room."

    n "Same silence."

    pause 0.5

    mc "That was weird."

    pause 0.5

    n "Not in a big way."

    n "Just… slightly."

    pause 0.5

    n "She knew my routine."

    n "That’s all."

    mc "…Coincidence."

    pause 0.7

    n "Probably."

    pause 0.5

    n "I put my bag down."

    n "The book from the library is still there."

    pause 0.5

    mc "…"

    n "I open it."

    n "Read a few lines."

    pause 0.5

    n "It’s quiet."

    n "Too quiet."

    pause 0.8

    mc "…I’m overthinking it."

    pause 0.5

    n "I close the book."

    pause 0.5

    n "Sleep comes easily."

    n "Like nothing happened."

    stop music fadeout 1.5

    jump day2_morning
