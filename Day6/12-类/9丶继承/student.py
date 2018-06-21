
from person import Person
class Student(Person):
    def __init__(self,name,age):
        #调用父类中的__init__
        super(Student,self).__init__(name,age)
