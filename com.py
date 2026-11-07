from pycomm3 import CIPDriver

HOST = "154.57.164.77"
PORT = 38166

with CIPDriver(f"{HOST}:{PORT}") as plc:
	response = plc.generic_message(
		service=0x0E,
		class_code=0x6B,
#		class_code=0xAB, works also
		instance=1,
		attribute=1
	)
	print(response.value)
