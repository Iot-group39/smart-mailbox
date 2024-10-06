from picamera2 import Picamera2
import time
import RPi.GPIO as GPIO
from config import Config
import requests

# Initialize the camera
camera = picamera2.Picamera2()

#Sets up the GPIO for the sensor and camera
def setup_camera():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Config.SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Config.LED_PIN, GPIO.OUT) 

    print("Camera set up is done")  # for debugging 

#Checks if the sensor is triggered (beam interrupted).
def is_sensor_triggered():
    return GPIO.input(Config.SENSOR_PIN) == GPIO.LOW

#Captures an image using the Pi Camera.
def capture_image():
    GPIO.output(LED_LIGHT_PIN, GPIO.HIGH)  # Turn on LED
    print("Capturing image...")
    camera.start()
    time.sleep(2)  
    camera.capture_file(Config.IMAGE_STORAGE_PATH)
    camera.stop()
    GPIO.output(LED_LIGHT_PIN, GPIO.LOW)  # Turn off LED

    print(f"Image saved at {Config.IMAGE_STORAGE_PATH}")

#Sends the captured image to the backend.
def send_image_to_backend():
    url = Config.API_ENDPOINTS['mail_event']
    files = {'file': open(Config.IMAGE_STORAGE_PATH, 'rb')}
    data = {'device_id': Config.DEVICE_ID}

    try:
        response = requests.post(url, files=files, data=data, timeout=Config.REQUEST_TIMEOUT)
        response.raise_for_status()
        print(f"Image sent to backend successfully: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send image: {e}")