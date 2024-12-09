from animationColors import animatedLights
from threading import Thread
from sense_hat import SenseHat
import os
# https://www.geeksforgeeks.org/randomly-select-elements-from-list-without-repetition-in-python/ to randomly pick a Pat song from th list
# importing the required module
import random

sense = SenseHat()

# https://forums.raspberrypi.com/viewtopic.php?t=235173
t1 = Thread(target=animatedLights)
threads = [t1]

# creating variables
pat1 = 'PatMethenyGroup_FollowMe_live.mp3'
pat2 = 'PatMethenyGroup_IntoTheDream.mp3'
pat3 = 'Pat_Metheny_Group_-_Last_Train_Home.mp3'

# list of items
List = [pat1, pat2, pat3]

# mpg 321 installation https://installati.one/install-mpg321-debian-11/
try: 
    def patMusic():
        print("Pat is on!!!\n")
        os.system(f"mpg321 {random.choice(List)}") 
        os.system("python blynkingMail.py")
    
except KeyboardInterrupt:
    os.clear()

# https://forums.raspberrypi.com/viewtopic.php?t=235173
t2 = Thread(target=patMusic)
threads += [t2]

t1.start()
t2.start()

try: 
    def patMusicOn():
        
        for tloop in threads:
            tloop.join()

except KeyboardInterrupt:
    os.clear()

if __name__ == "__main__":
    result = patMusicOn()
    print("Pat is on!!!\n")