# Define custom transforms here.

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
