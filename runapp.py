#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, string, os, sqlite3

if( not( os.path.isfile( 'run.db'))):
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
    
command = -1
while(command):
    print("1. Insert run data")
    print("2. Insert place data")
    print("0. Exit\n")
    print "Choice:",
    command = string.atoi( raw_input())
    print(command)
    
