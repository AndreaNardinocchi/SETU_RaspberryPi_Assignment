import os
 
def captureImagePath(path):
    print("Picture taken!!!\n")
    # https://www.raspberrypi.com/documentation/computers/camera_software.html#use-a-usb-webcam
    os.system(f"fswebcam {path}") # --no-banner
        
if __name__ == "__main__":
    captureImagePath("./images/image.jpg")

