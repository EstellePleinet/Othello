class Minmax:
    def __init__(self, game):
        self.game = game

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.game.is_terminal():
            return self.game.evaluate()

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.game.get_valid_moves():
                self.game.make_move(move)
                eval = self.minimax(depth - 1, False)
                self.game.undo_move(move)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.game.get_valid_moves():
                self.game.make_move(move)
                eval = self.minimax(depth - 1, True)
                self.game.undo_move(move)
                min_eval = min(min_eval, eval)
            return min_eval