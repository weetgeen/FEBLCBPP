import random

players = 5


def throwDices():

    dices = []
    for dice in range(6*players):
        dices.append(random.randint(1,6))

    return dices


dices = throwDices()

ones = dices.count(1)
twos = dices.count(2) + dices.count(1)
threes = dices.count(3) + dices.count(1)
fours = dices.count(4) + dices.count(1)
fives = dices.count(5) + dices.count(1)
sixes = dices.count(6) + dices.count(1)

print(ones)
print(twos)
print(threes)
print(fours)
print(fives)
print(sixes)




