from os import uname
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import themed_label

if uname()[0] == 'samd51':
    import board
else:
    from blinka_displayio_pygamedisplay import PyGameDisplay

if uname()[0] == 'samd51':
    display = board.DISPLAY
else:
    display = PyGameDisplay(width=320, height=240)

main_group = displayio.Group(max_size=100)
font_name = "fonts/LibreBodoniv2002-Bold-10.bdf"
MEDIUM_FONT = bitmap_font.load_font("fonts/leaguespartan11.bdf")
BIG_FONT = bitmap_font.load_font("fonts/LibreBodoniv2002-Bold-27.bdf")
TIME_PAUSE = 2

text_initial_specs = themed_label.Label(MEDIUM_FONT,
                                 "DarkBrown7",
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(display.width // 2, display.height // 2),
                                 anchor_point=(0.5, 0.5),
                                 )
main_group.append(text_initial_specs)
display.show(main_group)

text_initial_specs = themed_label.Label(MEDIUM_FONT,
                                 "LightTeal",
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(display.width, display.height),
                                 anchor_point=(1.0, 1.0),
                                 )

main_group.append(text_initial_specs)
text_initial_specs.display_themes(4)
display.show(main_group)

text_initial_specs = themed_label.Label(MEDIUM_FONT,
                                 "LightBlue1",
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(0, display.height),
                                 anchor_point=(0.0, 1.0),
                                 )

main_group.append(text_initial_specs)
text_initial_specs.display_themes(4)
display.show(main_group)

text_initial_specs = themed_label.Label(MEDIUM_FONT,
                                 "BrightColors",
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(0, 0),
                                 anchor_point=(0.0, 0.0),
                                 )

main_group.append(text_initial_specs)
text_initial_specs.display_themes(4)
display.show(main_group)

text_initial_specs = themed_label.Label(MEDIUM_FONT,
                                 "Reds",
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(display.width, 0),
                                 anchor_point=(1.0, 0.0),
                                 )

main_group.append(text_initial_specs)
# text_initial_specs.display_themes(4)
display.show(main_group)


while True:
    pass

