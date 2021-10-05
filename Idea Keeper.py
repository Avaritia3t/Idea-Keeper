#an example in creating an idea container. Will ultimately contain syntax checking, database integration, and data management content
#demonstration of general coding etiquette practices
#remember to increment id_number between calls
#create an 'after function is called, increment id_number by 1 master function
import time

global_trigger = 1
id_number = 0
id_session_number = 0

def increment():
    global id_number
    id_number = id_number + 1

def nextAction():
    next = input('Press 1 to create a new idea. ')

    if next == 1:
        idea.getNew() 
    else:
        quit()

class idea:
    '''container for any random idea'''

    def __init__(self, id, name, summary): #these parameters specify the default attributes "idea" will be created with
        self.id = id #such as an idea id [1, 2 3,... ]
        self.name = name #such as a name [super lazer gun of death, Code004, my_s3cr3t_1d]
        self.summary = summary #a brief description of the idea

    @classmethod ##function calls inside classes are better called as class methods
    def getNew(cls):
        return cls(
            id = int(input('Idea designation: ')), #storing a custom idea ID. Will ultimately turn this to a conditional
            name = input('Project name: '), #alternately referrable to as a project name
            summary = input('Project summary: ') #general project summary. 
        )

newIdea = idea.getNew() #initialize a first new idea.

#general print functionality for output verification. Will eventually contract into an idea replay function. Up next, sql connection to begin storing my ideas!
time.sleep(1)
print(newIdea.id)
time.sleep(1)
print(newIdea.name)
time.sleep(1)
print(newIdea.summary)

#while (global_trigger == 1):
    #keepGoing()
    #nextAction()
    

#remember to increment id_number between calls
#create an 'after function is called, increment id_number by 1 master function
#remember input to begin categorizing input for long-term data entry recognition

