#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, string, os, sqlite3
from datetime import date

#TODO: Verify key constraints & validate input formatting

def createdb():
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute('''create table heart_rates
    (date_rate string primary key, hrmax integer)''')
    c.execute('''create table places
    (id_place integer primary key, country text, town text,
     place text, obs_place text)''')
    c.execute('''create table trains
    (id_train integer primary key, duration_exp text, lim_min integer,
     lim_max integer, zone_exp text, max_run text, obs_train text)''')
    c.execute('''create table runs
    (id_run integer primary key, date_run text, duration_run text, hravg integer,
     hrmax_run integer, zone_run text, id_place integer references places,
     obs_run text)''')
    con.commit()
    c.close()
    createhr()

def createplace():
    country = raw_input("Country: ")
    town = raw_input("Town: ")
    place = raw_input("Place: ")
    obs = raw_input("Notes: ")
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute("""insert into places
                 values (null, ?, ?, ?, ?)""", 
                 (unicode(country, 'utf-8'), unicode(town, 'utf-8'), 
                  unicode(place, 'utf-8'), unicode(obs, 'utf-8')))
    con.commit()
    c.close()
    
def createrun():
    tod = date.today().isoformat()
    rdate = raw_input("Date (default: " + tod + ") YYYY-MM-DD: ")
    if( not( rdate)):
        rdate = tod
    print rdate
    rdur = raw_input("Duration HH:MM:SS: ")
    rhravg = string.atoi( raw_input("Average heart rate: "))

def createhr():
    tod = date.today().isoformat()
    hdate = raw_input("Date (default: " + tod + ") YYYY-MM-DD: ")
    if( not( hdate)):
        hdate = tod
    hrmax = string.atoi( raw_input("Maximum heart rate: "))
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute("""insert into heart_rates
                 values (?, ?)""", (hdate, hrmax))
    con.commit()
    c.close()

if( not( os.path.isfile( 'run.db'))):
    createdb()
command = -1
while(command):
    print "\n1. Insert run data"
    print "2. Insert place data"
    print "3. Insert new maximum heart rate"
    print "0. Exit\n"
    command = string.atoi( raw_input("Choice: "))
    if( command == 1):
        createrun()
    elif( command == 2):
        createplace()
    elif( command == 3):
        createhr()

    
