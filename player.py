from pl_type import PlType


class Player:
    def __init__(self, id, name, pl_type, price):
        self.id = id
        self.name = name
        self.pl_type = pl_type
        self.price = price

    def print_details(self):
        print("player id , name type price")
        print(self.id,self.name,self.pl_type,self.price)

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price

    def update_player_price(self):
        increase = self.price * 0.2
        self.price += increase
