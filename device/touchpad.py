import RPi.GPIO as GPIO
import time
from backend.password_manager import verify_password, store_password, load_password

P1 = 4
P2 = 3
P3 = 2
P4 = 18
P5 = 17
P6 = 15
P7 = 14

# Key mapping 
KEY = {
    (18, 4): "1",
    (18, 3): "2",
    (18, 2): "3",
    (17, 4): "4",
    (17, 3): "5",
    (17, 2): "6",
    (15, 4): "7",
    (15, 3): "8",
    (15, 2): "9",
    (14, 4): "*",
    (14, 3): "0",
    (14, 2): "#",
}

last = None

# Scanning the keypad
def scan():
    global last
    keys = []

    for col in [P1, P2, P3]:
        GPIO.output(col, GPIO.HIGH)
        for row in [P4, P5, P6, P7]:
            if GPIO.input(row):
                key = KEY[(row, col)]
                keys.append(key)
        GPIO.output(col, GPIO.LOW)

    if len(keys) != 1:
        last = None
        return None

    (key,) = keys
    if last == key:
        return None

    last = key
    return key


# Touchpad setup function
def setup_touchpad():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(P1, GPIO.OUT)
    GPIO.setup(P2, GPIO.OUT)
    GPIO.setup(P3, GPIO.OUT)

    GPIO.setup(P4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(P5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(P6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(P7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("Touchpad set up and ready to use.")

# Handle pin input
def input_password():
    password = ""
    while True:
        char = scan()
        if char:
            if char == "#":  # Input '#' to finish entering the password
                break
            elif char.isdigit():  # Only accept digits as password characters
                password += char
            print(f"Password so far: {password}")  # Debugging step to show progress
        time.sleep(0.1)
    return password


# Function to set a new PIN
def set_new_pin():
    print("Please enter a new PIN:")
    new_password = input_password()
    print("Please re-enter the new PIN for confirmation:")
    confirm_password = input_password()

    if new_password == confirm_password:
        store_password(new_password)  # Store the new PIN in the db
        print("New PIN set successfully.")
    else:
        print("PINs did not match. Please try again.")

# Handles resetting the PIN
def reset_pin():
    stored_password = load_password()
    if stored_password is None:
        print("No PIN found. Please set a new one.")
        set_new_pin()
        return
    
    # Verify the existing PIN first
    print("Enter your current PIN to reset:")
    if verify_password(input_password()):
        print("PIN verified. Proceeding to set a new PIN.")
        set_new_pin()  # Call to reset the PIN
    else:
        print("Incorrect PIN. Cannot reset.")
