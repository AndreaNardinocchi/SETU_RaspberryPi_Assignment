from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

# Define colors RGB
r = (255, 0, 0)
n = (0, 255, 0)
b = (0, 0, 255)
g = (120, 120, 120)
x = (255, 255, 255)
y = (0, 0, 0)



# Define the frames

frame1 = [
    y, r, r, r, r, r, r, y,
    y, r, r, r, r, r, r, r,
    y, r, r, y, y, y, r, r,
    y, r, r, r, r, r, r, r,
    y, r, r, r, r, r, r, y,
    y, r, r, y, y, y, y, y,
    y, r, r, y, y, y, y, y,
    y, r, r, y, y, y, y, y,
]

frame2 = [
    y, g, g, g, g, g, g, y,
    y, g, g, g, g, g, g, y,
    y, g, g, y, y, g, g, y,
    y, g, g, g, g, g, g, y,
    y, g, g, g, g, g, g, y,
    y, g, g, y, y, g, g, y,
    y, g, g, y, y, g, g, y,
    y, g, g, y, y, g, g, y,
]

frame3 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    y, y, y, b, b, y, y, y,
    y, y, y, b, b, y, y, y,
    y, y, y, b, b, y, y, y,
    y, y, y, b, b, y, y, y,
    y, y, y, b, b, y, y, y,
    y, y, y, b, b, y, y, y,
]

frame4 = [
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
]

frame5 = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
]

frame6 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

frame7 = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
]

frame8 = [
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
]

try:
    # Display the frames in a loop
    def animatedLights():
        while True:
            sense.set_rotation(180) 
            sense.set_pixels(frame1)
            time.sleep(0.5)
            sense.set_pixels(frame2)
            time.sleep(0.5)
            sense.set_pixels(frame3)
            time.sleep(0.5)
            sense.set_pixels(frame4)
            time.sleep(0.5)
            sense.set_pixels(frame5)
            time.sleep(0.5)
            sense.set_pixels(frame6)
            time.sleep(0.5)
            sense.set_pixels(frame7)
            time.sleep(0.5)
            sense.set_pixels(frame8)
            time.sleep(0.5)


except KeyboardInterrupt:
    sense.clear()

if __name__ == "__main__":
    result = animatedLights()