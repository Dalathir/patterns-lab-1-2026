from datetime import datetime

from clocks import AnalogClock
from consts import DayNightDivision
from clocks.clock_digital import DigitalClock
from facades.clock_facade import ClockFacade
from services import ClockFormatter, ClockHistory


def main() -> None:
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

    print("Исходный объект ClockFacade создан.")
    print(f"Дата по умолчанию цифровых часов: {facade.get_time(idx=0):%d.%m.%Y %H:%M:%S}")
    print(f"Дата по умолчанию аналоговых часов: {facade.get_time(idx=1):%d.%m.%Y %H:%M:%S}")

    facade.set_time(datetime(2026, 11, 7, 15, 42, 30))


    print(f"Дата после изменения цифровых часов: {facade.get_time(idx=0):%d.%m.%Y %H:%M:%S}")
    print(f"Дата после изменения аналоговых часов: {facade.get_time(idx=1):%d.%m.%Y %H:%M:%S}")
    print(f"Дата форматированного представления: {facade.get_time_format()}")
    print(f"История изменений: {facade.get_time_history()}")


if __name__ == "__main__":
    main()
