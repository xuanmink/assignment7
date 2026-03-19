import random
class Car:
    def __init__(self, reg_num, max_spd):
        self.registration_number= reg_num
        self.maximum_speed= max_spd
        self.current_speed= 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed = self.current_speed+ change
        if self.current_speed>self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance= self.travelled_distance + (self.current_speed * hours)
car1 = Car("ABC-123",142)
print("Properties:", car1.registration_number, car1.maximum_speed, car1.current_speed, car1.travelled_distance)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print("Speed:", car1.current_speed)
car1.accelerate(-200)
print("Final speed:", car1.current_speed)
cars = []
for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), random.randint(150, 200)))
race_on =True
while race_on:
    for c in cars:
        c.accelerate(random.randint(-10, 15))
        c.drive(1)
        if c.travelled_distance >= 10000:
            race_on = False
print("RegNum | MaxSpd | CurSpd | Distance")
for c in cars:
    print(c.registration_number + " | " + str(c.maximum_speed) + " | " + str(c.current_speed) + " | " + str(c.travelled_distance))