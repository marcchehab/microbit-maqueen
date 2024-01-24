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
            strength = int(message)
            maqueen.set_motor(0,strength)
            maqueen.set_motor(1,strength)

    # Die Fernsteuerung soll die Beschleunigung in Y-Richtung
    # messen und schicken
    else:
        display.show('F')
        y_strength = accelerometer.get_y()
        radio.send(str(y_strength//10))

    # Wir schlafen ein bisschen
    sleep(100)

