import time
import terminalio
import displayio
from os import uname
if uname()[0] == 'samd51':
    import board
else:
    from blinka_displayio_pygamedisplay import PyGameDisplay
from adafruit_display_text import label
from adafruit_display_text import bitmap_label
from adafruit_bitmap_font import bitmap_font
import fontio

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
ensayo=terminalio.FONT
# Tests

text_area = label.Label(terminalio.FONT,
                        text="Circuit Python",
                        max_glyphs=40)
main_group.append(text_area)
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing position setter
text_area.x = 10
text_area.y = 10
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing creating label with initial position
text_area.text = "Testing Position"
text_middle = label.Label(terminalio.FONT,
                        text="Circuit",
                        x=display.width // 2,
                        y=display.height // 2)
main_group.append(text_middle)
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing Text Setter
text_area.text = "Testing Changing Text"
text_middle.text = "Python"
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing a and y getter and setter
text_area.text = "Testing Changing Position"
text_middle.x = text_middle.x - 50
text_middle.y = text_middle.y - 50
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing font Getter and setter
text_area.text = "Testing Changing FONT"
if isinstance(text_middle.font, fontio.BuiltinFont):
    text_middle.font = MEDIUM_FONT
display.show(main_group)
time.sleep(TIME_PAUSE)

# Once this working we create another label with all the initial specs
main_group.pop()
# Testing Color
text_area.text = "Testing Color"
text_initial_specs = label.Label(MEDIUM_FONT,
                                 text="Circuit Python",
                                 x=display.width // 2,
                                 y=display.height // 2,)
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
text_initial_specs.color = 0x004400
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()
# Testing Background Color
text_area.text = "Testing Background Color"
text_initial_specs = label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,)
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
text_initial_specs.background_color = 0x990099
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()
# Testing Background Color
text_area.text = "Testing Background Tight"
text_initial_specs = label.Label(BIG_FONT,
                                 text="aaaaq~",
                                 x=0,
                                 max_glyphs=6,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 background_tight=True
                                 )
main_group.append(text_initial_specs)
text_initial_specs = label.Label(BIG_FONT,
                                 text="aaaaq~",
                                 x=90,
                                 max_glyphs=6,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 background_tight=False,
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()
main_group.pop()

# Testing Padding
text_area.text = "Testing Padding"
text_initial_specs = label.Label(BIG_FONT,
                                 text="CircuitPython",
                                 x=display.width // 4,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()

# Testing Anchor Point/ Anchored Position
text_area.text = "Testing Anchor Point/Anchored Position"
text_initial_specs = label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(1)
try:
    text_initial_specs.anchored_position(100, 100)
    text_initial_specs.anchor_point(0.5, 0.5)

except:
    print("Test is failing here")
    main_group.pop()
    warning_text = label.Label(BIG_FONT,
                                     text="Test Fail",
                                     x=display.width // 2,
                                     y=display.height // 4,
                                     background_color=0x004499)
    main_group.append(warning_text)
    time.sleep(3)
    display.show(main_group)
    pass
main_group.pop()

# Testing Scale
text_area.text = "Testing Scale"
text_initial_specs = label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(display.width // 2, display.height // 2),
                                 anchor_point=(0.5, 0.5),
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
text_initial_specs.scale = 2
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()

# Testing Base Alignment
text_area.text = "Testing Base Alignment"
text_initial_specs = label.Label(MEDIUM_FONT,
                                 text="python",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 base_alignment=True
                                 )
main_group.append(text_initial_specs)
text_initial_specs = label.Label(BIG_FONT,
                                 text="circuit",
                                 x=display.width // 2 - 100,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 base_alignment=True,)
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()
main_group.pop()
main_group.pop()

text_area = bitmap_label.Label(terminalio.FONT,
                        text="Circuit Python",
                        max_glyphs=40)
main_group.append(text_area)
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing position setter
text_area.x = 10
text_area.y = 10
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing creating label with initial position
text_area.text = "Testing Position"
text_middle = bitmap_label.Label(terminalio.FONT,
                        text="Circuit",
                        x=display.width // 2,
                        y=display.height // 2)
main_group.append(text_middle)
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing Text Setter
text_area.text = "Testing Changing Text"
text_middle.text = "Python"
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing a and y getter and setter
text_area.text = "Testing Changing Position"
text_middle.x = text_middle.x - 50
text_middle.y = text_middle.y - 50
display.show(main_group)
time.sleep(TIME_PAUSE)
# Testing font Getter and setter
text_area.text = "Testing Changing FONT"
if isinstance(text_middle.font, fontio.BuiltinFont):
    text_middle.font = MEDIUM_FONT
display.show(main_group)
time.sleep(TIME_PAUSE)

# Once this working we create another label with all the initial specs
main_group.pop()
# Testing Color
text_area.text = "Testing Color"
text_initial_specs = bitmap_label.Label(MEDIUM_FONT,
                                 text="Circuit Python",
                                 x=display.width // 2,
                                 y=display.height // 2,)
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
text_initial_specs.color = 0x004400
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()
# Testing Background Color
text_area.text = "Testing Background Color"
text_initial_specs = bitmap_label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,)
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
text_initial_specs.background_color = 0x990099
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()
# Testing Background Color
text_area.text = "Testing Background Tight"
text_initial_specs = bitmap_label.Label(BIG_FONT,
                                 text="aaaaq~",
                                 x=0,
                                 max_glyphs=6,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 background_tight=True
                                 )
main_group.append(text_initial_specs)
text_initial_specs = bitmap_label.Label(BIG_FONT,
                                 text="aaaaq~",
                                 x=90,
                                 max_glyphs=6,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 background_tight=False,
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()
main_group.pop()

# Testing Padding
text_area.text = "Testing Padding"
text_initial_specs = bitmap_label.Label(BIG_FONT,
                                 text="CircuitPython",
                                 x=display.width // 4,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()

# Testing Anchor Point/ Anchored Position
text_area.text = "Testing Anchor Point/Anchored Position"
text_initial_specs = bitmap_label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(1)
try:
    text_initial_specs.anchored_position(100, 100)
    text_initial_specs.anchor_point(0.5, 0.5)

except:
    print("Test is failing here")
    main_group.pop()
    warning_text = bitmap_label.Label(BIG_FONT,
                                     text="Test Fail",
                                     x=display.width // 2,
                                     y=display.height // 4,
                                     background_color=0x004499)
    main_group.append(warning_text)
    time.sleep(3)
    display.show(main_group)
    pass
main_group.pop()

# Testing Scale
text_area.text = "Testing Scale"
text_initial_specs = bitmap_label.Label(MEDIUM_FONT,
                                 text="CircuitPython",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 padding_right=10,
                                 padding_top=10,
                                 padding_bottom=10,
                                 padding_left=10,
                                 anchored_position=(display.width // 2, display.height // 2),
                                 anchor_point=(0.5, 0.5),
                                 )
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)
text_initial_specs.scale = 2
display.show(main_group)
time.sleep(TIME_PAUSE)
main_group.pop()

# Testing Base Alignment
text_area.text = "Testing Base Alignment"
text_initial_specs = bitmap_label.Label(MEDIUM_FONT,
                                 text="python",
                                 x=display.width // 2,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 base_alignment=True
                                 )
main_group.append(text_initial_specs)
text_initial_specs = bitmap_label.Label(BIG_FONT,
                                 text="circuit",
                                 x=display.width // 2 - 100,
                                 y=display.height // 2,
                                 color=0xFFFFFF,
                                 background_color=0x990099,
                                 base_alignment=True,)
main_group.append(text_initial_specs)
display.show(main_group)
time.sleep(TIME_PAUSE)