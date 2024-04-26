print("Digite uma temperatura em Celsius:")
tempCelsius = float(input())

def convertToFahrenheit(celsius):
 return  9 / 5 * celsius + 32

def convertToKelvin(celsius):
  return celsius + 273.15

tempFahrenheit = convertToFahrenheit(tempCelsius)
tempKelvin = convertToKelvin(tempCelsius)

print("A temperatura em Celsius é:" + str(tempCelsius) +"°C")
print("A temperatura em Fahrenheit é:" + str(tempFahrenheit) +"°F")
print("A temperatura em Kelvin é:" + str(tempKelvin) +"°K")
