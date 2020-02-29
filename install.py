import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install Ez-Tool [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #root : sudo -sH
          if os.path.exists(system.conf_dir+"/Ez-Tool"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Ez-Tool")
          os.system(system.sudo+" cp -r modules core Ez-Tool.py "+system.conf_dir+"/Ez-Tool")
          os.system(system.sudo+" cp -r core/Ez-Tool "+system.bin)
          os.system(system.sudo+" cp -r core/eztool "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Ez-Tool")
          os.system(system.sudo+" chmod +x "+system.bin+"/eztool")
          os.system("cd .. && "+system.sudo+" rm -rf Ez-Tool")
          if os.path.exists(system.bin+"/Ez-Tool") and os.path.exists(system.conf_dir+"/Ez-Tool"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/Ez-Tool"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Ez-Tool")
          os.system("cp -r modules core Ez-Tool.py "+system.conf_dir+"/Ez-Tool")
          os.system("cp -r core/Ez-Tool "+system.bin)
          os.system("cp -r core/eztool "+system.bin)
          os.system("chmod +x "+system.bin+"/Ez-Tool")
          os.system("chmod +x "+system.bin+"/eztool")
          os.system("cd .. && rm -rf Ez-Tool")
          if os.path.exists(system.bin+"/Ez-Tool") and os.path.exists(system.conf_dir+"/Ez-Tool"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
#code by doz
#29.2.2020