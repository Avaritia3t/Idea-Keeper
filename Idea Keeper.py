#an example in creating an idea container.
#currently contains: Basic input verification, basic database storage utility. Future updates to include query capability, web-scraping, and voice input.
#demonstration of general coding etiquette practices
#currently using psycopg(3) and postgresql, with pgadmin4 being used as a dbadmin/verification tool.

from datetime import date, datetime
from os import name
import time
import psycopg

i_o = True
ideacount = 0

def greet(): #say hello
    print('Hello. Welcome to Idea Storage Tool v0.02')

def turnOff(): #global control loop for the program. Useless for now, can input at any time with a while i_o == True loop.
    global i_o
    i_o = False

def terminate(): #closing text
    print('You have had: ', ideacount, ' ideas this session. See you next time.')
    countdown = [None]*3 #initializing array of 3 empty values for countdown loop.
    count = len(countdown)
    i = 0
    for i in range(count): #countdown loop
        print('Closing in ', count-i, '...')
        time.sleep(1)

def getNumInput(): #number input verification function. Useful for idea designation input verification. Will implement a variation of this as a str verification eventually. 
    userNum = input('Idea designation: ')
    isNum = False
    while isNum == False:
        if userNum.isdigit() == True: #isdigit is a nice function to test variable status. 
            isNum = True
            validNum = int(userNum)
            return validNum
        else:
            userNum = input('Please enter a designated number for this idea: ')

def getYNInput(): #function for capturing input, verifying if it's a string, and verifying if that string is y/n.
    try:  #try/except for input verification purposes. Would like to refine this. 
        userInput = (input('y/n: ')).lower()
        # print('You entered:', userInput) #validation, commented out for now.
        while userInput not in ['y', 'n']: #while input is not one of these two things
            isValidInput = False #set the trigger to false
            while isValidInput == False: #while trigger is false 
                userInput = (input('Invalid input. y/n: ')).lower() #prompt for valid input
                if userInput in ['y', 'n']: #keep testing....
                    #print('Valid input.') commented out verification line
                    isValidInput = True
        return userInput
    except ValueError:
        userInput = str(input('Invalid input. Enter y/n: ')).lower() #if there's an invalid input, keep prompting and loop infinitely.
        return userInput

def getNewIdea():
    CurrentIdea = idea.getNew()              
    #create a new idea, and store it in the currentIdea slot.
    ideaID = CurrentIdea.id
    ideaName = CurrentIdea.name
    ideaSummary = CurrentIdea.summary
    ideaTime = CurrentIdea.spawnTime

    varSQL = 'INSERT INTO ideastorage (given_idea_id, idea_designation, idea_summary, idea_creation_time) VALUES (%s, %s, %s, %s)'
    SQLcolumns = (ideaID, ideaName, ideaSummary, ideaTime)
    with psycopg.connect('dbname=ideatest user=postgres password=password') as conn: #connect to database, store relevant idea information.
        with conn.cursor() as cur:
            cur.execute(varSQL, SQLcolumns)

def retrieveIdeas():
    with psycopg.connect('dbname=ideatest user=postgres password=password') as conn: #connect to database, store relevant idea information.
        with conn.cursor() as cur:
            cur.execute('''
                SELECT idea_designation, idea_summary, idea_creation_time
                FROM ideastorage
                ORDER BY idea_designation'''
            )
            storedIdeas = cur.fetchall()
            return storedIdeas

def DoIContinue(): #universal test for program continuity status. 
    decision = getYNInput()
    if decision == 'y':
        return True
    if decision == 'n':
        return False

class sessiontime: #going to need to keep track of session time and eventually analyze it for properties, clues about usage history, etc. Keep track of logon times and append to list.
                   #but for now, these functions are pretty much just for show. 
    def __init__(self, stopNow=False): #initiating sessiontime with 1 attribute, stopNow
        self.stopNow = stopNow

    def GetStartTime(): #sessiontime.GetStartTime() will get current time, and save to file.
        StartTime = datetime.now()
        StartTimeString = StartTime.strftime('%m/%d/%y %H:%M:%S\n')
        print('Script started at: ', StartTimeString)

        with open(r'C:\Users\mathew.roberts\Desktop\Test Python Code\ScriptRunTime.txt', 'w') as TimeWriter:
            TimeWriter.writelines(StartTimeString)
    
    def GetCloseTime(): #sessiontime.GetCloseTime() will get current time, and save to file as well. 
        CloseTime = datetime.now()
        CloseTimeString = CloseTime.strftime('%m/%d/%y %H:%M:%S\n')
        print('Script terminated at: ', CloseTimeString)

        with open(r'C:\Users\mathew.roberts\Desktop\Test Python Code\ScriptRunTime.txt', 'a') as TimeWriter:
            TimeWriter.writelines(CloseTimeString)

class idea: #this will serve as the heart of the program for storing, retrieving, and prioritizing ideas. 
    '''container for any random idea'''

    def __init__(self, id, name, summary, spawnTime, shouldDo, shouldNotDo): #these parameters specify the default attributes "idea" will be created with
        self.id = id #such as an idea id [1, 2 3,... ]
        self.name = name #such as a name [super lazer gun of death, Code004, my_s3cr3t_1d]
        self.summary = summary #a brief description of the idea
        self.spawnTime = spawnTime #when the idea was created
        self.shouldDo = shouldDo #if the program should be acting on this idea
        self.shouldNotDo = shouldNotDo #if the program should deprioritize this idea. 
    
    def relay(self): #essentially print the idea values.
        print("\nThis idea is designated:", self.id)
        print("Project name:", self.name)
        print("Project summary:", self.summary)
        print("")

        if(self.shouldDo == True):
            print("This project is a priority.\n")

    def detach(self):
        setattr(self, 'shouldNotDo', True)
        print('This project is no longer a priority')

    @classmethod ##function calls inside classes are better called as class methods
    def getNew(cls):
        return cls(
            id = getNumInput(), #storing a custom idea ID. Will ultimately turn this to a conditional
            name = input('Project name: '), #alternately referrable to as a project name
            summary = input('Project summary: '), #general project summary.
            spawnTime = datetime.now().strftime('%m/%d/%y %H:%M:%S'), #when the idea was created.
            shouldDo = True, #a global 'thought' variable, guiding the architecture. If an action that should be done exists, that allows binary prioritization of tasks.
            shouldNotDo = False #same as above. 
        )

#class userInput: 
    #'''This will grow up into something much larger: a contextual input algorithm filter.'''
    #def __init__(self, moodContext, isKnown):
    # here, I'll need to create a global variable, and be able to assign an 'isAffirmative' or 'isNegative' or 'isNeutral' attribute to the input variable
    # and then assign a value to the attribute based upon analysis. 
    # but for now, we'll have to rely upon good user input


if __name__ == '__main__': #start the program here

    sessiontime.GetStartTime() #log when the program was started.
    i_o = True #global program control. This is the ###do not touch### and the ###oh shit stop it now### button at the same time.

    greet()
    getNewIdea()
    ideacount +=1

    keep_working = True
    while keep_working == True:
        print('Should I continue?')
        continue_decision = DoIContinue()
        if continue_decision == True:
            print('Okay. Continuing.')
            time.sleep(1)
            getNewIdea()
            ideacount += 1
        if continue_decision == False:
            print('Okay. Terminating program.')
            keep_working = False
    
    time.sleep(2)
    
    print('Here are your currently stored ideas: ', retrieveIdeas())

    time.sleep(2)
    
    terminate() #like tears... in rain.... (this is more of a closing message than it is actually 'closing' the program.)
                #'closing' the program would go here, in the form of an i_o = False trigger, closing an enclosing while i_o = True loop. 
    sessiontime.GetCloseTime() #log program ending time. 
    quit()
