import sys
import os
from os.path import exists
import random
from datetime import date
from prodstar_title import Introductions  # Import Class Introductions


def clear_console():
    os.system('clear')


def formatter(char, rows=1):
    rws = rows
    while rws > 0:
        return char * 80
        rws -= 1


def newline(num):
    return "\n" * num


def time_stamp():
    return date.today().strftime("%m/%d/%y")


def pick_selection():
    while True:
        select = input("\033[94mPlease enter your selection:\033[00m ")
        try:
            select = int(select)
            if select in range(1, 5):
                return select
                break
            else:
                print("\033[90mTry again! Please enter a number between 1-4\033[00m")
                continue
        except ValueError:
            print("\033[90mTry again! Please enter a valid number\033[00m")
            continue


def main_menu():
    intro = Introductions()  # Set intro to an instance of class Introductions
    intro.title_marquee()
    intro.menu_select()
    select = pick_selection()
    return select


def build_summary():
    l1 = "Here is a summary of today's Study Session ({})".format(time_stamp())
    l2 = formatter('-')
    l3 = "Focus Sessions completed:  {}".format(len(worked_on[1:]))
    time = len(worked_on[1:]) * focus_length
    l4 = "Minutes spent in Focused Mode: {0} (that is {1} hours)".format(time, (time/60))
    l5 = "Tasks you WORKED ON today:\n"
    l6 = [n for n in sorted(set(worked_on[1:]))]
    l7 = "Tasks you COMPLETED:\n"
    l8 = [a for a in sorted(set(completed[1:]))]
    summary_printout = [l1, l2, l3, l4, l2, l5, l6, l2, l7, l8]
    return summary_printout


def print_summary(summary):
    for item in summary:
        if not isinstance(item, (list,)):
            print(item)
        else:
            for elem in item:
                print("- " + elem)


def simple_pause():
    input("\033[94mPress <Enter> to continue\033[00m ")


def pause_program():
    while True:
        inp = input("\033[94mPress <Enter> to continue or type 'done' to exit:"
                    "\033[00m ")
        if inp == 'done':
            exit_and_progress()
        elif len(inp) > 0 and 'done' not in inp:
            print("Error! Invalid input")
        else:
            break


def back_to_main():
    input("\033[94mPress <Enter> to go back to main menu:\033[00m\n")



def pick_item():
    pick = random.choice(today_todos)
    return pick


def pick_check(choice):
    i = input("Did you finish \033[95m{}\033[00m?\ntype y/n: ".format(choice))
    if i.lower() == 'y':
        print("\nYay! I'll remove {} from your list of Todos".format(choice))
        completed.append(choice)
        today_todos.remove(choice)
    elif i.lower() == 'n':
        print("Okay. We'll keep it on the list.\n\n"
              "** Let's continue on to the next task **")
    else:
        print("Error! Please enter valid input.")
        pick_check(choice)


def writeout_completed(val):
    if output_file is not None:
        if exists(output_file):
            status = 'a'
        else:
            status = 'w'
    else:
        pass
    with open(output_file, status) as f_out:
        if status == 'a':
            f_out.write("\n\n\n\r")
        for item in val:
            if not isinstance(item, (list,)):
                f_out.write(item)
                f_out.write('\n')
            else:
                for elem in item:
                    f_out.write("- " + elem)
                    f_out.write('\n')


def write_ongoing(complete, orig_tasks):
    ongoing_tasks = []
    for task in orig_tasks:
        if task not in set(complete[1:]):
            ongoing_tasks.append(task)
    with open(input_file, "w") as f_inp:
        for item in ongoing_tasks:
            f_inp.write(item)
            f_inp.write("\n")


def exit_and_progress():
    os.system('clear')
    print(formatter('-'))
    print_summary(build_summary())
    writeout_completed(build_summary())
    write_ongoing(completed, today_todos)
    print(newline(1))
    print("\033[96m** GREAT WORK TODAY! SEE YOU TOMORROW! **\033[00m\n")
    exit()


def all_completed():
    os.system('clear')
    print(formatter('\033[95m*\033[00m', 11))
    print("{:^80}".format("CONGRATULATIONS!! YOU ARE DONE WITH YOUR TASKS!!"))
    print(formatter('\033[95m*\033[00m', 11))
    final = input("Press <Enter> to go to next screen")
    print(newline(1))
    exit_and_progress()



# Setup - Optimize terminal size for program
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=24, cols=80))

# Prints Title Screen and Captures Menu Selection
# select = main_menu()

while True:
    # Menu Select - 1. Start Studying
    select = main_menu()
    if select == 1:
        os.system('clear')
        print(formatter('*'))
        print("\033[96mWelcome to your Study Session for {}!\033[00m"
              .format(time_stamp()))
        print(formatter('*'))
        print(newline(0))
        worked_on = ["You did not work on any tasks today"]
        completed = ["You did not complete any tasks today"]
        focus_length = 0
        output_file = None
        print("Let's gather some information to get started....")
        print(newline(0))
        while True:
            try:
                input_file = input("\033[1mEnter filename (.txt) containing your list of "
                           "study items:\033[00m\n")
                open(input_file)
                print(newline(0))
                break
            except FileNotFoundError:
                print("Error! File not found. Please re-enter filename")

        while True:
            output_file = input("\033[1mEnter filename to store your completion summary:\033[00m\n")
            if output_file != input_file:
                print(newline(0))
                break
            else:
                print("Error! You can't have input and output as the same file.")

        focus_length = int(input("\033[1mEnter number of minutes for each Focus Session:\033[00m\n"))

        with open(input_file) as fhand:
            today_todos = []
            for line in fhand:
                line = line.rstrip()
                today_todos.append(line)

        os.system('clear')
        print(formatter('-'))
        print("Here is your list of Todos for today"
              " ({} items total): ".format(len(today_todos)))
        print(formatter('-'))
        for n in today_todos:
            print(n)
        print(newline(0))
        print("** Let's start your first Focus Session! **\n")

        while pause_program() is not 'done':
            new_pick = pick_item()
            print(formatter('*'))
            print("Your next task is: ")
            print(newline(8))
            print("\033[95m{:^80}\033[00m".format(new_pick))  # Centers string
            print(newline(9))
            print(formatter('*'))
            worked_on.append(new_pick)
            input("When Focus Session is over press <enter> to continue: ")
            pick_check(new_pick)

# Menu Select - 2. View Session Stats
    elif select == 2:
        sys.exit()
# Menu Select - 3. Preferences
    elif select == 3:
        sys.exit()
# Menu Select - 4. Help/About Us
    elif select == 4:
        os.system('clear')
        print(formatter('*'))
        print("\033[96m{:^80}\033[00m".format("Help/About Us"))
        print(formatter('*'))
        print(newline(0))
        with open('prod_star_info.txt') as fhandle:
            help_text = []
            for line in fhandle:
                line = line.rstrip()
                help_text.append(line)
            for n in help_text:
                print(n)
        print(newline(0))
        back_to_main()


# Gray formatting "\033[90m{}\033[00m"
# Red formatting "\033[91m{}\033[00m"
# Green formatting "\033[92m{}\033[00m"
# Yellow formatting "\033[93m{}\033[00m"
# Indigo formatting "\033[94m{}\033[00m"
# Pink formatting "\033[95m{}\033[00m"
# Turquoise formatting "\033[96m{}\033[00m"
# White bold formatting "\033[1m{}\033[00m"
