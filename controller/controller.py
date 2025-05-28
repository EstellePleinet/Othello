import copy
from AI.minmax import Minmax
from model import Player, Game, Move, Color
from view.view import View
# Othello/controller/controller.py

"""
Controller for the Othello game, managing the game flow and interactions between the model and view.
"""
class Controller:

    def __init__(self):
        self.game = None
        self.view = View()
        self.difficulty = 3

    def init_game(self):
        
        bot = self.view.ask_bot()
        if bot:
            self.difficulty = int(self.view.ask_difficulty())
            color = self.view.ask_color()
            if color in ["black", "b", "noir", "n"]:
                player1 = Player(self.view.ask_player_name(1), color=Color.BLACK, is_human=True)
                player2 = Player("Bot", color=Color.WHITE, is_human=False)
            else:
                player1 = Player("Bot", color=Color.BLACK, is_human=False)
                player2 = Player(self.view.ask_player_name(2), color=Color.WHITE, is_human=True)
        else:
            name1 = self.view.ask_player_name(1)
            name2 = self.view.ask_player_name(2)

            player1 = Player(name1, color=Color.BLACK, is_human=True)
            player2 = Player(name2, color=Color.WHITE, is_human=True)

        self.game = Game(player1, player2)

    def play_game(self):
        self.view.display_message("Welcome to Othello!")
        self.init_game()

        while not self.game.is_over:
            player = self.game.current_player

            if not any(self.game.board.valid_moves_iterator(player.color)):
                self.view.display_message(f"No valid moves for {player.name}. Turn skipped.")
                self.game.switch_turn()
                self.game.update_is_over()
                continue

            self.view.display_board(self.game.board)

            if player.is_human:
                self.ask_and_play_turn(player)
            else:
                self.play_ai_turn(player)

        self.view.display_board(self.game.board)
        self.view.display_message("This concludes the match! Let's see who won...")

        self.game.update_winner()
        winner = self.game.winner
        if winner:
            self.view.display_message(f"The winner is {winner.name}.")
        else:
            self.view.display_message("Draw!")



    def ask_and_play_turn(self, player: Player):
        while True:
            try:
                pos_str = self.view.ask_move(player)
                self.game.play_turn(pos_str, player)
                break
            except ValueError as e:
                self.view.display_error(str(e))
                


    def play_ai_turn(self, player: Player):
        self.view.display_message(f"{player.name} is thinking...")

        # Deepcopy temporaire
        game_copy = copy.deepcopy(self.game)

        ai = Minmax(game=game_copy, depth=self.difficulty, color=player.color)
        move = ai.best_move()

        if not move:
            self.view.display_message(f"{player} has no valid moves.")
            self.game.switch_turn()
            self.game.update_is_over()
            return

        label = move.starting_position.label
        self.view.display_message(f"{player} plays at {label}")

        try:
            self.game.play_turn(label, player)
        except ValueError as e:
            self.view.display_error(f"Erreur IA : {e}")   