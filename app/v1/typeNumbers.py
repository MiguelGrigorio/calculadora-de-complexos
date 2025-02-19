from math import sqrt, cos, sin, atan2, pi

class Graus:
    def __init__(self, graus):
        if graus >= 360:
            graus = graus % 360
        if graus < 0:
            graus = 360 + graus
        self.ang = graus
    def toRad(self):
        return Radianos(self.ang * pi / 180)

class Radianos:
    def __init__(self, rad):
        self.ang = rad
    def toGraus(self):
        return Graus(self.ang * 180 / pi)

class Polar:
    def __init__(self, r, theta):
        self.r = r
        if type(theta) == Graus:
            self.theta = theta.toRad()
        else:
            self.theta = theta

    def toRect(self):
        return Rect(self.r * cos(self.theta.ang), self.r * sin(self.theta.ang))
    
    def print(self, RG):
        return f"{round(self.r, 2)} <{round(self.theta.ang, 2) if RG == "R" else round(self.theta.toGraus().ang, 2)}{"°" if RG == 'G' else "rad"}>"
class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def toPolar(self):
        return Polar(sqrt(self.x**2 + self.y**2), Radianos(atan2(self.y, self.x)))
    def print(self, ang):
        # Ângulo não é necessário, pois o número é retangular mas é utilizado para manter a consistência
        return f"{round(self.x, 2)} + {round(self.y, 2)}j"