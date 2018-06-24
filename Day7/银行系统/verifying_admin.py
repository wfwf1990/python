# Author: wangfang
import time
class VerifyAdmin():
    def verify(self):
        count = 0
        dict1 = {}
        path = r"C:\Users\lovebaby\PycharmProjects\python\Day7\银行系统\file1"
        with open(path, "r", encoding="utf-8") as f1:
            while True:
                user_password = f1.readline().strip()
                if not user_password:
                    break
                user_password_list = user_password.split("---")
                dict1[user_password_list[0]] = user_password_list[1]
        while count < 3:
            user1 = input("请输入管理员账号:")
            password1 = input("请输入管理员密码:")
            for user2 in dict1:
                if user2 == user1:
                    if dict1[user1] == password1:
                        print("操作成功,请稍后！")
                        time.sleep(2)
                        count = 3
                        return  1
                        break
                    else:
                        print("密码错误")
                        count += 1
            try:
                dict1[user1]
            except:
                print("用户名不存在")
                count += 1
        return -1




