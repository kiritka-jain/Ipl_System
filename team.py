from player import Player


class Team:
    def __init__(self, id, name, players):
        self.id = id
        self.name = name
        self.players = players
        self.budget = 100
        self.value = 500

    def print_team(self):
        print("Team , player id, player name, player price")
        for player in self.players:
            print(f"{self.name}  {player.id}  {player.name}  {player.price}")

    def get_budget(self):
        return self.budget

    def get_value(self):
        return self.value

    def add_player(self, player: Player):
        self.players.append(player)
        self.value += player.price

    def remove_player(self, player_id):
        for player in self.players:
            if player.id == player_id:
                self.value -= player.price
                self.players.remove(player)
                return
        print("player not found.")

