from bulletbox import BulletBox
from gun import Gun
from person import Person

bulletbox = BulletBox(5)
gun = Gun(bulletbox)
per = Person(gun)


per.fire()
