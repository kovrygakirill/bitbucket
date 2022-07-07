import asyncio
import aiohttp

api_key = ""
cities_data = [{"lat": 53.9022, "lon": 27.5618},  # Minsk
               {"lat": 30.0561, "lon": 30.0561},  # Cairo
               {"lat": -15.7939, "lon": -47.8828}]  # Brasilia
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric"
weather_data = []


async def get_weather_data(lat, lon, num):
    async with aiohttp.ClientSession() as session:
        async with session.get(url % (lat, lon, api_key)) as resp:
            print(f"request {num}")
            weather_data.append(await resp.text())
            print(f"finish request {num}")


async def main():
    tasks = []
    for num, city in enumerate(cities_data, 1):
        tasks.append(asyncio.create_task(get_weather_data(**city, num=num)))

    for num, task in enumerate(tasks, 1):
        await task


asyncio.run(main())
