from typing import Callable

# Константы для подключения к API
API_KEY = 'd0b91a8a366a27778b9e5c42c592baae'
ULR_GEOCODING_API = 'http://api.openweathermap.org/geo/1.0/direct'
ULR_GEOCODING_REVERSE_API = "http://api.openweathermap.org/geo/1.0/reverse"
ULR_WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather'
URL_IPINFO = 'https://ipinfo.io'

# Константы для type-hinting
dict_with_action_options = dict[str, Callable | dict[str] | str]
dict_with_weather_info = dict[str, float | str]
dict_with_geocoding_info = dict[str, float | str]
