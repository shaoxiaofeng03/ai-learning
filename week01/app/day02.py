from decimal import Decimal

from pydantic import BaseModel, Field, computed_field, field_validator


# OrderItem顶一个dto的bean对象，BaseModel是pydantic提供的基类，继承后可以使用pydantic的校验功能
class OrderItem(BaseModel):
    sku: str = Field(
        min_length=1, max_length=100
    )  # sku: str 变量名称和字段类型，Field是pydantic提供的校验器，min_length=1, max_length=100是校验规则
    qty: int = Field(
        ge=1, le=1000
    )  # Field(ge=1, le=1000) ge=1表示大于等于1，le=1000表示小于等于1000
    price: Decimal = Field(
        gt=0, max_digits=10, decimal_places=2
    )  # Field(gt=0, max_digits=10, decimal_places=2) gt=0表示大于0，max_digits=10表示最大位数为10，decimal_places=2表示小数点后最多两位


# order dto包含orderItem
class Order(BaseModel):
    order_id: str = Field(
        pattern=r"^ORD-\d{6}$"
    )  # pattern=r"^ORD-\d{6}$"表示order_id必须以ORD-开头，后面跟着6位数字
    items: list[OrderItem] = Field(
        min_length=1
    )  # list[OrderItem]表示items是一个OrderItem对象的列表，min_items=1表示最少有一个元素

    @computed_field  # 让pydantic知道total_amount是一个计算字段，出现在序列化结果中
    @property  # 定义为order的字段
    def total_amount(self) -> Decimal:
        return sum(item.qty * item.price for item in self.items)


class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    age: int = Field(ge=1, le=120)
    is_active: bool = Field(default=True)

    @field_validator("username")
    @classmethod
    def trim_name(cls, value: str) -> str:
        return value.strip()  # 去掉首尾空格


# Field会自动校验接受到的值，不用添加@Valid类似的注解


# 类型的标注，java泛型编译器检查，python运行时不检查，主要用于IDE提示和静态分析工具检查
# String -> str
# Integer -> int
# Float -> float
# Boolean -> bool
# List<String> -> list[str]    ["a", "b", "c"]
# List<Integer> -> list[int]
# Map<String, String> -> dict[str, str]
# Optional[str] -> str | None
# Set<String> -> set[str]
# Tuple<String, Integer> -> tuple[str, int]


# def add(x: int, y: int) -> int:
#     return x + y


# print(add("1", "2"))  # 不报错，输出12，但是add(1, "2")这种会报错


# pydantic 校验
# 写测试
# 笔记
