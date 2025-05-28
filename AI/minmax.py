import copy
from model import Game, Move, Player, Color

class Minmax:
    def __init__(self, game: Game, depth: int = 3, color: Color = None):
        self.original_game = game
        self.depth = depth
        self.color = color

    def best_move(self) -> Move | None:
        best_score = float('-inf')
        best_move = None

        for move in self.original_game.board.valid_moves_iterator(self.color):
            game_copy = copy.deepcopy(self.original_game)
            compatible_moves = list(game_copy.board.compute_all_moves_from_position(move.starting_position, self.color))
            game_copy.play_move(move.starting_position, self.color, compatible_moves)

            score = self.minimax(game_copy, self.depth - 1, maximizing_player=False)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, game: Game, depth: int, maximizing_player: bool) -> float:
        if depth == 0 or game.is_terminal():
            return game.evaluate(self.color)

        current_color = self.color if maximizing_player else self.opponent_color(self.color)
        moves = list(game.board.valid_moves_iterator(current_color))

        if not moves:
            return self.minimax(game, depth - 1, not maximizing_player)  # passe

        best_eval = float('-inf') if maximizing_player else float('inf')

        for move in moves:
            game_copy = copy.deepcopy(game)
            compatible_moves = list(game_copy.board.compute_all_moves_from_position(move.starting_position, current_color))
            game_copy.play_move(move.starting_position, current_color, compatible_moves)

            eval_score = self.minimax(game_copy, depth - 1, not maximizing_player)

            if maximizing_player:
                best_eval = max(best_eval, eval_score)
            else:
                best_eval = min(best_eval, eval_score)

        return best_eval

    @staticmethod
    def opponent_color(color: Color) -> Color:
        return Color.NOIR if color == Color.BLANC else Color.BLANC
