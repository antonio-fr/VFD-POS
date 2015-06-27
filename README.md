  VFD PoS
===========

VFD PoS is a Python library dedicated for driving Wincor Nixdorf Point of Sale VFD USB, such as BA-66 USB. This library should be compatible with any WN BA-6x USB VFD.

Provides high level abstraction to use Wincor Nixdorf Point of Sale VFD USB

* Easy to use and handle, play with your VFD in no time
* Full python code to access VFD through USB
* Access using HID, no driver needed
* Plug and Play
* Character encoding automatic conversion
* Very limited python dependencies (provided in zip)


## Dependencies

This library needs pywinusb, and can only work in Windows. The Linux version should be easy to write following this code (don't forget to let it public or republish as this piece of software uses GPLv3 licence).

You don't need anything if your download direcly zip release package as VFD-POS_vxx.zip.

Some examples which pull info from Internet require Easy-REST-JSON library available at 
https://github.com/antonio-fr/Easy-REST-JSON

To test quickly, copy examples at the same level as the library (vfd_pos.py) and run them.

## Using library

If your OS is Windows, download direcly zip package release.

To use the library, just copy vfd_pos.py and use import as usual

    import vfd_pos

or

    from vfd_pos import *

#### Initialisation

Class constructor detects, tries to connect to VFD, initializes it and finally returns a library object to send commands. You need USB product ID (PID) of the VFD. For BA66 USB, this is 0x0201.

    MyVFD = vfd_pos.vfd_pos(PRODUCT_ID)


#### Self-Test

Tell the VFD to perform self-test. You may need to initialize VFD again after do so.

    MyVFD.selftest()


#### Reset

Tell the VFD to perform a reboot. You need to initialize VFD again after do so.

    MyVFD.reset()


#### Set Charset

Set the VFD charset. See your WN operational manual documentation for char code.
During initilisation, WN VFD is automatically set up to 0x31 = Code Page 858. Don't change it unless you really have specific need, this would cause issues with write_msg function.

Character tables are available in :
http://www.wincor-nixdorf.com/internet/cae/servlet/contentblob/614268/publicationFile/60592/BA6x_Character_Appendix_english.pdf

    MyVFD.set_charset(CHARSET_CODE)


#### Clear Screen

Clear and erase the VFD screen.

    MyVFD.clearscreen()


#### Print Character

Print a character from its number at the cursor position

    MyVFD.printchr(CHAR_CODE)


#### Position Cursor

Change the position of the cursor to a given column and line. If 0 is provided for a parameter, no change is performed for it.

    MyVFD.poscur(LINE, COLUMN)


#### Write Message

Write a message to the VFD screen at the cursor position. This function uses automatic decoding of any unicode character. In case you provide direclty the string don't forget trailing u (  u"string" ). If you change the charset to another one, this function might bring some issues. You can use "\r" and "\n" inside the string to get line control.

    MyVFD.write_msg(MESSAGE_STRING)


#### Close Device

Close the connection properly with the VFD, and VFD will be turned off. Normally, when python program stops, it closes the link automatically.

    MyVFD.close()


**Form more details: see code in examples directory**


## Example :
The following example displays a basic text on a BA66 USB VFD.

    import vfd_pos
    wnpos = vfd_pos.vfd_pos(0x0201)
    wnpos.write_msg("Hello World !\r\nThat works :)")
    raw_input("PRESS ENTER TO EXIT")
    wnpos.close()


Licence :
----------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
