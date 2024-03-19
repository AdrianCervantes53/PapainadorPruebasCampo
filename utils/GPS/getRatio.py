from icecream import ic

import math

from EarthRadius import CalculateRadius

def metersPerDegree(Latitude: float) -> float:
    radius = CalculateRadius(Latitude)
    perimeter = radius * 2 * math.pi
    ratio = perimeter/360
    return ratio

if __name__ == "__main__":
    ic(metersPerDegree(21.0893665))