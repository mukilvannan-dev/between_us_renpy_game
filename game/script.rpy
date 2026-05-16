define config.default_text_cps = 35
default preferences.text_cps = 35
define mc = Character("Ren", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define n = Character(None, what_slow_cps=35)
define none = Character("???", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define a = Character("Aira", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define r = Character("Reina", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define k = Character("Kuroha", what_prefix="\"", what_suffix="\"", what_slow_cps=35)

define mc_nvl = Character("Ren", kind=nvl, callback=Phone_SendSound)
define a_nvl = Character("Aira", kind=nvl, callback=Phone_ReceiveSound)
define r_nvl = Character("Reina", kind=nvl, callback=Phone_ReceiveSound)
define k_nvl = Character("Kuroha", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

default aira_affection=0
default reina_affection=0
default kuroha_affection = 0
default free_choice = None


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

    n "…"

    n "I turn around."

    show aira neutral at center:
        yalign -1.0
    with dissolve

    a "…You came here again."

    n "Of course it’s her. It’s always her."

    show aira pout at center:
        yalign -1.0

    a "You didn’t even wait for me. That’s kind of mean, you know?"


label aira_scene1:

    a "…Anyway, you shouldn’t come here alone. It feels weird."

    n "We’ve been here before a long time ago, back when things were simpler."

    a "Hey… you’re thinking too much again, aren’t you?"

    n "She always notices, even when I don’t say anything."

    a "Come on. Let’s go, we’ll be late."

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

    a "You still trip over nothing, or did you finally improve?"

    menu:
        "I’m still the same, I guess":
            $ aira_affection += 1
            show aira happy
            a "…Of course you are. Some things never change."

        "I’ve improved":
            a "Oh really? I’ll believe it when I see it."
            show aira neutral

        "Ignore her":
            $ aira_affection -= 1
            show aira pout
            a "…Hey. Don’t ignore me."
    show aira neutral

    n "We keep walking side by side, like always."

    n "But something feels… slightly off."

    a "…I’m glad, though. That you didn’t change."

    pause 0.2

    a "…Right?"

    menu:
        "Yeah, I’m the same":
            a "…Good."

        "People change":
            $ aira_affection -= 1
            show aira concerned at left:
                yalign -0.5
            a "…That’s not funny."

        "Stay silent":
            $ aira_affection -= 1
            a "…You’re doing it again. Thinking instead of answering."

    pause 0.6

label aira_arrival:

    scene school_gate:
        zoom 1.5
    with fade

    show aira happy at left:
        yalign -1.0
    with dissolve

    n "We reach the school. Same gate, same noise, same routine."

    a "We made it just in time. See? If I wasn’t here, you’d definitely be late."

    menu:
        "I would’ve made it":
            show aira pout at left:
                yalign -1.0
            a "Oh really? I doubt that."

        "Yeah, probably":
            a "Right? You should be grateful."
            show aira happy

        "Stay silent":
            $ aira_affection -= 1
            show aira pout 
            a "…Hey. Say something."

    n "Students pass by us—some laughing, some rushing. Normal."

    n "Too normal."

    n "I notice small things. Someone looking away too quickly, someone forcing a smile, someone pretending not to notice someone else."

    n "It’s always there. You just have to look."

    show aira neutral at center:
        yalign -1.0

    a "…You’re doing it again."

    menu:
        "Doing what?":
            a "That look."

        "Not really":
            a "Don’t lie."

        "Stay silent":
            $ aira_affection -= 1
            a "…You always go quiet when I ask something like that."

    a "You look at people like you’re trying to figure them out."

    pause 0.4

    a "It’s kind of… weird."

    n "She says it lightly, like it’s a joke. But it isn’t."

    show aira happy at center:
        yalign -1.0

    a "Anyway, come on. Let’s go—we still have time before class."

    n "She walks beside me. Like always."

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

    n "I walk toward the shelves. One book stands out—not because it looks special, just… familiar."

    mc "…"

    n "I take it and go back to my seat. I open it."

    pause 0.5

    r "…You’re reading that one?"

    pause 0.5

    scene reina_cg_library:
        zoom 1.4
    with fade

    n "I didn’t notice her earlier. She’s standing nearby."

    mc "Yeah. Why?"

    r "No reason… just people don’t usually pick it."

    mc "That bad?"

    r "No. Just ignored."

    pause 0.5

    n "She looks at the book on the table—the one I didn’t finish."

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

    mc "Sometimes."

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

    n "By the time I leave the school, the sky’s already changing."

    n "Most people are gone."

    pause 0.5

    show aira neutral at left:
        yalign -1.0
    with dissolve

    a "You’re late."

    mc "A little."

    a "You stayed back again?"

    menu:
        "Yeah":
            $ aira_affection += 1
            mc "Yeah. Library."
            a "…Again."

        "Just a bit":
            mc "Not that long."
            a "You say that every time."

        "Stay silent":
            $ aira_affection -= 1
            show aira pout at left:
                yalign -1.0
            a "…Hey. Answer me."

    a "You’ve been doing that a lot lately."

    mc "Doing what?"

    a "Staying back."

    pause 0.5

    show aira neutral at left:
        yalign -1.0

    a "It’s new."

    mc "Is it?"

    a "Yeah. You didn’t used to."

    mc "Maybe I felt like it."

    a "…Hmm."

    pause 0.5

    n "We start walking."

    scene corner_evening:
        zoom 1.5
    with fade

    show aira neutral at left:
        yalign -1.0
    with dissolve

    n "Same road. Same direction. Same as always."

    pause 0.5

    a "So? What were you doing?"

    mc "Reading."

    a "You?"

    mc "Yeah."

    a "Since when?"

    mc "…I don’t know."

    a "You don’t even finish the ones you start."

    mc "That’s true."

    pause 0.5

    a "Then why now?"

    mc "…"

    menu:
        "Just felt like it":
            a "That’s not an answer."

        "Someone told me to":
            $ aira_affection -= 1
            show aira pout
            a "…Someone?"

            mc "Library duty girl."

            pause 0.5

            a "…Oh."

        "I’m trying to finish things":
            $ aira_affection += 1
            a "…That’s new."

    pause 0.5

    show aira concerned

    n "She walks a little quieter now. Not far… but not as close as before."

    pause 0.5

    a "You’re changing."

    mc "Am I?"

    a "…A little."

    pause 0.5

    a "I don’t know if I like that."

    pause 0.8

    n "She says it lightly, like it’s nothing."

    n "But it stays."

    pause 1.0

    a "Anyway, don’t stay too late next time."

    a "It’s… weird walking alone."

    mc "You could go without me."

    a "I don’t want to."

    pause 0.5

    n "We keep walking."

    n "The distance between us is small… but noticeable."

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



label day2_morning:

    scene mc_room_day:
        zoom 1.5
    with fade

    play music morning_room fadein 1.5

    n "Morning."

    n "Nothing feels different."

    pause 0.5

    n "…That’s the first thing I notice."

    mc "…"

    n "I get ready like usual."

    n "Same routine. Same timing."

    pause 0.5

    n "But something lingers."

    pause 0.7

    n "Like I forgot something."

    pause 0.7

    n "Or someone."

    pause 0.8

    mc "…Probably nothing."

    stop music fadeout 1.0

    jump school_morning_day2


label school_morning_day2:

    scene school_road_without_rain:
        zoom 1.5
    with fade

    play music morning_room fadein 1.5

    n "The road is the same as always."

    n "People pass by. Conversations overlap."

    n "Normal."

    pause 0.5

    n "I walk at the same pace."

    pause 0.5

    n "Without thinking about it."

    pause 0.7

    n "For a second…"

    n "I feel like someone’s behind me."

    pause 0.5

    n "Close."

    pause 0.5

    n "I turn."

    pause 0.5

    n "No one."

    pause 0.7

    mc "…"

    n "Just my imagination."

    pause 0.5

    jump classroom_day2


label classroom_day2:

    scene classroom_day
    with fade

    n "Classes pass like usual."

    n "Nothing stands out."

    pause 0.5

    n "Which is… strange."

    pause 0.5

    n "Because it should."

    pause 0.7

    n "But it doesn’t."

    pause 0.8

    jump lunch_day2


label lunch_day2:

    scene classroom_day
    with fade

    show aira neutral at left:
        yalign -1.0
    with dissolve

    a "You’re quiet today."

    mc "Am I?"

    a "More than usual."

    pause 0.5

    mc "Just tired."

    a "…Hmm."

    pause 0.5

    a "You stayed back again yesterday."

    mc "Yeah."

    a "You’re doing that a lot."

    pause 0.5

    mc "Maybe."

    pause 0.5

    n "She watches me for a second."

    pause 0.5

    a "Don’t overdo it."

    mc "I won’t."

    pause 0.5

    a "You say that like you mean it."

    mc "I do."

    a "…Right."

    pause 0.5

    hide aira
    with dissolve

    n "Lunch ends."

    jump library_day2

label library_day2:

    scene library_day
    with fade

    play music library fadein 1.5

    n "I end up in the library again."

    n "This time… it feels less accidental."

    pause 0.5

    show reina normal at center:
        yalign -1.0
    with dissolve

    r "…You came back."

    mc "Yeah. You sound surprised."

    r "A little."

    r "You didn’t seem like the type to come twice in a row."

    mc "That’s kind of rude."

    r "It’s accurate."

    pause 0.5

    mc "…I finished the book."

    r "Did you?"

    mc "Yeah. Slowly."

    r "I expected you to stop halfway again."

    mc "You don’t trust me much, do you?"

    r "You didn’t give me a reason to."

    pause 0.5

    mc "…Fair."

    pause 0.5

    r "So?"

    r "Was it worth finishing?"

    mc "…Yeah."

    mc "It was slow, but not boring."

    r "That’s the point."

    pause 0.5

    r "You only notice that if you don’t quit."

    pause 0.6

    mc "You always talk like that?"
    
    show reina curiosity

    r "Like what?"

    mc "Like you’re testing people."

    pause 0.5

    r "…Maybe I am."

    r "You’re easy to test."

    mc "That doesn’t sound like a compliment."

    r "It’s not."

    pause 0.5

    mc "Wow."

    show reina smile

    r "You still came back."

    pause 0.5

    mc "…Yeah."
    
    menu:
        "You’re kind of strict":
            $ reina_affection += 2
            mc "You’re kind of strict, you know that?"

            show reina curiosity

            r "Only when it matters."

            mc "And this matters?"

            r "You came back. So yes."

        "You enjoy this, don’t you?":
            $ reina_affection += 2
            mc "You enjoy this, don’t you? Watching people struggle through books."

            r "Not people."

            pause 0.3

            r "Just you."

            mc "…That’s worse."

        "Stay quiet":
            $ reina_affection -= 1
            show reina normal
            n "I don’t respond."

            r "…You go quiet again."

            r "You do that when you don’t know what to say."
    pause 0.5

    r "Did you understand the ending?"

    mc "Mostly."

    r "Mostly?"

    mc "Some parts didn’t really explain themselves."

    r "They weren’t supposed to."

    pause 0.5

    mc "That’s annoying."

    r "That’s intentional."

    pause 0.5

    mc "You like things like that?"

    r "Things that don’t spell everything out?"

    mc "Yeah."

    r "…It’s better than things pretending to mean something when they don’t."

    pause 0.5

    mc "That sounded personal."

    r "It wasn’t."

    pause 0.3

    r "…Probably."

    pause 0.6

    r "So what now?"

    mc "What do you mean?"

    r "You finished one book."

    r "Don’t tell me that’s all it takes."

    mc "I might stop here."

    r "…Of course you would."

    pause 0.5

    mc "I’m joking."

    r "…You’re not convincing."

    mc "Hey."

    mc "I came back, didn’t I?"

    pause 0.5

    r "…You did."

    pause 0.5

    r "Then pick another one."

    mc "You’re assigning me homework now?"

    r "If I don’t, you’ll pick something random again."

    mc "That’s not wrong."

    pause 0.5

    r "Stay here."

    hide reina
    with dissolve

    n "She walks to the shelf without waiting for an answer."

    pause 0.8

    show reina normal at center:
        yalign -1.0
    with dissolve

    r "This one."

    mc "You already decided?"

    r "Yes."

    mc "I don’t get a say?"

    r "You do."

    pause 0.3

    r "But you’ll pick this anyway."

    mc "…You’re confident."

    r "I’m right."

    pause 0.5

    mc "…Fine. I’ll try it."

    pause 0.5

    r "Not try."

    r "Finish."

    pause 0.5

    mc "You’re really not letting that go."

    r "No."
    n "I sit down with the new book."

    pause 0.5

    mc "…You always do this?"

    r "Do what?"

    mc "Decide things for people."

    pause 0.5

    r "Only when they don’t decide for themselves."

    pause 0.6

    mc "…That’s annoying."

    r "You’re still here."

    pause 0.5

    mc "…Yeah."

    pause 0.7

    n "I start reading."

    n "And this time… I don’t feel like stopping."

    stop music fadeout 1.5
    
label reina_scene3:

    scene library_evening
    with fade

    play music calm_library fadein 1.5

    n "The library is quieter than usual."

    n "Even the few people who were here earlier are gone now."

    pause 0.5

    n "I didn’t notice when it got this late."

    pause 0.5

    show reina curiosity at center:
        yalign -1.0
    with dissolve

    r "…You’re still here."

    mc "So are you."

    r "I have to be."

    mc "Library duty?"

    r "Yes."

    pause 0.5

    r "You don’t, though."

    mc "…I know."

    pause 0.5

    r "Did you finish it?"

    mc "Not yet."

    mc "But I’m not stopping halfway this time."

    pause 0.5

    show reina smile

    r "…Good."

    pause 0.5

    n "She doesn’t say anything else."

    n "Just stands there for a second… like she’s deciding something."

    pause 0.7

    r "You’ve been staying longer lately."

    mc "Yeah."

    mc "Your fault."

    r "…My fault?"

    mc "You keep giving me things I can’t leave unfinished."

    pause 0.5

    r "That sounds like an excuse."

    mc "It is."

    pause 0.5

    r "At least you’re honest about it."

    pause 0.6

    n "She walks a little closer, not fully sitting, just near enough."

    pause 0.5

    r "Most people don’t stay this late."

    mc "You do."

    r "I don’t have a choice."

    mc "You could switch duties."
    show reina normal

    r "…I don’t want to."

    pause 0.5

    mc "You like it here?"

    pause 0.5

    r "It’s consistent."

    r "Same place. Same quiet."

    pause 0.5

    r "It doesn’t change depending on who’s around."

    pause 0.6

    mc "People do that."

    r "Yes."

    pause 0.5

    mc "You don’t like that?"

    pause 0.5

    r "…"

    pause 0.7

    r "It’s tiring."

    pause 0.6

    n "That’s the first time she doesn’t answer immediately."

    pause 0.6

    mc "…Yeah."

    pause 0.5

    mc "I get that."

    pause 0.5

    r "Do you?"

    mc "A little."

    mc "People act different depending on who they’re talking to."

    mc "It’s hard to tell what’s real sometimes."

    pause 0.6

    r "…"

    pause 0.5

    r "You notice that too."

    mc "I told you. I notice things."

    r "You don’t stay with them."

    mc "I’m trying to."

    pause 0.6

    n "She looks at me properly this time."

    pause 0.5

    r "…I can tell."

    pause 0.7
    menu:
        "You don’t have to stay alone":
            $ reina_affection += 2
            mc "You don’t have to stay here alone all the time."

            r "…I’m not alone."

            mc "You know what I mean."

            pause 0.5

            r "…"

            r "I’m used to it."

        "You really prefer this?":
            $ reina_affection += 0
            mc "You really prefer this over being with people?"

            r "It’s easier."

            mc "That doesn’t mean better."

            pause 0.5

            r "…Maybe not."

        "Stay quiet":
            $ reina_affection -= 1
            n "I don’t say anything."

            r "…You’re thinking again."

            r "You always stop at that point."

    pause 0.6

    r "People expect things."

    r "Even when they don’t say it."

    pause 0.5

    r "It’s easier not to deal with that."

    pause 0.6

    mc "…You think I expect something?"

    pause 0.5

    r "…No."

    pause 0.5

    r "That’s why this is fine."

    pause 0.7

    n "That lands differently than everything else she’s said."

    pause 0.6

    mc "…That’s a weird compliment."

    r "It wasn’t meant to be one."

    pause 0.5

    mc "I’ll take it anyway."

    pause 0.5

    r "…Do what you want."

    pause 0.6

    n "But she doesn’t look away this time."
 
    r "The library’s closing soon."

    mc "Yeah."

    pause 0.5

    r "…You can stay until I lock up."

    mc "You’re making an exception?"

    r "…Maybe."

    pause 0.5

    mc "That’s new."

    r "Don’t get used to it."

    pause 0.5

    mc "Too late."

    pause 0.6

    n "She exhales quietly."

    n "Not annoyed."

    n "Just… not pushing it away."

    pause 0.7

    n "I go back to reading."

    n "And for once…"

    n "the silence doesn’t feel empty."

    stop music fadeout 1.5


label kuroha_rain_scene:

    scene black
    play music bgm_rain fadein 1.5

    n "Rain starts just as I leave the school building."

    pause 0.5

    mc "…Seriously?"

    pause 0.5

    n "Not heavy."

    n "Just enough to make walking home annoying."

    pause 0.7

    n "I move under the small shelter near the gate."

    pause 0.8

    scene kuroha_cg_shelter:
        zoom 1.5
    with fade

    n "…And freeze for a second."

    pause 0.7

    n "It’s her."

    n "The girl from before."

    pause 0.8

    mc "…Oh."

    pause 0.5

    none "You’re late again."

    pause 0.8

    menu:
        "You remember that?":

            mc "You actually remembered that?"

            none "Mm."

            mc "That’s kinda impressive."


            none "…Weird, probably."

        "That’s a little creepy":
            mc "That’s a little creepy."


            none "…Sorry."

            mc "You apologize really fast."

        "You were waiting here?":

            mc "Wait… were you waiting here?"

            pause 0.5

            none "No."

            pause 0.5

            none "…Maybe a little."

    pause 0.8

    n "Rain taps softly against the roof above us."

    n "Neither of us says anything for a moment."

    pause 0.7

    mc "So do you always stand around in random places?"

    pause 0.5

    none "Not random places."

    mc "Then?"

    pause 0.5

    none "Places you pass by."

    pause 1.0

    mc "…That sounds worse somehow."


    none "I didn’t mean it like that."

    pause 0.6

    mc "Then how did you mean it?"

    pause 0.7

    none "…"

    pause 0.8

    none "I just notice you a lot."

    pause 1.0

    mc "We don’t even know each other."

    pause 0.5

    none "I know."

    pause 0.5

    menu:
        "Then why notice me?":

            mc "Then why pay attention to me at all?"

            pause 0.8

            none "…"

            pause 0.5

            none "You’re easy to notice."

            mc "That sounds fake."

            none "It’s not."

        "You say strange things":
            mc "You say strange things really casually."

            pause 0.5


            none "Sorry."

            mc "See? There it is again."

            pause 0.5

            none "…I’m not very good at this."

        "I’m just a normal guy":
            mc "I’m literally just some guy."

            none "Mm."

            pause 0.5

            none "That’s probably why."

    pause 0.7

    none "You always look distracted."

    pause 0.5

    none "Like part of you is somewhere else."

    pause 0.8

    mc "That’s kinda specific."

    none "Mm."

    pause 0.7

    n "She says things quietly."

    n "Not confidently."

    n "Just honestly."

    pause 0.8

    mc "Have you been watching me or something?"

    pause 0.7


    none "…That sounds bad when you say it out loud."

    mc "Because it is bad."

    pause 0.5

    none "Sorry."

    pause 0.6

    mc "You said that already."

    none "…Sorry."

    pause 0.7

    n "I almost laugh."

    n "Almost."

    pause 0.6

    scene school_shelter:
        zoom 1.5
    show kuroha normal at center:
        yalign -1.0
    with dissolve

    menu:
        "You’re kinda funny":

            mc "You’re kinda funny."

            pause 0.5

            none "…Am I being made fun of?"

            mc "Maybe a little."

            pause 0.5


            none "…That’s mean."

        "You’re really awkward":
            mc "You’re really awkward, huh?"

            pause 0.5

            none "…Probably."

            mc "At least you know."

        "You nervous or something?":

            mc "Are you nervous?"

            pause 0.8

            none "…A little."

            mc "Why?"

            pause 0.5

            none "I don’t usually start conversations."

    pause 0.8

    mc "Then why talk to me?"

    pause 1.0

    show kuroha sad

    none "…"

    pause 0.8


    none "Because if I waited longer…"

    pause 0.7

    none "someone else would always get there first."

    pause 1.0

    mc "…What does that mean?"

    pause 0.8

    none "You’re always with someone."

    pause 0.5

    none "Aira."

    pause 0.5

    none "And now the library girl too."

    pause 0.8

    mc "You know Reina?"

    none "Not really."

    pause 0.5

    none "I just see her around you now."

    pause 0.8

    n "The way she says it doesn’t sound angry."

    n "Just… quietly disappointed."

    pause 0.7

    menu:
        "You noticed all that?":
            $ kuroha_affection += 1

            mc "You noticed all that just from watching?"

            none "Mm."

            mc "That’s impressive."
            show kuroha s_blush

            none "…Still sounds creepy."

        "You overthink too much":
            mc "You overthink too much."

            pause 0.5

            none "…Maybe."

            pause 0.5

            none "But I kept thinking if I stayed quiet…"

            none "you’d never notice me."

        "That’s kinda cute":
            $ kuroha_affection += 1

            mc "That’s actually kinda cute."

            pause 1.0
            show kuroha full_blush

            none "…Cute?"

            mc "Yeah."

            pause 0.5

            none "…No one says that to me."

    pause 0.8

    mc "So you decided to suddenly talk to me because of that?"

    pause 0.8


    none "…Maybe."

    pause 0.5

    mc "That’s actually kind of funny."

    none "It is?"

    mc "A little."

    pause 0.5

    mc "You make it sound like I’m impossible to approach."

    none "You are."

    mc "I literally just stand around."

    none "Exactly."

    pause 0.7

    n "That answer comes out immediately."

    n "Like she’s thought about it before."

    pause 0.8

    menu:
        "You really are strange":
            $ kuroha_affection += 1

            mc "You really are strange."

            pause 0.5

            show kuroha genuine_smile

            none "…You noticed."

        "I still don’t get you":

            show kuroha normal

            mc "I still don’t understand you."

            pause 0.5

            none "…That’s okay."

            pause 0.5

            k "I don’t really understand myself either."

        "You’re more normal than you think":
            $ kuroha_affection += 1

            mc "You’re more normal than you think."

            pause 0.8

            show kuroha genuine_smile

            none "…Really?"

            mc "Yeah."

            pause 0.5

            none "…"

            pause 0.5

            none "That’s new."

    pause 0.7

    n "The rain slowly starts getting lighter."

    pause 0.5

    mc "Looks like it’s stopping."

    none "Mm."

    pause 0.6

    mc "I’m Ren, by the way."

    pause 0.7

    k "…Kuroha."

    mc "Kuroha, huh."

    pause 0.5

    k "Mm."

    pause 0.7

    menu:
        "It suits you":
            $ kuroha_affection += 1

            mc "It suits you."

            pause 0.8

            show kuroha s_blush

            k "…"

            mc "Why do you look surprised?"

            k "I wasn’t expecting a compliment."

        "Pretty unique":
            $kuroha_affection += 1

            mc "Pretty unique name."

            k "You think so?"

            mc "Yeah."

        "I’ll try to remember it":
            mc "I’ll try to remember it."

            pause 0.5

            show kuroha slight_smile

            k "…I’d like that."

    pause 0.8

    n "For a moment, neither of us moves."

    pause 0.7

    k "…Goodnight, Ren."

    mc "Goodnight."

    pause 0.8

    hide kuroha
    with dissolve

    n "She walks into the rain without looking back."

    pause 0.8

    n "…But this time."

    n "She doesn’t feel like a stranger anymore."

    stop music fadeout 2.0

label kuroha_true_persnolity:
    
    n "after ren left"

    show corner_night
    with fade

    show kuroha sweetSmile at center:
        yalign -1.0
    with dissolve
    
    k "I... I finally spoke to him"

    pause 1.0

    show kuroha yandere
    
    k "ah.... his voice... he... spoke to me"

    k "he is same as when i first met him...."

    k "ah ren...."

    k "you're mineee"

    k "mine only"

    k "no no get yourself together kuroha"

    show kuroha normal 
    
    k "ren......"

label ren_room_night:

    scene mc_room_night:
        zoom 1.5
    with fade

    play music homework fadein 1.5

    n "By the time I get home…"

    n "The rain is gone."

    pause 0.5

    n "Everything feels quieter after it."

    pause 0.7

    n "I drop my bag beside the desk."

    n "The room’s dark except for the desk lamp."

    pause 0.6

    mc "…"

    n "For a second, I just stand there."

    n "Thinking."

    pause 0.8

    n "Aira."

    pause 0.4

    n "Reina."

    pause 0.4

    n "Kuroha."

    pause 0.7

    mc "…Weird day."

    pause 0.8

    n "My eyes drift toward the book inside my bag."

    n "The one Reina told me to finish."

    pause 0.7

    mc "…"

    n "I sit down."

    pause 0.6

    n "Open the book."

    pause 0.8

    n "At first, it’s slow."

    n "Quiet."

    n "Almost frustratingly quiet."

    pause 0.8

    n "But little by little…"

    n "I start noticing things."

    pause 0.7

    n "Small details."

    n "Sentences that felt meaningless before."

    n "Lines repeated in different ways."

    pause 0.7

    n "Like the story was trying to say something indirectly."

    pause 0.8

    mc "…"

    pause 0.7

    n "I keep reading."

    n "Longer than I expected."

    pause 0.8

    n "At some point, I realize something."

    pause 0.7

    mc "I’m actually finishing it."

    pause 1.0

    n "That almost makes me laugh."

    pause 0.8

    n "Reina would probably say:"
    
    pause 0.5

    r "I told you so."

    pause 0.8

    mc "…Yeah."

    pause 0.7

    n "I close the book."

    n "The room feels smaller at night."

    pause 0.7

    n "Quieter too."

    pause 0.8

    n "Outside, a car passes somewhere far away."

    n "Then everything goes still again."

    pause 1.0

    mc "…"

    n "For a second…"

    n "I think about the shelter."

    pause 0.7

    n "About Kuroha standing there like she’d always been there."

    pause 0.8

    mc "She really was strange."

    pause 0.8

    n "But not unpleasant."

    pause 1.0

    n "Eventually, exhaustion catches up."

    pause 0.7

    scene black
    with fade

    n "I fall asleep thinking about unfinished things."

    stop music fadeout 2.0



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

    n "So I leave the classroom before someone tries to drag me into conversation."

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

    n "She shifts slightly on the bench."

    n "Like she was making space before I even arrived."

    pause 0.8

    mc "What are you doing back here?"

    pause 0.6

    k "Eating lunch."

    mc "Alone?"

    k "Usually."

    pause 0.7

    mc "This place is kinda hidden."

    pause 0.5

    k "That’s why I like it."

    pause 0.8

    n "There’s a small convenience store sandwich beside her."

    n "Untouched."

    pause 0.6

    mc "You haven’t eaten yet."

    k "I was waiting."

    pause 0.8

    mc "…Waiting?"

    pause 0.6

    k "For you."

    pause 1.0

    mc "That’s a little concerning."

    k "Sorry."

    mc "You always say sorry after saying something weird."

    pause 0.7

    k "Because you always call it weird."

    pause 0.8

    n "I sit on the other side of the bench."

    pause 0.5

    n "Kuroha glances at the distance between us."

    pause 0.6

    k "…You sat far away."

    mc "There’s literally space for one more person between us."

    k "Mm."

    pause 0.7

    n "She sounds oddly disappointed."

    pause 0.8

    mc "Did you know I’d come here?"

    pause 0.6

    scene backschool_day:
        zoom 1.5
    with fade

    show kuroha normal at center:
        yalign -1.0
    with dissolve

    k "I thought you might."

    mc "Why?"

    pause 0.5

    k "You look for quiet places when there’s too many people."

    pause 0.9

    mc "…"

    mc "You notice too much."

    pause 0.6

    k "Only about you."

    pause 1.0

    mc "That does NOT make it better."

    pause 0.7

    show kuroha genuine_smile

    n "Kuroha smiles faintly."

    n "Like she already expected that reaction."

    pause 0.8

    mc "So what?"

    mc "You’ve just been secretly observing me this whole time?"

    pause 0.7

    k "Not secretly."

    mc "Kuroha."

    k "…Mostly secretly."

    pause 0.8

    n "I almost laugh."

    pause 0.6

    mc "You’re honest about really strange things."

    pause 0.7

    k "You don’t get angry."

    mc "Should I be?"

    pause 0.8

    k "…I’d rather you weren’t."

    pause 0.9

    n "There’s something unexpectedly soft in that answer."

    pause 0.7

    menu:

        "Move a little closer":
            $ kuroha_affection += 2

            n "I shift slightly closer on the bench."

            pause 0.6

            n "Kuroha immediately notices."

            show kuroha s_blush

            k "…"

            mc "What?"

            pause 0.5

            k "Nothing."

            pause 0.5

        "Ask why she notices you so much":
            $ kuroha_affection += 1

            mc "Seriously though."

            mc "Why me?"

            pause 0.7

            k "I wil tell you one day"

            k "but for now its a secrete"

            k "after saw you in my school"

            k "And i noticed you once."

            pause 0.5

            k "Then I kept noticing you."

            pause 0.9

            mc "That sounds dangerously close to obsession."

            show kuroha s_blush

            k "…Maybe a little."

        "Tease her":
            $ kuroha_affection += 1

            mc "You sound like a stray cat that decided I belong to it."

            pause 0.7

            show kuroha sweetSmile

            k "…"

            pause 0.5

            k "That’s not completely wrong."

            pause 1.0

            mc "You admitted that WAY too easily."

            show kuroha slight_smile

    pause 0.8

    n "The wind moves softly through the trees behind us."

    pause 0.6

    n "For someone so quiet…"

    n "Kuroha somehow makes the silence feel full instead of empty."

    pause 0.8

    n "The wind moves softly through the trees behind us."

    pause 0.6

    n "Kuroha quietly unwraps her sandwich."

    pause 0.5

    n "Then stops halfway."

    pause 0.7

    k "…You came later than usual today."

    mc "You keep track of that too?"

    pause 0.5

    k "Mm."

    mc "That’s actually starting to sound dangerous."

    pause 0.8

    show kuroha s_blush

    k "I just notice things about you."

    mc "That’s not a normal amount of noticing."

    pause 0.7

    k "Maybe not."

    pause 0.8

    n "She says it without embarrassment."

    n "Almost like she doesn’t see the problem."

    pause 0.9

    mc "So what?"

    mc "Do you just watch me all day?"

    pause 0.7

    k "Not all day."

    pause 0.5

    k "Just when I can."

    pause 1.0

    mc "Kuroha."

    pause 0.6

    k "…Sorry."

    mc "You really make that word work overtime."

    pause 0.7

    n "She quietly takes a bite of her sandwich."

    pause 0.6

    k "You sit by the window during morning class."

    pause 0.5

    k "You stop paying attention after around twenty minutes."

    pause 0.5

    k "And when Aira talks to other people…"

    pause 0.5

    k "you look out the window instead of joining."

    pause 1.0

    mc "…Okay."

    mc "Now you sound like a stalker."

    pause 0.7

    show kuroha sad

    k "That’s bad, right?"

    mc "Very."

    pause 0.5

    k "Oh."

    pause 0.8

    n "She actually looks bothered by that."

    pause 0.6

    mc "…You really don’t realize how weird you sound sometimes?"

    pause 0.7

    k "Not until after I say it."

    pause 0.8

    mc "Amazing."

    pause 0.7

    n "Kuroha lowers her gaze for a moment."

    pause 0.5

    k "I tried not to talk to you before."

    pause 0.8

    mc "Before?"

    pause 0.5

    k "Mm."

    pause 0.6

    k "But then you started spending time with more people."

    pause 0.5

    k "Aira."

    pause 0.5

    k "The library girl."

    pause 0.8

    k "And I thought…"

    pause 0.7

    show kuroha s_blush

    k "if I waited longer…"

    pause 0.6

    k "you’d never notice me."

    pause 1.2

    mc "…"

    n "That answer comes out quieter than the others."

    pause 0.8

    mc "So this whole thing is because you got impatient?"

    pause 0.6

    show kuroha genuine_smile

    k "Mm."

    mc "That’s insane."

    pause 0.5

    k "A little."

    pause 0.8

    n "And somehow…"

    n "she sounds proud of it."

    pause 0.9

    mc "You know what the worst part is?"

    pause 0.5

    k "…?"

    mc "You say all this with a completely straight face."

    pause 0.7

    show kuroha sweetSmile

    k "Would it be better if I smiled more?"

    pause 0.8

    mc "That somehow makes it worse."

    pause 0.7

    n "Kuroha quietly laughs under her breath."

    pause 0.8

    n "Small."

    n "Soft."

    n "But definitely real."

    pause 0.9

    k "…Ren?"

    mc "Hm?"

    pause 0.5

    k "Come here again tomorrow."

    pause 0.9

    mc "Still assuming I will?"

    pause 0.6

    k "You probably will."

    pause 0.5

    k "You always come to quiet places eventually."

    pause 0.8

    k "So I’ll be here first."

    pause 1.0

    mc "That sounds like a threat."

    pause 0.5

    k "It’s not."

    pause 0.6

    k "Probably."

    pause 1.0

    n "…Yeah."

    n "Definitely strange."
    
    mc "Bye..."

    k "See you tommorow...."

    jump afternoon_transition

label afternoon_transition:

    scene classroom_afternoon
    with fade

    play music sweet fadein 1.5

    n "The rest of the afternoon passes slowly."

    pause 0.6

    n "Teachers talk."

    n "Pages turn."

    n "Someone yawns near the window."

    pause 0.8

    mc "…"

    pause 0.7

    if free_choice == "aira":

        n "For some reason…"

        n "I keep remembering Aira’s face during lunch."

        pause 0.8

        n "That stupid proud smile she makes when she wins an argument."

    elif free_choice == "reina":

        n "My thoughts drift back to the library."

        pause 0.8

        n "And Reina quietly smiling behind her book."

    elif free_choice == "kuroha":

        n "I keep thinking about the bench behind the school."

        pause 0.8

        n "\"You probably will.\""

        pause 0.7

        n "That weird confidence in Kuroha’s voice still lingers."

    pause 0.8

    n "The final bell finally echoes through the classroom."

    n "Another school day ends."

    stop music fadeout 1.5

    jump evening_transition

label evening_transition:

    scene school_gate_evening:
        zoom 1.5
    with fade

    play music sweet fadein 1.5

    n "By the time I leave the classroom…"

    n "the sky is already starting to change."

    pause 0.7

    n "Students slowly scatter in different directions."

    n "Some head to clubs."

    n "Some rush home."

    pause 0.8

    n "The school feels quieter now."

    pause 0.7

    mc "…"

    pause 0.6

    if free_choice == "aira":

        show aira happy at left:
            yalign -1.0
        with dissolve

        a "You took forever."

        mc "You waited?"

        a "Obviously."

        pause 0.5

        a "Who else is gonna walk home with you?"

        pause 0.7

        mc "You say that like I’ll collapse alone."

        show aira pout

        a "You probably would."

        pause 0.8

        n "She says it immediately."

        n "Without even thinking about it."

        pause 0.7

        hide aira
        with dissolve

    elif free_choice == "reina":

        n "As I pass the hallway near the library…"

        pause 0.7

        show reina normal at center:
            yalign -1.0
        with dissolve

        r "Going home?"

        mc "Eventually."

        pause 0.5

        r "…You kept staring at the same page earlier."

        mc "You noticed that?"

        pause 0.6

        r "Mm."

        pause 0.5

        r "You looked distracted."

        pause 0.7

        mc "Maybe your book’s too difficult."

        show reina slight_smile

        r "Or maybe you’re just bad at focusing."

        pause 0.8

        n "…Fair enough."

        hide reina
        with dissolve

    elif free_choice == "kuroha":

        n "I slow down near the back gate for some reason."

        pause 0.8

        n "…And immediately regret it."

        pause 0.7

        show kuroha normal at right:
            yalign -1.0
        with dissolve

        k "You came."

        mc "You make it sound like this was planned."

        pause 0.5

        k "Mm."

        pause 0.6

        mc "That answer is concerning."

        show kuroha sweetSmile

        k "You still stopped walking."

        pause 0.8

        n "…She has a point."

        hide kuroha
        with dissolve

    pause 0.9

    n "The evening air feels cooler now."

    pause 0.7

    n "Another normal day should be ending."

    pause 0.8

    n "But lately…"

    n "things don’t feel as routine anymore."

    stop music fadeout 1.5

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

    n "I reach for my phone."

    n "Scroll aimlessly for a while."

    pause 0.7

    n "Random videos."

    n "Random posts."

    n "Nothing interesting."

    pause 0.8

    mc "…"

    pause 0.7

    n "Eventually, I put it away."

    pause 0.8

    n "The ceiling stays dark and quiet above me."

    pause 1.0

    n "Another normal day ends."

    pause 0.8

    scene black
    with fade

    n "And tomorrow will probably be the same."

    stop music fadeout 2.0

    jump next_morning


