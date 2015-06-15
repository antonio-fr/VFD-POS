#!/usr/bin/python
# -*- coding: utf8 -*-

# Example for VFD PoS library for WN USB
# Displays present weather conditions in a defined city
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

from easy_rest_json import * 
from vfd_pos import *


city= "Paris"
country= "fr"


mypos = vfd_pos(0x0201)

myres = rest_json()
myres.set_url('http://api.openweathermap.org/data/2.5/weather')
myres.add_param({"q":city+","+country})
myres.get_data()
weather = myres.getkey("weather/0/main")
pres_temp = int(myres.getkey("main/temp"))

mypos.write_msg(u"The present\r\nweather")
mypos.write_msg(u" in Paris\r\nis %s\r\n" % weather)
mypos.write_msg(u"Temp is %i°F" % pres_temp)

raw_input("PRESS ENTER TO EXIT")
mypos.close()
