import string
from typing import Optional
from .pawn import Pawn, Color
from .position import Position, Direction

"""A class representing a move in the Othello game."""
class Move:
    def __init__(self, position : Position, pawn : Pawn, direction: Direction):
        if not isinstance(position, Position):
            raise ValueError("position must be a Position instance")
        if not isinstance(pawn, Pawn):
            raise ValueError("pawn must be a Pawn instance")
        if not isinstance(direction, Direction):
            raise ValueError("direction must be a Direction instance")
        self._starting_position = position
        self._starting_pawn = pawn
        self._direction = direction
        self._to_flip = []
        self._is_valid = False

    @property
    def starting_position(self) -> Position:
        return self._starting_position
    
    @property
    def starting_pawn(self) -> Pawn:
        return self._starting_pawn

    @property
    def direction(self) -> Direction:
        return self._direction

    @property
    def to_flip(self) -> list['Case']:
        return self._to_flip

    @property
    def is_valid(self) -> bool:
        return self._is_valid
    
    @is_valid.setter
    def is_valid(self, value: bool):
        if type(value) is not bool:
            raise ValueError("is_valid must be a boolean value")
        self._is_valid = value
        
    def clear_flip(self):
        self._to_flip.clear()
        self.is_valid = False
    
    def add_to_flip(self, case: 'Case'):
        if not isinstance(case, Case):
            raise ValueError("case must be a Case instance")
        self._to_flip.append(case)

""" A class representing a case on the Othello board, which can contain a pawn and has neighbors in different directions. """
class Case:
    
    def __init__(self, position: Position):
        if not isinstance(position, Position):
            raise ValueError("position must be a Position instance")
        self._position = position
        self._pawn = None
        self._neighbors = {direction: None for direction in Direction}

    @property
    def position(self) -> Position:
        return self._position

    @property
    def pawn(self) -> Pawn | None:
        return self._pawn

    @pawn.setter
    def pawn(self, pawn: Pawn | None):
        if pawn is not None and not isinstance(pawn, Pawn):
            raise ValueError("pawn must be a Pawn or None")
        self._pawn = pawn

    @property
    def neighbors(self) -> dict:
        return self._neighbors

    def get_neighbor(self, direction: Direction) -> Optional['Case']:
        return self._neighbors.get(direction)

    def set_neighbor(self, direction: Direction, neighbor: 'Case'):
        if direction not in self._neighbors:
            raise ValueError("Invalid direction.")
        self._neighbors[direction] = neighbor

    def has_all_neighbors(self) -> bool:
        return all(n is not None for n in self._neighbors.values())

    def get_empty_neighbors_directions(self) -> list[Direction]:
        return [d for d, neigbhor in self._neighbors.items()
                if neigbhor is not None and neigbhor.pawn is None
        ]

    def __str__(self) -> str:
        return str(self._pawn) if self._pawn else "·"

""" A class representing the Othello board, which contains a grid of cases and methods to manage the game state. """
class Board:
    
    def __init__(self, size=8, starting_pawns=True):
        if not isinstance(size, int) or not (5 <= size <= 9):
            raise ValueError("Size must be an integer between 5 and 9.")
        self._size = size
        self._grid = [[Case(Position(row, col)) for col in range(size)] for row in range(size)]

        self._init_neighbors()
        if starting_pawns:
            self._init_starting_pawns()

    @property
    def size(self) -> int:
        return self._size

    @property
    def grid(self) -> list[list[Case]]:
        return self._grid

    def _init_neighbors(self):
        """Initializes the neighbors for each case in the grid."""
        for row in self._grid:
            for case in row:
                for direction in Direction:
                    next_pos = case.position.next_position(direction)
                    if self.is_valid_position(next_pos):
                        neighbor_case = self._grid[next_pos.row][next_pos.col]
                        case.set_neighbor(direction, neighbor_case)

    def _init_starting_pawns(self):
        """Initializes the starting pawns in the center of the board."""
        mid = self._size // 2
        layout = [
            (mid - 1, mid - 1, Color.BLACK),
            (mid - 1, mid,     Color.WHITE),
            (mid,     mid - 1, Color.WHITE),
            (mid,     mid,     Color.BLACK),
        ]
        for row, col, color in layout:
            self._grid[row][col].pawn = Pawn(color)

    def is_full(self) -> bool:
        return all(case.pawn is not None for row in self._grid for case in row)

    def is_valid_position(self, pos: Position) -> bool:
        return 0 <= pos.row < self._size and 0 <= pos.col < self._size

    def case_at(self, position: Position) -> Case:
        return self._grid[position.row][position.col]

    def cases_with_pawn_color(self, color: Color) -> list[Case]:
        """Returns all cases that contain a pawn of the specified color."""
        cases = []
        for row in self.grid:
            for case in row:
                if case.pawn is not None and case.pawn.color == color:
                    cases.append(case)
        return cases
    
    def compute_move(self, position: Position, pawn: Pawn, direction: Direction) -> Move:
        """Computes a move based on the position, pawn, and direction."""
        
        move = Move(position, pawn, direction)
        case_to_compare =  self.case_at(position).get_neighbor(direction)
        
        while case_to_compare is not None and case_to_compare.pawn is not None:
            if case_to_compare.pawn.color != pawn.color :
                move.add_to_flip(case_to_compare)
            elif case_to_compare.pawn.color == pawn.color :
                move.is_valid = bool(move.to_flip)
                return move
            
            case_to_compare = case_to_compare.get_neighbor(direction)

        move.clear_flip()
        return move
    
    def possible_moves(self, color: Color) -> list[Move]:
        """Returns all valid moves for the given color."""
        
        possible_moves = []
        enemy_cases = self.cases_with_pawn_color(color.opposite())

        for enemy_case in enemy_cases:
            directions = enemy_case.get_empty_neighbors_directions() 
            if directions:
                for direction in directions:
                    candidate_position = enemy_case.position.next_position(direction)
                    if self.is_valid_position(candidate_position):
                        move = self.compute_move(candidate_position, Pawn(color), direction.get_opposite_direction())
                        if move.is_valid:
                            possible_moves.append(move)
        return possible_moves
    
    def filter_compatible_moves(self, possible_moves: list[Move], position: Position, color: Color) -> list[Move]:
        """Filters moves to keep only those that match the pawn's position."""
        compatible_moves = []
        for move in possible_moves:
            if move.starting_position == position and move.starting_pawn.color == color:
                compatible_moves.append(move)
        return compatible_moves
    
    def flip_pawns(self, moves: list[Move]):
        """Flips the pawns based on the provided moves."""
        for move in moves:
            for case in move.to_flip:
                case.pawn.flip()
        
    def __str__(self) -> str:
        col_headers = string.ascii_uppercase[:self._size]
        board_str = "   " + " ".join(col_headers) + "\n"
        for i, row in enumerate(self._grid):
            board_str += f"{i+1:2} " + " ".join(str(cell) for cell in row) + "\n"
        return board_str
