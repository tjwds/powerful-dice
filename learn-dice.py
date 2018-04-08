import random

# create a list of every possible die combination

def increment_die(x, y):
    if x[y] < 6:
        x[y] = x[y] + 1
        return x
    else:
        x[y] = 0
        y = y - 1
        x = increment_die(x, y)
        return x

def all_possible():
    x = [0, 0, 0, 0, 0, 0]
    possible_dice = []
    while sum(x) != 36:
        y = 5
        if sum(x) == 21:
            if sorted(x) not in possible_dice:
                possible_dice.append(sorted(x))
        x = increment_die(x, y)
    return possible_dice

all_possible = all_possible()
        
# procedurally go through dictionary and have the die play 1000 rounds against all the other dice 
possible_contest = [[x[:], 0] for x in all_possible]
for die in possible_contest:
    for competition in possible_contest:
        for x in range(50000):
            die_rand = random.randint(0,5)
            comp_rand = random.randint(0,5)
            if die[0][die_rand] > competition[0][comp_rand]:
                die[1] = die[1] + 1

# sort list and print it 
sorted_results = sorted(possible_contest, key=lambda x: x[1])
print(sorted_results)