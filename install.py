#!/usr/bin/pyhton

# IMPORTACIONES
import os, time
from colorama import Fore, Back, Style, init
init()

##################################################################
# By: Mr. Good                                                   #
# Canal de YouTube: https://www.youtube.com/c/MrGoodCanalOficial #
# Soy el creador de esta herramienta :v compartela               #  
#                                                                #
# Este script esta hecho con el fin de poder instalar            #
# todos los paquetes necesarios para el uso de nuestro           #
# sistema Linux :)                                               #
##################################################################


os.system("clear")
os.system("bash .install-menu.sh")

run = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)

# CONDICIONAL
if run == "run":
    os.system("clear")
    print('\nElije tu sistema :D')
    
    print(Fore.WHITE + Style.BRIGHT + "\n(1)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Termux" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "\n(2)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Kali, Ubuntu o Parrot" + Style.RESET_ALL)
    print('')
    #TERMUX
    sistema = int(input('>: '))
    os.system("clear")


    if sistema == 1:
        # ACTUALIZANDO REPOSITORIOS
        print(Fore.GREEN + Style.BRIGHT + "\nBuscando paquetes que faltan por actualizar...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("pkg update")
        time.sleep(1)
        
        
        print(Fore.GREEN + Style.BRIGHT + "\nActualizando los paquetes desactualizados...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("pkg upgrade -y")
        
        os.system("clear")
        
        # INSTALANDO PHP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando php...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install php -y")
        
        # INSTALANDO SSH/OPENSSH
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando ssh...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install openssh -y")
        
        # INSTALANDO PYTHON3
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando la ultima version de Python...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install python3 -y")
        
        # INSTALANDO PYTHON2
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando python2...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install python2 -y")
        
        # INSTALANDO COLORAMA
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando colorama...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pip install colorama")
        
        # INSTALANDO BASH
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando bash...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install bash -y")
        
        # INSTALANDO OPENSSL
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando openssl...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install openssl -y")
        
        # INSTALANDO GIT
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando git...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install git -y")
        
        # INSTALANDO CURL
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando curl...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install curl -y")
        
        # INSTALANDO UNZIP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando unzip...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install unzip -y")
        
        # INSTALANDO WGET
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando wget...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install wget -y")
        
        # INSTALANDO VIM
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando vim...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install vim -y")
        
        # INSTALANDO PROOT
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando proot...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install proot -y")
        
        # INSTALANDO RUBY
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando ruby...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install ruby -y")
        
        # INSTALANDO NANO
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando nano...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install nano -y")
        
        # INSTALANDO PROCPS
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando procps...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install procps -y")
        time.sleep(1)
        
        # INSTALANDO NMAP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando nmap...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install nmap -y")
        time.sleep(1)
        
        # INSTALANDO NSLOOKUP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando nslookup...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install dnsutils -y")
        time.sleep(1)

        # INSTALANDO FIGLET
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando figlet...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("pkg install figlet -y")
        time.sleep(1)
        
        os.system("clear")
        
        # ACTUALIZANDO TODOS LOS PAQUETES INSTALADOS
        print(Fore.GREEN + Style.BRIGHT + "\nBuscando actualizaciones de los paquetes que se instalaron...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("pkg update")
        
        
        print(Fore.GREEN + Style.BRIGHT + "\nActualizando los paquetes instalados...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("pkg upgrade -y")
        time.sleep(2)
        os.system("clear")
        
        # CREADOR :V
        print(Fore.WHITE + Style.BRIGHT + "\nCreado por" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + ":" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Mr. Good" + Style.RESET_ALL)
        
        # LISTA DE PAQUETES INSTALADOS
        print(Fore.BLUE + Style.BRIGHT + "\nLista de paquetes instalados:" + Style.RESET_ALL)

        print(Fore.GREEN + "\nphp" + Style.RESET_ALL)
        print(Fore.GREEN + "openssh" + Style.RESET_ALL)
        print(Fore.GREEN + "python3" + Style.RESET_ALL)
        print(Fore.GREEN + "python2" + Style.RESET_ALL)
        print(Fore.GREEN + "bash" + Style.RESET_ALL)
        print(Fore.GREEN + "openssl" + Style.RESET_ALL)
        print(Fore.GREEN + "git" + Style.RESET_ALL)
        print(Fore.GREEN + "curl" + Style.RESET_ALL)
        print(Fore.GREEN + "unzip" + Style.RESET_ALL)
        print(Fore.GREEN + "wget" + Style.RESET_ALL)
        print(Fore.GREEN + "vim" + Style.RESET_ALL)
        print(Fore.GREEN + "proot" + Style.RESET_ALL)
        print(Fore.GREEN + "ruby" + Style.RESET_ALL)
        print(Fore.GREEN + "nano" + Style.RESET_ALL)
        print(Fore.GREEN + "procps" + Style.RESET_ALL)
        print(Fore.GREEN + "nmap" + Style.RESET_ALL)
        print(Fore.GREEN + "nslookup" + Style.RESET_ALL)
        print(Fore.GREEN + "figlet" + Style.RESET_ALL)
        
        print(Fore.BLUE + Style.BRIGHT + "\nFecha de terminacion del script:" + Style.RESET_ALL)
        os.system("date")
        time.sleep(8)
        
        os.system("python nmap-mg.py")


    # KALI, UBUNTU O PARROT
    elif sistema == 2:

        os.system("clear")
        
        # ACTUALIZANDO REPOSITORIOS
        print(Fore.GREEN + Style.BRIGHT + "\nBuscando paquetes que faltan por actualizar...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("sudo apt-get update")
        time.sleep(1)
        
        
        print(Fore.GREEN + Style.BRIGHT + "\nActualizando los paquetes desactualizados...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("sudo apt-get upgrade -y")
        
        os.system("clear")
        
        # INSTALANDO PHP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando php...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install php -y")
        
        # INSTALANDO SSH/OPENSSH
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando ssh...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install openssh -y")
        
        # INSTALANDO PYTHON3
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando la ultima version de Python...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install python3 -y")
        
        # INSTALANDO PYTHON2
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando python2...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install python2 -y")
        
        # INSTALANDO COLORAMA
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando colorama...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo pip install colorama")
        
        # INSTALANDO BASH
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando bash...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install bash -y")
        
        # INSTALANDO OPENSSL
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando openssl...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install openssl -y")
        
        # INSTALANDO GIT
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando git...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install git -y")
        
        # INSTALANDO CURL
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando curl...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install curl -y")
        
        # INSTALANDO UNZIP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando unzip...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install unzip -y")
        
        # INSTALANDO WGET
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando wget...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install wget -y")
        
        # INSTALANDO VIM
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando vim...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install vim -y")
        
        # INSTALANDO PROOT
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando proot...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install proot -y")
        
        # INSTALANDO RUBY
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando ruby...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install ruby -y")
        
        # INSTALANDO NANO
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando nano...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install nano -y")
        
        # INSTALANDO PROCPS
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando procps...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install procps -y")
        time.sleep(1)
        
        # INSTALANDO NMAP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando nmap...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install nmap -y")
        time.sleep(1)
        
        # INSTALANDO NSLOOKUP
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando nslookup...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install dnsutils -y")
        time.sleep(1)

        # INSTALANDO FIGLET
        print(Fore.GREEN + Style.BRIGHT + "\nInstalando figlet...." + Style.RESET_ALL)
        time.sleep(1)
        os.system("sudo apt-get install figlet -y")
        time.sleep(1)
        
        os.system("clear")
        
        # ACTUALIZANDO TODOS LOS PAQUETES INSTALADOS
        print(Fore.GREEN + Style.BRIGHT + "\nBuscando actualizaciones de los paquetes que se instalaron...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("sudo apt-get update")
        
        
        print(Fore.GREEN + Style.BRIGHT + "\nActualizando los paquetes instalados...." + Style.RESET_ALL)
        time.sleep(2)
        os.system("sudo apt-get upgrade -y")
        time.sleep(2)
        os.system("clear")
        
        # CREADOR :V
        print(Fore.WHITE + Style.BRIGHT + "\nCreado por" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + ":" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Mr. Good" + Style.RESET_ALL)
        
        # LISTA DE PAQUETES INSTALADOS
        print(Fore.BLUE + Style.BRIGHT + "\nLista de paquetes instalados:" + Style.RESET_ALL)

        print(Fore.GREEN + "\nphp" + Style.RESET_ALL)
        print(Fore.GREEN + "openssh" + Style.RESET_ALL)
        print(Fore.GREEN + "python3" + Style.RESET_ALL)
        print(Fore.GREEN + "python2" + Style.RESET_ALL)
        print(Fore.GREEN + "bash" + Style.RESET_ALL)
        print(Fore.GREEN + "openssl" + Style.RESET_ALL)
        print(Fore.GREEN + "git" + Style.RESET_ALL)
        print(Fore.GREEN + "curl" + Style.RESET_ALL)
        print(Fore.GREEN + "unzip" + Style.RESET_ALL)
        print(Fore.GREEN + "wget" + Style.RESET_ALL)
        print(Fore.GREEN + "vim" + Style.RESET_ALL)
        print(Fore.GREEN + "proot" + Style.RESET_ALL)
        print(Fore.GREEN + "ruby" + Style.RESET_ALL)
        print(Fore.GREEN + "nano" + Style.RESET_ALL)
        print(Fore.GREEN + "procps" + Style.RESET_ALL)
        print(Fore.GREEN + "nmap" + Style.RESET_ALL)
        print(Fore.GREEN + "nslookup" + Style.RESET_ALL)
        
        print(Fore.BLUE + Style.BRIGHT + "\nFecha de terminacion del script:" + Style.RESET_ALL)
        os.system("date")
        time.sleep(8)
        
        os.system("python nmapMG.py")