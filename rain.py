"""
#1: GitHub repo containing a real-world problem modeled using OOP
 while taking advantage of inheritance, encapsulation, polymorphism and the other OOP concepts.

"""
openWeatherMap_key = "bf535a3579ee4b5aa616bf965e7225f5"
from urllib2 import Request, urlopen, URLError
import json


def Ask_Location():
	city_travel = raw_input('Which city will you be travelling to?  Enter it\'s zip code:')
	api_request = Request('http:/api.openweathermap.org/data/2.5/forecast?q='+city_travel+',us&mode=xml')
	response = urlopen('http://samples.openweathermap.org/data/2.5/forecast?zip='+city_travel+'&appid='+openWeatherMap_key+'')
	json_object = response.read().decode('utf-8')
	data = json.loads(json_object)
	print ('The rain condition in '+city_travel+'for the last three hours is '+str(data['list'][1]['rain']['3h'])+'mm')  # prints "Clear"
	


Ask_Location()
