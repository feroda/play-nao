
import serial

possible_devices = [
	'/dev/ttyACM0',
	'/dev/ttyACM1',
	'/dev/ttyACM2',
	'/dev/ttyACM3'
]

for device in possible_devices:
	ser = serial.Serial(port=device, 
		baudrate=9600, bytesize=serial.EIGHTBITS, 
		parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
	print("Serial device %s opened" % device)
	break


ser.readline()
while True:
    dataIn=ser.readline()
    print(dataIn)
