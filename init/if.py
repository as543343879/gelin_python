import  init.file.file_two

def myFunction():
    print('变量 __name__ 的值是 ' + __name__)
def main2():
    print('变量 __name__ 的值是 ' + __name__)
    myFunction()


print("File one __name__ is set to: {}" .format(__name__))

if __name__ == '__main__':
    main2()

