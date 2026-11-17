from week01.app.day02 import OrderItem, User, Order


def test_user_valid_success() -> None:
    user = User(
        username="alice",
        email="alice@example.com",
        age=25,
    )

    assert user.username == "alice"
    assert user.email == "alice@example.com"
    assert user.age == 25
    assert user.is_active is True


def test_user_invalid_username() -> None:
    try:
        user = User(
            username="",  # Too shoralt
            email="alice@example.com",
            age=25,
        )
        assert False, "Expected ValueError for invalid username"
    except ValueError:
        pass


# username中文长度
def test_user_invalid_username_chinese() -> None:
    try:
        user = User(
            username="张三",  # Too short
            email="alice@example.com",
            age=25,
        )
        assert False, "Expected ValueError for invalid username"
    except ValueError:
        pass


def test_user_invalid_username_chinese_1() -> None:
    try:
        user = User(
            username="张",  # Too short
            email="alice@example.com",
            age=25,
        )
        assert False, "Expected ValueError for invalid username"
    except ValueError:
        pass


def test_user_invalid_age_0() -> None:
    try:
        user = User(
            username="alice",
            email="alice@example.com",
            age=0,  # Invalid age
        )
        assert False, "Expected ValueError for invalid age"
    except ValueError:
        pass


def test_user_invalid_age_121() -> None:
    try:
        user = User(
            username="alice",
            email="alice@example.com",
            age=121,  # Invalid age
        )
        assert False, "Expected ValueError for invalid age"
    except ValueError:
        pass


def test_user_invalid_email() -> None:
    try:
        user = User(
            username="alice",
            email="invalid-email",  # Invalid email format
            age=25,
        )
        assert False, "Expected ValueError for invalid email"
    except ValueError:
        pass


def test_qty_0() -> None:
    try:
        order_item = OrderItem(sku="SKU123", qty=0, price=10.0)  # Invalid qty
        assert False, "Expected ValueError for invalid qty"
    except ValueError:
        pass


# items=[]
def test_order_empty_items() -> None:

    try:
        order = Order(order_id="ORD-123456", items=[])  # Invalid items
        assert False, "Expected ValueError for empty items"
    except ValueError:
        pass
