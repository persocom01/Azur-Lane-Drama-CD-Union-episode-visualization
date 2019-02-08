# Define custom transforms here.

transform bobble:
    yoffset 0
    easein_quad 0.1 yoffset -15
    easeout_quad 0.1 yoffset 0
    easein_quad 0.1 yoffset -15
    easeout_quad 0.1 yoffset 0

transform shake:
    xoffset 0
    linear 0.4 xoffset 15
    linear 0.4 xoffset 0
    linear 0.4 xoffset 15
    linear 0.4 xoffset 0
