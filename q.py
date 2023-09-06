import random

numbers2 = [100 ,101 ,102]
for i in range(1,4):
    winner = random.choice(numbers2)
    numbers2.remove(winner)
    print(numbers2)
    print(f"The winner no.{i} has got the number {winner}")