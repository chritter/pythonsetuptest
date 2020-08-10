
class TowerPart(object):
    def __init__(self, x):
        self.x = x

@profile
def test():
    f = [TowerPart(42) for i in range(100000)]

if __name__ == '__main__':
    test()

@profile
class TowerPartCheaper(object):
    __slots__ = ('x',)

    def __init__(self, x):
        self.x = x

