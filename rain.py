"""
#1: GitHub repo containing a real-world problem modeled using OOP
 while taking advantage of inheritance, encapsulation, polymorphism and the other OOP concepts.

"""
openWeatherMap_key = "bf535a3579ee4b5aa616bf965e7225f5"
from urllib2 import Request, urlopen, URLError
import socket, json
def Internet_connection_check():
	host="8.8.4.4"
	port = 53
	timeout = 2
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except Exception as e:
		print str(e)
		return False

def Ask_Weather_At_Location():
	#First we need to check for internet connection
	city_travel = raw_input('Which city will you be travelling to?  Enter it\'s zip code:')
	api_request = Request('http:/api.openweathermap.org/data/2.5/forecast?q='+city_travel+',us&mode=xml')
	response = urlopen('http://samples.openweathermap.org/data/2.5/forecast?zip='+city_travel+'&appid='+openWeatherMap_key+'')
	code_status = 	response.getcode()
	if(code_status == 400):
		print("It seems we have a bad request")
		return False
	elif code_status == 404:
		print("Our resource at openweatherMap is not available")
		return False
	elif code_status == 401:
		print("Not authenticated for API access")
		return False
	elif code_status == 403:
		print("Resource requires permission for viewing")
		return False
	elif code_status == 200 or code_status == 301:
		json_object = response.read().decode('utf-8')
		data = json.loads(json_object)
		print ('The rain condition in '+city_travel+'for the last three hours is '+str(data['list'][1]['rain']['3h'])+'mm')  # prints "Clear"
	else:
		pass



if Internet_connection_check():
	Ask_Weather_At_Location()