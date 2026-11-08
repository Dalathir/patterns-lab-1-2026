
from datetime import datetime

from interfaces import BaseDigitalClock


class DigitalClock(BaseDigitalClock):
    def __init__(self, date: datetime = datetime.now()):
        self.date = date

    def set_date_time(self, date: datetime) -> None:
        self.date = date

    def get_date_time(self) -> datetime:
        return self.date