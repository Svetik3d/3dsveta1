#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

import json
import requests
import datetime

URL = 'https://api.sunrise-sunset.org/json?lat=55.729887&lng=38.941911&date=today&formatted=1'
uts = 1

def sunsetfunkcia(nowh = datetime.datetime.now().hour, 	nowm = datetime.datetime.now().minute):
	result = requests.get(URL).json()["results"]["sunset"]
	sunset = result.split(":")
	sunseth = int(sunset[0])+12+uts
	sunsetm = int(sunset[1])
	if sunseth>24:
		sunseth=sunseth-24
	if nowh == sunseth and sunsetm >= nowm and nowm < sunsetm+5:
		return "ON"
	if nowh >=20 and nowm>=5:
		return "OFF"

for h in range(24):
	for m in range(0,60,5):
		print sunsetfunkcia(h,m)
