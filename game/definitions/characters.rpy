# ==============================================================================
# Characters & State Definitions
# ==============================================================================

# Text speed configuration
define config.default_text_cps = 35
default preferences.text_cps = 35

# ADV Dialogue Characters
define mc = Character("Ren", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define n = Character(None, what_slow_cps=35)
define none = Character("???", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define a = Character("Aira", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define r = Character("Reina", what_prefix="\"", what_suffix="\"", what_slow_cps=35)
define k = Character("Kuroha", what_prefix="\"", what_suffix="\"", what_slow_cps=35)

# Phone / NVL Dialogue Characters
define mc_nvl = Character("Ren", kind=nvl, callback=Phone_SendSound)
define a_nvl = Character("Aira", kind=nvl, callback=Phone_ReceiveSound)
define r_nvl = Character("Reina", kind=nvl, callback=Phone_ReceiveSound)
define k_nvl = Character("Kuroha", kind=nvl, callback=Phone_ReceiveSound)

# NVL Transitions
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# Story & Affection Variables
default aira_affection = 0
default reina_affection = 0
default kuroha_affection = 0
default free_choice = None

# ==============================================================================
# Character Sprites
# ==============================================================================

# Aira Sprites
image aira neutral = "images/characters/Aira/aira_nuetral.png"
image aira happy = "images/characters/Aira/aira_happy.png"
image aira pout = "images/characters/Aira/aira_pout.png"
image aira concerned = "images/characters/Aira/aira_concerned.png"
image aira twisted = "images/characters/Aira/aira_twisted.png"
image aira cry = "images/characters/Aira/aira_cry.png"
image aira embarrassed = "images/characters/Aira/aira_embarassed.png"
image aira full_blush = "images/characters/Aira/aira_full_blush.png"

# Reina Sprites
image reina normal = "images/characters/reina/reina_normal.png"
image reina smile = "images/characters/reina/smile_reina.png"
image reina sad = "images/characters/reina/sad_reina.png"
image reina curiosity = "images/characters/reina/curiosity_reina.png"
image reina embarrassed = "images/characters/reina/reina_embarassed.png"
image reina pout = "images/characters/reina/reina_pout.png"
image reina slight_smile = "images/characters/reina/reina_slightSmile.png"

# Kuroha Sprites
image kuroha normal = "images/characters/kuroha/kuroha_normal_1.png"
image kuroha blush = "images/characters/kuroha/kuroha_blush.png"
image kuroha s_blush = "images/characters/kuroha/kuroha_slight_blush.png"
image kuroha sad = "images/characters/kuroha/kuroha_sad.png"
image kuroha full_blush = "images/characters/kuroha/kuroha_full_blush.png"
image kuroha genuine_smile = "images/characters/kuroha/kuroha_genuine_smile.png"
image kuroha yandere = "images/characters/kuroha/kuroha_yandere.png"
image kuroha sweetSmile = "images/characters/kuroha/kuroha_sweet_smile.png"
image kuroha extreme = "images/characters/kuroha/kuroha_extreme.png"
image kuroha normal2 = "images/characters/kuroha/kuroha_normal_2.png"
