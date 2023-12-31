import json
import os

class TicTacToe:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if 1 <= position <= 9 and self.board[position - 1] == ' ':
            self.board[position - 1] = self.current_player
            return True
        else:
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]

        return 'Tie' if ' ' not in self.board else None

    def save_score(self, winner):
        scores = self.load_scores()
        scores[winner] = scores.get(winner, 0) + 1
        with open('scores.json', 'w') as file:
            json.dump(scores, file)

    def load_scores(self):
        if os.path.exists('scores.json'):
            with open('scores.json', 'r') as file:
                return json.load(file)
        return {}


def main():
    game = TicTacToe()

    while True:
        print("\n=== Tic Tac Toe ===")
        print("1. Nowa gra")
        print("2. Tablica wyników")
        print("3. Ustawienia")
        print("4. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            game.reset_board()

            while True:
                game.print_board()
                position = int(input(f"{game.current_player}'s turn. Enter position (1-9): "))

                if game.make_move(position):
                    winner = game.check_winner()

                    if winner:
                        game.print_board()
                        if winner == 'Tie':
                            print("Remis!")
                        else:
                            print(f"{winner} wygrywa!")
                            game.save_score(winner)
                        break

                    game.switch_player()
                else:
                    print("Nieprawidlowy ruch. Spróbuj ponownie.")
        elif choice == '2':
            scores = game.load_scores()
            print("\n=== Tablica wyników ===")
            for player, score in scores.items():
                print(f"{player}: {score} zwycięstw")
        elif choice == '3':
            print("\n=== Ustawienia ===")
        elif choice == '4':
            print("Dziękujemy za grę! Do zobaczenia.")
            break
        else:
            print("Nieprawidlowy wybor. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
