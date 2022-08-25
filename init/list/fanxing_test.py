import uuid
from typing import Generic, TypeVar
from pydantic import BaseModel


class ModelSchema(BaseModel):
    name: str
    age: int


Model = TypeVar("Model", bound=BaseModel)


class CRUDBase(Generic[Model]):
    def print_type(a: Model):
        print(a)
        print(type(a))


class Service1(CRUDBase[ModelSchema]):
    pass


from typing import TypeVar, Type

T = TypeVar('T')


class Test(Generic[T]):

    def __init__(self, t: Generic[T]) -> None:
        super().__init__()
        self.t = t

    def hello(self):
        my_type = T  # this is wrong!
        print("I am {0},{1}".format(my_type, type(self.t)))


Test[int]('12312').hello()
print(uuid.uuid1())
