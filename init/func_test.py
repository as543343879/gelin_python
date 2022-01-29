def get_message(message):
    return 'Got a message: ' + message


def root_call(func, message):
    print(func(message))


root_call(get_message, 'hello world')


def func(message):
    def get_message(message):
        print('Got a message: {}'.format(message))

    return get_message(message)


func('hello world')