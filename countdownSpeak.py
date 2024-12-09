from sense_hat import SenseHat
import time
import pyttsx3

# source: https://codefather.tech/blog/text-to-speech-in-python/ 
# source: https://projects.raspberrypi.org/en/projects/countdown-timer/2
# One time initialization
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

sense = SenseHat()

R = (200, 0, 0)
B = (0, 127, 255)
G = (0, 200, 0)
X = (0, 0, 0)
W = (255,255,255)


def countdownSpeak():

    for i in range(30, -1, -1):
        sense.set_rotation(180) 
        if i >15:
            from digitalClock import clock
            clock()        
        elif i>12 :
           sense.clear(B)
        elif i > 9 :
           sense.clear(R)
        elif i >= 4 :
            text = R
            bg = W
            sense.show_letter(str(i), text, bg)
        else:
            text = G
            bg = X
            sense.show_letter(str(i), text, bg)
        time.sleep(1)


    for i in range(7, -1, -1):
        if i>0:
            sense.show_message("BOOM!!!!", scroll_speed=0.03, text_colour=[255, 255, 255])
            bg = X 
            # Speaking
            engine.say("Andrea shut that freaking laptop, and get the hell out of here now")
            # Flush the say() queue and play the audio
            engine.runAndWait()
            # Program will not continue execution until
            # all speech is done talking
            time.sleep(0.1) 
        elif i<=0:
            sense.clear(255,255,255)
            from music import patMusicOn
            patMusicOn()
            time.sleep(0.1) 
        else:
            sense.clear(255,255,255)

sense.clear()
    









    # time.sleep(0.1) 
           # for i in range(350, -1, -1):
            #    if i > 5: