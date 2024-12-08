import BlynkLib
from time import sleep
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
from urllib.parse import urlparse
from datetime import datetime
from capture_image_usb import captureImagePath
from upload_image import upload_image

# initiate SenseHat
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = 'bNfDoU1l_1iSHEIBZrzzGdpa_VtC6rhv'
# Initialize the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)


IMAGE_PATH="./images/busted_image.jpg"

# parse mqtt url for connection details
URL = urlparse("mqtt://broker.emqx.io:1883/AndreaNardinocchi/home/cameras/cam1")
BASE_TOPIC = URL.path[1:]

# MQTT event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
         print("Connected successfully")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message ID: {mid} published successfully")

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")
    if rc != 0:
        print("Unexpected disconnection. Reconnecting...")
        client.reconnect()

mqttc = mqtt.Client()

# check if useame and password in the url (there isn't in this basic example)
if (URL.username):
    mqttc.username_pw_set(URL.username, URL.password)

# Connect
mqttc.connect(URL.hostname, URL.port)
mqttc.loop_start()


blynk.log_event('email_sent')
current_time = datetime.now()
sense.clear(255,255,255)
captureImagePath(IMAGE_PATH)
result = print(f'Email sent off to your mum with your picture, and now you got yourself in trouble if you are still on your desk...') 
blynk.set_property(0,"urls", result) 
message = f"Photo taken at {current_time:%H:%M} | url: {upload_image(IMAGE_PATH)}"
mqttc.publish(BASE_TOPIC, message)
print("Message published:", message)
    
sleep(1) # This makes the countdown work

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    
    try:
        while True:
            blynk.run() # Process Blynk events
            sleep(2)  # Add a short delay to avoid high CPU usage

    except KeyboardInterrupt:
        print("Blynk application stopped.")

