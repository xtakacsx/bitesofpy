from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, date: datetime):
        self.name = name
        self.date = date

    @property
    def expired(self) -> bool:
        return NOW > self.date
