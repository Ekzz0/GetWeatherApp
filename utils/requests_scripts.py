import requests
import utils
from .errors_processing import open_weather_error_processing, requests_error_processing


def geocoding_get(city_name: str) -> dict[str, float]:
    try:
        # Запрос на Geocoding API
        response = requests.get(utils.ULR_GEOCODING_API,
                                params={'q': city_name, 'appid': utils.API_KEY, 'limit': 1})
        # print(response.json())
        # Проверка на ошибки из Open Weather Map
        open_weather_error_processing(response.status_code)
        data = response.json()[0]
    except requests.HTTPError:
        raise
    except requests.ConnectionError:
        print("Ошибка подключения")
    except requests.Timeout:
        print("Ошибка тайм-аута")
    except requests.RequestException:
        print("Ошибка запроса")
    else:
        # Обработка запроса
        lat = data['lat']
        lon = data['lon']

        # Формирование отчета
        report = {'lat': lat, 'lon': lon, 'city_name': city_name}

        return report


def weather_map_get(report_geo: dict[str, float]) -> dict[str, float]:
    try:
        # Запрос на OpenWeatherMap API
        response = requests.get(utils.ULR_WEATHER_API,
                                params={'lat': report_geo['lat'], 'lon': report_geo['lon'],
                                        'appid': utils.API_KEY, 'lang': "ru", "units": 'metric'
                                        }
                                )
        # print(response.status_code)
        open_weather_error_processing(response.status_code)
        data = response.json()
        # print(data)
    except requests.HTTPError:  # 200, 400, 401
        pass
    except requests.ConnectionError:
        print("Ошибка подключения")
    except requests.Timeout:
        print("Ошибка тайм-аута")
    except requests.RequestException:
        print("Ошибка запроса")
    else:
        # Обработка запроса
        weather_description = data['weather'][0]["description"]
        current_temp = data['main']["temp"]
        current_temp_feels_like = data['main']["feels_like"]
        wind_speed = data['wind']['speed']

        # Формирование отчета
        report = {"city_name": report_geo.get("city_name", "Город не указан"),
                  "weather_description": weather_description,
                  "current_temp": current_temp,
                  "current_temp_feels_like": current_temp_feels_like,
                  "wind_speed": wind_speed
                  }

        return report



