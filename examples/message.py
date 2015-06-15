#!/usr/bin/python
# -*- coding: utf8 -*-

# Example for VFD PoS library for WN USB
# Displays messages with unicode characters at different locations
# Copyright (C) 2015  Antoine FERRON

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import vfd_pos

mypos = vfd_pos.vfd_pos(0x0201)

mypos.poscur(3,5)
mypos.printchr(0xC8)
mypos.poscur(4,15)
mypos.write_msg(u"¤")
mypos.poscur(0,0)
mypos.write_msg(u"Cet été sera\n\rtrès chaud!")
mypos.write_msg("CALIENTE!")

raw_input("PRESS ENTER TO EXIT")
mypos.close()
