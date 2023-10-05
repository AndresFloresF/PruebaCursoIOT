from gpiozero import LED
from time import sleep


red = LED(17)

while True:
    print("Hola soy Andres")
    red.on()
    sleep(4)
    red.off()
    sleep(4)