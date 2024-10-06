import os

class Config:
    DEVICE_ID = os.getenv('DEVICE_ID', 'default-device-id')
    BACKEND_API_BASE_URL = os.getenv('BACKEND_API_BASE_URL', 'http://localhost:5000')

    API_ENDPOINTS = {
        'register_device': f"{BACKEND_API_BASE_URL}/register-device",
        'mail_event': f"{BACKEND_API_BASE_URL}/mail-event",
        'unlock_mailbox': f"{BACKEND_API_BASE_URL}/unlock-mailbox",
        'update_password': f"{BACKEND_API_BASE_URL}/update-password",
        'device_status': f"{BACKEND_API_BASE_URL}/device-status",
    }

    IMAGE_STORAGE_PATH = os.getenv('IMAGE_STORAGE_PATH', './images/')

    SENSOR_PIN = 25
    RELAY_PIN = 26 
    LED_PIN = 23

    CAMERA_RESOLUTION = (1024, 768)

    REQUEST_TIMEOUT = 10

    LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', './logs/device.log')
    LOG_LEVEL = 'INFO'
