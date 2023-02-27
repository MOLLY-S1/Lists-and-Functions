
def error():
    while True:
        try:
            speed = int(input("Enter speed above limit: "))
            return speed
        except ValueError:
            print("please enter an integer")


fines = {}
arrest = []

print("Enter 'x' to end")
name = input("Name: ").lower()
while name != 'x':

    speed = error()

    fines[name] = speed

    if speed >= 45:
        fine = 630
    elif speed > 40:
        fine = 510
    elif speed > 35:
        fine = 400
    elif speed > 30:
        fine = 300
    elif speed > 25:
        fine = 230
    elif speed > 20:
        fine = 170
    elif speed >15:
        fine = 120
    elif speed > 10:
        fine = 80
    elif speed < 10:
        fine = 30

    print(f"fine for {name} is ${fine}")
    if name in arrest:
        print(f"There is a warrant for {name} arrest")

    name = input("Name: ").lower()

new_dic = sorted(fines)
for hmm in new_dic:
    num = fines[hmm]
print()

print(hmm, num)
