
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
num = random.randint(0, 1)
if num == 1:
    print("Heads")
else:
    print("Tails")

