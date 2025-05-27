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

    def init_game(self):
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
            possible_moves = self.game.board.possible_moves(player.color)

            if not possible_moves:
                self.view.display_message(f"No valid moves for {player.name}. Turn skipped.")
                self.game.switch_turn()
                self.game.update_is_over()
                continue

            self.view.display_board(self.game.board)

            if player.is_human:
                self.ask_and_play_turn(player)
            else:
                self.play_ai_turn(player, possible_moves)

        self.view.display_board(self.game.board)
        self.view.display_message("This concludes the match ! Let's see who won...")

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
                

    def play_ai_turn(self, player: Player, possible_moves: list[Move]):
        move = possible_moves[0]  # À remplacer plus tard par un algo
        self.view.display_message(f"{player.name} plays at {move.starting_position.to_label()}")
        self.game.play_turn(move.starting_position.to_label(), player) 
            