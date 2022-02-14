import functools


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


def greet():
    print('execute greet function')


# greet = my_decorator(greet)
# greet()

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(4)
def greet(message):
    print(message)


# greet('hello world')
print(greet.__name__)
# help(greet)


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)


print(greet.__name__)
print('------------')
print(greet('123'))



