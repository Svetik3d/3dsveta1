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
	n = datetime.datetime.now()
	nh = n.hour
	nm = n.minute
	if nh >= sunseth and sunsetm >= nm and nm < sunsetm+5:
		return "ON"
	if nh >=20 and nm>=5:
		return "OFF"

print sunsetfunkcia()







