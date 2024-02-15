import os
from random import randint

os.system('color a')
while True:
    print("="*9,"MENU","="*9)
    print("1. Start the bot.")
    print("2. Change the color of text.")
    print("3. Credits")
    print("4. Exit")
    print("="*24)
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("Starting the bot.....")
        ntimes=int(input("Enter the number of box you want to fill in your contribution graph : "))
        for i in range(0,ntimes):
            for j in range(0, randint(1,10)):
                d = str(i) + ' day ago'
                with open('file.txt', 'a') as file:
                    file.write(d)
                os.system('git add .')
                os.system('git commit --date="' + d + '" -m "commit"')
            os.system('git push -u origin main')
    elif choice==2:
        print("=====MENU=====")
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
        print("15. Light Yellow")
        print("16. Bright White")
        print("==============")
        colchoice=int(input("Enter your color choice : "))
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
        else:
            print("Wrong parameters.")
            
