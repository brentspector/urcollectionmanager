from urcollectionmanager.purchase import Purchase
from datetime import date, time, datetime, timedelta

FULL_PURCHASE = {"name": "Bob", "id": 1, "price": 1, "level": 1, "purchase_date": "Tuesday 14/01, 11:30"}

def test_init_no_args():
    """Happy Path - Init No Args"""
    obj = Purchase()
    assert obj.name == ""
    assert obj.id == 0
    assert obj.price == 0
    assert obj.level == 0
    # Cannot guarantee timestamp but date should work
    assert obj.purchase_date.date() == date.today()


def test_init_full_arg():
    """Happy Path - Init All Args Named"""
    obj = Purchase(**FULL_PURCHASE)
    assert obj.name == "Bob"
    assert obj.id == 1
    assert obj.price == 1
    assert obj.level == 1
    assert obj.purchase_date == datetime(2020, 1, 14, 11, 30)

def test_purchase_date_today():
    obj = Purchase(purchase_date="Today at 12:34")
    assert obj.purchase_date == datetime.combine(date.today(), time(12, 34))

def test_purchase_date_yesterday():
    obj = Purchase(purchase_date="Yesterday at 12:34")
    assert obj.purchase_date == datetime.combine(date.today()-timedelta(days=1), time(12, 34))

def test_purchase_date_with_year():
    obj = Purchase(purchase_date="Sunday 17/03/2019, 20:36")
    assert obj.purchase_date == datetime(2019, 3, 17, 20, 36)
