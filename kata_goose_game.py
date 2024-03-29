import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

class KataGoose:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        if not name:
            return f"Please enter a valid name."
        elif any(player.name.lower() == name.lower() for player in self.players):
            return f"{name}: already existing player"
        else:
            self.players.append(Player(name))
            return f"players: {', '.join(player.name for player in self.players)}"


    def roll_and_move_player(self, player):
        roll = tuple(random.randint(1, 6) for _ in range(2))
        total_roll = sum(roll)
        player.position += total_roll
        return roll, total_roll


    def handle_goose(self, player):
        goose_positions = [5, 9, 14, 18, 23, 27]
        if player.position in goose_positions:
            return True
        return False


    def handle_prank(self, player, total_roll, response):
        for other_player in self.players:
            if other_player != player and other_player.position == player.position:
                other_player.position = player.position - total_roll
                response += f". On {player.position} there is {other_player.name}, who returns to {other_player.position}"
                break

        return response


    def play_turn(self, player, carries_roll, roll):
        if carries_roll:
            total_roll = sum(roll)
        else:
            roll, total_roll = self.roll_and_move_player(player)

        if player.position == 6: # This is the case for Bridge.
            player.position = 12
            response = f"{player.name} rolls {roll[0]},{roll[1]}. {player.name} moves from {6-total_roll} to the Bridge. {player.name} jumps to 12"
            response = self.handle_prank(player, total_roll, response)
            return response

        if self.handle_goose(player): # This is the case for Goose.
            response = f"{player.name} rolls {roll[0]},{roll[1]}. {player.name} moves from {player.position-total_roll} to {player.position}, The Goose. {player.name} moves again and goes to {player.position + total_roll}"
            player.position += total_roll
            while self.handle_goose(player):
                response += f", The Goose. {player.name} moves again and goes to {player.position + total_roll}"
                player.position += total_roll

        else:
            response = f"{player.name} rolls {roll[0]},{roll[1]}. {player.name} moves from {player.position - total_roll} to {player.position}"


        response = self.handle_prank(player, total_roll, response)


        if player.position == 63: # This is the case for exact wining position.
            return f"{response}. {player.name} Wins!!!"
        elif player.position > 63: # This is the case for exceeding the wining position.
            player.position = 63 - (player.position - 63)
            return f"{response}. {player.name} bounces! {player.name} returns to {player.position}"
        else:
            return response


    def play(self):
        while True:
            for player in self.players:
                input_roll = input(f"{player.name} rolls (give two numbers separated by comma or just press ENTER): ")
                input_roll = input_roll.strip()

                if not input_roll:
                    print(self.play_turn(player, False, 0))
                else:
                    roll = tuple(map(int, input_roll.split(',')))
                    if len(roll) != 2:
                        print("Invalid input. Please provide two numbers separated by a comma.")
                        continue
                    player.position += sum(roll)
                    print(self.play_turn(player, True, roll))
                    if player.position >= 63:
                        return

if __name__ == "__main__":
    game = KataGoose()
    while True:
        new_player = input("Add player name (or type 'start' to begin game): ")

        if new_player.lower() == 'start':
            if len(game.players) < 2:
              print("Requires minimum two players to start the game.")
              continue
            break
        print(game.add_player(new_player))

    game.play()
