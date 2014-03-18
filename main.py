import serial
import sys


def main(argv):
    port = argv[0] 
    ser = serial.Serial(port,timeout=30)
    print "Monitoring %s" % ser.name

    while True:
        line = ser.readline()
        if not line:
            break

	(temp, humid) = map(float, line.split())
        print "Temp: %.1f, Humidity: %.1f" % (temp, humid)

    ser.close()


if __name__ == '__main__':
    main(sys.argv[1:]);

