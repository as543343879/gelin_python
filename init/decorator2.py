def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
        print('in end  decorator')

    return wrapper


def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print(type(args), args)
        print(type(kwargs),kwargs)
        print('wrapper of my_decorator2')
        func(*args, **kwargs)
    return wrapper



#@my_decorator
@my_decorator2
def greet(name, age):
    print('name:',name, 'age',age, 'hello world')


greet('xxp',18)
