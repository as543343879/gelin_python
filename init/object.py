class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello,我是" + self.name)
        print("我今年" + str(self.age) + "岁")
        print("另外,我是" + self.gender)

    def get_age(self):
        return self.age


xm = Person("小明", 25, "男生")
print(xm.get_age())
xm.introduce()



