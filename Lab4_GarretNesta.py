#------- Garret Nesta | Lab 4 ----------

import csv

total_records = 0

desk_over = 0
laptop_over = 0

replacement = []

type = []
manu = []
processor = []
ram = []
hd_size = []
disk2 = []
no_hdd = []
os = []
year = []

#------------------------------------------

print("{:8} \t {:12} \t {:10} \t {:4} \t {:8}\t{:6} {:6} \t{:6}\t {:6}\t{:3}".format("TYPE", "MANUFACTURER", "PROCESSOR", "RAM", "HD SIZE", "# HDD", "2ND DISK", "OS", "YEAR", "REPLACE?"))

#------------------------------------------

with open("C:/Users/Garret/Desktop/Python/Intermediate/lab4a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        total_records += 1

        type.append(rec[0])
        manu.append(rec[1])
        processor.append(rec[2])
        ram.append(rec[3])
        hd_size.append(rec[4])
        no_hdd.append(int(rec[5]))
        replacement.append(" ")

        if int(rec[5]) == 1:
            disk2.append(" ")
            os.append(rec[6])
            year.append(int(rec[7]))

        elif int(rec[5]) == 2:
            disk2.append(rec[6])
            os.append(rec[7])
            year.append(int(rec[8]))

        else:
            print("ERROR!* incompatible number of hard disks")

for index in range (0, total_records):
                version = 19 - year[index]

                if type[index] == "D":

                    if version > 2:
                        desk_over += 1
                        replacement[index] = "***"

                if type[index] == "L":

                    if version > 2:
                        laptop_over += 1
                        replacement[index] = "***"

for index in range (0, total_records):
    
    if type[index] == "D":
        type[index] = "DESKTOP"
    elif type[index] == "L":
        type[index] = "LAPTOP"
    else:
        type[index] = "--ERROR--"

    if manu[index] == "DL":
        manu[index] = "Dell"
    elif manu[index] == "HP":
        manu[index] = "HewittPackard"
    elif manu[index] == "GW":
        manu[index] = "Gateway"


for index in range (0, total_records):

    print("{:8} \t {:12} \t {:10} \t {:2}GB \t {:8}\t{:6} {:6} \t{:6}\t {:6}\t{:3}".format(type[index], manu[index], processor[index], ram[index], hd_size[index], no_hdd[index], disk2[index], os[index], year[index], replacement[index]))


desk_cost = desk_over * 2000
lap_cost = laptop_over * 1500

print("Machines in file: ", total_records, "\n")
print("DESKTOPS over: {0} [ x $2000/ea ] ESTIMATED COST: $ {1:8.2f}".format(desk_over, desk_cost))
print("LAPTOPS over: {0} [ x $1500/ea ] ESTIMATED COST: $ {1:8.2f}".format(laptop_over, lap_cost))