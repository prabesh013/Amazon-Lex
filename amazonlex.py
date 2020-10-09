import json
from botocore.vendored import requests
import datetime
def lambda_handler(event, context):
    city = event["currentIntent"]["slots"]["City"]
    res = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={"q": city , "appid":"Enter your api key"}).json()
    
    description = res["weather"][0]["description"]
    temperature = res["main"]["temp"]
    pressure = res["main"]["pressure"]
    humidity = res["main"]["humidity"]
    wind_speed = res["wind"]["speed"]
   
    output = 'For {} the weather today is: {} with Temperature: {} , Pressure: {} , Humidity: {} and Wind speed: {} '.format(city, description, temperature, pressure, humidity, wind_speed)
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": output
            }
        }
    }

