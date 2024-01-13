import requests
import json
api_key = "d6a9287145fb2e02357d432fc58c0c5e"  # Replace with your API key

location = input("Enter city or ZIP code: ")

base_url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': location,
    'appid': api_key,
    'units': 'metric'  # Use 'imperial' for Fahrenheit
}

try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    try:
        weather_data = response.json()
        print("\nCurrent Weather:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    except ValueError:
        print("Error: Invalid JSON in the API response")
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {str(e)}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
