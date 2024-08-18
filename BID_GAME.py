import random
things = [
    "Vintage Vinyl Records",
    "Antique Furniture",
    "Rare Comic Books",
    "Gold Jewelry",
    "Collectible Coins",
    "Fine Art Paintings",
    "Designer Handbags",
    "Classic Cars",
    "Sports Memorabilia",
    "Vintage Watches",
    "Luxury Watches",
    "Historical Artifacts",
    "Mid-Century Modern Furniture",
    "Rare Stamps",
    "High-End Electronics",
    "Limited Edition Prints",
    "Old Maps",
    "Sculptures",
    "Persian Rugs",
    "Unique Pottery",
    "Musical Instruments"
]

thing = random.choice(things)
auction_dictionary={}
print("Welcome to SR7 auction")
flag = True
while flag:
    name = input("Enter your name: ")
    price = int(input(f"Enter price for the auction of {thing} $: "))
    auction_dictionary[name]=price
    print("More bidders?")
    x=""
    while x != "stop":
        x = input("yes to continue, no to see the result: ")
        if x == "yes":
            print("\n"*20)
            x="stop"
        elif x == "no":
            flag = False
            print("\n"*20)
            max_bid = -1
            winner = ""
            for key in auction_dictionary:
                if auction_dictionary[key] > max_bid:
                    max_bid = auction_dictionary[key]
                    winner = key
            print(f"The winner is {winner} with a bid of ${max_bid}:")
            x="stop"
        else:
            print("********INVALID INPUT********* \n\n\n")
#note 
# you can use max(auction_dictionary,key=auction_dictionary.get)    to get the max value key easily (adjust code accordingly)
            
