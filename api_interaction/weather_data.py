import requests

def fetch_weather(api_key, city):
    """
    Fetches and prints weather data for a given city using OpenWeatherMap API.

    :param api_key: Your OpenWeatherMap API key.
    :param city: City name to fetch the weather for.
    """
    # API endpoint
    url = 'http://api.openweathermap.org/data/2.5/weather'

    # Parameters to be sent with the request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        # Send GET request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse JSON response
        data = response.json()

        # Extract weather information
        city_name = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Print weather information
        print(f"Weather in {city_name}:")
        print(f"  Description: {weather}")
        print(f"  Temperature: {temp}°C")
        print(f"  Feels Like: {feels_like}°C")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError as e:
        print(f"Error parsing weather data: {e}")

# Example usage
api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
city = 'London'
fetch_weather(api_key, city)