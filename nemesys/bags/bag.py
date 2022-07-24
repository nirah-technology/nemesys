from abc import abstractmethod
from nemesys.items import Item
from nemesys.items.item import Quality

class NoSpaceLeftInContainerException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ItemNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Container:
    @abstractmethod
    def add(self, item: Item):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, item: Item):
        raise NotImplementedError()

    @abstractmethod
    def display_all_items(self) -> list[Item]:
        raise NotImplementedError()
    
    @abstractmethod
    def search_item(self, item: Item) -> Item:
        raise NotImplementedError()


class Bag(Container):
    def __init__(self, name: str, size: int, quality=Quality.COMMON) -> None:
        self.__items: list[Item] = [];
        self.__size: int = size;
        self.__name: str = name;
        self.__quality: Quality = quality
    
    def add(self, item: Item):
        if (len(self.__items) > self.__size):
            self.__items.append(item);
        else:
            raise NoSpaceLeftInContainerException();
    
    def delete(self, item: Item):
        if (self.__items.count(item) > 0):
            try:
                self.__items.remove(item)
            except ValueError:
                raise ItemNotFoundException()
    
    def display_all_items(self):
        return self.__items

    def search_item(self, item: Item) -> Item:
        index: int
        try:
            index = self.__items.index(item)
        except ValueError:
            raise ItemNotFoundException()
        else:
            return self.__items[index]
