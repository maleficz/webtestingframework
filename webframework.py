#!/usr/bin/python2
# encoding: utf-8
# Testing Web Framework - Copyright (C) <2016> - <Hanom1960>
#
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
from modules import adminder
from modules import inurlsearch
from modules import sqlimod
from modules import portsmod
from modules import fingerwebmod
from modules import checker

def logo():
    print """
 _____          _   _             __    __     _     
/__   \___  ___| |_(_)_ __   __ _/ / /\ \ \___| |__  
  / /\/ _ \/ __| __| | '_ \ / _` \ \/  \/ / _ \ '_ \ 
 / / |  __/\__ \ |_| | | | | (_| |\  /\  /  __/ |_) |
 \/   \___||___/\__|_|_| |_|\__, | \/  \/ \___|_.__/ 
                            |___/                    
   ___                                            _    
  / __\ __ __ _ _ __ ___   _____      _____  _ __| | __
 / _\| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
/ /  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
\/   |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\


	Coder: Hanom1960 Email/XMPP: hanom1960@cock.lu
		Twitter: @hanomlulzsec
"""
def gems():
+    print "Checking if Bundler is installed ..."
+    gem=os.system("cd joomlavs && bundle | grep 'Bundle complete! 5 Gemfile dependencies, 15 gems now installed.'")
+    if gem == 0:
+        print "Bundler is installed. Continuing."
+        pass
+    else:
+        print """You need to install bundler, proceeding to the installation.
+ Bundler is required for a vulnerabilities scanner, you need root or sudo privileges to install.
+It can take a while."""     
+        inst = raw_input("You want to continue with the installation? y/n : ")
+        if inst=="y":
+            print "Installing bundler..."
+            os.system("cd joomlavs && sudo gem install bundler && bundle install")
+            pass
+        elif inst=="n":
+            print "Installation canceled, this will create problems in the option d) of the menu using joomlavs. Continuing ..."
+            pass
def disclaimer():
    print "[!] legal disclaimer: Usage of Testing Web Framework for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program"
try:
    logo()
    print ""
    disclaimer()
    print ""
    gems()
    print ""
    checker.check()
    def webframework():
        print ""
        print """Select only one opcion.
        a) Search for SQLi, LFI, RCE, XSS vulnerables URLs.
        b) Make SQLi to a vulnerable web
        c) Make a compleate scann to an host, enumerate DNS, Bypass Cloudflare y more.
	d) Make web penetration tests & vulnerabilities analisys.
        e) Search for the web site's admin panel.
        f) Exit.
        """
        sel=raw_input("Select: ")
        if sel == "a":
            inurlsearch.execute()
            webframework()
        elif sel == "b":
            sqlimod.execute()
            webframework()
        elif sel == "c":
            portsmod.menu()
            webframework()
        elif sel == "d":
            fingerwebmod.execute()
            webframework()
        elif sel == "e":
            adminder.adminfind()
            webframework()
        elif sel == "f":
            print "Exiting."
        else:
            webframework()
    webframework()

except KeyboardInterrupt:
    print "Exiting."
    pass
os._exit(0)
