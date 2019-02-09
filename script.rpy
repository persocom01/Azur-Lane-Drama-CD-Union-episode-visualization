# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define la = Character("Laffey", color="#AAED60")
define mc = Character("McCall", color="#AAED60")
define li = Character("Long Island", color="#AAED60")
define sd = Character("San Diego", color="#AAED60")


# The game starts here.

default box = 1

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    window hide
    scene black
    show skip at skip_button, skip_button_animation onlayer ontop
    show opening_text "Azur Lane Drama CD Union Episode\n\nPart 1" with Dissolve(2)
    hide opening_text with Dissolve(2)
    scene bg beach
    show skip at skip_button, skip_button_animation onlayer ontop
    show next at next_prompt, next_prompt_animation onlayer ontop
    with Fade(0, 0, 2)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show laffey dark at center
    show laffey with dis

    # These display lines of dialogue.

    la "This is good ice cream, McCall. Thanks."

    window hide
    show laffey:
        linear 0.5 xpos 270
    show laffey dark with dissolve
    show laffey dark:
        xpos 270
    show mccall dark at right
    show mccall with dis
    $ box = 2

    mc "Don’t mention it. I just wanted my good friend Laffey to know how great it is to eat popsicles on the beach under a parasol."

    show mccall dark
    with dis
    show laffey
    with dis
    $ box = 1

    la "Uh huh. It’s really great."

    show laffey dark
    with dis
    show mccall
    with dis
    $ box = 2

    mc "Right? Nothing better than wasting your day off eating ice cream until the sun sets."

    show mccall dark
    with dis
    show laffey
    with dis
    $ box = 1

    la "But it’s only 10AM. Ice cream is great and all, but won’t you get a stomach ache eating that much?"

    show laffey dark
    with dis
    show mccall
    with dis
    $ box = 2

    mc "Nope. I’ve got an iron gut when it comes to ice cream."

    show mccall dark
    with dis
    show laffey
    with dis
    $ box = 1

    la "Iron gut? Not a second stomach?"

    show laffey dark
    with dis
    show mccall
    with dis
    $ box = 2

    mc "Yeah. My stomach is strong as iron!"

    show mccall dark
    with dis
    show laffey
    with dis
    $ box = 1

    la "Lucky. I think two or three is my limit. Like how I could barely eat anything at the mushroom party yesterday. It sucked."

    show laffey dark
    with dis
    show mccall
    with dis
    $ box = 2

    mc "I don’t really care for mushrooms either. But hey, at least you can drink me under the table, Laffey."

    show mccall dark
    with dis
    show laffey
    with dis
    $ box = 1

    la "That’s true."

    show laffey dark
    with dis
    show mccall
    with dis
    $ box = 2

    mc "It’s hard to fill up on your favorite things, but if you get too greedy, you’ll pay for it in the end. As for mushrooms, you might be better off not eating too many."

    show mccall dark
    with dis
    show laffey
    with dis
    $ box = 1

    la "What do you mean?"

    show laffey dark
    with dis
    show mccall
    with dis
    $ box = 2

    mc "Like, you know all those mushrooms San Diego’s been growing in her room?"

    show mccall dark
    with dis
    show laffey
    with dis
    $ box = 1

    la "That’s a little weird no matter which way you put it."

    show laffey dark
    with dis
    show mccall
    with dis
    $ box = 2

    mc "Right? She gets all sparkly and giggly from inhaling those spores."

    show laffey
    with dis
    $ box = 1

    "{color=#AAED60}Both{/color}" "Yeahhh."

    hide laffey
    hide mccall

    "pause for seagulls"

    show mccall at center

    mc "It’s nice to just unwind and eat."

    window hide
    show mccall:
        linear 0.5 xpos 1010
    show mccall dark with dissolve
    show mccall dark:
        xpos 1010
    show laffey at left

    la "I think the red and white ones are prettier so they’re tastier."

    show mccall
    with dis

    "{color=#AAED60}Both{/color}" "Ahhh. So relaxing."

    hide laffey
    hide mccall
    show long island dark at center
    show long island with dis

    li "Heyyy! I found Laffey and McCall! Heeeeyyyy!"

    hide long island
    show laffey at center

    la "Long Island."

    hide laffey
    show mccall at center

    mc "Where’s the fire?"

    hide mccall
    show long island at center, bobble2

    li "Listen up. Both of you went to San Diego’s mushroom party last night?"

    hide long island
    show laffey at center

    la "Yup. We were there. We were just talking about it actually."

    hide laffey
    show mccall at center

    mc "Uh huh. You didn’t go, Long Island?"

    hide mccall
    show long island at center, bobble1

    li "I may be a ghost, but I’m not gonna risk my life eating unidentified mushrooms."

    hide long island
    show laffey at center

    la "Did we risk our lives?"

    hide laffey
    show mccall at center

    mc "Well, I can’t argue with that."

    hide mccall
    show long island at center, shake

    li "But actually I wish I wasn’t so careful just yesterday. I should’ve gone."

    hide long island
    show laffey at center

    la "Why? Do you like mushrooms?"

    hide laffey
    show mccall at center

    mc "I think not going was the right move. Honestly."

    hide mccall
    show long island at center, shake

    li "It actually looks like you haven’t changed at all. Lemme see."

    hide long island
    show laffey at center

    la "Why are you staring at our breasts, Long Island?"

    hide laffey
    show mccall at center

    mc "You’re creeping me out. What the hell?"

    window hide
    show mccall:
        linear 0.5 xpos 1010
    show mccall dark with dissolve
    show mccall dark:
        xpos 1010
    show long island at left

    li "Hmm. Seems I can’t tell without a more direct approach!"
    "(BOING)"
    la "Gasp"
    mc "Wh- what? Don’t just suddenly grab my chest like that."
    li "Hmm. Turns out you haven’t changed at all. Too bad. It was all for nothing."
    la "What do you mean?"
    mc "Tell us what’s going on or I’ll get you with this popsicle."
    li "Your eyes are scaring me. Okay, settle down, I’ll explain. We can all come out winners here."
    la "Winners?"
    mc "Huh?"
    li "The truth is I heard San Diego’s mushrooms have some awesome side effects."
    mc "Awesome side effects? Like what?"
    li "Check it out. If you eat San Diego’s mushrooms… your breasts… look bigger!"
    la "Ugh. I’m sleepy."
    mc "Yeah. I think it’s time for a nap."
    li "Wait wait! Don’t nap! It’s true! Everyone’s been talking about it. This isn’t just something I made up!"
    la "But… I’m still the same."
    mc "Mine didn’t get any bigger either."
    li "It’s gotta be because you didn’t eat enough, or you ate the wrong kind."
    la "Now that you mention it, there were different colored mushrooms."
    mc "I think I ate like a red and white striped one."
    la "Yeah. Same."
    li "Hmm. Then the red and white striped one isn’t it. Neither of you took any other mushrooms? Everyone took home what they couldn’t finish eating."
    la "I was too full so I didn’t take any."
    mc "Me too."
    li "All right. Damn. Okay, we gotta go find some other partygoers. Right! Let’s make our breasts bigger so the Commander will drool at us! Let’s go!"
    la "Wait."
    li "What’s wrong?"
    la "The Commander… likes big breasts?"
    li "Umm… he didn’t say so directly. But the bigger ones seem to have more charm."
    la "Laffey will go too."
    li "Really!? Ehehehe. My party has grown! What do you think, McCall?"
    mc "Um. I don’t really care about the size of my chest…"
    li "So, you’re not coming?"
    mc "Umm… I do want to know if the rumor is true. I’ll go."
    li "Da-daaaaan! McCall has joined my party! It’s time for us three to set out on our mushroom search adventure. Let’s go!"
    la "Ok."
    "Break"
    li "And so, Long Island and her merry men arrived at San Diego’s room."
    la "We’re merry?"
    mc "Well, as merry as a group hunting for breast-growing mushrooms can be."
    li "Hey, cut the chatter, it’s an ambush! There may still be mushrooms here."
    "Knock knock"
    li "Anybody home!?"
    sd "Yeess? Who is iiit?"
    li "It’s Long Island!"
    la "Laffey and McCall too."
    mc "Can we come in?"
    sd "Sure! Ah! Just give me a minute here. Let yourselves in! Welcome welcome!"
    li "All right, coming in. Sorry to bother you!"
    sd "Hello! Lovely weather, isn’t it? I’m a little tired but let’s dance!"
    la "San Diego’s really dancing."
    mc "She seems kind of tense. Maybe some ice cream would calm her down."
    sd "Huuuh? That’s right! I’ve been dancing nonstop! Kinda weird!"
    li "You didn’t even notice you’ve been dancing? It must be… ah! There’s a half-eaten mushroom on the table there!"
    la "Did San Diego eat it?"
    sd "Yeah! I ate it! Just about the time I wanted to break into dance! Everybody join me!"
    mc "No. The real reason you’re dancing is because of this mushroom."
    li "That sounds right. So then… this star-shaped yellow one with spots all over it must be a dancing mushroom!"
    sd "Yeeaahh! Dancing dancing!!"
    la "So then, what were the ones we ate?"
    li "Those were fail mushrooms!"
    mc "Feels more like a win mushroom to me."
    sd "Win? Fail? Nah! I dunno why everybody came to my room, but you better dance with me!"
    la "Not now. Laffey and friends came to find the mushroom that makes your breasts bigger."
    li "That’s right. Long Island and her band of merry men are on a quest for the BUST UP mushroom!"
    mc "When you call it a BUST UP mushroom I feel like we’ve fallen into something really shady."
    sd "Eeeeeeh? Is there really a mushroom like that? Amazing!"
    li "Yeah! Do you have any more mushrooms laying around, San Diego?"
    sd "Nope! That dancing mushroom I just ate was the last one!"
    la "Damn."
    li "But we did learn the effect of one type of mushroom. Let’s press on to find the next!"
    mc "Ah! I think we should go to Cassin next. I saw her fidgeting with a weird looking purple mushroom."
    sd "Wait up! I’m going too!"
    la "While dancing?"
    sd "Yeah! Dancing! LET’S GO!"
    mc "She’s got some moves!"
    li "Da-daan! The dancer has joined my party!"
    la "Attack power UP? Heh. Right?"


    # This ends the game.

    return
