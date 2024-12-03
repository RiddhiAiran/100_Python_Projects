import pic
def find_highest_bid(bidding_dict):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid= bid_amount
            winner = bidder

    print(f'the winner is {winner} with a bid of {highest_bid}')

bid_dict = {}
Should_Run = True
while Should_Run:
    print(pic.logo)
    name = input("What is your name? : ")
    bid = float(input("What is your bid?: $"))
    bid_dict[name] = bid
    check_bidders = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    if check_bidders == 'no':
        Should_Run = False
        find_highest_bid(bid_dict)
    else:
        pic.clear_screen()
