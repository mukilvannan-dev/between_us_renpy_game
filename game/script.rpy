# ==============================================================================
# Between Us - Main Script Entry Point
# ==============================================================================
#
# Project Architecture:
# - game/definitions/
#     characters.rpy  : Character declarations, affection meters, sprite mappings
#     images.rpy      : Backgrounds, CGs, and menu images
#     audio.rpy       : BGM and SFX audio channels
#
# - game/story/
#     day1.rpy        : Prologue & Day 1 (label start)
#     day2.rpy        : Day 2 (label day2_morning)
#     day3.rpy        : Day 3 (label morning_classroom_scene)
#
# ==============================================================================

label splashscreen:
    scene black
    $ renpy.pause(0.5, hard=True)

    show title with dissolve
    $ renpy.pause(3, hard=True)

    scene black with dissolve
    $ renpy.pause(1, hard=True)

    scene black
    $ renpy.pause(0.5, hard=True)

    play sound gorogoro
    show mukil_presents with dissolve
    $ renpy.pause(3, hard=True)

    scene black with dissolve
    $ renpy.pause(1, hard=True)

    return
