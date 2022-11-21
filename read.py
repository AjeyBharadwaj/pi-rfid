import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from datetime import datetime

reader = SimpleMFRC522()

while True:
    try:
        id, text = reader.read()
        print(f"{id} : {text} : {datetime.now()}")
    except Exception as e:
        print(f"Exception {e}")
