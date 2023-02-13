children = []
CHARGE = 12

def dropOff():
    child = input("Child name:")
    children.append(child)
    print(f"{child} has been dropped off")
    print()

def pickup():
    child = input("Child name:")
    if child in children:
        children.remove(child)
        print(f"{child} has been picked up")
        print()
    else:
        print(f"Sorry, the child {child} does not exist in the system, "
              "please ensure you have spelt the name correctly.")
        print()


def calcost():
    hours = int(input("Hours: "))
    num = len(children)
    cost = num * hours * CHARGE
    print(f"The total cost for {num} children for {hours} hours is ${cost}")
    print()


def printroll():
    print()
    print(f"The current roll for MGS Childcare is:")
    for i in children:
        print(i, end = ", ")
    print()
    print()

def main():
    choice = 0
    while choice!=5:

        print("-----------------------------------------------------------------------")
        print("Welcome to MGS Childcare")
        print("What would you like to do? Please choose one of the items below")
        print("-----------------------------------------------------------------------")
        print()
        print("1 Drop off a child")
        print("2 Pick up a child")
        print("3 Calculate cost")
        print("4 Print roll")
        print("5 Exit the system")
        print()
        choice=int(input("Enter your choice (number between 1 and 5): "))
        print()

        if choice==1:
            dropOff()


        if choice == 2:
            pickup()

        if choice == 3:
            calcost()

        if choice == 4:
            printroll()

    return ("Goodbye")

print(main())
print()
