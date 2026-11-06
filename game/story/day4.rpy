# ==============================================================================
# Story - Day 4
# ==============================================================================

label day4_morning:

    scene black
    with fade

    pause 1.0

    if free_choice == "kuroha":
        play music creepy fadein 2.0
        
        n "My eyes open before the alarm even sounds."
        
        pause 0.6
        
        scene mc_room_day:
            zoom 1.5
        with fade

        n "Morning light cuts across the floorboards in thin, pale slats."
        
        pause 0.5
        
        n "The room is quiet. Completely still."
        
        n "Just like it was last night."
        
        pause 0.7
        
        n "I sit up, staring at the nightstand."
        
        pause 0.8
        
        n "Her words from the text message linger in the air like smoke."
        
        n "{i}Your emergency contact sheet was right in the front pocket.{/i}"
        
        pause 0.8
        
        n "I slowly push the blanket aside and walk over to my school bag."
        
        n "I reach inside and pull out my student handbook."
        
        pause 0.7
        
        n "The clear plastic sleeve in the front cover."
        
        n "The paper inside is still there. Folded."
        
        pause 0.6
        
        n "She actually touched it."
        
        n "She stood right beside my empty desk during second period... while I was just down the hall."
        
        pause 0.9
        
        mc "…"
        
        mc "She was completely serious."
        
        pause 0.8
        
        n "A cold shiver runs down my spine."
        
        n "She told me to come back to the bench behind the school today."
        
        n "Like it was already decided."
        
        pause 1.0

        stop music fadeout 2.0

    elif free_choice == "reina":
        play music morning_room fadein 1.5
        
        scene mc_room_day:
            zoom 1.5
        with fade
        
        n "The gentle hum of the morning wakes me before the alarm goes off."
        
        pause 0.6
        
        n "I blink against the soft sunlight spilling across my pillow."
        
        pause 0.7
        
        n "I reach out and pick up my phone from the nightstand."
        
        n "Reina's message is still on the screen."
        
        pause 0.8
        
        n "{i}You left your bookmark at the counter. Don't lose your place in the book tomorrow.{/i}"
        
        pause 0.7
        
        n "I check my jacket pocket on the back of the chair."
        
        n "Empty."
        
        pause 0.5
        
        n "A faint, quiet smile pulls at the corner of my mouth."
        
        mc "She actually kept it."
        
        pause 0.7
        
        n "The memory of the quiet library from yesterday comes back with surprising clarity."
        
        n "Her asleep by the window. The steady tick of the clock."
        
        pause 0.8
        
        n "I'll have to stop by the library to pick it up."
        
        pause 0.9
        
        stop music fadeout 1.5

    else:
        # free_choice == "aira"
        play music morning_casual fadein 1.5
        
        scene mc_room_day:
            zoom 1.5
        with fade
        
        n "The sharp buzz of my alarm jolts me awake."
        
        pause 0.5
        
        mc "Ugh..."
        
        pause 0.5
        
        n "I grab my phone, fumbling to shut off the ringing."
        
        n "Right under the alarm banner is Aira's message from last night."
        
        pause 0.7
        
        n "{i}Don't be late tomorrow morning or I'm leaving you.{/i}"
        
        pause 0.6
        
        mc "Shoot. What time is it...?"
        
        pause 0.5
        
        n "I check the clock. If I don't leave in ten minutes, she actually will."
        
        pause 0.6
        
        n "I quickly pull on my uniform, grab my bag, and head downstairs."
        
        pause 0.8
        
        stop music fadeout 1.5

# ==============================================================================
# The Morning Walk
# ==============================================================================

if free_choice == "aira":
    scene school_road:
        zoom 1.0
    with fade
    
    play music morning_casual fadein 1.5
    
    n "The morning breeze is cool, shaking the leaves along the path."
    
    pause 0.6
    
    n "At the corner where the street bends toward the main road, someone is already leaning against the stone wall."
    
    pause 0.7
    
    show aira pout at center:
        yalign -1.0
    with dissolve
    
    n "Aira."
    
    pause 0.5
    
    n "She's tapping the toe of her shoe against the pavement, looking down at her watch."
    
    pause 0.7
    
    mc "I made it."
    
    pause 0.5
    
    a "By two minutes."
    
    show aira neutral
    
    a "I was literally thirty seconds away from walking off."
    
    mc "You say that every single time."
    
    show aira happy
    
    a "One of these days I'll actually do it, and you'll be crying alone at the crosswalk."
    
    mc "I think I'd survive."
    
    show aira pout
    
    a "Rude."
    
    pause 0.6
    
    n "She pushes off the wall and falls into step beside me."
    
    pause 0.7
    
    show aira neutral
    
    a "You look less like a ghost today, at least."
    
    mc "Thanks. High praise."
    
    a "Don't get used to it."
    
    pause 0.7
    
    n "We walk side by side toward the school gate, the familiar rhythm of our steps keeping time."
    
    pause 0.8
    
    scene school_gate:
        zoom 1.0
    with fade
    
    n "Students are pouring through the gate in noisy clumps."
    
    hide aira

elif free_choice == "reina":
    scene school_road_without_rain:
        zoom 1.0
    with fade
    
    play music morning_casual fadein 1.5
    
    n "The road to school is quieter than yesterday."
    
    n "The clouds from yesterday have cleared out, leaving a pale, washed-out blue sky."
    
    pause 0.7
    
    n "I walk at an unhurried pace, watching the morning commuters rush past."
    
    pause 0.8
    
    scene school_gate:
        zoom 1.0
    with fade
    
    n "As I reach the school gate, my eyes instinctively drift toward the second floor of the east wing."
    
    pause 0.6
    
    n "The library."
    
    pause 0.7
    
    n "Through the large glass windows, the rows of dark wooden bookshelves stand silent."
    
    n "The morning sun reflects softly off the glass."
    
    pause 0.6
    
    mc "She's probably already in there..."
    
    pause 0.8
    
    n "I tighten my grip on my bag strap and step through the gates."

else:
    # free_choice == "kuroha"
    scene school_road:
        zoom 1.0
    with fade
    
    play music uncertainity fadein 1.5
    
    n "I keep my hands shoved deep inside my pockets as I walk."
    
    pause 0.6
    
    n "Every passing uniform on the sidewalk makes me look twice."
    
    pause 0.7
    
    n "Every pair of footsteps behind me feels slightly closer than it should be."
    
    pause 0.7
    
    mc "Get a grip. She's just a student."
    
    pause 0.6
    
    n "I say that to myself, but the rationalization feels thin."
    
    pause 0.8
    
    scene school_gate:
        zoom 1.0
    with fade
    
    n "I reach the front gate where the morning crowd bottlenecks."
    
    pause 0.6
    
    n "And then... I stop."
    
    pause 0.8
    
    show kuroha normal2 at right:
        yalign -1.0
    with dissolve
    
    n "Standing just beside the brick pillar near the bike racks."
    
    pause 0.7
    
    n "Kuroha."
    
    pause 0.6
    
    n "She's holding the straps of her bag with both hands, watching the crowd."
    
    pause 0.7
    
    n "Her eyes scan across the gate... and land directly on me."
    
    pause 0.8
    
    show kuroha sweetSmile
    
    n "She doesn't flinch. She doesn't look away."
    
    pause 0.6
    
    n "She just gives me a small, calm nod. Sincere. Welcoming."
    
    pause 0.8
    
    show kuroha normal2
    
    n "Then, as smoothly as she appeared, she turns and blends into the stream of students heading inside."
    
    hide kuroha with dissolve
    
    pause 0.8
    
    mc "…"
    
    n "My pulse quickens."
    
    n "She was waiting to see if I'd show up."

# ==============================================================================
# Homeroom & Morning Classes
# ==============================================================================

scene classroom_day:
    zoom 1.0
with fade

play music classroom_casual fadein 1.5

n "The morning bell echoes through the corridors, cutting off the noise in the hallway."

pause 0.6

n "I take my seat near the middle of the room, pulling out my notebook and pencil case."

pause 0.7

show aira neutral at left:
    yalign -1.0
with dissolve

if free_choice == "aira":
    a "Don't forget we have that pop quiz in third period."
    
    mc "Since when do you remind people about quizzes?"
    
    show aira pout
    
    a "Since I didn't study either, so if you fail too, the class average goes down."
    
    mc "That's diabolical."
    
    show aira happy
    
    a "Survival of the fittest."

else:
    a "Hey, Ren."
    
    pause 0.5
    
    a "You looked distracted walking in today."
    
    mc "Just thinking."
    
    show aira pout
    
    a "You think too much. It's bad for your brain."
    
    mc "I'll keep that in mind."

pause 0.8

hide aira with dissolve

n "The homeroom teacher slides open the door with a loud clatter, carrying a stack of handouts."

pause 0.7

n "Classes begin."

pause 1.0

scene classroom_day
with dissolve

n "First period."

pause 0.5

n "Second period."

pause 0.6

n "The morning drags along to the rhythmic scraping of chalk on the blackboard."

pause 0.8

if free_choice == "reina":
    n "During the ten-minute passing period between second and third period, I stand up and stretch."
    
    n "Through the hallway window, I catch a brief glimpse of Reina walking past with a stack of catalog slips in her arms."
    
    n "She looks as detached as ever, completely tuned out of the loud conversations around her."
    
    pause 0.6
    
    n "She doesn't turn toward my classroom."
    
    n "But I remember the bookmark."
    
    pause 0.8

elif free_choice == "kuroha":
    n "During the passing period, every time someone brushes past my desk, I instinctively look up."
    
    pause 0.6
    
    n "Kuroha isn't in my class, but her presence feels like a faint chill against the back of my neck."
    
    pause 0.7
    
    n "{i}'Come back to this bench tomorrow...'{/i}"
    
    pause 0.7
    
    n "The third period bell rings before I can dwell on it any longer."

else:
    n "Aira turns around every now and then to doodle in the margins of her notebook, showing me terrible caricatures of the history teacher."
    
    pause 0.6
    
    n "It feels like our usual rhythm."
    
    pause 0.7

# ==============================================================================
# Lunch Break - The Decision Point
# ==============================================================================

scene classroom_day
with fade

stop music fadeout 2.0
pause 0.5

n "The noon chime rings loud and clear across the school."

play music classroom_casual fadein 1.5

pause 0.6

n "In seconds, the quiet classroom erupts into chatter."

n "Chairs scrape back. Lunch bags are unzipped."

pause 0.7

show aira neutral at left:
    yalign -1.0
with dissolve

a "Finally. Freedom."

pause 0.5

show aira pout

a "So? What's the plan for lunch today, Ren?"

pause 0.7

mc "…"

n "I pause, sitting back in my chair."

pause 0.8

# [DAY 4 LUNCH CHOICE]
# You can now specify what each path should contain!
menu:
    "Eat lunch with Aira":
        $ free_choice_day4 = "aira"
        jump day4_lunch_aira

    "Go to the library":
        $ free_choice_day4 = "reina"
        jump day4_lunch_reina

    "Walk around behind the school":
        $ free_choice_day4 = "kuroha"
        jump day4_lunch_kuroha

# Temporary placeholders for the branches
label day4_lunch_aira:
    n "To be continued in Aira's Day 4 branch..."
    return

label day4_lunch_reina:
    n "To be continued in Reina's Day 4 branch..."
    return

label day4_lunch_kuroha:
    n "To be continued in Kuroha's Day 4 branch..."
    return
