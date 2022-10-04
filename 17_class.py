from turtle import speed


class unit: # class 이름이 unit
    def __init__(self, name, hp, damage):
        self.na = name
        self.hp = hp
        self.da = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.na))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.da))
        
marine1 = unit("마린", 40, 5)
marine2 = unit("마린", 40, 5)
tank1 = unit("탱크", 150, 35)
# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 탱크 유닛이 생성 되었습니다.
# 체력 150, 공격력 35

#==== __init__(생성자) ====
# 객체(marine1, tank1 - 클래스로 부터 만들어지는 것)가 만들어질 때 자동으로 호출되는 부분
# marine1, tank1는 unit 클래스의 인스턴스
# self를 제외한 같은 갯수(name, hp, damage 3개)를 보내야 함.

#==== 맴버변수 - 클래스 내에서 정의된 변수 ====
#self.na, self.hp, self.da
#.format(wraith1.na, wraith1.da) - 맴버변수를 클래스 외부에서도 사용가능
wraith1 = unit("레이스", 80, 5)
print("(맴버변수 활용)유닛이름: {0}, 공격력: {1}".format(wraith1.na, wraith1.da))
# 레이스 유닛이 생성 되었습니다.
# 체력 80, 공격력 5
# (맴버변수 활용)유닛이름: 레이스, 공격력: 5

wraith2 = unit("클로킹레이스", 80, 5)
wraith2.clocking = True # clocking이라는 변수를 추가 할당한 것임. / 변수.변수
if wraith2.clocking == True:
    print("{0}는 보이지 않는 상태입니다.".format(wraith2.na))
# 클로킹레이스 유닛이 생성 되었습니다.
# 체력 80, 공격력 5
# 클로킹레이스는 보이지 않는 상태입니다.

#==== 메소드(class 안의 함수) ====
class attackunit: # class 이름이 attackunit
    def __init__(self, name, hp, damage):
        self.na = name
        self.hp = hp
        self.da = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.na))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.da))
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]" \
            .format(self.na, location, self.da))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 받았습니다.".format(self.na, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.na, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.na))

firebat1 = attackunit("파이어뱃", 50, 16) # 파이어뱃 유닛이 생성 되었습니다.
                                         # 체력 50, 공격력 16
firebat1.attack("5시") # 파이어뱃 : 5시 방향으로 적군을 공격 합니다.[공격력 16]

firebat1.damaged(25) # 파이어뱃 : 25 데미지를 받았습니다.
                     # 파이어뱃 : 현재 체력은 25 입니다.
firebat1.damaged(25) # 파이어뱃 : 25 데미지를 받았습니다.
                     # 파이어뱃 : 현재 체력은 0 입니다.
                     # 파이어뱃 : 파괴되었습니다.

#==== 상속(다른 class의 정보를 받아서 사용함) ====
class attackunit: # class 이름이 attackunit
    def __init__(self, name, hp, damage):
        self.na = name
        self.hp = hp
        self.da = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.na))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.da))
class flyable:
    def __init__(self, speed):
        self.flying = speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying))
class flyableattack(attackunit, flyable): 
    def __init__(self, name, hp, damage, speed):
        attackunit.__init__(self, name, hp, damage)
        flyable.__init__(self, speed)
# 상속관계에 있는 것들의 __init__( )를 같은 이름으로 사용한다.
        
valkyrie = flyableattack("발키리", 200, 6, 5)
# 발키리 유닛이 생성 되었습니다.
# 체력 200, 공격력 6

valkyrie.fly(valkyrie.na, "3시")
# 발키리 : 3시 방향으로 날아갑니다. [속도 5]

#==== 연산자오버라이딩: 자식클레스에서 정의한 메소드를 사용하고 싶을때 ====