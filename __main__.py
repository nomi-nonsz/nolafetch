import time
import sys, os, platform, socket, psutil, getpass, cpuinfo

def getNameComponent(index):
  comp = {}
  comp[1] = "  \ |        |          _ \    __| "
  comp[2] = " .  |   _ \  |   _` |  (   | \__ \ "
  comp[3] = "_|\_| \___/ _| \__,_| \___/  ____/ "
  comp[0] = "-"*len(comp[1])
  if index > 0 and index < 4:
    return "\033[1;36m" + (" "*4) + comp[index] + "\033[1;35m"
  
  return (" "*4) + comp[index]

def getHost():
  return " "*4 + f"\033[0;36m{getpass.getuser()}\033[0m@\033[0;36m{socket.gethostname()}\033[1;35m"

def getSystemInfo():
  uname = platform.uname()

  memory = psutil.virtual_memory()
  memory_used = str(round(memory.used / 1024 ** 2)) + "MB"
  memory_total = str(round(memory.total / 1024 ** 2)) + "MB"

  info = {}
  info['system'] = uname.system
  info['kernel'] = uname.release
  info['version'] = uname.version
  info['arch'] = uname.machine
  info['host'] = socket.gethostname()
  info['ip'] = socket.gethostbyname(socket.gethostname())
  info['processor'] = cpuinfo.get_cpu_info()['brand_raw']
  info['memory'] = f"{memory_used} / {memory_total}"
  return info

def printSystemInfo(name, key):
  info = getSystemInfo()
  return " "*4 + f"\033[1;35m{name}: \033[0m{info[key]}\033[1;35m"

def getMotd():
  return f"""\033[1;35m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠶⠿⠛⠛⠻⡶⠾⠟⠛⠛⠛⠻⠷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{getHost()}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀{getNameComponent(0)}
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀{getNameComponent(1)}
⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠀⠀⠀⠀⠀⠀{getNameComponent(2)}
⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀{getNameComponent(3)}
⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀{getNameComponent(0)}
⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀{printSystemInfo('Processor', 'processor')}
⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⢠⡿⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀
⠀⠀⠀⣼⠇⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀
⠀⠀⢰⡿⠀⠀⠀⠀⠀⣻⡇⣀⣤⡶⠿⠻⣿⣆⠀⠀⠀⠀⢸⣇⠀⠛⠛⠛⠛⠳⣺⣿⡀⠀⠀⢠⣄⠀⠀⠘⣷⡀⠀
⠀⠀⣾⠃⠀⠀⠀⠀⠀⣿⡿⠿⣧⣤⣤⣴⠿⠛⠷⣦⣤⣤⣼⣿⣦⣤⣤⣤⣤⣶⠟⢹⣧⠀⠀⠈⢻⡆⠀⠀⠹⣧⠀
⠀⣸⡟⠀⠀⢀⡀⠀⠀⣿⡃⠀⠀⠀⣀⣤⣶⣶⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠈⢿⡄⠀⠀⢻⡇
⢠⡿⠀⠀⠀⣾⠃⠀⠀⢽⡇⢠⣶⠟⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⡶⠋⠀⢸⣇⠀⠀⠀⢸⣧⠀⠀⠈⣿
⣼⡇⠀⠀⢀⣿⠀⠀⠀⢺⡇⠀⠀⠀⠘⢿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⣿⠀⠀⠀⣿
⢹⡇⠀⠀⢸⣿⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣿⠀⠀⣰⡟
⠈⢿⡄⠀⠸⣿⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠶⣦⣶⠾⠛⠛⠛⠛⠉⠀⠀⠀⢀⣠⣾⣿⠀⠀⠀⠀⣿⣤⡾⠋⠀
⠀⠈⢻⣆⠀⣿⡀⠀⠀⠀⢸⣧⣤⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣤⣴⡶⠾⠛⠉⢸⡏⠀⠀⠀⣰⡟⠁⠀⠀⠀
⠀⠀⠀⠙⢷⣽⣇⠀⠀⠀⠀⢿⡌⠉⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀⣀⣴⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢻⣆⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣤⣀⣘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

\033[0m
NolaOS v1.0.2-ginger
Copyright 2021 (c) Norman Andrians
 
"""

def run():
  print("Starting Nola motd with fetch...")

  motd = getMotd()

  os.system("clear")

  for p in motd:
    print(p, end='')
    sys.stdout.flush()
    time.sleep(0.00001)

if __name__ == '__main__':
  run()