from gpiozero import LED
from time import sleep


red = LED(17)

while True:
    print("Hola clase! sin errores");
    red.on()
    sleep(1)
    red.off()
    sleep(1)