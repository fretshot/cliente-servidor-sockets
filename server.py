
import socket

# Intantianre object s to work with sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind works to head conections. use " " to hear any IP conection in that port.  
s.bind(("", 9999))
 
# Accept just 1 conection in the socket
s.listen(1)
 
#Instantiate object sc. s.accept  return 2 values, IP and Port from new conection
sc, addr = s.accept()
 
while True:

	try:
		#Receiving client messages. Method recv receive data and 1024 is the amount of bytes
		recibido = sc.recv(1024).decode()
		print(str(addr),": ",recibido)

		if recibido == "close":
			#break the while bucle
			break
		
		if recibido == "hello":
			print("Comando recibido!")    	
		
	except Exception as e:
		print("Ha ocurrido un error ",e)
		break

print ("Adios.")
 
sc.close()
s.close()