# Author: wangfang

class User(object):
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("first name is %s, last name is %s" %(self.first_name,self.last_name))
    def greet_user(self):
        print("hello " + self.first_name + " " + self.last_name)
    def incrementLoginAttempts(self):
        self.login_attempts += 1
    def resetLoginAttempts(self):
        self.login_attempts = 0
    def getLoginAttempts(self):
        print("登录次数为：%d" %self.login_attempts)
        super(Admin, self).__init__(first_name,last_name)
        self.privileges = Privileges()      #Privileges实例作为属性


