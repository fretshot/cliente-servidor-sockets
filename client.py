 
import socket
from time import gmtime, strftime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
while True:
	try:
		ip = input("Ingrese la IP del servidor: ")
		s.connect((ip, 9999))
		break
	except Exception as e:
		print("\n>> Imposible conectar...")
		

while True:
	
	localtime = strftime("%H:%M:%S", gmtime())
	mensaje = input("Mensaje: ")

	s.send(mensaje.encode())
	
	if mensaje == "close":
		break

print ("\n\tAdios.")
s.close()