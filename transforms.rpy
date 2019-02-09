# Define custom transforms here.

transform skip_button:
    xanchor 1.0
    xpos 1280
    yanchor 0.0
    ypos 0


transform skip_button_animation:
    alpha 1.0
    linear 0.75 alpha 0.4
    pause 0.5
    linear 0.75 alpha 1.0
    repeat


transform next_prompt:
    xanchor 1.0
    xpos 1240
    yanchor 1.0
    ypos 700


transform next_prompt_animation:
    yoffset 0
    linear 0.5 yoffset -10
    linear 0.5 yoffset 0
    repeat


transform left:
    xanchor 0.5
    xpos 270
    yanchor 0.5
    ypos 450


transform center:
    xanchor 0.5
    xpos 640
    yanchor 0.5
    ypos 450


transform right:
    xanchor 0.5
    xpos 1010
    yanchor 0.5
    ypos 450


transform bobble1:
    yoffset 0
    easein_quad 0.1 yoffset -25
    easeout_quad 0.1 yoffset 0


transform bobble2:
    yoffset 0
    easein_quad 0.1 yoffset -25
    easeout_quad 0.1 yoffset 0
    easein_quad 0.1 yoffset -25
    easeout_quad 0.1 yoffset 0


transform shake:
    xoffset 0
    linear 0.4 xoffset 25
    linear 0.4 xoffset 0
    linear 0.4 xoffset 25
    linear 0.4 xoffset 0
