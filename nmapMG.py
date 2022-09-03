#!/usr/bin/python

# IMPORTANDO LOS MODULOS
import os, time, subprocess
from colorama import Fore, Back, Style, init
init()

##################################################################
# By: Mr. Good                                                   #
# Canal de YouTube: https://www.youtube.com/c/MrGoodCanalOficial #
# Soy el creador de esta herramienta :v compartela               #  
#                                                                #
# Este script esta hecho con el fin de poder escanear            #
# redes con nmap de manera facil :)                              #
##################################################################

os.system("clear")
os.system("bash .menu-nmap.sh")

print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)

# ****************************************************************************************************
# MENU
print (Fore.WHITE + Style.BRIGHT + "\n(1)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escaneo basico a un target" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(2)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear tu router" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(3)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Mostrar todos los dispostivos conectados a tu router" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(4)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear un puerto en especial de un target" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(5)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Ver la version de los protocolos de un target" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(6)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Ver la ruta por la que pasa una WEB" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(7)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear los puertos importante de un target" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(8)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Ver posibles vulnerabilidades de un target" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(9)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Detectar sistema operativo del target" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(10)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear archivo con lista de target" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(11)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Sacar IP de pagina WEB" + Style.RESET_ALL)
print (Fore.WHITE + Style.BRIGHT + "(0)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " Salir" + Style.RESET_ALL)


# OPCION

print (Fore.WHITE + Style.BRIGHT + Back.BLUE + "\n Elije una opcion. Ej: 11" + Style.RESET_ALL)
opcion = int(input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL))

# ****************************************************************************************************
# CONDICIONAL NUMERO 1
if opcion == 1:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(1)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escaneo basico a un target" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce el objetivo para escanear. Ej: ip o www.example.com" + Style.RESET_ALL)

	target = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap "+ target)
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 2
elif opcion == 2:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(2)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear tu router" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la IP de tu router. EJ: 1xx.1xx.xx.255" + Style.RESET_ALL)

	target_router = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap "+target_router+"/24")
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 3
elif opcion == 3:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(3)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Mostrar todos los dispostivos conectados a tu router" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce tu IP" + Style.RESET_ALL)

	my_ip = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap -sn "+my_ip+"/24 -oG -")
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 4
elif opcion == 4:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(4)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear un puerto en especial de un target" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la IP o WEB del target" + Style.RESET_ALL)
	ip_target = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	print (Fore.GREEN + Style.BRIGHT + "Introduce el puerto a escanear" + Style.RESET_ALL)
	ip_target_port = input(Fore.WHITE + Style.BRIGHT + ">> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap -p "+" "+ip_target_port+" "+ip_target)
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 5
elif opcion == 5:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(5)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Ver la version de los protocolos de un target" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la IP o WEB" + Style.RESET_ALL)

	target_ip_web = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap -Pn "+target_ip_web)
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 6
elif opcion == 6:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(6)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Ver la ruta por la que pasa una WEB" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la IP o WEB" + Style.RESET_ALL)

	ruta_target = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap -vv "+ruta_target+"-225")
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 7
elif opcion == 7:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(7)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear los puertos importante de un target" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la IP o WEB" + Style.RESET_ALL)
	port_importante = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la escala. EJ: 1-100" + Style.RESET_ALL)
	escala = input(Fore.WHITE + Style.BRIGHT + ">> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap -top-ports "+escala+" "+port_importante)
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 8
elif opcion == 8:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(8)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Ver posibles vulnerabilidades de un target" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la IP o WEB" + Style.RESET_ALL)

	vuln_target = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap -Pn --script vuln "+vuln_target)
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 9
elif opcion == 9:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(9)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Detectar sistema operativo del target" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la IP o WEB" + Style.RESET_ALL)

	the_target = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nmap -O "+the_target)
	os.system("sudo nmap -O "+the_target)
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 10
elif opcion == 10:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(10)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Escanear archivo con lista de target" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nElije :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(1)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Usar archivo existente" + Style.RESET_ALL)

	new_option = int(input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL))

	if new_option == 1:
		print(Fore.RED + Style.BRIGHT + "\nMueve el archivo dentro del directorio de la herramienta Nmap-MG" + Style.RESET_ALL)
	
		print(Fore.WHITE + Style.BRIGHT + "\nIntroduce el nombre del archivo para reconocerlo. Ej: file.txt " + Style.RESET_ALL)
		
		name_file = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
		os.system("clear")
		print('')
		os.system("nmap -iL "+name_file)
	
	
# ****************************************************************************************************
# CONDICIONAL NUMERO 11
elif opcion == 11:
	os.system("clear")
	os.system("bash .menu-nmap.sh")
	print(Fore.BLUE + Style.BRIGHT + "   Nmap-MG" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " es lo mismo que" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Nmap" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " pero de\n   manera sencilla y atuomatizada :)" + Style.RESET_ALL)
	
	print (Fore.WHITE + Style.BRIGHT + "\n(11)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Sacar IP de pagina WEB" + Style.RESET_ALL)
	
	print (Fore.GREEN + Style.BRIGHT + "\nIntroduce la WEB" + Style.RESET_ALL)

	ip_web = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system("clear")
	print('')
	os.system("nslookup "+ip_web)
	
	
else:
	os.system("clear")
