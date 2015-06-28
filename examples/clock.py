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

wnpos = vfd_pos.vfd_pos(0x0200)
print "PRESS CTRL+C TO QUIT"

def printdate(onepos):
		present_time = time.localtime()
		onepos.poscur(1,1)
		remaining = 60 - present_time.tm_sec
		date = time.strftime("%a %d %b %Y", present_time).center(20)
		onepos.write_msg(date)
		hour = time.strftime("%H:%M", present_time).center(20)
		onepos.poscur(2,1)
		onepos.write_msg(hour)
		time.sleep(remaining)

try:
	while True:
		printdate(wnpos)
except KeyboardInterrupt:
	pass
wnpos.close()
