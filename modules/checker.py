#!/usr/bin/python2
# encoding: utf-8
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import os
isnm=os.path.isfile("/usr/bin/nmap")
isfierce=os.path.isfile("/usr/bin/fierce")
ismap=os.path.isfile("/usr/bin/sqlmap")
isenum=os.path.isfile("/usr/bin/dnsenum")
isnikto=os.path.isfile("/usr/bin/nikto")
iswhatw=os.path.isfile("/usr/bin/whatweb")
iswp=os.path.isfile("/usr/bin/wpscan")
def check():
    if isnm and isfierce and ismap and isenum and isnikto and iswhatw and iswp:
        print "All needed is installed, worcking."
    elif isnm == False:
        print "You need nmap installed."
        os._exit(0)
    elif isfierce == False:
        print "You need fierce installed."
        os._exit(0)
    elif ismap == False:
        print "You need sqlmap installed."
        os._exit(0)
    elif isenum == False:
        print "You need dnsenum installed."
        os._exit(0)
    elif isnikto == False:
        print "You need Nikto installed."
        os._exit(0)
    elif iswhatw == False:
        print "You need Whatweb installed."
        os._exit(0)
    elif iswp == False:
        print "You need Wpscan installed."
        os._exit(0)

