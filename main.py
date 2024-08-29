from committee import Committee
from player import Player
from pl_type import PlType
from team import Team
from transfer import Transfer

players = []
for player_id in range(40):
    players.append(Player(100 + player_id, 'A', PlType.ALL_ROUNDER, 50))

team_1 = Team(1, 'team1', players[:10])
team_2 = Team(2, 'team2', players[10:20])
team_3 = Team(3, 'team3', players[20:30])
team_4 = Team(4, 'team4', players[30:])
# team_1.print_team()
transfer_1 = Transfer(players[2], team_1, players[2].get_price()+100)
transfer_2 = Transfer(players[12], team_2, players[12].get_price()+150)
committee = Committee()
committee.initiate_transfer(transfer_1)
committee.initiate_transfer(transfer_2)
committee.complete_transfer(players[2].get_id(), team_3)
# committee.complete_transfer(players[2].get_id(), team_1)
committee.complete_transfer(players[12].get_id(), team_3)
print(team_3.get_budget())
print(team_1.get_budget())
committee.print_transfers()
# team_1.print_team()
# team_2.print_team()
# team_3.print_team()

