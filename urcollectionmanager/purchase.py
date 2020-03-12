from .database import Base
from datetime import date, timedelta, datetime
from typing import Optional
from sqlalchemy import Column, String, Integer, DATETIME
from sqlalchemy.ext.hybrid import hybrid_property


class Purchase(Base):
    __tablename__ = "purchase"
    name = Column(String(255))
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    level = Column(Integer)
    _purchase_date = Column(DATETIME)

    @hybrid_property
    def purchase_date(self):
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        # Friday 06/03, 20:39
        # Today at 11:30
        if type(purchase_date) is datetime:
            self._purchase_date = purchase_date
            return
        split_date = str(purchase_date).split()
        purch_date = datetime.combine(datetime.now(), datetime.strptime(split_date[2], "%H:%M").time())
        if split_date[0] == "Yesterday":
            purch_date -= timedelta(days=1)
        elif split_date[1] != "at":
            if len(split_date[1].split("/")) == 2:
                purch_date = datetime.strptime(purchase_date, "%A %d/%m, %H:%M")
                purch_date = purch_date.replace(year=datetime.now().year)
            else:
                purch_date = datetime.strptime(purchase_date, "%A %d/%m/%Y, %H:%M")

        self._purchase_date = purch_date

    def __init__(self,
                 name: Optional[str] = "",
                 id: Optional[int] = 0,
                 price: Optional[int] = 0,
                 level: Optional[int] = 0,
                 purchase_date: Optional[str] = datetime.now()):
        self.name = str(name)
        self.id = int(id)
        self.price = int(price)
        self.level = int(level)
        self.purchase_date = purchase_date

    def __repr__(self):
        return 'id: ' + repr(self.id)

    def __str__(self):
        return ",".join(f"{item[0]}: {item[1]}" for item in vars(self).items())

    def __eq__(self, other):
        if not isinstance(other, Purchase):
            # don't attempt to compare against unrelated types
            return NotImplemented

        # Check all values that are not "instance" ex _sa_instance_state
        return all(self.__getattribute__(item[0]) == other.__getattribute__(item[0])
                   for item in vars(self).items() if "instance" not in item[0])