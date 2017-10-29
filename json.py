#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

import json
import requests
import datetime
import os

URL = 'https://api.sunrise-sunset.org/json?lat=55.729887&lng=38.941911&date=today&formatted=1'
uts = 1

def sunsetfunkcia(nowh = datetime.datetime.now().hour, 	nowm = datetime.datetime.now().minute):
	nalf = os.path.exists("/tmp/saved_time")
	with open("/tmp/saved_time", "r") as files:
		d  = datetime.datetime.now().day
		w = files.read().split(":")
		date = w[0]
		if date == str(d) and nalf == True:
			sunseth = int(w[1])
			sunsetm = int(w[2])
		if nalf == False or date != str(d):
			with open("/tmp/saved_time", "w") as files:
				result = requests.get(URL).json()["results"]["sunset"]
				sunset = result.split(":")
				sunseth = int(sunset[0])+12+uts
				sunsetm = int(sunset[1])
				sumarno = str(d) +":"+ str(sunseth)+":"+str(sunsetm)
				files.write(sumarno)
	if sunseth>24:
		sunseth=sunseth-24
	if sunseth <= nowh < 20:
		return "ON"
	if nowh >=20 or nowh<sunseth:
		return "OFF"

for h in range(12,24):
	for m in range(0,60,5):
		print str(h)+":"+str(m)
		print sunsetfunkcia(h,m)
