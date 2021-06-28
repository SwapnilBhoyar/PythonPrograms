"""
@Author: Swapnil Bhoyar
@Date: 2021-06-28 22:35:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-28 22:35:00
@Title: Find effevtive temperature
"""
def calculateWindChill(temperatureValue, windSpeed):
    """
    Description:
        this function effective temperature
    Parameter:
        temperatureValue parameter consist temperature value
        windSpeed parameter consist wind speed value
    Return:
        retun wind chill value
    """
    windChill = 35.74 + 0.6215 * temperatureValue + (0.4275 * temperatureValue - 35.75) * (windSpeed ** 0.16)
    return windChill

try:
    temperatureValue = int(input("Enter temperatute value:"))
    windSpeed = int(input("Enter wind speed:"))
except ValueError:
    print("Enter proper value")

windChill = calculateWindChill(temperatureValue, windSpeed)
print("WindChill:", windChill)