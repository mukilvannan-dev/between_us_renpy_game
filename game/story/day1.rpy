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

    a "Come on, let’s go before we’re late."

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

    a "So?"

    a "Still tripping over absolutely nothing while walking?"

    menu:
        "Yeah, probably":
            show aira happy
            a "Knew it."

        "Only in public":
            a "That somehow makes it worse."

        "I evolved":
            a "Into what?"

            mc "A better idiot."

            show aira happy
            a "Fair enough."

    show aira neutral

    n "We walk beside each other like usual."

    n "The silence between us never feels awkward."

    a "You know…"

    a "It’s kinda nice walking like this again."

    menu:
        "Yeah. Feels normal":
            a "Exactly."

        "You sound old":
            show aira pout
            a "And you sound annoying."

        "You getting emotional?":
            show aira happy
            a "Shut up before I leave you behind."
label aira_arrival:

    scene school_gate:
        zoom 1.5
    with fade

    show aira happy at left:
        yalign -1.0
    with dissolve

    n "We reach the school gate."

    n "The same crowded entrance. The same noisy morning."

    a "See?"

    a "If I wasn’t here, you’d definitely be late."

    menu:
        "I would've made it":
            show aira pout at left:
                yalign -1.0
            a "Yeah, sure."

            a "And I’m the principal."

        "Yeah, probably":
            $ aira_affection += 1
            show aira happy
            a "Finally."

            a "You admit I’m useful."

        "You talk too much":
            show aira pout
            a "Wow."

            a "And yet you still listen to me."

    n "Students pass by us laughing, arguing, half-asleep."

    n "Everything feels normal."

    n "Too normal."

    n "Someone laughs louder than they mean to."

    n "Someone avoids looking at another person."

    n "Small things stand out when you pay attention."

    show aira neutral at center:
        yalign -1.0

    a "…You’re doing it again."

    menu:
        "Doing what?":
            a "That staring thing."

        "I’m literally just standing here":
            a "Mhm."

            a "And overthinking."

        "You notice too much":
            $ aira_affection += 1
            show aira happy
            a "Well, someone has to keep an eye on you."

    a "You always start observing everyone like you're solving a mystery."

    mc "Maybe I am."

    show aira pout at center:
        yalign -1.0

    a "Please."

    a "You’d be the worst detective ever."

    mc "That’s rude."

    show aira happy at center:
        yalign -1.0

    a "But accurate."

    a "Come on, we still have time before class."

    n "She starts walking ahead."

    n "And without thinking, I follow beside her like always."

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

    n "Lunch break."

    a "You didn’t bring anything again, did you?"

    mc "…I thought about it."

    a "That’s not the same as bringing it."

    mc "I know."

    a "You’re impossible."

    menu:
        "I forgot":
            $ aira_affection += 1
            mc "I actually forgot this time."
            a "…You say that every time. Here."

        "I wasn’t hungry":
            mc "I wasn’t really hungry."
            a "You say that now, but you’ll complain later. Here."

        "Stay silent":
            $ aira_affection -= 1
            a "…Hey. Don’t just sit there quietly."

    a "I made extra."

    mc "You always do."

    a "And you always don’t bring lunch."

    mc "Fair."

    show aira happy

    a "Say ‘ah’."

    menu:
        "Accept":
            $ aira_affection += 1
            mc "…Fine."
            a "Good."

        "Take it yourself":
            mc "I can eat on my own."
            a "Where’s the fun in that?"

        "Refuse":
            $ aira_affection -= 1
            mc "I’m good."
            show aira pout
            a "…Oh. Okay."

    n "I take a bite."

    mc "It’s good."

    a "That sounded forced."

    mc "It’s not."

    a "Then say it properly."

    mc "…It’s really good."

    a "Better."

    show aira neutral

    pause 0.5

    a "You’re still clumsy though, right?"

    mc "Yeah… probably."

    a "I figured. Some things don’t change."

    mc "You sound relieved."

    a "Maybe I am."

    pause 0.5

    a "…Hey. You’ve been a bit weird lately."

    mc "Weird how?"

    a "I don’t know. You just… go quiet sometimes. More than usual."

    mc "It’s nothing."

    a "If you say so."
    pause 0.3

    n "For a second… I feel like someone’s watching."

    pause 0.3

    n "I glance around."

    n "Nothing unusual."

    pause 0.3

    pause 0.5

    show aira pout

    a "Just don’t skip meals. You’re already bad enough as it is."

    mc "Wow."

    a "I’m serious. You’d probably collapse without me."

    mc "That bad?"

    a "Worse."

    show aira happy

    n "She smiles like it’s a joke."

    n "It probably is… mostly."

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

    play music sad1 fadein 1.5

    n "By the time I leave school, the sun’s already starting to set."

    n "Most students are already gone."

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

    a "That’s not how numbers work."

    a "You stayed back again?"

    menu:
        "Yeah":
            $ aira_affection += 1
            mc "Library."

            a "Wow."

            a "Look at you being academic."

        "Just a little":
            mc "It wasn’t that long."

            a "You always say that."

        "Got distracted":
            show aira happy
            mc "There was a cat outside."

            a "…Okay, that’s actually believable."

    show aira neutral at left:
        yalign -1.0

    a "You’ve been doing that a lot lately though."

    mc "Doing what?"

    a "Staying behind after class."

    pause 0.4

    a "It’s weird."

    mc "Why?"

    a "Because you used to run out of school like your life depended on it."

    mc "Maybe I matured."

    show aira happy

    a "No chance."

    pause 0.5

    n "We start walking home together."

    scene corner_evening:
        zoom 1.5
    with fade

    show aira neutral at left:
        yalign -1.0
    with dissolve

    n "Same road."

    n "Same evening routine."

    a "So what do you even do there that long?"

    mc "Reading."

    pause 0.2

    a "…You?"

    mc "Why does everyone react like that?"

    a "Because you once used a book as a pillow."

    mc "That was one time."

    a "Three times."

    menu:
        "I’m improving":
            $ aira_affection += 1
            a "Scary."

            a "At this rate you might actually become responsible."

        "Books are less boring now":
            a "Wow."

            a "Character development."

        "Someone recommended one":
            show aira pout
            a "Oh?"

            a "Who?"

    pause 0.4

    mc "Why do you sound so suspicious?"

    a "I’m not suspicious."

    pause 0.2

    show aira happy

    a "I’m judging you."

    mc "That’s worse."

    n "She laughs quietly."

    pause 0.5

    a "Still…"

    a "Don’t stay too late every day."

    mc "Why? You get lonely walking home alone?"

    show aira pout

    a "Obviously."

    a "Who else am I supposed to bully on the way home?"

    mc "So I’m just entertainment?"

    show aira happy

    a "Exactly."

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
