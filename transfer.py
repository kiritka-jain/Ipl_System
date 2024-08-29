from player import Player
from team import Team


class Transfer:
    def __init__(self, player: Player, seller: Team, price: int, buyer: Team = None):
        self.player = player
        self.buyer = buyer
        self.price = price
        self.seller = seller

    def print_transfer(self):
        if self.buyer is not None:
            print(self.player.id, self.buyer.name, self.seller.name, self.price)
        else:
            print(f"{self.player.id}, None, {self.seller.name}, {self.price}")

    def start_transfer(self, p_id, buyer_team):
        if self.seller.id == buyer_team.id:
            print("buyer team and seller team cannot be same.")
            return
        if buyer_team.get_budget() < self.price:
            print("budget of buyer team is not sufficient for transaction.")
            return
        self.seller.remove_player(player_id=p_id)
        self.player.update_player_price()
        self.buyer = buyer_team
        self.buyer.add_player(self.player)
        self.buyer.budget -= self.price
        self.seller.budget += self.price
