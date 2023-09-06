import random # imports a module 'random' to access it in code.

import getpass 
# This module makes the letters of selected input invisible on screen while typing it.

import pyttsx3 # This module converts text to speech.


engine = pyttsx3.init() # Initiation.
engine.setProperty('rate',150) # Sets rate.
engine.setProperty('volume',1.0) # Sets volume.
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) # Sets voice either male or female.


def englishToLeetMessage(message):
    # Convert the English string in message to leetmessage and return leetmessage.

    # Make sure all the keys in `charMapping` are lowercase.
    charMapping = {
    'a': ['4','@','/-\\','^'],'b':['|>','|o'],'c': ['(','[','<'], 'd': ['|)','<|','o|'],
    'e': ['3','[-','(-'],'f': ['ph'],'g':['C','9'],
    'h': [']-[', '|-|','(-)','}{','/-/','\-\\',')-('],
    'i': ['1', '!', '|','I'],'j':['J','7'],'k': [']<',')<','|<',],'l':['|_','/'],
    'm':['^^','|\/|','/\/\\','(\/)',']\/['],'n':['|\|',']\[','(\)','/\/'],
    'o': ['0'],'s': ['$', '5'], 't': ['+','|-',], 'u': ['|_|','(_)'],
    'v': ['\\/','V'],'w':['vv','|/\|','(/\)',']/\[','\/\/','VV'],'x':['><'],'z':['2','Z']}
    leetMessage = '' # An empty string.

    for char in message:  # Checks each character:
        # There is a 70% chance we change the character to leetmessage.

        if char.lower() in charMapping and random.random() <= 0.70: # Enters loop only if true.
            possibleLeetReplacements = charMapping[char.lower()] # All possibilities.
            leetReplacement = random.choice(possibleLeetReplacements)
            # Selects only one possibility using random module.
            leetMessage = leetMessage + leetReplacement + ' '

        else:
            # 30% chance to enter this loop.....
            # Untranslated characters:
            leetMessage = leetMessage + char + ' '       
    return leetMessage

def game():
    english = getpass.getpass(prompt='Enter your english language message:')
    print("\n") # New - line character.
    '''Takes the input in English.But letters getting typed are invisible on screen due to
    the module 'getpass'.'''
    leetMessage = englishToLeetMessage(english)
    # Calls the function to convert the English message to hackers language.
    print(leetMessage)# Prints the message returned by the above function.
    print("\n") # New - line character.

    print("Guess the english message for this leetmessage displayed....\n")
    engine.say("Guess the english message for this leetmessage displayed")
    engine.runAndWait()
    
    print("You have 3 attempts to guess the answer\n") 
    engine.say("You have 3 attempts to guess the answer")
    engine.runAndWait()
    
    englishList = list(english.lower()) # Conversion of data type : string to list.

    print(f"The answer is a '{len(englishList)}' - letter word\n")
    engine.say(f"The answer is a '{len(englishList)}' - letter word")
    engine.runAndWait()
    
    for chances in range(1,4):
       
        engine.say(f"This is your attempt no.{chances}")
        engine.runAndWait()
        answer = input(f"This is your attempt no.{chances}\n\nType the answer here\n\n>>>")
        
        print("\n") # New - line character.

        answerList = list(answer.lower()) # Conversion of data type : string to list.

        for j in range(len(englishList)): # A loop to check all the letters of our answer.

            if answerList[j] == englishList[j]:
                print(f"The character '{answerList[j]}' in your answer is correct")
                print("\n") # New - line character.
                continue

            else:
                print(f"The character '{answerList[j]}' in your answer is incorrect")
                # Only wrong characters are displayed.
                print("\n") # New - line character.
                
        if answerList == englishList:
            print("You have guessed it RIGHT !!!")
            engine.say("You have guessed it RIGHT !!!")
            engine.runAndWait()           
            break

        else:
            print("You have guessed it WRONG !!!")
            engine.say("You have guessed it WRONG !!!")
            engine.runAndWait()            
            print("\n") # New - line character.

    print(f"The answer is {english}.....")
    engine.say(f"The answer is {english}")
    engine.runAndWait()
    
    print("\n") # New - line character.

game() # Calling the function 'game'.
while True: # This is a continuous loop.

    engine.say("Do you want to continue the game ?")
    engine.runAndWait()
    yesOrNo = input("Do you want to continue the game ? Type Y/N....")

    print("\n") # New - line character.

    if yesOrNo.capitalize() == "N":

        print("OK ! Have a nice day")
        engine.say("OK ! Have a nice day")
        engine.runAndWait()
        quit() # Program ends.

    elif (yesOrNo.capitalize() == "Y"):

        print("Wow ! Amazing ! Lets move ahead")
        engine.say("Wow ! Amazing ! Lets move ahead")
        engine.runAndWait()
        game() # If "Y", the function 'game' is called again.

    else:

        print("Type only 'y' or 'n' in any lower or upper case") 
        # In case anything else is typed.
        engine.say("Type only 'y' or 'n' in any lower or upper case")
        engine.runAndWait()
        
        print("\n") # New - line character.

          


    

           





    

    

