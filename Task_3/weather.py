from get_weather import weather_data

with open("weather.txt", "w") as f:
    for city_data in weather_data:
        f.write(f"{city_data} '\n'")
