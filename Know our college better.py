import csv # Imports module specially made to read csv files.

# Reading the information stored about faculty and staff from csv file named GLWEC info.
elementsFile = open('GLWEC info.csv', encoding='utf-8') # Opening the file.
elementsCsvReader = csv.reader(elementsFile) # Reading the file.
elements = list(elementsCsvReader) # Storing the content of file to the list.
elementsFile.close() # Closing the file.

# Side-headings of 22 characteristics are stored in another list below.
ALL_COLUMNS = ['Name','Designation','Qualification','Achievements','Teaching subject',
'Something that everyone likes in this person','Behaviour with students',
'Way of teaching','What seems funny about this person?',
'What could the person be if they weren\'t in current profession?','Hobbies',
'Favourite place','Things that this person likes in GLWEC students',
'Things that this person likes about GLWEC','This person\'s friend in GLWEC',
'Memorable moments in GLWEC','This person\'s expectations from students',
'This person\'s expectations from college','Experience in current profession',
'Future goals','Contact info','Gmail id','Our gratitude for this person']

# An empty dictionary is created to store characteristics wise information of every person.
ELEMENTS = {}
for line in elements:
    element = {'Name'                                                            : line[0],
               'Designation'                                                     : line[1],
               'Qualification'                                                   : line[2],
               'Achievements'                                                    : line[3],
               'Teaching subject'                                                : line[4],
               'Something that everyone likes in this person'                    : line[5],
               'Behaviour with students'                                         : line[6],
               'Way of teaching'                                                 : line[7],
               'What seems funny about this person?'                             : line[8],
               'What could the person be if they weren\'t in current profession?': line[9],
               'Hobbies'                                                         : line[10],
               'Favourite place'                                                 : line[11],
               'Things that this person likes in GLWEC students'                 : line[12],
               'Things that this person likes about GLWEC'                       : line[13],
               'This person\'s friend in GLWEC'                                  : line[14],
               'Memorable moments in GLWEC'                                      : line[15],
               'This person\'s expectations from students'                       : line[16],
               'This person\'s expectations from college'                        : line[17],
               'Experience in current profession'                                : line[18],
               'Future goals'                                                    : line[19],
               'Contact info'                                                    : line[20],
               'Gmail id'                                                        : line[21],
               'Our gratitude for this person'                                   : line[22]}

    ELEMENTS[line[0]] = element # Assigns person's name to each person's details respectively.
    
while True: # Prints a table containing names of all faculty and staff.
    print("--------------------------------------------------------------------------------------------------------------")
    print(
'''     Sirisha                Sailaja             Mohan Rao            Appa Rao           deepthi   
                                                                                                                      
                Saimatha             Deepa Ganu            Swathi              Rekha                Rajini           
                                                                                                                
    Sneha Priya             Viswanath             Gopi                 Jaya               Karthika  


             Snigdha              Nagamani             Dr Hanuman              Jyothsna             Jyothi      


    Jayanthi                Madhuri               Diya                 Vijayalaxmi         Vani          ''')
    print("--------------------------------------------------------------------------------------------------------------")
    print("")          
    print('Enter name of the person you are interested to know about , or QUIT to quit.\n')
    response = input('>>>').title()
    ''' This makes words of input start with uppercased characters 
      and all remaining cased characters have lower case '''
    print('\n') # Prints a new line character. 
    
    if response == 'Quit':
        quit() # This will end the program.

    if response in ELEMENTS:
        for keys in ALL_COLUMNS:
            print('*' , keys,':\n', ELEMENTS[response][keys],'\n')
            '''Prints the 22 characteristics of the person'''

    else:
        print("You have given the wrong input. Please give the correct input")
''' This print statement works when the input is wrong,i.e. if the input is neither quit
nor the name of faculty'''         
         
         

          


    
       

