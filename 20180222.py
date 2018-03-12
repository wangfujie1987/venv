# class Car:
#     speed = 0
#     def drive(self, distance):
#         time = distance / self.speed
#         print (time)
#
# car1 = Car()
# car1.speed = 60.0
# car1.drive(100.0)
# car1.drive(200.0)
#
# car2 = Car()
# car2.speed = 150.0
# car2.drive(100.0)
# car2.drive(200.0)
# class MyClass:
#     name='Dennis'
#     def sayHi(self):
#         print('Hello %s'%self.name)
#
# mc = MyClass()
# print (mc.name)
# mc.sayHi()
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print ('need %f hour(s)' % (distance / self.speed))

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print ('need %f fuels' % (distance * self.fuel))
b = Bike(15.0)
c = Car(80.0,0.012)
b.drive(100.0)
c.drive(100.0)
