from microbit import *
# Um den Maqueen Roboter zu steuern benutzen wir das maqueen-Modul.
import maqueen
import radio
radio.config(group=23)
radio.on()

# Hilfsvariabeln
# Bin ich ein Roboter oder eine Fernsteuerung?
amiarobot = True
# Läuft das Programm?
RUNNING = True

while RUNNING:
    # Knopfdrücke überprüfen
    if button_a.was_pressed():
        amiarobot = not amiarobot
    if button_b.was_pressed():
        maqueen.motor_stop_all()
        RUNNING = False

    # Der Roboter soll die Nachricht empfangen und je nachdem
    # Geschwindigkeit und Richtung anpassen
    if amiarobot:
        display.show('R')
        message = radio.receive()
        if message:
            list = message.split(":")
            speed = min(max(int(list[0]),-200),200) # Geschwindigkeit zwischen -200 und +200
            richtung = min(max(int(list[1]),-100),100) # Richtung zwischen -100 und +100
            speedL = speed*min(1,(richtung/100)+1)
            speedR = speed*min(1,(richtung/-100)+1)
            print(speedL, speedR)
            maqueen.set_motor(0,speedL)
            maqueen.set_motor(1,speedR)

    # Die Fernsteuerung soll die Beschleunigung messen und schicken
    else:
        display.show('F')
        x_strength = accelerometer.get_x()
        y_strength = -accelerometer.get_y()
        msg = str(y_strength//8)+":"+str(x_strength//20)
        print(msg)
        radio.send(msg)

    # Wir schlafen ein bisschen
    sleep(100)

