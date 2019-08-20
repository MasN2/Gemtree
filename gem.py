class Gem:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self):
        return str(self.__dict__)

parameters = {
    "damage": (0.87, 0.71, 0.86, 0.7, 0.85, 0.69),
    "speed": (0.74, 0.44, 0.8, 0.25, 0.92, 0.09),
    "bloodbound": (0.78, 0.31, 0.79, 0.29, 0.8, 0.27),
    "crit_chance": (0.81, 0.35, 0.8, 0.28, 0.79, 0.22),
    "crit_mult": (0.88, 0.5, 0.88, 0.44, 0.88, 0.44),
    "chain": (0.88, 0.5, 0.9, 0.47, 0.92, 0.44),
    "leech": (0.88, 0.5, 0.89, 0.44, 0.9, 0.38),
    "poolbound": (0.87, 0.38, 0.87, 0.38, 0.87, 0.38)

}

BasicGem = Gem(value=1, grade=1)
for p in parameters:
    BasicGem.__setattr__(p, 1)


def combine(g1: Gem, g2: Gem) -> Gem:
    rv = Gem()
    rv.value = g1.value + g2.value
    if abs(g1.grade - g2.grade) == 0:
        rv.grade = max(g1.grade, g2.grade) + 1
        for p in parameters:
            rv.__setattr__(p, parameters[p][0] * max(g1.__getattribute__(p), g2.__getattribute__(p)) +
                           parameters[p][1] * min(g1.__getattribute__(p), g2.__getattribute__(p)))
    elif abs(g1.grade - g2.grade) == 1:
        rv.grade = max(g1.grade, g2.grade)
        for p in parameters:
            rv.__setattr__(p, parameters[p][2] * max(g1.__getattribute__(p), g2.__getattribute__(p)) +
                           parameters[p][3] * min(g1.__getattribute__(p), g2.__getattribute__(p)))
    else:
        rv.grade = max(g1.grade, g2.grade)
        for p in parameters:
            rv.__setattr__(p, parameters[p][4] * max(g1.__getattribute__(p), g2.__getattribute__(p)) +
                           parameters[p][5] * min(g1.__getattribute__(p), g2.__getattribute__(p)))
    return rv

def power(g: Gem):
    return g.damage * g.crit_mult * g.bloodbound * g.bloodbound

def growth(g: Gem):
    import math
    return math.log(power(g)) / math.log(g.value) if g.value > 1 else 0