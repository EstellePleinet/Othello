from enum import Enum

"""Direction enum representing the 8 possible directions in a grid."""
class Direction(Enum):
    
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)
    NORTHEAST = (-1, 1)
    NORTHWEST = (-1, -1)
    SOUTHEAST = (1, 1)
    SOUTHWEST = (1, -1)
    
    def get_opposite_direction(self)  -> 'Direction':
        """Returns the opposite direction."""
        opposite = (-self.value[0], -self.value[1])
        for direction in Direction:
            if direction.value == opposite:
                return direction