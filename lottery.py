import random

PARTICIPANTS = {}
numbers = [100 ,101 ,102 ,103 ,104 ,105 ,106 ,107 ,108 ,109 ,110 ,111 ,112 ,113 ,114 
    ,115 ,116 ,117 ,118 ,119 ,120 ,121 ,122 ,123 ,124 ,125 ,126 ,127 ,128 ,129 ,130 ,131 
    ,132 ,133 ,134 ,135 ,136 ,137 ,138 ,139 ,140 ,141 ,142 ,143 ,144 ,145 ,146 ,147 ,148 
    ,149 ,150 ,151 ,152 ,153 ,154 ,155 ,156 ,157 ,158 ,159 ,160 ,161 ,162 ,163 ,164 ,165 
    ,166 ,167 ,168 ,169 ,170 ,171 ,172 ,173 ,174 ,175 ,176 ,177 ,178 ,179 ,180 ,181 ,182 
    ,183 ,184 ,185 ,186 ,187 ,188 ,189 ,190 ,191 ,192 ,193 ,194 ,195 ,196 ,197 ,198 ,199 ,200]
for i in range(100,201):
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
        
numbers2 = [100 ,101 ,102 ,103 ,104 ,105 ,106 ,107 ,108 ,109 ,110 ,111 ,112 ,113 ,114 
    ,115 ,116 ,117 ,118 ,119 ,120 ,121 ,122 ,123 ,124 ,125 ,126 ,127 ,128 ,129 ,130 ,131 
    ,132 ,133 ,134 ,135 ,136 ,137 ,138 ,139 ,140 ,141 ,142 ,143 ,144 ,145 ,146 ,147 ,148 
    ,149 ,150 ,151 ,152 ,153 ,154 ,155 ,156 ,157 ,158 ,159 ,160 ,161 ,162 ,163 ,164 ,165 
    ,166 ,167 ,168 ,169 ,170 ,171 ,172 ,173 ,174 ,175 ,176 ,177 ,178 ,179 ,180 ,181 ,182 
    ,183 ,184 ,185 ,186 ,187 ,188 ,189 ,190 ,191 ,192 ,193 ,194 ,195 ,196 ,197 ,198 ,199 ,200]
for i in range(1,4):
    winner = random.choice(numbers2)
    numbers2.remove(winner)
    print("\n")
    print(f"The contestant who has the ticket number - {winner} is the winner no.{i} ")
    print(f" The winner no.{i} in this game is", PARTICIPANTS[winner])
    print("\n")