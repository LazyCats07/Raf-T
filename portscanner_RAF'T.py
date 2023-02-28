
# Import Library
import socket    # Digunakan untuk berkomunikasi dengan mesin lain menggunakan protokol TCP dan UDP 
import termcolor # Mencetak beberapa pernyataan dalam warna yang berbeda 
from pyfiglet import figlet_format

#AsCII Art
print("\n")
print(figlet_format("R A F ' T", font="colossal"))

# Process
def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports): # Akan melakukan pengulangan dari jumlah inputan yang di isi 
		scan_port(target, port)

def scan_port(ipaddress, port):
	try : 
		# try to menginisasi objek socket  
		sock = socket.socket()
		# terhubung ke port tertentu pada alamat IP tertentu yang akan ditentukan nanti. 
		sock.connect((ipaddress, port)) 
		# Menampilkan atau print hasil dari fungsi di atas 
		print("\t[+] Port Terbuka " + str(port))
		# Setelah berhasil menyelesaikan suatu tindakan, seperti menemukan port terbuka, Kita bisa menutup objek socket
		sock.close()
	except : # Jika tidak berhasil terhubung, maka itu akan melanjutkan ke pernyataan "Except" yang akan melakukan print  "Port Tertutup"
			# print("[-] Port Closed " + str(port))
  			pass

# Bagian Input 
# Input Target IP
print("Ex : 192.168.1.1-192.168.1.5")	 
targets = input("[*] Enter Targets to Scan (Split them by - ): ")
# input Jumlah target port
ports = int(input("[*] Enter How Many Ports You Want to Scan: "))

if '-' in targets:
	print(termcolor.colored(("[*]Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split('-'):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)

