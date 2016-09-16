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
def host():
    global host
    host=raw_input("Introduce the target host for scan: ")
    if host == "":
        print "Invalid Host."
        menu()
    else:
        return host
def port():
    global port
    port=raw_input("Introduce the port or ports who you need scan (if you wish use a port range, write on this way 1-1000): ")
    if port == "":
        print "Invalid Puerto."
        menu()
    else:
        return port
def intensescan():
    host()
    print "For this scan you need sudo or root privileges, so please put your password here if you'r not root."
    subprocess.call(["sudo","nmap","-A","-T4","-sS","-Pn","-O","-sV","-p","1-10000","-v",host])
    menu()
def fastscan():
    host()
    subprocess.call(["nmap","-F",host])
    menu()
def detectserv():
    host()
    subprocess.call(["nmap","-sP",host])
    menu()
def detectver():
    host()
    subprocess.call(["nmap","-sV",host])
    menu()
def escanport():
    host()
    port()
    subprocess.call(["nmap","-p",port,host])
    menu()
def recsystem():
    host()
    print "For this scan you need sudo or root privileges, so please put your password here if you'r not root."
    subprocess.call(["sudo","nmap","-O",host])
    menu()
def enumdns():
    host()
    print "Enumerating DNS's"
    subprocess.call(["dnsenum",host])
    menu()
def bypasscloud():
    host()
    print "Try to Bypass Cloudflare using fierce..."
    subprocess.call(["fierce","-dns",host])
    menu()
def menu():
    print """Pleace select one of the next options
    a) Host full scan (Slow but the most complete).
    b) Host fast scan.
    c) Detect host running servers.
    d) Detect host running servers versions.
    e) Scan a specific  port or a port range.
    f) Detect host operative system .
    g) Enumerate host DNS.
    h) Bypass cloudflare.
    i) Exit.
    """
    sel=raw_input("Introduce your option: ")
    if sel == "a":
        intensescan()
    elif sel == "b":
        fastscan()
    elif sel == "c":
        detectserv()
    elif sel == "d":
        detectver()
    elif sel == "e":
        escanport()
    elif sel == "f":
        recsystem()
    elif sel == "g":
        enumdns()
    elif sel == "h":
        bypasscloud()
    elif sel == "i":
        print "Exiting."
    else:
        print "Invalid Option."
        menu()         
