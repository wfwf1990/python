# Author: wangfang

class Card():
    #卡号，预存款丶卡密码
    def __init__(self,cardId="5",preMoney="5",cardPassword="5"):
        self.cardId = cardId
        self.preMoney = preMoney
        self.cardPassword = cardPassword
    def write_card_output_file(self):
        path = r"C:\Users\lovebaby\PycharmProjects\python\Day7\银行系统\file3"
        with open(path,"a",encoding="utf-8") as f1:
            constr = "---"
            f1.write(self.cardId + constr + self.preMoney + constr + self.cardPassword  + "\n")

    #验证卡号

class User():
    #姓名丶手机号码，身份证号码，卡
    def __init__(self,name,phoneNumber,userId):
        self.name = name
        self.phoneNumber = phoneNumber
        self.userId = userId
        #self.cardId = cardId
        self.card = Card()
    def write_user_output_file(self):
        path = r"C:\Users\lovebaby\PycharmProjects\python\Day7\银行系统\file2"
        with open(path,"a",encoding="utf-8") as f1:
            constr = "---"
            f1.write(self.name + constr + self.phoneNumber + constr + self.userId +constr + self.card.cardId + constr + self.card.preMoney + constr + self.card.cardPassword  + "\n")
            #f1.write(self.name + constr + self.phoneNumber  + constr + self.userId +constr + self.cardId +"\n")

    def verify_card_id(self,card_id):
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
                    break

