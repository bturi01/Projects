#import speech
import datetime
import os

def getCurrentTime():
	"""
	Returns the properly formatted current time
	"""
	now = datetime.datetime.now()
	hr = now.hour
	greeting = ""
	ampm = ""
	if (hr < 12): #morning
		hr = hr
		greeting = "morning"
		ampm = "am"
	elif (hr >= 12 and hr < 1): #afternoon
		hr = hr
		greeting = "afternoon"
		ampm = "noon"
	elif (hr > 12 and hr < 19): #evening
		hr = hr - 12
		greeting = "evening"
		ampm = "pm"
	else:  #night
		hr = hr - 12
		greeting = "night"
		ampm = "pm"
	return str(hr) + ':' + str(now.minute),ampm, ' in the ', greeting

print getCurrentTime()
