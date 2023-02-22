
def error():
    while True:
        try:
            absence = int(input("Enter absences: "))
            return absence
        except ValueError:
            print("please enter an integer")







av = 0
most = ""
most_num = 0
workers_not_absent = []
count = 0
dic = {}



name = input("Please enter name: ")

while name != "$":
    absence = error()
    dic[name] = absence
    av += absence
    count += 1
    if absence > most_num:
        most = name
        most_num = absence
    elif absence == 0:
        workers_not_absent.append(name)

    name = input("Please enter name: ")

avdays = av/ count
new_list = sorted(workers_not_absent)
print()
print(f"The average number of absent days this year was {av/count}\n")
print(f"The person with the most absence days was {most} with {most_num} days "
      f"absent\n"
      f"The people who were not absent throughout the year were:")
for people in new_list:
    print(people)

print()
print(f"The people with more absence days than the average are:")
new_dic = sorted(dic)
for hmm in new_dic:
    num = dic[hmm]

    if num > avdays:
        print(hmm, num)












