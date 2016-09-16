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
import os
import subprocess
import portsmod

def whatw():
    host=portsmod.host()
    print "Receiving information from the web site."
    print ""
    subprocess.call(["whatweb","-v",host])
    execute()
def nickscan():
    host=portsmod.host()
    print "Looking for vulnerabilities on the web site with nikto..."
    subprocess.call(["nikto","-no404","-host",host])
    execute()
def joomsc():
    host=host=portsmod.host()
    print "Looking for vulnerabilities on the web site with joomlavs..."
    subprocess.call(["chmod","+x","joomlavs"])
    subprocess.call(["./joomlavs","-u",host,"-a"])
    execute()
def joomsctor():
    host=host=portsmod.host()
    print "Looking for vulnerabilities on the web site with joomlavs through TOR..."
    subprocess.call(["chmod","+x","joomlavs"])
    subprocess.call(["./joomlavs","-u",host,"--proxy","SOCKS5://127.0.0.1:9050","-a"])
    execute()

def wordpresscan():
    host=host=portsmod.host()
    print "Looking for vulnerabilities on the web site with wpscan..."
    subprocess.call(["sudo","wpscan","-u",host,"--enumerate","p","--enumerate","t","--enumerate","u"])
    execute()
def wordpresscantor():
    host=host=portsmod.host()
    print "Looking for vulnerabilities on the web site with wpscan through tor..."
    subprocess.call(["sudo","wpscan","-u",host,"--enumerate","p","--enumerate","t","--enumerate","u","--proxy","socks5://127.0.0.1:9050"])
    execute()

def execute():
    print """Choose one of the next opcions:
    a) Receive information form the web site, server, Ip, CMS, server's Software and other things.
    b) Looking for web vulnerabilities using nikto.
    c) Looking for Joomla web vulnerabilities.
    d) Looking for Joomla web vulnerabilities using TOR.
    e) Looking for WordPress web vulnerabilities.
    f) Looking for WordPress web vulnerabilities using TOR.
    g) Exit."""
    sel=raw_input("Put your option: ")
    if sel== "a":
        whatw()
    elif sel == "b":
        nickscan()
    elif sel == "c":
        joomsc()
    elif sel == "d":
        joomsctor()
    elif sel == "e":
        wordpresscan()
    elif sel == "f":
        wordpresscantor()
    elif sel == "g":
        print "Exiting."
    else:
        execute()
