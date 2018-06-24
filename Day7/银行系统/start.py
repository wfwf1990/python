# Author: wangfang
from adminview import Welcomeview
from verifying_admin import VerifyAdmin
from user import User,Card
def main():
    adminview = Welcomeview()
    adminview.welcome()

    #验证管理员账号
    verifty_admin = VerifyAdmin()
    #if verifty_admin.verify():
    #        return -1
    adminview.FuncationMenu()
    while True:
        adminview.UserInput()
        adminview.FuncationMenu()

if __name__ == "__main__":
    main()





