from bakery_weather import get_weather

for forecast in get_weather(39.6782, -75.7616).forecast:
    print(forecast)
    
print(get_weather(39.6782, -75.7616).current.humidity)