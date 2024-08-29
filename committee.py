from transfer import Transfer


class Committee:

    def __init__(self):
        self.transfers = []

    def print_transfers(self):
        print("player id, buyer team, seller team, transfer price")
        for transfer in self.transfers:
            transfer.print_transfer()

    def initiate_transfer(self, transfer):
        self.transfers.append(transfer)

    def complete_transfer(self, p_id, buyer_team):
        transaction = None
        for transfer in self.transfers:
            if not transfer.buyer and transfer.player.id == p_id:
                transaction = transfer
        if not transaction:
            print("player not available in transfer_list.")
            return
        transaction.start_transfer(p_id, buyer_team)
