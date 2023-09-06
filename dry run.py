import random

PARTICIPANTS = {}
numbers = [100 ,101 ,102]
for i in range(100,103):
    print("\n")
    print(f'DEAR CONTESTANT')
    print("\n")
    print("WELCOME TO THE LOTTERY GAME ! ")
    print("\n")
    print("WIN EXCITING PRIZES\nTHERE ARE PRIZES FOR 1st , 2nd , 3rd WINNERS")
    print("\n")
    print(" KNOW THE RESULTS BY EVENING ! ")
    print("\n\n\n")
    print(" EACH TICKET  COSTS 10/- ")

    inputNo = random.choice(numbers)
    numbers.remove(inputNo)
    print("\n")
    inputName = input('Enter the name of the contestant : ')
    ticket = { (inputNo) : (inputName)  }
    print(ticket)
    PARTICIPANTS.update(ticket)
print(PARTICIPANTS)    
        
numbers2 = [100 ,101 ,102]
for i in range(1,4):
    winner = random.choice(numbers2)
    numbers2.remove(winner)
    print("\n")
    print(f"The contestant who has the ticket number - {winner} is the winner no.{i} ")
    print(f" The winner no.{i} in this game is", PARTICIPANTS[winner])
    print("\n")
    
    