#Importing os and randint from random
import os
from random import randint
#While True is used for the infinite loop.
while True:
    print("="*9,"MAIN MENU","="*9)
    print("1. Start the bot.") #Option no 1 to start the bot.
    print("2. Change the color of text.") #Option no 2 to change the color of cmd prompt text.
    print("3. Credits") #Credits menu.
    print("4. Exit") #Exit part of the code.
    print("="*30) 
    choice=int(input("Enter your choice : ")) #choice asking.
    if choice==1:
        print("Starting the bot.....") #Bot starting code.
        ntimes=int(input("Enter the number of box you want to fill in your contribution graph : ")) #It will fill the box of your contribution graph, according to user choice. 
        for i in range(6976,ntimes): #ntimes is selected by the number of boxes.
            for j in range(0, randint(1,10)):
                d = str(i) + ' day ago' #The string message that will get write in to the file.txt
                with open('file.txt', 'a') as file: #The writing part.
                    file.write(d)
                os.system('git add .') #Commiting the changes part.
                os.system('git commit --date="' + d + '" -m "commit"') #"commit" msg is configurable.
            os.system('git push -u origin main') #It will push the changes into the main repository
    elif choice==2:
        #Color coding part for the cmd prompt.
        print("=====COLOR MENU=====") 
        print("1. Blue ")
        print("2. Green")
        print("3. Aqua")
        print("4. Red")
        print("5. Purple")
        print("6. Yellow")
        print("7. White")
        print("8. Gray")
        print("9. Light Blue")
        print("10. Light Green")
        print("11. Light Aqua")
        print("12. Light Red")
        print("13. Light Purple")
        print("14. Light Yellow")
        print("15. Bright White")
        print("=======================")
        colchoice=int(input("Enter your color choice : ")) #it will ask user for choice.
        #for more information search about color coding in windows.
        if colchoice==1:
            print("Changing color to Blue...")
            os.system('color 1')
        elif colchoice==2:
            print("Changing color to Green...")
            os.system('color 2')
        elif colchoice==3:
            print("Changing color to Aqua...")
            os.system('color 3')
        elif colchoice==4:
            print("Changing color to Red...")
            os.system('color 4')
        elif colchoice==5:
            print("Changing color to Purple...")
            os.system('color 5')
        elif colchoice==6:
            print("Changing color to Yellow...")
            os.system('color 6')
        elif colchoice==7:
            print("Changing color to White...")
            os.system('color 7')
        elif colchoice==8:
            print("Changing color to Gray...")
            os.system('color 8')
        elif colchoice==9:
            print("Changing color to Light Blue...")
            os.system('color 9')
        elif colchoice==10:
            print("Changing color to Light Green...")
            os.system('color a')
        elif colchoice==11:
            print("Changing color to Light Aqua...")
            os.system('color b')
        elif colchoice==12:
            print("Changing color to Light Red...")
            os.system('color c')
        elif colchoice==13:
            print("Changing color to Light Purple...")
            os.system('color d')
        elif colchoice==14:
            print("Changing color to Light Yellow...")
            os.system('color e')
        elif colchoice==15:
            print("Changing color to Light White...")
            os.system('color f')
        else: #Else part of the colorcoding part.
            print("Wrong parameters.")
    elif choice==3: #Credit part.
        print("==============================================================")
        print("This code was originally coded by Rishab") #Don't Try to change it.
        print("Github Source : https://github.com/RISHAB-CREATOR/RgCommitBot/ ") #The real source of the code, make sure to follow me on github and star the repository too!
        print("Instagram : https://www.instagram.com/rishabnotfound/") #Make sure to follow me.
        print("Youtube : https://www.youtube.com/@Rishab07") #Make sure to subscribe :D.
        print("==============================================================")
    elif choice==4: #The terminating part.
        print("====================")
        print("Quitting the code now")
        print("====================")
        quit() #You can use break statement too, for breaking the loop.
    else: #Else part of the main menu.
        print("Wrong parameters.")
