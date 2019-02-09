# Define custom transforms here.

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


transform bobble:
    yoffset 0
    easein_quad 0.15 yoffset -25
    easeout_quad 0.15 yoffset 0
    easein_quad 0.15 yoffset -25
    easeout_quad 0.15 yoffset 0


transform shake:
    xoffset 0
    linear 0.4 xoffset 25
    linear 0.4 xoffset 0
    linear 0.4 xoffset 25
    linear 0.4 xoffset 0
