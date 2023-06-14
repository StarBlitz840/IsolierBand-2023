from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Remote
from pybricks.parameters import Button
from pybricks.parameters import Port, Direction
from pybricks.robotics import GyroDriveBase
# from pybricksdev.connections import PybricksHub
# from pybricksdev.ble import find_device


leftW = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightW = Motor(Port.F)
CS = ColorSensor(Port.D)
wheels = GyroDriveBase(leftW,rightW,56,135)

kp = 2.17
SPEED = 65
error = 0
BLACK = 12
WHITE = 87
CONST = 70
target = (BLACK + WHITE) / 2

shtrongolong = 1.7
spid_minus = 5

print(CS.reflection())
while True:

    error = CS.reflection() - target


    # while CS.reflection <= target:    
        # leftW.dc(SPEED + 10)
        # rightW.dc(SPEED)
    if error < CONST:
        leftW.dc(shtrongolong*((SPEED - spid_minus) - error * kp))
        rightW.dc(shtrongolong*((SPEED - spid_minus) + error * kp))
    elif error > - CONST:
        rightW.dc(shtrongolong*((SPEED - spid_minus) + error * kp))
        leftW.dc(shtrongolong*((SPEED - spid_minus)  - error * kp))
    else:
        rightW.dc((SPEED))
        leftW.dc((SPEED))

    


