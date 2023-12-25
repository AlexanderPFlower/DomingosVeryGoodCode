import random, os
from subprocess import call
from time import sleep

#### AUXILIARY CODE TO ANIMATE RESULTS  #### 
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

# slowprint before RNG lottery
def slowprint(x):
    for i in x:
        print(i)
        sleep(0.5)


#####     MAIN PROGRAM STARTS HERE      ####  
def selector():
    # Get number of choices, typecast to int as to prepare for loop
    clear()
    print("Number of choices:")
    x = input("> ")
    x = int(x)
    i = 0
    clear()

    # preparing str choices to be added to a list
    choice_count = 0
    choiceList = []

    # While i/0 is less than x, ask for a new choice, store choice into list
    while i < x:
        print(f"Choice {i}: ")
        decide = input("> ")
        choiceList.append(decide)
        choice_count += 1
        i += 1

    # RNG for choice decider!
    clear()
    slowprint("...")

    decider = random.choice(choiceList)
    print(decider + " :)")

selector()
