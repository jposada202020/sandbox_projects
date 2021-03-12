import displayio
from os import uname
if uname()[0] == 'samd51':
    import board
else:
    from blinka_displayio_pygamedisplay import PyGameDisplay
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

if uname()[0] == 'samd51':
    display= board.DISPLAY
else:
    display = PyGameDisplay(width=320, height=240)
main_group = displayio.Group(max_size=100)
font_name = "fonts/LibreBodoniv2002-Bold-10.bdf"
MEDIUM_FONT = bitmap_font.load_font("fonts/LibreBodoniv2002-Bold-10.bdf")
BIG_FONT = bitmap_font.load_font("fonts/LibreBodoniv2002-Bold-27.bdf")
TIME_PAUSE = 2

bitmap = displayio.Bitmap(4, 320, 2)
palette = displayio.Palette(2)
palette[0] = 0x004400
palette[1] = 0x00FFFF
horizontal_line = displayio.TileGrid(bitmap,
                               pixel_shader=palette,
                               x=155,
                               y=0)
main_group.append(horizontal_line)

bitmap = displayio.Bitmap(320, 4, 2)
vertica_line = displayio.TileGrid(bitmap,
                               pixel_shader=palette,
                               x=0,
                               y=110)
main_group.append(vertica_line)

text_initial_specs = label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(display.width // 2, display.height // 2),
                                 anchor_point=(0.5, 0.5),
                                 theme="MAGTAG",
                                 )
main_group.append(text_initial_specs)


text_initial_specs2 = label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0x44FF44,
                                 background_color=990099,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(display.width // 2, (display.height // 2)+30),
                                 anchor_point=(0.5, 0.5),
                                 )
main_group.append(text_initial_specs2)
display.show(main_group)

while True:
    pass