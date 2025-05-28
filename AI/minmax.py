import copy
from model import Game, Move, Player, Color

class Minmax:
    def __init__(self, game: Game, depth: int = 3, color: Color = None):
        self.original_game = game
        self.depth = depth
        self.color = color

    def best_move(self) -> Move | None:
        # Find the best move for the current player using the minimax algorithm
        best_score = float('-inf')
        best_move = None

        # Iterate through all valid moves for the bot's color
        for move in self.original_game.board.valid_moves_iterator(self.color):
            # Play the move on a copy of the game
            game_copy = copy.deepcopy(self.original_game)
            compute_moves_from_position = list(game_copy.board.compute_all_moves_from_position(move.starting_position, self.color))
            game_copy.play_move(move.starting_position, self.color, compute_moves_from_position)

            # Evaluate the score of the move using minimax
            # If the game is over, or depth = 0 we return the evaluation score for this iteration
            score = self.minimax(game_copy, self.depth - 1, maximizing_player=False)

            # If the score is better than the best score found so far, update the best score and move
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, game: Game, depth: int, maximizing_player: bool) -> float:
        # Base case: if depth is 0 or the game is over, return the evaluation score
        # color of the bot - color of the opponent
        if depth == 0 or game.game_is_over():
            return game.game_evaluate(self.color)

        # if not maximizing_player, we are evaluating the opponent's turn : we take the opponent's color
        current_color = self.color if maximizing_player else self.opponent_color(self.color)
        
        # Evaluation : 
        moves = list(game.board.valid_moves_iterator(current_color))

        # If there are no valid moves, we pass the turn
        if not moves:
            return self.minimax(game, depth - 1, not maximizing_player)  # not maximizing_player -> other player's turn

        # best_eval is initialized to negative or positive infinity depending on whether we are maximizing or minimizing
        best_eval = float('-inf') if maximizing_player else float('inf')

        # Iterate through all valid moves for the current player
        for move in moves:
            # play the move on a copy of the game
            game_copy = copy.deepcopy(game)
            compatible_moves = list(game_copy.board.compute_all_moves_from_position(move.starting_position, current_color))
            game_copy.play_move(move.starting_position, current_color, compatible_moves)

            # evalate the score of the move using minimax
            eval_score = self.minimax(game_copy, depth - 1, not maximizing_player)

            # Best evaluation when ennemy is min of evaluate(color of bot)
            # Best evaluation when bot is max of evaluate(color of bot)
            if maximizing_player:
                best_eval = max(best_eval, eval_score)
            else:
                best_eval = min(best_eval, eval_score)

        return best_eval

    @staticmethod
    def opponent_color(color: Color) -> Color:
        return Color.BLACK if color == Color.WHITE else Color.WHITE
