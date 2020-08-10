'''builds garage'''
import logging
log = logging.getLogger("my-logger")

class Garage:
    """
    Helps with building garage
    """
    def __init__(self, material):
        super().__init__()
        self.material = material

    def car_door(self, roof_type):
        log.info('build door with type '+roof_type)
        return roof_type+'_'+self.material+'_door'

    def coloring(self, paint_color):
        log.info('coloring with '+paint_color)
        return True