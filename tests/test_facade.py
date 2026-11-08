from datetime import datetime

from clocks import AnalogClock
from consts import DayNightDivision
from facades.clock_digital import DigitalClock
from facades.clock_facade import ClockFacade
from services import ClockFormatter, ClockHistory


def test_facade() -> None:
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


    facade.set_time(datetime(2026, 11, 7, 15, 42, 30))
    assert facade.get_time(idx=0) == datetime(2026, 11, 7, 15, 42, 30)
    assert facade.get_time(idx=1) == datetime(2026, 11, 7, 15, 42, 30)
    assert facade.get_time_format(idx=0) == f"{datetime(2026, 11, 7, 15, 42, 30):%d.%m.%Y %H:%M:%S}"
    assert facade.get_time_format(idx=1) == f"{datetime(2026, 11, 7, 15, 42, 30):%d.%m.%Y %H:%M:%S}"

    facade.set_time(datetime(2027, 11, 7, 15, 42, 30))
    assert len(facade.get_time_history()) == 2


