# ##### BEGIN MIT LICENSE BLOCK #####
#
# MIT License
#
# Copyright (c) 2023 Steven Garcia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ##### END MIT LICENSE BLOCK #####

from mathutils import Vector
from enum import Flag, Enum, auto
from ..file_device.format import DeviceAsset

class ControlTypeEnum(Enum):
    toggle_switch = 0
    on_button = auto()
    off_button = auto()
    call_button = auto()

class TriggersWhenEnum(Enum):
    touched_by_player = 0
    destroyed = auto()

class ControlAsset(DeviceAsset):
    def __init__(self, control_type=0, triggers_when=0, call_value=0.0, action_string="", action_string_length=0, on=None, off=None, 
                 deny=None):
        super().__init__()
        self.control_type = control_type
        self.triggers_when = triggers_when
        self.call_value = call_value
        self.action_string = action_string
        self.action_string_length = action_string_length
        self.on = on
        self.off = off
        self.deny = deny
