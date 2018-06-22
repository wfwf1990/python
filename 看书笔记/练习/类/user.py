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

'''
user_tom = User("tom","alex")
user_tom.describe_user()
user_tom.greet_user()

user_jack = User("jack","alex")
user_jack.describe_user()
user_jack.greet_user()
'''

user_sam = User("sam","alex")
user_sam.describe_user()
user_sam.incrementLoginAttempts()
user_sam.getLoginAttempts()
user_sam.incrementLoginAttempts()
user_sam.getLoginAttempts()
user_sam.resetLoginAttempts()
user_sam.getLoginAttempts()
