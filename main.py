from model import ScrabbleModel
from controller import Controller
from view import View
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("total_players", help="How many players will this game have?")
    parser.add_argument("word_list", help="Which word list should be used? (Only CSW2019 is supported so far)")
    parser.add_argument("challenge_rule", help="Penalty for an unsuccessful challenge")
    args = parser.parse_args()
    controller = Controller(int(args.total_players), args.word_list, args.challenge_rule)
    controller.start_game()


if __name__ == "__main__":
    main()