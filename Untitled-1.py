gamers = {"DulliWarum" : [[10, 15], [5, 10], [2, 1.5], [100, 50]]}

XP_PER_HIT = 10

XP_BONUS_THRESHOLD = 25

XP_BONUS = 75

def menu():
    name = name_input()
    while True:
        print(f"{"MAIN MENU":.^60}")
        print(f"|{"OPTION 0":<10}{"Stop the program":>50}|")
        print(f"|{"OPTION 1":<10}{"Enter game results":>50}|")
        print(f"|{"OPTION 2":<10}{"Show a summary of all results":>50}|")
        print(f"|{"OPTION 3":<10}{"Show individual game data ":>50}|")
        print(f"|{"OPTION 4":<10}{"Enter a new gamer ":>50}|")
        option = input("Enter your option: ")
        if option == "1":
           enter_results(name, gamers)
        elif option == "2":
            summary(name, gamers)
        elif option == "3":
            individual_data(name, gamers)
        elif option == "4":
            menu()
        elif option == "0":
            break
        else:
            print("Enter a valid option")
            
  
def name_input():
    name = input("Enter your gamertag: ")
    if name in gamers:
        return name
    else: 
        gamers[name] = [[], [], [], []]
        return name


def enter_results(name, gamers):
    hits = int_input("hits")
    misses = int_input("misses")
    gamers[name][0].append(hits)
    gamers[name][1].append(misses)
    ratio = ratio_calc(hits, misses)
    xp_points = hits * XP_PER_HIT
    if hits >= XP_BONUS_THRESHOLD:
        xp_points += XP_BONUS
    gamers[name][2].append(ratio)
    gamers[name][3].append(xp_points)
    print(f"You had {hits} hits, {misses} misses, h/m ratio: {ratio:.2f}, xp gained: {xp_points}")


def int_input(type):
    while True:
        try:
            num = int(input(f"Enter the number of {type}: "))
            if num >= 0:
                return num
            else:
                print("INVALID INPUT")
        except ValueError:
            print("INVALID INPUT")


def summary(name, gamers):
    if len(gamers[name][0]) > 0:
        total_hits = sum(gamers[name][0])
        total_misses = sum(gamers[name][1])
        average_ratio = ratio_calc(sum(gamers[name][2]), len(gamers[name][2]))
        total_xp = sum(gamers[name][3])
        most_hits = max(gamers[name][0])
        most_misses = max(gamers[name][1])
        best_ratio = max(gamers[name][2])
        most_xp = max(gamers[name][3])
        print(f"|{name}| {total_hits} total hits | {most_hits} most hits | {total_misses} misses | {most_misses} most misses | {average_ratio:.2f} H/M ratio | {best_ratio:.2f} best ratio | {total_xp} XP | {most_xp} most XP |")
    else:
        print("NO DATA AVAILABLE")


def ratio_calc(x, y):
    try:
        ratio = x / y
        return ratio
    except ZeroDivisionError:
        return x


def individual_data(name, gamers):
    if len(gamers[name][0]) > 0:
        count = 1
        for game in range(len(gamers[name][0])):
            print(f"|GAME {count} | {gamers[name][0][game]} hits | {gamers[name][1][game]} misses | {gamers[name][2][game]:.2f} H/M ratio | {gamers[name][3][game]}")
            count += 1
    else:
        print("NO DATA AVAILABLE")


print(f"{"WELCOME TO THE CALL OF BATTLEFIELD DATABASE":.^60}")
print("*"*60)
menu()