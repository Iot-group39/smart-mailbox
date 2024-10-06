from camera import setup_camera, is_sensor_triggered, capture_image, send_image_to_backend
from backend.password_manager import store_password, load_password
from lock import setup_lock, handle_lock
from touchpad import setup_touchpad, scan, reset_pin
import RPi.GPIO as GPIO
import time

def main():
    try:
        # Set up the camera, sensor, solenoid lock, and touchpad
        setup_camera()
        setup_lock()
        setup_touchpad()

        print("Waiting for mail detection...")

        while True:
            #Monitor the sensor trigger
            if is_sensor_triggered():
                print("Mail detected, capturing image...")
                capture_image()
                send_image_to_backend()
                time.sleep(5)  # Prevent immediate re-triggering
            
            # Monitor the touchpad trigger 
            char = scan()
            if char == "*":  # Initiates password entry/checking
                print(f"Key detected: {char}, Checking password...")
                handle_lock()  # Handle locking and unlocking the mailbox with the touchpad
            
            elif char == "*#":  # Initiates the reset PIN process
                print(f"Key detected: {char},Resetting PIN...")
                reset_pin()  # Handles the process to reset the PIN

            
            time.sleep(5)  # Prevent immediate re-triggering

    except KeyboardInterrupt:
        print("Program interrupted")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()