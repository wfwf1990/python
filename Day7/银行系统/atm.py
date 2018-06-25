# Author: wangfang

from user import User,Card
from verifying_admin import VerifyAdmin
import random

class ATM():
    def __init__(self):
        self.user = {}

    def createUser(self):
        user = input("请输入用户名:")
        phoneNumber = input("请输入你的手机号码：")
        userId = input("请输入你的身份证号码:")
        preMoney = int(input("请输入你的预存款："))
        if preMoney <= 0:
            print("输入的金额不对,开户失败！")
            return  -1
        onePassword = input("请输入你的密码：")
        if not self.checkPassword(onePassword):
            print("密码输入错误，开户失败！")
            return -1

        str1 = str(self.verfication_code())


        #card = Card(str1,str(preMoney),onePassword)
        user_information = User(user, phoneNumber, userId)
        user_information.card.preMoney = str(preMoney)
        user_information.card.cardPassword = onePassword
        user_information.card.cardId = str1
        #card.write_card_output_file()
        user_information.write_user_output_file()
        print("请牢记卡号%s" %str)

    def searchUser(self):
        temp_num = input("请输入你的卡号：")
        user = self.verify_card_id(temp_num)
        print(user)
        if not user:
            print("card_id 不存在！")
            return -1
        temp_password = input("请输入你的密码：")
        password = self.verify_user_password(temp_num,temp_password)
        print(type(password))
        if  not password:
            print("输入的密码不正确")
            return -1






    def checkPassword(self,onePassword):
        for i in range(3):
            twoPassword = input("请再次输入密码:")
            if twoPassword == onePassword:
                return True
        return -1

    def verfication_code(self):
        self.temp = ''
        for i in range(6):
            num = random.randrange(0,6)
            self.temp += str(num)
        if not self.user.get(self.temp):
            return self.temp

    def verify_card_id(self, card_id):
        path = r"C:\Users\lovebaby\PycharmProjects\python\Day7\银行系统\file2"
        with open(path, "r", encoding="utf-8") as f2:
            while True:
                line = f2.readline().strip()
                if not line:
                    break
                card_ids = line.strip().split("---")[3]
                print(card_ids)
                if card_ids == card_id:
                    print("card right！")
                    return  1

    def verify_user_password(self,temp_cardId, temp_password):
        path = r"C:\Users\lovebaby\PycharmProjects\python\Day7\银行系统\file2"
        with open(path, "r", encoding="utf-8") as f2:
            while True:
                line = f2.readline().strip()
                if not line:
                    break
                user_password = line.strip().split("---")[-1]
                card_ids = line.strip().split("---")[3]
            for i in range(3):
                temp_password = input("请输入你的密码：")
                if temp_password == user_password and card_ids == temp_cardId:
                    print("密码验证成功")
                    return 1
            return False


