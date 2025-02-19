from typeNumbers import Graus, Radianos, Polar, Rect

def soma(V1, V2):
    if type(V1) == Polar:
        V1 = V1.toRect()
    if type(V2) == Polar:
        V2 = V2.toRect()
    return Rect(V1.x + V2.x, V1.y + V2.y).toPolar()

def subtracao(V1, V2):
    if type(V1) == Polar:
        V1 = V1.toRect()
    if type(V2) == Polar:
        V2 = V2.toRect()
    return Rect(V1.x - V2.x, V1.y - V2.y).toPolar()

def multiplicacao(V1, V2):
    if type(V1) == Rect:
        V1 = V1.toPolar()
    if type(V2) == Rect:
        V2 = V2.toPolar()
    return Polar(V1.r * V2.r, Radianos(V1.theta.ang + V2.theta.ang))

def divisao(V1, V2):
    if type(V1) == Rect:
        V1 = V1.toPolar()
    if type(V2) == Rect:
        V2 = V2.toPolar()
    if V2.r == 0:
        raise ZeroDivisionError
    return Polar(V1.r / V2.r, Radianos(V1.theta.ang - V2.theta.ang))
    