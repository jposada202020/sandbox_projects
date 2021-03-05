# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This examples shows the use of anchor_point and anchored_position.
"""

from blinka_displayio_pygamedisplay import PyGameDisplay
import displayio
import terminalio
from adafruit_display_text import bitmap_label
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

display = PyGameDisplay(width=320, height=240)

TEXT_BACKGROUND_COLOR = [0xE0433, 0x990099, 0xD6D714, 0xD73014, 0x1415D7, 0x71646F]
TEXT_COLOR = 0x00FF00
FONT_TESTS = [bitmap_font.load_font("fonts/Helvetica-Bold-16.bdf"),
    bitmap_font.load_font("fonts/LeagueSpartan-Bold-16.bdf"),
    terminalio.FONT,
]

TEXT = "ApQq~"


# text_area_top_left = label.Label(FONT_TESTS[1],
#                                  text=TEXT,
#                                  background_color=TEXT_BACKGROUND_COLOR[1],
#                                  x=20,
#                                  y=100)
# text_area_top_left.anchor_point = (0.5, 0.0)
# # text_area_top_left.anchored_position = (20, 100)

text_area_top_middle = label.Label(FONT_TESTS[1],
                                   text=TEXT,
                                   background_color=TEXT_BACKGROUND_COLOR[1],
                                   x=100,
                                   y=100,
                                   scale=1)
text_area_top_middle.anchor_point = (0.0, 0.0)
text_area_top_middle.anchored_position = (100, 100)

text_area_top_top = label.Label(FONT_TESTS[1],
                                   text=TEXT,
                                   background_color=TEXT_BACKGROUND_COLOR[1],
                                   x=100,
                                   y=40,
                                   scale=2)
text_area_top_top.anchor_point = (0.0, 0.0)
text_area_top_top.anchored_position = (100, 40)

text_area_mid_bottom = bitmap_label.Label(FONT_TESTS[1],
                                   text=TEXT,
                                    color=0x4455AA,
                                   background_color=TEXT_BACKGROUND_COLOR[1],
                                   x=100,
                                   y=140,
                                   scale=1)
text_area_mid_bottom.anchor_point = (0.5, 0.5)
text_area_mid_bottom.anchored_position = (100, 140)

text_area_mid_bottom2 = label.Label(FONT_TESTS[1],
                                   text=TEXT,
                                   background_color=TEXT_BACKGROUND_COLOR[1],
                                   scale=1,
                                   padding_bottom=10,
                                   padding_left=18,
                                   padding_right=5,
                                   padding_top=0,
                                    base_alignment=False,
                                    )
text_area_mid_bottom2.anchor_point = (1.0, 0.0)
text_area_mid_bottom2.anchored_position = (100, 180)

text_area_mid_bottom3 = label.Label(FONT_TESTS[2],
                                   text=TEXT,
                                   background_color=TEXT_BACKGROUND_COLOR[1],
                                   scale=1,
                                   padding_bottom=10,
                                   padding_left=18,
                                   padding_right=5,
                                   padding_top=0,
                                    base_alignment=True,
                                    )
text_area_mid_bottom3.anchor_point = (1.0, 0.0)
text_area_mid_bottom3.anchored_position = (160, 180)


main_group = displayio.Group(max_size=10)
main_group.append(text_area_top_top)
main_group.append(text_area_top_middle)
main_group.append(text_area_mid_bottom)
main_group.append(text_area_mid_bottom2)
main_group.append(text_area_mid_bottom3)

bitmap = displayio.Bitmap(320, 2, 2)
palette = displayio.Palette(2)
palette[0] = 0x004400
palette[1] = 0x00FFFF
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=100)
main_group.append(tile_grid)

bitmap2 = displayio.Bitmap(2, 320, 2)
tile_grid2 = displayio.TileGrid(bitmap2, pixel_shader=palette, x=100, y=0)
main_group.append(tile_grid2)

bitmap3 = displayio.Bitmap(320, 2, 2)
tile_grid3 = displayio.TileGrid(bitmap3, pixel_shader=palette, x=0, y=40)
main_group.append(tile_grid3)

line4 = displayio.Bitmap(320, 2, 2)
tile_grid4 = displayio.TileGrid(line4, pixel_shader=palette, x=0, y=140)
main_group.append(tile_grid4)

line5 = displayio.Bitmap(320, 2, 2)
tile_grid5 = displayio.TileGrid(line4, pixel_shader=palette, x=0, y=180)
main_group.append(tile_grid5)

display.show(main_group)

while True:
    pass
