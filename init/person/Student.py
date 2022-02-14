class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


stu = Student()

try:
    stu.score = -1
    print(stu.score)
except:
    print("参数不合法")

stu.score = 10
print(stu.score)
