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
     id_train integer references trains, obs_run text)''')
    con.commit()
    c.close()
    createhr()

def createhr():
    tod = date.today().isoformat()
    hdate = raw_input("Date (default: " + tod + ") (YYYY-MM-DD): ")
    if( not( hdate)):
        hdate = tod
    hrmax = string.atoi( raw_input("Maximum heart rate: "))
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute("""insert into heart_rates
                 values (?, ?)""", (hdate, hrmax))
    con.commit()
    c.close()

def createtrain():
    tdur = raw_input("Duration (HH:MM:SS): ")
    tlmin = string.atoi( raw_input("Minimum heart rate: "))
    tlmax = string.atoi( raw_input("Maximum heart rate: "))
    tzone = raw_input("Time in training zone (HH:MM:SS): ")
    trun = raw_input("Maximum contiguous run duration (HH:MM:SS): ")
    obs = raw_input("Notes: ")
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute("""insert into trains
                 values (null, ?, ?, ?, ?, ?, ?)""", 
              (tdur, tlmin, tlmax, tzone, trun, unicode(obs, 'utf-8')))
    con.commit()
    c.close()

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
    
def listrains():
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute('select id_train, obs_train from trains order by id_train')
    print
    for row in c:
        print str(row[0]) + ". " + row[1]
    c.close()
    print
    
def listplaces():
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute('select * from places order by id_place')
    print
    for row in c:
        print str(row[0]) + ". " + row[3] + " - " + row[2] + ", " + row[1]
    c.close()
    print
    
def createrun():
    tod = date.today().isoformat()
    rdate = raw_input("Date (default: " + tod + ") (YYYY-MM-DD): ")
    if( not( rdate)):
        rdate = tod
    print rdate
    rdur = raw_input("Duration (HH:MM:SS): ")
    listrains()
    rtrain = string.atoi( raw_input("Running plan: "))
    rhravg = string.atoi( raw_input("Average heart rate: "))
    rhrmax = string.atoi( raw_input("Maximum heart rate: "))
    rzone = raw_input("Time in training zone (HH:MM:SS): ")
    listplaces()
    rplace = string.atoi( raw_input("Running place: "))
    robs = raw_input("Notes: ")
    con = sqlite3.connect('run.db')
    c = con.cursor()
    c.execute("""insert into runs
                 values (null, ?, ?, ?, ?, ?, ?, ?, ?)""", 
              (rdate, rdur, rhravg, rhrmax, rzone, rplace, rtrain,
               unicode(robs, 'utf-8')))
    con.commit()
    c.close()

if( not( os.path.isfile( 'run.db'))):
    createdb()
command = -1
while(command):
    print "\n1. Insert run"
    print "2. Insert train"
    print "3. Insert place"
    print "4. Insert new maximum heart rate"
    print "0. Exit\n"
    command = string.atoi( raw_input("Choice: "))
    if( command == 1):
        createrun()
    elif(command == 2):
        createtrain()
    elif( command == 3):
        createplace()
    elif( command == 4):
        createhr()

    
