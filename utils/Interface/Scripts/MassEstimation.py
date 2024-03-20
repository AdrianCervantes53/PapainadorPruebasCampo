from icecream import ic

import math

def calculateVolume(minorAxis: float, majorAxis: float) -> float:
    print(round(minorAxis, 3), round(majorAxis, 3))
    volumen = (4 * math.pi * (majorAxis/2000) * (minorAxis/2000)**2)/3
    #ic(volumen)
    return volumen

def calculateMass(volumen: float) -> float:
    densidad = 1175.21
    coeficiente = 0.56
    mass = volumen * 530
    return mass

if __name__ == "__main__":
    x = 77
    y = 96

    vol = calculateVolume(x, y)
    mass = calculateMass(vol)
    ic(mass)