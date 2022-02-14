import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('wrapper of decorator')

    return wrapper


@my_decorator
def greet(message):
    print(message)

if __name__ == '__main__':
    print(greet.__name__)
    print('------------')
    print(greet('123'))