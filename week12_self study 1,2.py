# self study 12-1

## 클래스 선언 부분 ##
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self,value):
        self.speed += value
        if self.speed > 150: # 속도가 150을 초과하면 150으로 조절
            self.speed = 150
        
    def downSpeed(self,value):
        self.speed -= value
        
## 메인 코드 부분 ## 
myCar1=Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2=Car()
myCar2.color = "파랑"
myCar2.speed = 0   

myCar3=Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(300)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar1.color, myCar1.speed))

myCar2.upSpeed(4000)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar3.color, myCar3.speed))


# self study 12-2

class Car :
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        
        print("현재 속도(슈퍼 클래스): %d" %self.speed)
        
class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(서브 클래스): %d" %self.speed)
        
class Truck(Car):
    pass

class Sonata(Sedan): # Sonata 클래스는 Sedan을 상속받음
    pass # 특별히 추가하는 필드나 메서드가 없으므로 pass

sedan1, truck1, sonata1 = None, None, None # sonata1 변수 추가

truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata() # Sonata 객체 생성

print("트럭 -->", end="")
truck1.upSpeed(200)

print("승용차 -->", end="")
sedan1.upSpeed(200)

print("쏘나타 -->", end="") # 쏘나타 객체로 upSpeed 호출
sonata1.upSpeed(200)