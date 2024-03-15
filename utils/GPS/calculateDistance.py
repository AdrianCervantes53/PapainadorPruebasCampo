from icecream import ic

import math

from getRatio import metersPerDegree

class CoordinateDistance():
    def __init__(self):
        ...

    def setStartPoints(self, lat: float, long: float) -> None:
        self.lat = lat
        self.long = long

    def convertToDegrees(self, coordenada, digits):
        grados = int(coordenada[:digits])
        minutos_decimales = float(coordenada[2:]) / 60.0
        return grados + minutos_decimales

    def calcular_distancia(self, latIn, longIn, latFin, longFin):
        # Convertir coordenadas a grados decimales
        latIn_dec = self.convertToDegrees(latIn, 2)
        longIn_dec = self.convertToDegrees(longIn, 3)
        latFin_dec = self.convertToDegrees(latFin, 2)
        longFin_dec = self.convertToDegrees(longFin, 3)
        ratio = metersPerDegree((latIn_dec + latFin_dec)/2)

        # Calcular la distancia euclidiana en metros (fórmula plana)
        distancia = math.sqrt((latFin_dec - latIn_dec)**2 + (longFin_dec - longIn_dec)**2) * ratio

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