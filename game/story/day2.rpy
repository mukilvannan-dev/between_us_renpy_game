# ==============================================================================
# Story - Day 2
# ==============================================================================

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
    pause 0.6
    scene black
    with fade
    play music bgm_rain fadein 1.5

    n "Rain starts just as I leave the school building."

    pause 0.5

    mc "…Seriously?"

    pause 0.5

    n "Not heavy."

    n "Just enough to make walking home annoying."

    pause 0.7

    n "I move under the small shelter near the gate, pulling my collar up."

    pause 0.8

    scene kuroha_cg_shelter:
        zoom 1.5
    with fade

    n "…And freeze for a second."

    pause 0.7

    n "It’s her."

    n "The quiet girl from before. She’s leaning against the pillar, looking out into the gray rain."

    pause 0.8

    mc "…Oh."

    pause 0.5

    none "You took the long way down the hall today."

    pause 0.8

    menu:
        "You remember that?":
            $kuroha_affection +=1

            mc "Wait… you notice stuff like that?"

            none "Mm. You usually walk past the courtyard, but you used the science wing stairs today."

            mc "That’s kinda impressive."

            none "…Is it? I just… like paying attention to things."

        "That’s a little creepy":
            mc "That’s... honestly a little creepy."

            none "…Sorry."

            mc "You apologize really fast."

            none "I don't want you to think badly of me. I just happen to remember things."

        "You were waiting here?":

            mc "Were you waiting here for the rain to stop?"

            pause 0.5

            none "No."

            pause 0.5

            none "…I was just waiting for you to come out."

    pause 0.8

    n "Rain taps softly against the roof above us."

    n "She shifts a little closer, her eyes locked onto the pavement between us."

    pause 0.7

    mc "So do you always stand around in random places?"

    pause 0.5

    none "Not random places."

    mc "Then?"

    pause 0.5

    none "Just places where I know I can see you."

    pause 1.0

    mc "…That sounds a little intense."

    none "I didn’t mean it badly. It’s just comfort, I guess."

    pause 0.6

    mc "Comfort?"

    pause 0.7

    none "…"

    pause 0.8

    none "The school is very loud. But when I look at you, everything feels quiet."

    pause 1.0

    mc "We don’t even know each other."

    pause 0.5

    none "I know."

    pause 0.5

    menu:
        "Then why notice me?":

            mc "Then why look at me at all? I’m completely ordinary."

            pause 0.8

            none "…"

            pause 0.5

            none "Ordinary people don't make me feel like this."

            mc "Like what?"

            none "Like nothing else matters."

        "You say strange things":

            $kuroha_affection +=1

            mc "You say things like that completely casually, you know that?"

            pause 0.5

            none "Sorry."

            mc "See? There it is again."

            pause 0.5

            none "…I’m not very good at talking to people. My heart beats too fast."

        "I’m just a normal guy":
            mc "I’m literally just some guy."

            none "Mm."

            pause 0.5

            none "That’s what I like about you. You don't realize how much space you take up in my mind."

    pause 0.7

    none "But you’ve looked tired lately, Ren."

    pause 0.5

    none "Your posture is different when you're thinking about someone else."

    pause 0.8

    mc "That’s... pretty specific. How could you possibly tell that?"

    none "Because I know exactly how you look when you're just being yourself."

    pause 0.7

    n "She says it softly, with a small, gentle smile."

    n "But her eyes don't blink. They are heavy, focused entirely on my face."

    pause 0.8

    mc "Have you been watching me or something?"

    pause 0.7

    none "…That sounds a bit dramatic, doesn't it?"

    mc "I mean, it sounds like you're tracking me."

    pause 0.5

    none "I just care. More than other people do."

    pause 0.6

    mc "Other people?"

    none "The people who take you for granted."

    pause 0.7

    n "I study her face for a second. There's no malice there, just a strange, absolute sincerity."

    pause 0.6

    scene school_shelter:
        zoom 1.5
    show kuroha normal at center:
        yalign -1.0
    with dissolve

    menu:
        "You’re kinda funny":

            $kuroha_affection +=1

            mc "You’re kinda funny. You say the most intense things with a straight face."

            pause 0.5

            none "…Am I being weird?"

            mc "Maybe a little. But it’s better than you being mean."

            pause 0.5

            none "…I could never be mean to you. I wouldn't dare."

        "You’re really awkward":

            $kuroha_affection+=1
            mc "You’re really awkward, aren't you?"

            pause 0.5

            none "…Probably. I think about talking to you all the time, but my mind goes blank when it actually happens."

            mc "At least you’re honest about it."

        "You nervous or something?":

            mc "Are you nervous right now? Your voice is shaking a bit."

            pause 0.8

            none "…A little."

            mc "Why? We're just talking."

            pause 0.5

            none "Because you're finally looking back at me."

    pause 0.8

    mc "So... why did you decide to step out and talk to me today?"

    pause 1.0

    show kuroha sad

    none "…"

    pause 0.8

    none "Because if I waited longer…"

    pause 0.7

    none "I was worried someone else would take all your time."

    pause 1.0

    mc "…What does that mean?"

    pause 0.8

    none "You're always giving your attention away."

    pause 0.5

    none "Aira."

    pause 0.5

    none "And that girl in the library. Reina."

    pause 0.8

    mc "You know Reina?"

    none "I saw her give you that book. She stayed close to you for a long time."

    pause 0.5

    none "I didn’t like how she looked at you. Like she thought she understood you."

    pause 0.8

    n "Her voice doesn't change, but the temperature in the air suddenly feels lower."

    n "She says it with the calm disappointment of someone stating a simple fact."

    pause 0.7

    menu:
        "You noticed all that?":
            $ kuroha_affection += 1

            mc "You noticed all that just from across the room?"

            none "Mm. I notice everything that involves you."

            mc "That’s... dynamic."
            show kuroha s_blush

            none "…I just want to be the one who knows you best."

        "You overthink too much":
            mc "You overthink things too much. They're just my friends."

            pause 0.5

            none "…Maybe."

            pause 0.5

            none "But friends can be replaced. I don't want to just be a friend."

        "That’s kinda cute":
            $ kuroha_affection += 1

            mc "The fact that you’re worrying over something like that is actually kind of cute."

            pause 1.0
            show kuroha full_blush

            none "…Cute? You think I'm cute?"

            mc "Yeah. In a quiet sort of way."

            pause 0.5

            none "…Good. Then keep your eyes on me. Just me."

    pause 0.8

    mc "You talk like you’ve been planning this conversation for a while."

    pause 0.8

    none "…Maybe a little."

    pause 0.5

    mc "Well, you don't have to worry. I’m not going anywhere."

    none "I know."

    mc "You do?"

    none "Mm. Because I won't let you."

    pause 0.7

    n "She laughs softly right after saying it, a small, airy sound."

    n "It feels like a joke. But her eyes stay completely still."

    pause 0.8

    menu:
        "You really are strange":
            $ kuroha_affection += 1

            mc "You really are a strange girl."

            pause 0.5

            show kuroha genuine_smile

            none "…Is that a bad thing?"

            mc "Not necessarily. Just... different."

        "I still don’t get you":

            show kuroha normal

            mc "I still don’t really understand you."

            pause 0.5

            none "…That’s okay."

            pause 0.5

            none "You don’t have to understand me. Just get used to me."

        "You’re more normal than you think":
            $ kuroha_affection += 1

            mc "You’re trying so hard to sound mysterious, but you're probably just a normal girl."

            pause 0.8

            show kuroha genuine_smile

            none "…Do you really think so?"

            mc "Yeah. Just a little shy."

            pause 0.5

            none "…"

            pause 0.5

            none "If that makes you comfortable... then yes. I'm completely normal."

    pause 0.7

    n "The lunch bell cuts through the air, signaling the end of the break."

    pause 0.5

    mc "Looks like it’s over. I should probably get back to home."

    none "Mm."

    pause 0.6

    mc "By the way... I never got your name."

    pause 0.7

    none "…"

    pause 0.5

    show kuroha genuine_smile

    none "Kuroha."

    mc "Kuroha, huh."

    pause 0.5

    k "Mm."

    pause 0.7

    menu:
        "It suits you":
            $ kuroha_affection += 1

            mc "It suits you. Quiet, but it stays with you."

            pause 0.8

            show kuroha s_blush

            k "…"

            mc "What’s wrong?"

            k "Nothing. I’m just going to keep thinking about you saying that all night."

        "Pretty unique":
            $ kuroha_affection += 1

            mc "Pretty unique name. Definitely won't forget it."

            k "Good. I want to be a permanent fixture in your mind."

        "I’ll try to remember it":
            mc "I’ll try to remember it."

            pause 0.5

            show kuroha slight_smile

            k "…You will. I’ll make sure we talk again soon."

    pause 0.8

    n "She takes a half-step back, melting smoothly into the shadow of the brick gate."

    pause 0.7

    k "…Have a safe walk home, Ren. Don't look back."

    mc "Uh, alright. Goodnight."

    pause 0.8

    hide kuroha
    with dissolve

    n "She turns and walks into the drizzling evening, her movements quiet and graceful."

    pause 0.8

    n "…But as I start walking away, a strange feeling settles in my chest."

    n "She didn’t ask for my number. She didn't ask where I live."

    n "Yet, I get the distinct impression that she already knows exactly where I’m going."

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

    jump morning_classroom_scene
