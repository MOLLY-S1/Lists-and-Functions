item = input("Enter item to be auctioned: ")
reserve = float(input("Enter item reserve bid: "))
print()
highest = 0

# Intro screen
print(f"The auction for the {item} has begun."
      "When you stop bidding enter '-1' to terminate auction")
print()

# loop to continue auction until "-1" is entered
while True:
    print(f"The highest bid so far is ${highest}")
    bid = float(input("What is your bid?"))
    print()

    #if a higher bid is entered replace the current
    if bid > highest:
        highest = bid
    
    elif bid< highest and bid != -1:
        print("Higher bid needed")
        print()
    elif bid == -1:
        break


if highest >= reserve:
    print(f"The {item} was sold for a bid of ${highest}")
else:
    print(f"The {item} did not sell")
