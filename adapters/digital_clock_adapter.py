"""
Здесь необходимо реализовать Adapter.

Класс должен реализовать interfaces.BaseDigitalClock и использовать
существующий clocks.AnalogClock через композицию.
"""
from datetime import datetime

from consts import DayNightDivision
from interfaces import BaseDigitalClock, BaseAnalogClock


class DigitalClockAdapter(BaseDigitalClock):
    def __init__(self, analog_clock:BaseAnalogClock):
        self.analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        self.analog_clock.set_date_time(year=date.year,
                                        month=date.month,
                                        day=date.day,
                                        hour_angle=(date.hour % 12) * 30,
                                        minute_angle=date.minute * 6.0,
                                        second_angle=date.second * 6.0,
                                        day_night_division= DayNightDivision.AM if date.hour < 12 else DayNightDivision.PM)

    def get_date_time(self) -> datetime:
        analog_hour = round((self.analog_clock.get_hour_angle() % 360) / 30) % 12
        is_pm = self.analog_clock.get_day_night_division() == DayNightDivision.PM
        hour = (analog_hour + 12) % 24 if is_pm else analog_hour % 12
        return datetime(
            year=self.analog_clock.get_year(),
            month=self.analog_clock.get_month(),
            day=self.analog_clock.get_day(),
            hour=int(hour),
            minute=int(round(self.analog_clock.get_minute_angle() % 360 / 6) % 60),
            second=int(round(self.analog_clock.get_second_angle() % 360 / 6) % 60))