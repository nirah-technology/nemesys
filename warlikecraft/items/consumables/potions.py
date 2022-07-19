from abc import abstractmethod
from ..item import Item, Quality

class Consumable(Item):
    @abstractmethod
    def consume(self):
        raise NotImplementedError()

class Potion(Consumable):
    def __init__(self, name: str, instant: int, delay_value: int, delay_interval_seconds: int, delay_duration: int) -> None:
        super().__init__(name, Quality.COMMON)