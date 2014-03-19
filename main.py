import serial
import sys
import time
from controls import FanController

def main(argv):
    port = argv[0] 
    ser = serial.Serial(port,timeout=30)
    print "Monitoring %s" % ser.name

    with FanController() as fans:

        fans.fan_off(FanController.ONE)
        fans.fan_off(FanController.TWO)
        fans.fan_off(FanController.THREE)
        fans.fan_off(FanController.FOUR)

	time.sleep(6)

        fans.fan_on(FanController.ONE)
        fans.fan_on(FanController.TWO)
        fans.fan_on(FanController.THREE)
        fans.fan_on(FanController.FOUR)
        while True:
            line = ser.readline()
            if not line:
                break

	    (temp, humid) = map(float, line.split())
            print "Temp: %.1f, Humidity: %.1f" % (temp, humid)

    ser.close()


if __name__ == '__main__':
    main(sys.argv[1:]);

