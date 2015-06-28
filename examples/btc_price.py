#!/usr/bin/python
# -*- coding: utf8 -*-

# Example for VFD PoS library for WN USB
# Displays Bitcoin Price in real-time
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

import time
from vfd_pos import *
from easy_rest_json import * 


mypos = vfd_pos(0x0200)
price_api = rest_json('https://api.coindesk.com/v1/bpi/currentprice.json')

print "PRESS CTRL+C TO QUIT"
try:
	while True:
		price_api.get_data()
		btc_price = float( price_api.getkey("bpi/USD/rate") )
		mypos.poscur(0,0)
		mypos.write_msg("Bitcoin Price\r\n 1 BTC = %.2f USD  "%btc_price)
		time.sleep(60)
except KeyboardInterrupt:
	pass
mypos.close()
