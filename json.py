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
	def settime():
		with open("/tmp/saved_time", "w") as files:
			d  = datetime.datetime.now().day
			result = requests.get(URL).json()["results"]["sunset"]
			sunset = result.split(":")
			sunseth = int(sunset[0])+12+uts
			sunsetm = int(sunset[1])
			sumarno = str(d) +":"+ str(sunseth)+":"+str(sunsetm)
			files.write(sumarno)
			return sunseth, sunsetm
	nalf = os.path.exists("/tmp/saved_time")
	if nalf == False:
		sunseth, sunsetm = settime()
	else:
		with open("/tmp/saved_time", "r") as files:
			d  = datetime.datetime.now().day
			w = files.read().split(":")
			date = w[0]
			if date == str(d):
				sunseth = int(w[1])
				sunsetm = int(w[2])
			else:
				sunseth, sunsetm = settime()
	if sunseth>24:
		sunseth=sunseth-24
	if sunseth == nowh  and sunsetm <= nowm:
		return "ON"
	if sunseth < nowh < 20:
		return "ON"
	if nowh >=20 or nowh<sunseth:
		return "OFF"
	if nowh == sunseth or nowm<sunsetm:
		return "OFF"

for h in range(24):
	for m in range(0,60,1):
		print str(h)+":"+str(m)+ " "+str(sunsetfunkcia(h,m))
