# Eetu Kyrönlahti
# 18.10.2026
# Focarin funktiot

# Lisätään laitteen pinnit
from machine import Pin, PWM

# Lisätään aikamoduulista sleep
from time import sleep

# Moottori A pinnien lisääminen
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B pinnien lisääminen
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# Lisätään ledin kontrollointi
led = Pin("LED", Pin.OUT)

# Määritellään liikkumisen ja ledin funktiot

def eteenpain(nopeus = 49181, aika = 4):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    

def taaksepain(nopeus = 49181, aika = 4):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    
    
def vasemmalle(nopeus = 60000, nopeus2 = 16200, aika = 2):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus2)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    

def oikealle(nopeus = 60000, nopeus2 = 16200, aika = 2):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus2)
    e2.duty_u16(nopeus)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    

def ledpaalle(aika = 1):
    led.on()
    sleep(aika)
    led.off()

