# The Monty Hall Problem - Frequency Analysis - www.101computing.net/the-monty-hall-problem
import random
import numpy as np

#Let's initialise our 3 doors
doors = ["goat", "goat", "car"]

# Randomly position the two goats and the car behind the three doors
random.shuffle(doors)

# Randomly pick a door and display the selected door number
# Get the computer to identify the two doors which have not been selected
#   If only one of these two doors contains a goat, display the door number to reveal the goat
#   If both doors contain a goat, pick one of the two doors randomly and display its number to reveal the goat
# Get the computer to randomly decide whether it will keep the selected door or switch to the other closed door
# Reveal the content of all three doors
# Check if the car was behind the selected door
# Keep count of wins and loses when the user decide to switch doors or not
# Display these counters/statistics
# Repeat the above process 100 times.
# If your code is working fine you should reach statistics to confirm that:
#     When switching doors your are twice as likely to win the car
#     When not switching doors your are twice as likely to get the goat!

TRIES, SWITCH, KEEP = 0, 1, 2
results_arr = np.array([1000, 0, 0], dtype=int)

for n in range(results_arr[TRIES]):
    my_doors = doors.copy()
    chosen_door = my_doors.pop(random.randint(0,2))
    open_door = my_doors.pop(my_doors.index("goat"))
    if my_doors[0] == "car":
        results_arr[SWITCH] += 1
    else:
        results_arr[KEEP] += 1

print(f"""Our statistics out of {results_arr[TRIES]} attempts...
{'-'*50}
Number of wins after switching doors: {results_arr[SWITCH]}, {results_arr[SWITCH]/results_arr[TRIES]*100}%
Number of losses after switching doors: {results_arr[TRIES]-results_arr[SWITCH]}
{'-'*50}
Number of wins when not switching doors: {results_arr[KEEP]}, {results_arr[KEEP]/results_arr[TRIES]*100}%
Number of losses when not switching doors: {results_arr[TRIES]-results_arr[KEEP]}
""")
