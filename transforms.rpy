# Define custom transforms here.

transform skip_button_animation:
    alpha 1.0
    linear 1 alpha 0.4
    linear 1 alpha 1.0
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


transform move_left:
    linear 0.5 xpos 270


transform move_lefta:
    xpos 270


transform center:
    xanchor 0.5
    xpos 640
    yanchor 0.5
    ypos 450


transform move_center:
    linear 0.5 xpos 640


transform move_centera:
    xpos 640


transform right:
    xanchor 0.5
    xpos 1010
    yanchor 0.5
    ypos 450


transform move_right:
    linear 0.5 xpos 1010


transform move_righta:
    xpos 1010


transform move_right_off:
    linear 1 xpos 1820


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


transform bobble3:
    yoffset 0
    easein_quad 0.1 yoffset -25
    easeout_quad 0.1 yoffset 0
    easein_quad 0.1 yoffset -25
    easeout_quad 0.1 yoffset 0
    easein_quad 0.1 yoffset -25
    easeout_quad 0.1 yoffset 0


transform grabL:
    xoffset 0
    easein_quad 0.5 xoffset -550


transform grabR:
    xoffset 0
    easein_quad 0.5 xoffset 550


transform shake1:
    xoffset 0
    linear 0.4 xoffset 25
    linear 0.4 xoffset 0


transform shake2:
    xoffset 0
    linear 0.4 xoffset 25
    linear 0.4 xoffset 0
    linear 0.4 xoffset 25
    linear 0.4 xoffset 0
