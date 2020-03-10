from typing import Optional


class Purchase:
    @property
    def name(self):
        """
        The name of the character this purchase refers to.

        :getter: Returns this Purchase's name
        :setter: Sets this Purchase's name
        :type: str (conversion is applied)
        """
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = str(name)

    @property
    def id(self):
        """
        The character id this purchase refers to.

        :getter: Returns this Purchase's id
        :setter: Sets this Purchase's id
        :type: int (conversion is applied)
        """
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = int(id)

    @property
    def price(self):
        """
        The price that was paid in this purchase.

        :getter: Returns this Purchase's price
        :setter: Sets this Purchase's price
        :type: int (conversion is applied)
        """
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = int(price)

    @property
    def level(self):
        """
        The level of the character when this purchase occurred.

        :getter: Returns this Purchase's level
        :setter: Sets this Purchase's level
        :type: int (conversion is applied)
        """
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = int(level)

    def __init__(self,
                 name: Optional[str] = "",
                 id: Optional[int] = 0,
                 price: Optional[int] = 0,
                 level: Optional[int] = 0):
        self.name = name
        self.id = id
        self.price = price
        self.level = level

    def __repr__(self):
        return 'id: ' + repr(self.id)

    def __str__(self):
        return ",".join(f"{item[0]}: {item[1]}" for item in vars(self).items())
