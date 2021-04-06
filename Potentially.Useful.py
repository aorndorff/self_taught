import math

class Displacement():
    def __init__(self, a, d):
        self.angle = a 
        self.distance = d
    
    def hDist(self):
        return(self.distance * math.tan(self.angle * math.pi/180))
      

hDist1 = Displacement(45, 10)
print(hDist1.angle)
print(hDist1.distance)
print(hDist1.hDist())