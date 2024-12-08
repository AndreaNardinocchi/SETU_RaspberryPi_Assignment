import os
 
def captureImagePath(path):
    print("Picture taken!!!\n")
    os.system(f"fswebcam {path}") # --no-banner
        
if __name__ == "__main__":
    captureImagePath("./images/image.jpg")

