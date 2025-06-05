import requests

def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f"\n📍 Weather in {city}:")
        print(f"🌡 Temperature: {temp}°C")
        print(f"🌥 Condition: {desc}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🍃 Wind Speed: {wind} m/s")
    else:
        print("❌ City not found or invalid API key.")

# Replace with your actual API key
API_KEY = "7ea8dc5860ee5595b31202f66d467ebf"

# Ask user for city
city = input("Enter city name: ")
get_weather(city, API_KEY)
