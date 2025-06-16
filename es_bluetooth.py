from pybricks.hubs import EssentialHub, ThisHub

from pybricks.pupdevices import Motor, ColorSensor, ColorLightMatrix
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = EssentialHub()
hub = ThisHub(observe_channels=[1])

colors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.VIOLET, Color.MAGENTA]

while True:

    data = hub.ble.observe(1)

    if data is not None:
        
        print(colors[data])
        hub.light.on(colors[data])

        wait(2000)

