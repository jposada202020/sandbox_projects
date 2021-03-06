# SPDX-FileCopyrightText: 2021 Jose David M
#
# SPDX-License-Identifier: MIT
#############################
"""
This is a basic demonstration of a Scale Class.
"""

import time
import board
from scales import Scale

display = board.DISPLAY

my_scale = Scale(
    x=50,
    y=180,
    direction="vertical",
    divisions=3,
    limits=(0, 80),
)


display.show(my_scale)

values = [56, 58, 60, 65, 63, 60, 56, 54, 53, 42, 43, 44, 45, 52, 54]

for val in values:
    my_scale.animate_pointer(val)
    time.sleep(2)
