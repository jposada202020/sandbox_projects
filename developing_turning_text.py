import displayio
from adafruit_bitmap_font import bitmap_font
from os import uname
if uname()[0] == 'samd51':
    import board
else:
    from blinka_displayio_pygamedisplay import PyGameDisplay


def get_ascent_descent(font):
    """ Private function to calculate ascent and descent font values """
    if hasattr(font, "ascent"):
        return font.ascent, font.descent

    # check a few glyphs for maximum ascender and descender height
    glyphs = "M j'"  # choose glyphs with highest ascender and lowest
    try:
        font.load_glyphs(glyphs)
    except AttributeError:
        # Builtin font doesn't have or need load_glyphs
        pass
    # descender, will depend upon font used
    ascender_max = descender_max = 0
    for char in glyphs:
        this_glyph = font.get_glyph(ord(char))
        if this_glyph:
            ascender_max = max(ascender_max, this_glyph.height + this_glyph.dy)
            descender_max = max(descender_max, -this_glyph.dy)
    return ascender_max, descender_max


def get_width(font):
    """ Private function to calculate average width font value """
    # check a few glyphs for maximum ascender and descender height
    glyphs = "M j'"  # choose glyphs with highest ascender and lowest
    try:
        font.load_glyphs(glyphs)
    except AttributeError:
        # Builtin font doesn't have or need load_glyphs
        pass
    width_max = 0
    for char in glyphs:
        this_glyph = font.get_glyph(ord(char))
        if this_glyph:
            width_max = max(width_max, this_glyph.width+this_glyph.dx)
    return width_max

def get_glyph_values(letter):
    glyphc= font.get_glyph(ord(letter))
    print(f"Character:{letter} height:{glyphc.height} width:{glyphc.width} dx:{glyphc.dx} dy:{glyphc.dy}"
          f" shiftx:{glyphc.shift_x} shifty: {glyphc.shift_y}")


def directional_text(text, local_group, x, y, offset, offset_x, direction):
    for letter in text_test:
        glyph = font.get_glyph(ord(letter))

        if direction == "Straight":
            pos_y = y - glyph.height - glyph.dy + offset
            pos_x = x + glyph.dx
        if direction == "upwards":
            pos_y = x - glyph.width - glyph.dx
            pos_x = y - glyph.height - glyph.dy + offset
        if direction == "downwards":
            pos_y = y + glyph.dx
            pos_x = x + glyph.dy + offset
        if direction == "top_bottom":
            pos_y = y - glyph.dy
            pos_x = x + offset_x - glyph.width//2
        if direction == "right_to_left":
            pos_y = y - glyph.height - glyph.dy + offset
            pos_x = x + glyph.dx

        face = displayio.TileGrid(
            glyph.bitmap,
            pixel_shader=palette,
            default_tile=glyph.tile_index,
            tile_width=glyph.width,
            tile_height=glyph.height,
            x=pos_x,
            y=pos_y, )
        if direction == "upwards":
            face.transpose_xy = True
            face.flip_x = True
        if direction == "downwards":
            face.transpose_xy = True
            face.flip_y = True
        if direction == "right_to_left":
            face.flip_x = True

        local_group.append(face)

        if direction == "Straight":
            x = x + glyph.shift_x
        if direction == "upwards":
            x = x - glyph.shift_x
        if direction == "downwards":
            y = y + glyph.shift_x
        if direction == "top_bottom":
            y = y + glyph.height
        if direction == "right_to_left":
            x = x - glyph.shift_x


if uname()[0] == 'samd51':
    display= board.DISPLAY
else:
    display = PyGameDisplay(width=320, height=240)

local_group = displayio.Group(max_size=100, scale=1)
font = bitmap_font.load_font("fonts/Helvetica-Bold-16.bdf")
palette = displayio.Palette(2)
palette[0] = 0x004400
palette[1] = 0x00FFFF

ascent, descent = get_ascent_descent(font)
width = get_width(font)

bitmap3 = displayio.Bitmap(320, 2, 2)
tile_grid3 = displayio.TileGrid(bitmap3, pixel_shader=palette, x=0, y=50)
local_group.append(tile_grid3)

bitmap2 = displayio.Bitmap(2, 320, 2)
tile_grid2 = displayio.TileGrid(bitmap2, pixel_shader=palette, x=50, y=0)
local_group.append(tile_grid2)

offset_x = width // 2
offset = ascent // 2

text_test = "CircuitPython"

directional_text(text_test, local_group, 50, 50, offset, offset_x, "Straight")
directional_text(text_test, local_group, 50, 50, offset, offset_x, "upwards")
directional_text(text_test, local_group, 50, 50, offset, offset_x, "downwards")
directional_text(text_test, local_group, 200, 50, offset, offset_x, "top_bottom")
directional_text(text_test, local_group, 300, 220, offset, offset_x, "right_to_left")

display.show(local_group)

while True:
    pass
