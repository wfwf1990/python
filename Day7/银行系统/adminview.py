# Author: wangfang
import time
from verifying_admin import VerifyAdmin
from atm import ATM

class Welcomeview():
    def welcome(self):
        print("******************************")
        print("*                            *")
        print("*                            *")
        print("*     欢迎来到中国银行管理系统  *")
        print("*                            *")
        print("*                            *")
        print("******************************")
    def FuncationMenu(self):
        print("******************************")
        print("*    开户(1)       查询(2)    *")
        print("*    取款(3)       存款(4)    *")
        print("*    转账(5)       改密(6)    *")
        print("*    锁定(7)       解锁(8)    *")
        print("*    补卡(9)       销户(10)   *")
        print("******************************")
    def UserInput(self):
        adminview = Welcomeview()
        while True:
            option = input("等待用户输入:")
            if option == "1":
                atm_create = ATM()
                atm_create.createUser()
                break
            elif option == "2":
                atm_search = ATM()
                atm_search.searchUser()
                return -1
            elif option == "3":
                print("取款")
            elif option == "4":
                print("存款")
            elif option == "5":
                print("转账")
            elif option == "6":
                print("改密")
            elif option == "7":
                print("锁定")
            elif option == "8":
                print("解锁")
            elif option == "9":
                print("补卡")
            elif option == "10":
                print("销户")
            elif option == "q":
                verifty_admin = VerifyAdmin()
                if verifty_admin.verify() == 1:
                    break
            else:
                print("请输入正常的数字:")
            time.sleep(2)