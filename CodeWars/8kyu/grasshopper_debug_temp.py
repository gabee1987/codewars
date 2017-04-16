def weather_info(temp):
    c = float(convertToCelsius(temp))
    if (c <= 0):
        return str(c) + " is freezing temperature"
        print(str(c) + " is freezing temperature")
    else:
        return str(c) + " is above freezing temperature"
        print(str(c) + " is freezing temperature")
    
def convertToCelsius(temperature):
  celsius = (temperature - 32) * (5.0 / 9.0)
  print(celsius)
  return celsius

weather_info(50)
weather_info(23)