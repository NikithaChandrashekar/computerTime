import time
import os 
import shutil

def getComputerTime():
    t=time.localtime()
    currentTime=time.stfrtime("%H:%M:%S" , t)
    print(currentTime)

question=input("wanna know the exact time of ur computer?")
if(question=="yes"):
    print("Yay!ok so let me show you the time!")

getComputerTime()

