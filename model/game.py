from .player import Player
from .pawn import Pawn, Color
from .position import Position, Direction
from .board import Board, Move

class Game:
    
    def __init__(self, player_one: Player, player_two: Player, size=8):
        if not isinstance(player_one, Player) or not isinstance(player_two, Player):
            raise ValueError("Both players must be instances of Player.")
        
        self._board = Board(size)
        self._players = [player_one, player_two]
        self._current_player_index = 0
        self._is_over = False 
        self._winner = None
    
    @property
    def board(self):
        return self._board
    
    @property
    def players(self):
        return self._players
    
    @property
    def current_player(self):
        return self.players[self._current_player_index]
    
    @property
    def is_over(self):
        return self._is_over
    
    @property
    def winner(self):
        return self._winner
    
    def switch_turn(self):
        self._current_player_index = 1 - self._current_player_index
        
    def update_winner(self):
        """Updates the winner of the game if it is finished."""
        if self.is_over:
            black_pawns = self.board.cases_with_pawn_color(Color.BLACK)
            white_pawns = self.board.cases_with_pawn_color(Color.WHITE)
            if len(black_pawns) > len(white_pawns):
                self._winner = self.players[0]
            elif len(white_pawns) > len(black_pawns):
                self._winner = self.players[1]
            else:
                self._winner = None
    
    def update_is_over(self):
        possible_moves_black = self.board.possible_moves(Color.BLACK)
        possible_moves_white = self.board.possible_moves(Color.WHITE)
        self._is_over = self.board.is_full() or (not (possible_moves_black or possible_moves_white))

    def play_turn(self, pos_str: str, player: Player):
        if self.is_over:
            raise ValueError("The game is over. No more moves can be played.")
        
        if player != self.current_player:
            raise ValueError("It's not your turn.")

        color = player.color
        possible_moves = self.board.possible_moves(color)

        if not possible_moves:
            raise ValueError(f"No valid moves available for {player.name}.")

        position = Position(label=pos_str.strip().upper())

        return self.play_move(position, color, possible_moves)

    
    def play_move(self, pos: Position, color: Color, possible_moves: list[Move]):
        if not self.board.is_valid_position(pos):
            raise ValueError("Invalid position.")

        if self.board.case_at(pos).pawn is not None:
            raise ValueError("The position is already occupied.")

        compatible_moves = [m for m in possible_moves if m.starting_position == pos]
        
        if not compatible_moves:
            raise ValueError("No valid move at this position.")

        self.board.case_at(pos).pawn = Pawn(color)
        self.board.flip_pawns(compatible_moves)

        self.update_is_over()
        if not self.is_over:
            self.switch_turn()
        else:
            self.update_winner()

        return True

