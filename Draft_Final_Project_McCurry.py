#import requests - Don't quite understand this aspect just yet

def fetch_data(zip = None, city = None):
    
    #base URL for fetching weather
    baseUrl = "http://api.openweathermap.org/data/2.5/weather"

    #API ID for the website
    apiid = "15d4c5a3f9b3c88912845f2aaed85595"

    #Checking if input is zipcode or city name
    if zip is not None:
        baseUrl += "?zip=" + str(zip) + ",us"
    
    else:
        baseUrl += "?q=" + str(city) + ",us"

    baseUrl += "&appid=" + str(apiid)

    r = requests.get(baseUrl) #How does this connect to the import?

    return r

def showResults(resp):

    #Output to show request was successful
    if resp.status_code == 200:
        data = resp.json()
        print(data ['name'])
        print(f"""{data['name']} Weather Forecast:
        There will be {data['weather'] [0] ['description']} with wind speed of {data ['wind'] ['speed']}.
        Wisibility will be {data ['visilbility']}.
        Min. Temp will be {data ['main'] ['temp_min']} and max will be {data ['main'] ['temp_max']}.
        """)