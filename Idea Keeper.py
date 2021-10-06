#an example in creating an idea container. Will ultimately contain syntax checking, database integration, and data management content
#demonstration of general coding etiquette practices

from datetime import date, datetime
import time

i_o = True
ideacount = 0

def turnOff():
    global i_o
    i_o = False

def terminate():
    print('You have had: ', ideacount, ' ideas this session. See you next time.')
    countdown = [None]*3
    count = len(countdown)
    i = 0
    for i in range(count):
        print('Closing in ', count-i, '...')
        time.sleep(1)

def GetNewIdea():
    CurrentIdea = idea.getNew() #create a new idea, and store it in the currentIdea slot.
    CurrentIdea.relay() #just for verification purposes, we're going to return a brief summary of the current idea. This will be super handy.

def DoIContinue(): #the guiding logic for the program. Pretty cut and dry. 
    QueryString=str(input('Do you have a new idea? y/n: ')) #receive input from the user. That's what we'll be basing the entire program off of, assn to a variable. 
    if QueryString == 'y': #test the string literal, not == y. If you have a new idea, then....
        pass
    elif QueryString == 'n': #but if you don't, just close for now. That's okay too!
        turnOff()

# next up is exception handling here. We need to make sure we don't receive any input we don't recognize. 

class sessiontime: #going to need to keep track of session time and eventually analyze it for properties, clues about usage history, etc. Keep track of logon times and append to list.
                   #but for now, these functions are pretty much just for show. 
    def __init__(self, stopNow=False):
        self.stopNow = stopNow

    def GetStartTime():
        StartTime = datetime.now()
        StartTimeString = StartTime.strftime('%m/%d/%y %H:%M:%S\n')
        print('Script started at: ', StartTimeString)

        with open(r'C:\Users\Kal\Desktop\Python Code\ScriptRunTime.txt', 'w') as TimeWriter:
            TimeWriter.writelines(StartTimeString)
    
    def GetCloseTime():
        CloseTime = datetime.now()
        CloseTimeString = CloseTime.strftime('%m/%d/%y %H:%M:%S\n')
        print('Script terminated at: ', CloseTimeString)

        with open(r'C:\Users\Kal\Desktop\Python Code\ScriptRunTime.txt', 'a') as TimeWriter:
            TimeWriter.writelines(CloseTimeString)

class idea:
    '''container for any random idea'''

    def __init__(self, id, name, summary, shouldDo, shouldNotDo): #these parameters specify the default attributes "idea" will be created with
        self.id = id #such as an idea id [1, 2 3,... ]
        self.name = name #such as a name [super lazer gun of death, Code004, my_s3cr3t_1d]
        self.summary = summary #a brief description of the idea
        self.shouldDo = shouldDo
        self.shouldNotDo = shouldNotDo
    
    def relay(self):
        print("\nThis idea is designated: ", self.id)
        print("Project name: ", self.name)
        print("Project summary: ", self.summary)

        if(self.shouldDo == True):
            print("This project is a priority.\n")

    def detach(self):
        setattr(self, 'shouldNotDo', True)

    @classmethod ##function calls inside classes are better called as class methods
    def getNew(cls):
        return cls(
            id = int(input('Idea designation: ')), #storing a custom idea ID. Will ultimately turn this to a conditional
            name = input('Project name: '), #alternately referrable to as a project name
            summary = input('Project summary: '), #general project summary.
            shouldDo = True, #a global 'thought' variable, guiding the architecture. If an action that should be done exists, that allows binary prioritization of tasks.
            shouldNotDo = False
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
    
    while i_o == True: #while the program is on...
        GetNewIdea() #accept new input.
        DoIContinue() #evaluate if the program is still needed.
        ideacount += 1

    time.sleep(2)
    terminate() #like tears... in rain.... 

    sessiontime.GetCloseTime() #log program ending time. 
    quit()
