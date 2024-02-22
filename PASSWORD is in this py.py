import os #Importing os module to execute windows cmds.
import ctypes #Importing ctypes to change the cmd prompt title.

ctypes.windll.kernel32.SetConsoleTitleW("RgCommitBot") #This title is configurable.
print('\n\tThe password is : "jaishreeram"\n\tyou can also visit : https://github.com/RISHAB-CREATOR/RgCommitBot to get the password.') #Password and links part.
input("\n\tPress ENTER key to continue.......") #Just an userfriendly enter key here good for nothing...

os.system('cls') #cls inbuilt windows cmd for clearing logs.
os.system('bot.exe') #inbult windows cmd for executing the bot.exe
