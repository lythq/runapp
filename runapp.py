#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, string, os, sqlite3
from datetime import date

def createdb():
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute('''create table places
    (id_place integer primary key, country text, town text, place text)''')
    c.execute('''create table runs
    (id_run integer primary key, date text, duration text, hravg integer,
     hrmax_session integer, hrmax_total integer, lim_min integer,
     lim_max integer, zone_run text, zone_expected text, max_run text, 
     id_place integer references places)''')
    con.commit()
    c.close()

def createplace():
    country = raw_input("Country: ")
    town = raw_input("Town: ")
    place = raw_input("Place: ")
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute("""insert into places
                 values (null, ?, ?, ?)""", (country, town, place))
    con.commit()
    c.close()
    
def createrun():
    tod = date.today().isoformat()
    rdate = raw_input("Date (default: " + tod + ") YYYY-MM-DD: ")
    if( not( rdate)):
        rdate = tod
    print rdate

if( not( os.path.isfile( 'run.db'))):
    createdb()
command = -1
while(command):
    print "\n1. Insert run data"
    print "2. Insert place data"
    print "0. Exit\n"
    command = string.atoi( raw_input("Choice: "))
    if( command == 1):
        createrun()
    elif( command == 2):
        createplace()

    
