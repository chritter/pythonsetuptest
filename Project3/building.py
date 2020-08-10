''' building your house '''

import time

class BuildingWork:
    """
    Helps you with building your own house.
    """
    def __init__(self, material):
        self.material = material

    def set_foundation(self):
        """
        test12313
        """
        print('setting up foundation with', self.material)

    def start_building(self, rows):
        for row in range(rows):
            time.sleep(row)

if __name__ == "__main__":

    setup = BuildingWork('stone')
    setup.set_foundation()
    setup.start_building(3)

    