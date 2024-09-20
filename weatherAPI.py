import requests
from PIL import Image as im
from io import BytesIO
from datetime import datetime

apiKey = "-"


    
    
def GetWeather(lon,lat):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,daily,hourly,alerts&units=metric&appid={apiKey}"
    airUrl = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apiKey}"
    
    response = requests.get(url)
    airResponse = requests.get(airUrl)

    if response.status_code == 200:
        data = response.json()
        airData = airResponse.json()
        
        currentTemp = data["current"]["temp"] ## in degrees
        feelsLikeTemp = data["current"]["feels_like"] ## in degrees °
        uvIndex = data["current"]["uvi"] ## in uv index 
        cloudPercent = data["current"]["clouds"] ## in percentage
        windSpeed = data["current"]["wind_speed"] ## * 3.6 to convert to km/h
        humidity = data["current"]["humidity"] ## in percentage
        pressure = data["current"]["pressure"] ## in hPa
        windDirection = data["current"]["wind_deg"] ## in degrees (direction)
        visibility = data["current"]["visibility"] ## in meters
        iconVal = data["current"]["weather"][0]["icon"] ## returns icon code use https://openweathermap.org/img/wn/{CODE}@2x.png to retrive 
        airQual = airData["list"][0]["main"]["aqi"] ## in air quality index
        cabonMon = airData["list"][0]["components"]["co"] ## in μg/m3
        nitrogenMon = airData["list"][0]["components"]["no"] ## in μg/m3
        nitrogenDio = airData["list"][0]["components"]["no2"] ## in μg/m3
        ozone = airData["list"][0]["components"]["o3"] ## in μg/m3
        sulpherDio = airData["list"][0]["components"]["so2"] ## in μg/m3
        finePart = airData["list"][0]["components"]["pm2_5"] ##  in μg/m3
        coarsePart = airData["list"][0]["components"]["pm10"] ## in μg/m3
        ammonia = airData["list"][0]["components"]["nh3"] ## in μg/m3
        sunset = data["current"]["sunset"] ## prints as int
        sunrise = data["current"]["sunrise"] ## prints as int
        dewPoint = data["current"]["dew_point"] ## in degrees °
        timeOffset = data["timezone_offset"]
        
        dtSet = datetime.fromtimestamp((sunset - 7200) + timeOffset)  ## need to take away the timestamp offset of the server
        dtRise = datetime.fromtimestamp((sunrise - 7200) + timeOffset)
        legSunset = dtSet.strftime("%H:%M:%S") ## PRINTS IN LOCAL GIB TIME
        legSunrise = dtRise.strftime("%H:%M:%S")  ## PRINTS IN LOCAL GIB TIME
        
        
        #print(data)  ## use for testing
        
        
        
        ## Store the image
        imgUrl = f"https://openweathermap.org/img/wn/{iconVal}@2x.png"
        imgResponse = requests.get(imgUrl)
        
        if imgResponse.status_code == 200:
            image = im.open(BytesIO(imgResponse.content)) ## saves the image to the variable
            #image.show()
        else:
            print(f"Error, could not save image , status code: {imgResponse.status_code}")
         
        print(data)
        print(airData)

    else:
        print(f"Request failled, Status Code: {response.status_code}")
        
def getLoc(place):
    
    
    url =  f"http://api.openweathermap.org/geo/1.0/direct?q={place},&limit=1&appid={apiKey}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data[0]["lat"])
        print(data[0]["lon"])
    else:
        print(f"Error, Status Code: {response.status_code}")
    
    lat = data[0]["lat"]
    lon = data[0]["lon"]

    GetWeather(lon, lat)


def main():
    inp = input("Select the following: \n 1. Search by location \n 2. Search by coords\n")
    
    if inp.isalpha():
        print("Error, please only enter numbers")
        main()
    elif inp.isdigit():
        match inp:
            case "1":
                inpPlace = input("Enter Place:\n")
                getLoc(inpPlace)
            case "2":
                inpLat = input("Enter Lat:\n")
                inpLon = input("Enter Lon:\n")
                GetWeather(inpLon,inpLat)
            case _:
                print("Unknown Command")
                main()
                






main()
