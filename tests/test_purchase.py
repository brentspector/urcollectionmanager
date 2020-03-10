from urcollectionmanager.purchase import Purchase

FULL_PURCHASE = {"name": "Bob", "id": 1, "price": 1, "level": 1}


def test_init_no_args():
    """Happy Path - Init No Args"""
    obj = Purchase()
    assert obj.name == ""
    assert obj.id == 0
    assert obj.price == 0
    assert obj.level == 0


def test_init_full_arg():
    """Happy Path - Init All Args Named"""
    obj = Purchase(**FULL_PURCHASE)
    assert obj.name == "Bob"
    assert obj.id == 1
    assert obj.price == 1
    assert obj.level == 1
