from icecream import ic

import math

from EarthRadius import CalculateRadius

def metersPerDegree(Latitude: float) -> float:
    radius = CalculateRadius(Latitude)
    perimeter = radius * 2 * math.pi
    ratio = perimeter/360
    return ratio

if __name__ == "__main__":
    for i in range(20, 30):
        ic(metersPerDegree(i))