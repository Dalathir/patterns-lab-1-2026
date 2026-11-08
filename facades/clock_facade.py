"""
Здесь необходимо реализовать Facade.

Фасад должен скрывать работу как минимум с:
- цифровым адаптером;
- ClockFormatter;
- ClockHistory.
"""

from typing import Union
from datetime import datetime
from adapters.digital_clock_adapter import DigitalClockAdapter
from interfaces import BaseDigitalClock, BaseAnalogClock
from services import ClockFormatter, ClockHistory



# TODO: реализуйте ClockFacade.

class ClockFacade:

    def __init__(self, *args: Union[BaseDigitalClock, BaseAnalogClock],
                 formatter: ClockFormatter, history: ClockHistory):

        self.formatter = formatter
        self.history = history
        self.clocks = []
        for clock in args:
            self.add_clocks(clock)

    def add_clocks(self, clock: Union[BaseDigitalClock, BaseAnalogClock]) -> None:
        """добавить часы"""
        if isinstance(clock, BaseAnalogClock):
            self.clocks.append(DigitalClockAdapter(clock))
        elif isinstance(clock, BaseDigitalClock):
            self.clocks.append(clock)
        else:
            raise TypeError()

    def set_time(self, date: datetime) -> None:
        """установка текущих даты и времени"""
        for clock in self.clocks:
            clock.set_date_time(date)
        self.history.add(date)

    def get_count_clocks(self) -> int:
        return len(self.clocks)

    def get_time(self, idx: int = 0) -> datetime:
        """Получение текущих даты и времени"""
        return self.clocks[idx].get_date_time()

    def get_time_format(self, idx: int = 0, fmt: str = "%d.%m.%Y %H:%M:%S") -> str:
        """Получение форматированного представления"""
        return self.formatter.format(self.get_time(idx), fmt)

    def get_time_history(self) -> tuple[datetime, ...]:
        """Получение истории изменений"""
        return self.history.all()



