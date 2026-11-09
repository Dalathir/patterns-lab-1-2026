from datetime import datetime

from clocks import AnalogClock
from consts import DayNightDivision
from clocks.clock_digital import DigitalClock
from facades.clock_facade import ClockFacade
from services import ClockFormatter, ClockHistory

def get_facade() -> ClockFacade:
    analog_clock = AnalogClock()
    analog_clock.set_date_time(
        year=2026,
        month=9,
        day=24,
        hour_angle=90.0,
        minute_angle=180.0,
        second_angle=270.0,
        day_night_division=DayNightDivision.PM,
    )
    digital_clock = DigitalClock()

    facade = ClockFacade(
        digital_clock,
        analog_clock,
        formatter=ClockFormatter(),
        history=ClockHistory(),
    )
    return facade

def test_facade_1() -> None:
    """проверяем поменялось ли время на всех часах"""
    facade = get_facade()
    date = datetime(2026, 11, 7, 15, 42, 30)
    facade.set_time(date)
    assert facade.get_time(idx=0) == date
    assert facade.get_time(idx=1) == date

def test_facade_1_1() -> None:
    """проверяем поменялось ли время на всех часах"""
    facade = get_facade()
    date = datetime(2026, 11, 8, 0, 0, 0)
    facade.set_time(date)
    assert facade.get_time(idx=0) == date
    assert facade.get_time(idx=1) == date

def test_facade_2() -> None:
    """проверяем правильно ли форматируется время"""
    facade = get_facade()
    date = datetime(2026, 11, 7, 15, 42, 30)
    facade.set_time(date)
    assert facade.get_time_format(idx=0) == f"{date:%d.%m.%Y %H:%M:%S}"
    assert facade.get_time_format(idx=1) == f"{date:%d.%m.%Y %H:%M:%S}"

def test_facade_3() -> None:
    """проверяем как работает история изменений"""
    facade = get_facade()
    date = datetime(2026, 11, 7, 15, 42, 30)
    facade.set_time(date)
    facade.set_time(date)
    assert len(facade.get_time_history()) == 2


