import RPi.GPIO as GPIO
import time
from config import Config
from touchpad import input_password, set_new_pin
from backend.password_manager import verify_password, load_password

# Set up GPIO for solenoid lock
def setup_lock():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Config.RELAY_PIN, GPIO.OUT)
    print("Lock set up done")  # for debugging 


#Closes the solenoid lock.
def lock_close():
    print("Locking mailbox...")
    GPIO.output(Config.RELAY_PIN, GPIO.HIGH)

#Opens the solenoid lock.
def lock_open():
    print("Unlocking mailbox...")
    GPIO.output(Config.RELAY_PIN, GPIO.LOW)

#Handles locking/unlocking based on the correct password.
def handle_lock():
    stored_password = load_password()    # Load the stored (hashed) password from file
    if stored_password is None:
        print("No password found.")
        set_new_pin()
    
    else:
        # Ask the user to input the password
        if verify_password(input_password()):
            lock_open()
            print("Mailbox unlocked")
            time.sleep(5)  # Keep the lock open for 5 seconds
            lock_close()
            print("Mailbox locked")
        else:
            print("Incorrect password.")