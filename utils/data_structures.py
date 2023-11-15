from dataclasses import dataclass, asdict


@dataclass
class WeatherInfo:
    weather_description: str = ''
    current_temp: str = ''
    current_temp_feels_like: str = ''
    wind_speed: str = ''
    dt: str = ''
    city_name: str = 'Город не указан'

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}

    def print_weather_info(self):
        """
        Метод, который выводит данные о погоде.
        """
        print('Текущее время:', self.dt)
        print('Название города:', self.city_name)
        print('Погодные условия:', self.weather_description)
        print('Текущая температура:', self.current_temp, 'градусов по цельсию')
        print('Ощущается как:', self.current_temp_feels_like, 'градусов по цельсию')
        print('Скорость ветра:', self.wind_speed, 'м/с')


@dataclass
class Coordinates:
    lat: float
    lon: float

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
