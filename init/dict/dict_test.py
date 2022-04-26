# 对象类
from sklearn.gaussian_process.kernels import Product


class User:
    is_admin = False
    desc = ''

    def __init__(self, name) -> None:
        self.name = name
        self.age = 1


# 测试方法
class MyTestCase:
    def test_user(self):
        user = User('iworkh')
        user.is_admin = True
        # 只有塞值的时候，才会转化为dic
        # desc没有塞值，dic中没有
        print(user.__dict__)
        pass

    def test_dict_to_obj(self):
        product_dic = {'name': 'python', 'price': 10, 'desc': 'python对象和dic转化'}
        product_obj = Product('test')
        objDictTool.to_obj(product_obj, **product_dic)
        print("名称: {}, 价格: {},  描述: {}".format(product_obj.name, product_obj.price, product_obj.desc))


mt = MyTestCase()
print(mt.test_user())


class objDictTool:
    @staticmethod
    def to_obj(obj: object, **data):
        obj.__dict__.update(data)
