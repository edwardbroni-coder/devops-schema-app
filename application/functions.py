import requests
from pypdf import PdfReader
import json
import pandas as pd
import re
import weather_codes_icons


def get_schema()->list: 
	"""
	Funktion som skrapar schema från hemsida och sparar en pdf file.
	Samt tar fram data om vilket datum nästa lektion är. 	
	"""
	# Definerandet av sökväg och url.
	local_path = "./static/"
	url = "https://cloud.timeedit.net/nackademin/web/1/ri.pdf?h=t&sid=19&p=0.m%2C12.w&objects=4662.6&ox=0&types=0&fe=0&mw=300&ps=A4&sp=f&pl=2&fs=9&cl=x90&shf=0&title=Schema%201%20DevOps"
	
	# Scrapa Schema från timeedit
	response = requests.get(url)

	# Spara data som fil: schema.pdf
	try:
		with open(local_path+"schema.pdf", "wb") as file:
			file.write(response.content)
	except:
		print('\nError writing schema.pdf')
	finally:
		print('\nFile schema.pdf saved successfully')

	#Läs in schema pdf från fil
	reader = PdfReader(local_path+"schema.pdf")
	page = reader.pages[0]
	text = page.extract_text()
	
    #REGEX hitta mönster i schema sträng för att plocka fram data + SPLICE nästa lektions datum.
	p = re.compile(r'\w\w\w+\s\d\d\d\d.')
	m = p.search(text)
	a = m.start()
	m = p.search(text, pos=101)
	b = m.start()

    #Skapa next date och next_class variabler
	next_date :str = text[(a+4):(a+9)]+text[(a+10):(a+15)]
	next_class :str = text[a:(a+9)]+text[(a+10):(a+15)]+text[(a+15):b]
	next_class : list = next_class.split(sep='\n')

	return next_date, next_class


def get_weather(next_date:str) -> list:
	"""
	Function that gets 7 days of daily weather info.
	Args: date of next "class" as next_class
	Returns LIST and Pandas DF
	"""
	url = "https://api.open-meteo.com/v1/forecast"
	
	#Nackademins Location 59.3455220833232, 18.02341592893776
	params = {
	"latitude": 59.34,
	"longitude": 18.02,
	"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "rain_sum", "showers_sum", "snowfall_sum", "precipitation_sum", "precipitation_hours", "precipitation_probability_max", "wind_speed_10m_max"],
	"timezone": "Europe/Berlin",
	"wind_speed_unit": "ms",
	}
	# Hämta Väderdata från OpenMeteo-API
	response = requests.get(url, params=params)
	data = response.json()
	
    # Processa dagligdata i separata variabler.
	daily = data['daily']
	units = data['daily_units']
	#print(units)

	dates = daily['time']
	daily_weather_code = daily['weather_code']
	daily_temperature_2m_max = daily['temperature_2m_max']
	daily_temperature_2m_min = daily['temperature_2m_min']
	daily_sunrise = daily['sunrise']
	daily_sunset = daily['sunset']
	daily_daylight_duration = daily['daylight_duration']
	daily_sunshine_duration = daily['sunshine_duration']
	daily_rain_sum = daily['rain_sum']
	daily_showers_sum = daily['showers_sum']
	daily_snowfall_sum = daily['snowfall_sum']
	daily_precipitation_sum = daily['precipitation_sum']
	daily_precipitation_hours = daily['precipitation_hours']
	daily_precipitation_probability_max = daily['precipitation_probability_max']
	daily_wind_speed_10m_max = daily['wind_speed_10m_max']


    # Skapa Dict som inkluderar enheter.
	daily_data = {}
	daily_data["datum"] = dates
	daily_data["weather_code"] = daily_weather_code
	daily_data["temperature_2m_max" + " °C"] = daily_temperature_2m_max
	daily_data["temperature_2m_min" + " °C"] = daily_temperature_2m_min
	daily_data["sunrise"] = daily_sunrise
	daily_data["sunset"] = daily_sunset
	daily_data["daylight_duration"] = daily_daylight_duration
	daily_data["sunshine_duration"] = daily_sunshine_duration
	daily_data["rain_sum" + " mm"] = daily_rain_sum
	daily_data["showers_sum"+ " mm"] = daily_showers_sum
	daily_data["snowfall_sum"+ " cm"] = daily_snowfall_sum
	daily_data["precipitation_sum"+ " mm"] = daily_precipitation_sum
	daily_data["precipitation_hours"] = daily_precipitation_hours
	daily_data["precipitation_probability_max"+ " %"] = daily_precipitation_probability_max
	daily_data["wind_speed_10m_max"+ " m/s"] = daily_wind_speed_10m_max

	# Skapa Pandas DataFrame och Runda värden till 1 decimal
	daily_dataframe = pd.DataFrame(data = daily_data)
	daily_dataframe = daily_dataframe.round(1)

    # For loop to match next_class date with weather data.
	weather_info : list=[]
	i = 0
	for x in dates:
		if next_date == x:
			weather_info = [daily_weather_code[i], 
				   			daily_temperature_2m_max[i], 
							daily_temperature_2m_min[i], 
							daily_precipitation_sum[i]
							]
		i +=1	

	return weather_info, daily_dataframe


def weather_text(weather_code : str) -> str:
	""" 
	Funktion som matchar Väderkod med Beskrivning av väder från weather_codes_icons.py
	Returnerar Beskrivning av väder som str.
	"""
	for x in weather_codes_icons.weathercodes.keys():
			if x == weather_code:
				w_text = weather_codes_icons.weathercodes.get(x)
				
				return w_text


def get_icon(weather_code : str) -> str:
	""" 
	Funktion som matchar Väderkod med Ikon från weather_codes_icons.py
	Returnerar Beskrivning av väder som STR path till icon.
	"""
	for x in weather_codes_icons.weather_icons.keys():
			if x == weather_code:
				icon_path = weather_codes_icons.weather_icons.get(x)
				icon_path = './static/images/' + icon_path
				return icon_path


def post_to_DISCORD(content) -> None:
    """
	POST STRING TO DISCORD-CHANNEL via Discords-API.
	Möjlighet att ersätta input från form på hemsidan.
	För DEMO kör vi på det här. 
	"""
    url = 'INPUT UNIQUE DISCORD URL'
    authorization = 'INPUT YOUR UNIQUE AUTHORIZATION CODE FROM DISCORD'
	
	# CONTENT and AUTHORIZATION VALUES FROM DISCORD CHANNEL
    payload = {'content' : content}
    headers= {'Authorization' : authorization}
	
    # Post to Discord channel
    response = requests.post(url, payload, headers=headers)







if __name__ == "__main__":
    next_date, next_class  = get_schema()
    weather_from_api, daily_df = get_weather(next_date)
    print('\nWeather_Code: {}\nMax_Temp:{}\nMin_Temp:{}\nTot_regn/snö:{}'.format(weather_from_api[0],weather_from_api[1],weather_from_api[2],weather_from_api[3]))
    
    weather_code = str(weather_from_api[0])
    weather_description = weather_text(weather_code)
    icon_path = get_icon(weather_code)
    print(weather_description)
    print(icon_path)

	#Message to Discord med Markdown-syntax
    weather_text_info = f'\n{weather_description}\nMax_Temp:{weather_from_api[1]}\nMin_Temp:{weather_from_api[2]}\nTot_regn/snö:{weather_from_api[3]}'
    content : str = f"""Om det här meddelandet går fram funkar all backend.\n\n
						**Next Class: {next_class[0]}**\n
						**Info:**\n{next_class[1]}\n{next_class[2]}\n
						**Weather Forcast:**\n{weather_text_info}\n
						***Hello World, från vår App!***"""
	

    print('\nContent to Discord: ',content)
    post_to_DISCORD(content)