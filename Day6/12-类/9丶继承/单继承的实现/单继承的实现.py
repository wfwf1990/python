from student import Student
from worker import Worker
stu = Student("tom",18,1000,19)
print(stu.name,stu.age,stu.stuID)
stu.run()
print(stu.getMoney())   #通过方法获取父类的私有属性

wor = Worker("jack",19,1000)
print(wor.name,wor.age)
wor.run()