import requests
from pprint import pprint

'''
inspired by https://www.youtube.com/channel/UC2R1v4d75yXisbufyoLYryA
'''


def get_lat_lon():
	'''
	# find lattitude and longtitude from your ip
	output lat and long
	'''

	# find lattitude and longtitude from your ip
	latloc = requests.get('https://ipinfo.io')
	dat_latloc = latloc.json()

	# extract lat and lon
	location = dat_latloc['loc'].split(',')
	latitute = location[0]
	longtitue = location[1]

	# url of the open weather map
	url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=bbf0596b81ffe5ea776815493c47d627&units=metric'.format(
		latitute, longtitue)

	return url


def get_city_name(name_of_city):

	'''
	In case searching direct from city name
	'''
	# city = 'Istanbul'
	city = name_of_city

	# url of the open weather map
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=bbf0596b81ffe5ea776815493c47d627&units=metric'.format(city)
	
	return url


def get_data(url):


	# requesting get
	res = requests.get(url)
	data = res.json()
	return data

def printing_formatter(data):

	print('City Name = {}'.format(data['name']))
	print('Temp = {} Celcius'.format(data['main']['temp']))


def main():
	url = get_lat_lon()
	data = get_data(url)
	printing_formatter(data)

if __name__ == '__main__':
	main()

# main = data['main']
