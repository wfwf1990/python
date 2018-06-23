# Author: wangfang
from user import User
class Admin(User):
    def __init__(self,first_name,last_name):
        super(Admin, self).__init__(first_name,last_name)
        self.privileges = Privileges()
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def showPrivileges(self):
        for privileges in self.privileges:
            print("The authority of admin is " + privileges)