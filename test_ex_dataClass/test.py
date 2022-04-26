import typing
from ex_dataclass import ex_dataclass, field, asdict, EXpack


@ex_dataclass
class User:
    name: str = field(default_factory=str)
    # default: 给定一个默认值, 再不给定的时候默认会使用
    age: int = field(default=18)


u1 = User()
print(u1)


# 赋值方法-1
u1 = User(name="u1", age=20)
u1.age
u1.name

# 赋值方法-2
data = {"name": "u2", "age": 18}
u2 = User(**data)
u2.name

# 冗余数据会被丢弃
data = {"name": "u2", "age": 18, "ignore": True}
u3 = User(**data)
print(u3)
# :return: User(name='u2', age=18)

# 对象数据转dict
data_dict = asdict(u3)
print(data_dict)
