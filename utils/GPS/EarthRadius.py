import math
from icecream import ic

def CalculateRadius(latitude: float) ->float:
    """Funcion que calcula el radio aproximado de la tierra
    respecto a la latitud
    
    Keyword arguments:
    latitude: Latitud en grados decimales ej.(GG.GGGGG)
    Return: Radio de la tierra en metros
    """
    
    l = math.radians(latitude)

    a = 6378137
    b = 6356752.3142

    f1 = ((a**2) * math.cos(l))**2
    f2 = ((b**2) * math.sin(l))**2
    f3 = (a * math.cos(l))**2
    f4 = (b * math.sin(l))**2

    earthRadius = math.sqrt((f1 + f2)/ (f3 + f4))

    return earthRadius


if __name__ == "__main__":
    for i in range(20, 30):
        ic(CalculateRadius(i))
