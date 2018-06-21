class Gun(object):

    def __init__(self,bulletBox,count = 0):
        self.bulletBox = bulletBox
        self.count = count
    def shoot(self,count):
        if self.bulletBox.count  == 0:
            print("没有子弹了")
        else:
            self.bulletBox.count  -= 1
            print("开了%d枪, 剩余子弹%d" % (self.bulletBox.count))

