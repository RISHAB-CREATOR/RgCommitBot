import os
from random import randint

os.system('color a')
for i in range(1,1000):

    for j in range(0, randint(1,10)):
        d = str(i) + ' day ago'
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

    os.system('git push -u origin main')
