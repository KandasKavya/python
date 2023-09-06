import numbers


import random


numbers = [102,103,105]
sel = [103,104]
def choice():
    inputNo = random.choice(numbers)
    return inputNo
j = choice()        
if j not in sel:
     inputNo = choice()
else:
    choice()    

