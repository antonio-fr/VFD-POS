#!/usr/bin/python
# -*- coding: utf8 -*-

# VFD PoS library for WN USB
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

import pywinusb.hid as hid

class vfd_pos:
	def __init__(self,pid):
		devlist= hid.HidDeviceFilter(vendor_id = 0x0aa7, product_id=pid).get_devices()
		try:
			self.device = devlist[0]
			self.device.open()
			self.report = self.device.find_output_reports()[0]
			if self.report._HidReport__raw_report_size!=33:
				self.device.close()
				self.device = devlist[1]
				self.device.open()
				self.report = self.device.find_output_reports()[0]
			assert(self.report._HidReport__raw_report_size==33)
		except:
			raise IOError("Error : Connect PoS VFD WN USB")
		self.set_charset(0x31)
		self.clearscreen()
		self.poscur(0,0)
	
	def close(self):
		self.device.close()
		
	def send_buffer(self,buffer):
		self.report.set_raw_data(buffer)
		self.report.send()
		
	def selftest(self):
		buffer = [0x00]*33
		buffer[2] = 0x10
		self.send_buffer(buffer)
		
	def reset(self):
		buffer = [0x00]*33
		buffer[2] = 0x40
		self.send_buffer(buffer)
		
	def send_ctrl_seq(self,esc_seq):
		buffer = [0x00]*33
		buffer[1] = 0x02
		len_seq = len(esc_seq)
		buffer[3] = len_seq
		for datx in range(0, len_seq):
			buffer[4+datx] = esc_seq[datx]
		self.send_buffer(buffer)
		
	def set_charset(self,chrset):
		self.send_ctrl_seq( [0x1B, 0x52, chrset] )
		
	def clearscreen(self):
		self.send_ctrl_seq( [0x1B, 0x5B, 0x32, 0x4A] )
		
	def printchr(self,chr):
		self.send_ctrl_seq( [chr] )
		
	def poscur(self,line,col):
		seq=[]
		seq.append( 0x1B )
		seq.append( 0x5B )
		assert( 0 <= line <= 9)
		seq.append( 0x30 + line )
		seq.append( 0x3B )
		assert( 0 <= col <= 99)
		diz,unit = divmod(col,10)
		seq.append( 0x30 + diz)
		seq.append( 0x30 + unit)
		seq.append( 0x48 )
		self.send_ctrl_seq( seq )
		
	def write_msg(self,msgu):
		msg=msgu.encode('cp858')
		msg_chr=list(msg)[0:29]
		self.send_ctrl_seq(map( ord, msg_chr ))
	

