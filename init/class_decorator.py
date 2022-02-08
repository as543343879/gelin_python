class Count:
    def __init__(self, func):
        print('__init__: ')
        self.func = func
        self.num_calls = 0

    # 是使实例能够像函数一样被调用，同时不影响实例本身的生命周期,但是__call__()可以用来改变实例的内部成员的值。
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")


example()
