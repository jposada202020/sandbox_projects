# SPDX-FileCopyrightText: 2021 Jose David M.
#
# SPDX-License-Identifier: MIT
"""

`scale`
================================================================================
A cartesian plane widget for displaying graphical information.

* Author(s): Jose David M.

Implementation Notes
--------------------

This library is closely related with Cartesian. The Cartesian library was developed first.
After this, new granular classes were created for Axes. and new methods to calculate the
conversion between range, pixels and values given


"""

# pylint: disable=too-many-lines, too-many-instance-attributes, too-many-arguments
# pylint: disable=too-many-locals, too-many-statements

import displayio
from vectorio import VectorShape, Polygon


class Axes(displayio.Group):
    def __init__(
        self,
        x=0,
        y=0,
        limits=(0, 100),
        divisions=10,
        direction="horizontal",
        stroke=3,
        length=100,
        color=0x990099,
    ):

        super().__init__(max_size=1)

        self.x = x
        self.y = y
        self.limits = limits

        self.divisions = divisions

        if direction == "horizontal":
            self.direction = True
        else:
            self.direction = False

        self.stroke = stroke
        self.length = length

        self._palette = displayio.Palette(2)
        self._palette.make_transparent(0)
        self._palette[1] = color

    def _draw_line(self):
        if self.direction:
            points = [
                (self.x, self.y),
                (self.x + self.length, self.y),
                (self.x + self.length, self.y - self.stroke),
                (self.x, self.y - self.stroke),
            ]
        else:
            points = [
                (self.x, self.y),
                (self.x, self.y - self.length),
                (self.x + self.stroke, self.y - self.length),
                (self.x + self.stroke, self.y),
            ]

        line_base = Polygon(points=points)
        line_vector_shape = VectorShape(
            shape=line_base,
            pixel_shader=self._palette,
            x=0,
            y=-self.y,
        )
        self.append(line_vector_shape)

    def _draw_ticks(self, tick_length=10, tick_stroke=4):
        self._tick_length = tick_length
        self._tick_stroke = tick_stroke
        self._conversion()

        if self.direction:
            for val in self.ticks[:-1]:
                tick = Polygon(
                    points=[
                        (self.x + val - 1, self.y - self.stroke),
                        (self.x + val - 1, self.y - self.stroke - self._tick_length),
                        (self.x + val + 1, self.y - self.stroke - self._tick_length),
                        (self.x + val + 1, self.y - self.stroke),
                    ]
                )
                tick_shape = VectorShape(
                    shape=tick,
                    pixel_shader=self._palette,
                    x=0,
                    y=-self.y,
                )
                self.append(tick_shape)

        else:
            for val in self.ticks[:-1]:
                tick = Polygon(
                    points=[
                        (self.x + self.stroke, self.y - val - 1),
                        (self.x + self.stroke + self._tick_length, self.y - val - 1),
                        (self.x + self.stroke + self._tick_length, self.y - val + 1),
                        (self.x + self.stroke, self.y - val + 1),
                    ]
                )

                tick_shape = VectorShape(
                    shape=tick,
                    pixel_shader=self._palette,
                    x=0,
                    y=-self.y,
                )

                self.append(tick_shape)

    def _conversion(self):
        self.ticks = list()
        self.text_ticks = list()
        espace = round(self.length / self.divisions)
        rang_discrete = self.limits[1] - self.limits[0]
        factorp = self.length / rang_discrete
        for i in range(espace, self.length + 1, espace):
            self.ticks.append(i)
            self.text_ticks.append(str(int(self.limits[0] + i * 1 / factorp)))


class Scale(Axes):
    """
    :param int x: pixel position, defaults to 0
    :param int y: pixel position, defaults to 0

    :param str direction: direction of the scale either ``horizontal`` or ``vertical``
     defaults to ``horizontal``

    :param int stroke: width in pixels of the scale axes. Defaults to 3

    :param int length: sacle length in pixels. Defaults to 100
     that extends the touch response boundary, defaults to 0

    :param int color: 24-bit hex value axes line color, Defaults is Purple 0x990099

    :param int width: scale width in pixels. Defaults to 50

    :param limits: tuple of value range for the scale. Defaults to (0, 100)
    :param int divisions: Divisions number

    :param int back_color: 24-bit hex value axes line color, Defaults is Light Blue 0x9FFFFF

    :param int tick_length: Scale tick lenght in pixels. Defaults to 10
    :param int tick_stroke: Scale tick width in pixels. Defaults to 4


    **Quickstart: Importing and using Scales**

    Here is one way of importing the ``Scales`` class so you can use it as
    the name ``my_scale``:

    .. code-block:: python

        from Cartesian import Scale

    Now you can create an vertical Scale at pixel position x=50, y=180 with 3 divisions and a range
    of 0 to 80 using:

    .. code-block:: python

        my_scale = Scale(x=50, y=180, direction="vertical", divisions=3, limits=(0, 80))

    Once you setup your display, you can now add ``my_scale`` to your display using:

    .. code-block:: python

        display.show(my_scale)

    If you want to have multiple display elements, you can create a group and then
    append the scale and the other elements to the group.  Then, you can add the full
    group to the display as in this example:

    .. code-block:: python

        my_scale= Scale(x=20, y=30)
        my_group = displayio.Group(max_size=10) # make a group that can hold 10 items
        my_group.append(my_scale) # Add my_slider to the group

        #
        # Append other display elements to the group
        #

        display.show(my_group) # add the group to the display


    **Summary: Slider Features and input variables**

    The ``Scale`` class has some options for controlling its position, visible appearance,
    and value through a collection of input variables:

        - **position**: ``x``, ``y``

        - **size**: ``length`` and ``width``

        - **color**: ``color``, ``back_color``

        - **linewidths**: ``stroke`` and ``tick_stroke``

        - **value**: Set ``value`` to the initial value (True or False)

        - **range and divisions**: ``limits`` and ``divisions``


    """

    def __init__(
        self,
        x=0,
        y=0,
        direction="horizontal",
        stroke=3,
        length=100,
        color=0x990099,
        width=50,
        limits=(0, 100),
        divisions=10,
        back_color=0x9FFFFF,
        tick_length=10,
        tick_stroke=4,
    ):

        super().__init__(
            x=x,
            y=y,
            direction=direction,
            stroke=stroke,
            length=length,
            limits=limits,
            divisions=divisions,
            color=color,
        )

        self._width = width
        self._back_color = back_color
        self._draw_background()
        self._draw_line()
        self._draw_ticks()

        self._tick_length = tick_length
        self._tick_stroke = tick_stroke

        self.pointer = None

        self._draw_pointer()

    def _draw_background(self):
        back_palette = displayio.Palette(2)
        back_palette.make_transparent(0)
        back_palette[1] = self._back_color

        if self.direction:
            points = [
                (self.x, self.y),
                (self.x + self.length, self.y),
                (self.x + self.length, self.y - self._width),
                (self.x, self.y - self._width),
            ]
        else:

            points = [
                (self.x + self.stroke, self.y),
                (self.x + self._width, self.y),
                (self.x + self._width, self.y - self.length),
                (self.x + self.stroke, self.y - self.length),
            ]

        background = Polygon(points=points)
        back_shape = VectorShape(
            shape=background,
            pixel_shader=back_palette,
            x=0,
            y=-self.y,
        )
        self.append(back_shape)

    def _draw_pointer(
        self, color=0xFFFF00, val_ini=15, space=3, pointer_length=20, pointer_stroke=6
    ):
        pointer_palette = displayio.Palette(2)
        pointer_palette.make_transparent(0)
        pointer_palette[1] = color

        self._pointer_length = pointer_length
        self._space = space
        self._pointer_stroke = pointer_stroke

        if self.direction:
            self.pointer = Polygon(
                points=[
                    (
                        self.x - self._pointer_stroke // 2 + val_ini,
                        self.y - self.stroke - self._tick_length - self._space,
                    ),
                    (
                        self.x - self._pointer_stroke // 2 + val_ini,
                        self.y
                        - self.stroke
                        - self._tick_length
                        - self._space
                        - self._pointer_length,
                    ),
                    (
                        self.x + self._pointer_stroke // 2 + val_ini,
                        self.y
                        - self.stroke
                        - self._tick_length
                        - self._space
                        - self._pointer_length,
                    ),
                    (
                        self.x + self._pointer_stroke // 2 + val_ini,
                        self.y - self.stroke - self._tick_length - self._space,
                    ),
                ]
            )
        else:
            self.pointer = Polygon(
                points=[
                    (
                        self.x + self.stroke + self._tick_length + space,
                        self.y + self._pointer_stroke // 2 - val_ini,
                    ),
                    (
                        self.x
                        + self.stroke
                        + self._tick_length
                        + self._space
                        + self._pointer_length,
                        self.y + self._pointer_stroke // 2 - val_ini,
                    ),
                    (
                        self.x
                        + self.stroke
                        + self._tick_length
                        + self._space
                        + self._pointer_length,
                        self.y - self._pointer_stroke // 2 - val_ini,
                    ),
                    (
                        self.x + self.stroke + self._tick_length + self._space,
                        self.y - self._pointer_stroke // 2 - val_ini,
                    ),
                ]
            )

        pointer_shape = VectorShape(
            shape=self.pointer,
            pixel_shader=pointer_palette,
            x=0,
            y=-self.y,
        )

        self.append(pointer_shape)

    def animate_pointer(self, value):
        self.pointer.points = [
            (
                self.x + self.stroke + self._tick_length + self._space,
                self.y + self._pointer_stroke // 2 - value,
            ),
            (
                self.x
                + self.stroke
                + self._tick_length
                + self._space
                + self._pointer_length,
                self.y + self._pointer_stroke // 2 - value,
            ),
            (
                self.x
                + self.stroke
                + self._tick_length
                + self._space
                + self._pointer_length,
                self.y - self._pointer_stroke // 2 - value,
            ),
            (
                self.x + self.stroke + self._tick_length + self._space,
                self.y - self._pointer_stroke // 2 - value,
            ),
        ]
