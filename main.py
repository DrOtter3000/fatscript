#TODO: Add option to delete last entry in csv

import matplotlib.pyplot as plt


def menu():
    print("What do you want to do?")
    print("(1): Update weight, (2): show table, (Q:): Quit")
    action = input()
    if action == "1":
        update_weight()
    if action == "2":
        show_weight()
    if action == "q" or action == "Q":
        quit()
    else:
        menu()


def update_weight():
    from datetime import date
    date = date.today()
    weight = int(input("Your weight: "))
    data_to_string = str(date) + ", " + str(weight) + "\n"
    with open("fatdata.csv", "a") as fatdata:
        fatdata.write(data_to_string)
    menu()


def show_weight():
    date_axis = []
    weight_axis = []
    with open("fatdata.csv", "r") as fatdata:
        line_list = []
        for line in fatdata:
            line_list = line.strip().split(", ")
            date_axis.append(line_list[0])            
            weight_axis.append(int(line_list[1]))
    plt.plot(date_axis, weight_axis)
    plt.show()
    menu()



menu()