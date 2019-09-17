#---------- Lab 5 | Garret Nesta ----------

import csv

num_rec = 0

first = []
last = []
age = []
nickname = []
house = []
motto = []

stark = 0
tully = 0
nw = 0
lannister = 0
baratheon = 0
targ = 0

with open("C:/Users/Garret/Desktop/Python/Intermediate/lab5_GOT.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        num_rec += 1

        first.append(rec[0])
        last.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        house.append(rec[4])

#---------------------------------------------------------------------------

print("{0:10} \t {1:12} \t {2:3} \t {3:18} \t {4}".format("FIRSTNAME", "LASTNAME", "AGE", "NICKNAME", "ALLEGIANCE"))

#---------------------------------------------------------------------------

for i in range(0, num_rec):
      print("{0:10} \t {1:12} \t {2:3} \t {3:18} \t {4}".format(first[i], last[i], age[i], nickname[i], house[i]))
      
for i in range(0, num_rec):

    if house[i] == "House Stark":
        stark += 1
        motto_var = "Winter is Coming."

    elif house[i] == "House Tully":
        tully += 1
        motto_var = "Duty. Family. Honor."

    elif house[i] == "Night's Watch":
        nw += 1
        motto_var = "The Sword in the Darkness"

    elif house[i] == "House Baratheon":
        baratheon += 1
        motto_var = "Ours is the Fury!"

    elif house[i] == "House Lannister":
        lannister += 1
        motto_var = "Hear me Roar!"

    elif house[i] == "House Targaryen":
        targ += 1
        motto_var = "Fire & Blood"

    else:
        motto_var = "*ERROR*ERROR*"

    motto.append(motto_var)

print("\n\n\n")
#-------------------------------------------------------------

print("{0:10} \t {1:12} \t {2:3} \t {3:18} \t {4:15} \t {5}".format("FIRSTNAME", "LASTNAME", "AGE", "NICKNAME", "ALLEGIANCE","MOTTO")) 

#-------------------------------------------------------------

for i in range(0, num_rec):
    print("{0:10} \t {1:12} \t {2:3} \t {3:18} \t {4:15} \t {5}".format(first[i], last[i], age[i], nickname[i], house[i], motto[i]))

print("\n\n\n")

total_age = 0

for i in range(0, num_rec):

    total_age += age[i]

avg_age = total_age / num_rec
print("There are: ", num_rec," people in the list.")
print("The average age of the list is: {0:.2f} years old".format(avg_age)) 
print("\n\t\tHOUSE COUNTS")
print("\t---------------------------")
print("\t      STARKS: {0:5}".format(stark))
print("\tNIGHTS WATCH: {0:5}".format(nw))
print("\t      TULLYS: {0:5}".format(tully))
print("\t  BARATHEONS: {0:5}".format(baratheon))
print("\t  LANNISTERS: {0:5}".format(lannister))
print("\t  TARGARYENS: {0:5}".format(targ))