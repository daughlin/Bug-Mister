from gpiozero import LED
from time import sleep


pump = LED(27)
pump.on()
sleep(10)

led = LED(17)
print ("on");
led.on()
sleep(4)
print ("off");
led.off()
pump.off()
