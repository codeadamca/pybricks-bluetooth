from pybricks.hubs import InventorHub, ThisHub

from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from urandom import randint

# from pybricks.iodevices import XboxController

hub = InventorHub()
hub = ThisHub(broadcast_channel=39)

colors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.VIOLET, Color.MAGENTA]

while True:

    rand = randint(0, 7)
    
    print(colors[rand])
    hub.ble.broadcast(rand)

    hub.light.on(colors[rand])

    wait(2000)
