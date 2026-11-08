from datetime import datetime

from adapters.digital_clock_adapter import DigitalClockAdapter
from clocks import AnalogClock


def test_adapter() -> None:
    clock = DigitalClockAdapter(AnalogClock())

    clock.set_date_time(datetime(2026, 11, 8, 15, 42, 30))
    assert clock.get_date_time() == datetime(2026, 11, 8, 15, 42, 30)

    clock.set_date_time(datetime(2026, 11, 8, 0, 0, 0))
    assert clock.get_date_time() == datetime(2026, 11, 8, 0, 0, 0)

    clock.set_date_time(datetime(2026, 11, 8, 23, 59, 59))
    assert clock.get_date_time() == datetime(2026, 11, 8, 23, 59, 59)

    clock.set_date_time(datetime(2026, 11, 8, 11, 59, 59))
    assert clock.get_date_time() == datetime(2026, 11, 8, 11, 59, 59)

    clock.set_date_time(datetime(2026, 11, 8, 12, 0, 0))
    assert clock.get_date_time() == datetime(2026, 11, 8, 12, 0, 0)


