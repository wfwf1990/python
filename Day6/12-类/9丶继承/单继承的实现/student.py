
from person import Person
class Student(Person):
    #子类中拥有独立的属性
    def __init__(self,name,age,money,stuID):
        #调用父类中的__init__
        super(Student,self).__init__(name,age,money)
        self.stuID = stuID

