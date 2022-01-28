print("hello World")
print ("你好，世界")

a2 = 100
a3 = 135
print(a2 + a3)
print(type(a2))

stu_score = 93
a7 = stu_score > 90
a8 = stu_score < 60
a9 = a7 and a8
a10 = a7 or a8
print(a7,type(a7),a8,type(a8), a9, type(a9), a10, type(a10))

a1 = "Hello, Data Science"
a2 = "I'm coming"
a3 = a1 + ", " + a2
print(a1, type(a1))
print(a3, type(a3))

tc_a1=10
tc_a2=1.5
tc_a3=tc_a1+tc_a2
print(tc_a3,type(tc_a3))

tc_a1 = 10
la = [1,2,3,tc_a1]
print("Listis:",la)
print("Listlength:",len(la))
print("Listtail:",la[-1])
print("Listhead:",la[0])
la.append("Hello")
print("Afterappend:",la)
la.remove(2)
print("Afterremove:",la)

print(la[0],type(la[0]))
print(la[len(la) - 1], type(la[len(la) - 1]))
