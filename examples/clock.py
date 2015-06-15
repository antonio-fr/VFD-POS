#!/usr/bin/python
# -*- coding: utf8 -*-

# Example for VFD PoS library for WN USB
# Displays date and time as a clock app
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
import time

wnpos = vfd_pos.vfd_pos(0x0201)
print "PRESS CTRL+C TO QUIT"
try:
	while True:
		wnpos.poscur(1,1)
		prestime = time.localtime()
		date = time.strftime("%a %d %b %Y", prestime).center(20)
		wnpos.write_msg(date)
		hour = time.strftime("%H:%M", prestime).center(20)
		wnpos.poscur(3,1)
		wnpos.write_msg(hour) 
		time.sleep(10)
except KeyboardInterrupt:
	pass
wnpos.close()
