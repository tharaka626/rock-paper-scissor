import sys
import random
from enum import Enum


def rps(name):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(
            f"\n{name}, please enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors: \n\n")

        if player_choice not in ['1', '2', '3']:
            print(f"{name}, Invalid choice. Please enter 1, 2 or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')} .\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == computer:
                return "🤝 Tie game!"
            else:
                python_wins += 1
                return f"🖥️ Python wins! \nSorry, {name}.. 😞"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉 🎉 🎉 🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=False, help="The name of the person playing a game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name if args.name else "PlayerOne")
    rock_paper_scissors()  # Call the function to start the game
