from datetime import date, datetime
import time

def GetStartTime():
    StartTime = datetime.now()
    StartTimeString = StartTime.strftime('%m/%d/%y %H:%M:%S\n')
    print('Script started at: ', StartTimeString)

    with open(r'C:\Users\mathew.roberts\Desktop\Test Python Code\ScriptRunTime.txt', 'w') as TimeWriter:
        TimeWriter.writelines(StartTimeString)

def GetCloseTime():
    CloseTime = datetime.now()
    CloseTimeString = CloseTime.strftime('%m/%d/%y %H:%M:%S\n')
    print('Script terminated at: ', CloseTimeString)

    with open(r'C:\Users\mathew.roberts\Desktop\Test Python Code\ScriptRunTime.txt', 'a') as TimeWriter:
        TimeWriter.writelines(CloseTimeString)

GetStartTime()
print("The program is currently running.\n")
time.sleep(5)
GetCloseTime()
quit()