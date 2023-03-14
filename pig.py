import argparse
from player import Player
import random
random.seed(0)

def roll_dice():
    return random.randint(1,6)

def game(numPlayers):
    players = []
    game_over = False

    # set up players name
    for i in range(1, numPlayers + 1):
        player_name = input("Player{} please input your name:".format(i))
        players.append(Player(player_name))

    # taking turns until the game is done
    while not game_over:
        for current_player in players:
            player_name = current_player.check_player_name()
            print("==================\n{} it's your turn!".format(player_name))
            print("Your total score:{}".format(current_player.check_total_score()))
            current_player.start_turn()

            # 1. prompt the user to roll or hold
            # 2. if the prompt is invalid, just keep prompting
            # 3. if the input is r, roll the dice; if h, hold
            # 4. if the player is winning (100+ total score), end the game
            while current_player.check_turn():
                player_action = input("type 'r' to roll, type 'h' to hold:")
                if player_action.lower() not in ('r', 'h'):
                    print("Not an appropriate input.")
                else:
                    player_action = player_action.lower()
                    if player_action == 'r':
                        current_player.roll(roll_dice())
                    else:
                        current_player.hold()
                    if current_player.check_winning_status():
                        game_over = True
                        return

def main(numPlayers):
    game(numPlayers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", help="Number of players",type=int, required=True)
    args = parser.parse_args()
    main(args.numPlayers)
