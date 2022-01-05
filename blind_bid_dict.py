from replit import clear
from blind_bid_art import logo

print(logo)
bidding_finish = False
bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while not bidding_finish:
    name_input = input("What is your name?: \n")
    bid = input("What your bid?: \n")
    bid_input = int(bid)
    bids[name_input] = bid_input
    should_continue = input("Are there any other bidders? type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
