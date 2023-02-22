BASE_FEE = 10

time_total = 0
income = 0
trips = 0


name = input("Enter your name:")
choice = input("Would you like to start a trip: (yes or no) ").lower()

while choice != "no" or choice != "yes":
    print("please enter yes or no")
    choice = input("Would you like to start a trip: (yes or no) ").lower()

while choice == 'yes':
    time = int(input("How long was the trip (in minutes): "))
    time_total += time

    cost = BASE_FEE + 2*time
    print(f"The trip cost ${cost}")
    income += cost

    trips += 1

    choice = input("Would you like to start a trip: (yes or no) ").lower()

if choice == "no":
    print()
    print(f"The name of the driver is {name}\n"
          f"The total time of all trips was {time_total}\n"
          f"The average time of all trips was {time_total/trips}\n"
          f"The total income of all trips was ${income}\n"
          f"The average income of all trips was ${income/trips}\n"
          f"Goodbye"
          f"")




