from icecream import ic

import math

from utils.GPS.getRatio import metersPerDegree

class CoordinateDistance():
    def __init__(self):
        ...

    def setStartPoints(self, lat: float, long: float) -> None:
        self.latitude = lat
        self.longitude = long

    def convertToDegrees(self, coordenada, digits):
        grados = int(coordenada[:digits])
        minutos_decimales = float(coordenada[2:]) / 60.0
        return grados + minutos_decimales
    
    def setRatio(self, lat: float):
        self.ratio = metersPerDegree(lat)

    def calculateDistance(self, latFin, longFin):
        # Calcular la distancia euclidiana en metros (fórmula plana)
        distancia = math.sqrt((latFin - self.latitude)**2 + (longFin - self.longitude)**2) * self.ratio

        return distancia


if __name__ == "__main__":
    # Ejemplo de coordenadas en formato ddmm.mmmmm
    latIn = '2112.345'  # Por ejemplo
    longIn = '101234.567'  # Por ejemplo

    latFin = '2112.344'  # Por ejemplo
    longFin = '101234.565'  # Por ejemplo

    distance = CoordinateDistance()

    # Calcular la distancia
    distancia = distance.calcular_distancia(latIn, longIn, latFin, longFin)

    # Umbral de alerta
    umbral_alerta = 5  # 5 metros

    # Verificar si la distancia supera el umbral
    ic(distancia)
    if distancia > umbral_alerta:
        ic("¡Alerta! La distancia es mayor a 5 metros.")
    else:
        ic("La distancia es aceptable.")