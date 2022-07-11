import os
import sys
print("this is debian based os only")
if input("Continue (Y/N)") != "Y":
    print("Aborted.")
    sys.exit(1)
os.system('apt install -y neofetch') 
os.system('neofetch')
print("here is your distro")
os.system('apt install -y xfce4')
os.system('apt install -y golang')
print("okay its installed now")
