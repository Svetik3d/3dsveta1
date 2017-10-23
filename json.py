#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

import json
import requests
import datetime

URL = 'https://api.sunrise-sunset.org/json?lat=55.729887&lng=38.941911&date=today&formatted=1'

def sunsetfunkcia():
	result = requests.get(URL).json()["results"]["sunset"]
	sunset = result.split(":")
	sunseth = int(sunset[0])
	sunsetm = int(sunset[1])
	nowt = datetime.datetime.now()
	nowh = nowt.hour+15
	if nowh<0:
		nowh=nowh-24
	nowm = nowt.minute
	if nowh >= sunseth and sunsetm >= nowm and nowm < sunsetm+5:
		return "ON"
	if nowh >=20 and nowm>=5:
		return "OFF"

print sunsetfunkcia()
