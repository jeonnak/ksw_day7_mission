'''
10.10
Laser, Claw, SmartPhone 클래스를 정의한다.
각 클래스는 does() 메서드를 갖고 있다.
각 메서드는 'disintegrate' (Laser),
'crush' (Claw) 또는 'ring' (Smart Phone)을
반환한다. 그리고 각 클래스의 객체를 갖는 Robot 클래스를 정의한다.
Robot 클래스의 객체가 갖고 있는 내용을 출력하는 does() 메서드를 정의한다.
'''

class Laser():
    def __init__(self, disintegrate):
        self.disintegrate = disintegrate

ob1 = Laser('dang')

class Claw():
    def __init__(self, crush):
        self.crush = crush

ob2 = Claw('wack')

class Smartphone():
    def __init__(self, ring):
        self.ring = ring

ob3 = Smartphone('zing')

class Robot():
    def __init__(self, ob1, ob2, ob3):
       self.ob1 = ob1
       self.ob2 = ob2
       self.ob3 = ob3
    def does():
        print(ob1, ob2, ob3)

Robot.does()