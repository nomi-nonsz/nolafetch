import time
from datetime import datetime
import sys, os, platform, socket, psutil, getpass, cpuinfo, lsb_release
import psutil._psutil_linux, subprocess
import pyautogui


BOLD_ICON = False
BOLD_ICON_CHAR = "\033[1;35m" if BOLD_ICON == True else "\033[0;35m"

def getNameComponent(index):
  comp = {}
  comp[1] = "  \ |        |          _ \    __| "
  comp[2] = " .  |   _ \  |   _` |  (   | \__ \ "
  comp[3] = "_|\_| \___/ _| \__,_| \___/  ____/ "
  comp[0] = "-"*len(comp[1])
  if index > 0 and index < 4:
    return "\033[1;36m" + (" "*4) + comp[index] + BOLD_ICON_CHAR
  
  return (" "*4) + comp[index]

def get_host():
  return " "*4 + f"\033[0;36m{getpass.getuser()}\033[0m@\033[0;36m{platform.node() + BOLD_ICON_CHAR}"

def get_product_name() -> str:
  path_name = '/sys/devices/virtual/dmi/id/product_name'
  path_ver = '/sys/devices/virtual/dmi/id/product_version'

  if os.path.isfile(path_name) and os.path.isfile(path_ver):
    product_name = open(path_name, 'r').read().strip()
    product_version = open(path_ver, 'r').read().strip()
    return f"{product_name} - {product_version}"
  
  return "Not Supported"

def get_boottime() -> str:
  uptimestp = psutil.boot_time()
  uptime = datetime.fromtimestamp(uptimestp)
  return f"{uptime.hour} Hours {uptime.minute} Mins"

def get_uptime():
  f_uptime_raw = open('/proc/uptime').readline()
  f_uptime_sec = float(f_uptime_raw.split()[0])

  uptime = {}
  uptime['hour'] = int(f_uptime_sec / 3600)
  uptime['mins'] = int((f_uptime_sec % 3600) / 60)

  return uptime

def get_packages():
  packages = {}
  packages['dpkg'] = int(subprocess.check_output('dpkg --list | wc -l', shell=True).strip()) - 1
  packages['snap'] = int(subprocess.check_output('snap list --all | wc -l', shell=True).strip())
  return packages

def get_shell():
  return os.path.realpath(os.path.join('/proc/', str(os.getppid()), 'exe'))

def get_memory():
  memory = psutil.virtual_memory()
  mem = {}
  mem['used'] = str(round(memory.used / 1024 ** 2)) + "MB"
  mem['total'] = str(round(memory.total / 1024 ** 2)) + "MB"
  mem['percent'] = str(memory.percent) + "%"
  return mem

def get_os():
  release = lsb_release.get_os_release()
  return f"{release['DESCRIPTION']} [{release['CODENAME']}]"

def get_resolution():
  res = pyautogui.size()
  return f"{res.width}x{res.height}"

def getSystemInfo():
  uname = platform.uname()

  memory = get_memory()

  info = {}
  info['system'] = get_os()
  info['kernel'] = uname.release
  info['version'] = uname.version
  info['shell'] = get_shell()
  info['arch'] = uname.machine
  info['host'] = get_product_name()
  info['ip'] = socket.gethostbyname(socket.gethostname())
  info['processor'] = cpuinfo.get_cpu_info()['brand_raw']
  info['memory'] = f"{memory['used']} / {memory['total']} ({memory['percent']})"
  info['uptime'] = f"{get_uptime()['hour']} Hour, {get_uptime()['mins']} Mins"
  info['boottime'] = get_boottime()
  info['packages'] = f"{get_packages()['dpkg']} [dpkg], {get_packages()['snap']} [snap]"
  info['resolution'] = get_resolution()
  return info

def printSystemInfo(name, key):
  info = getSystemInfo()
  return " "*4 + f"\033[1;35m{name}: \033[0m{info[key] + BOLD_ICON_CHAR}"

def get_icon():
  return f"""{BOLD_ICON_CHAR}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠶⠿⠛⠛⠻⡶⠾⠟⠛⠛⠛⠻⠷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀
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

"""

def fetch():
  icon_component = get_icon().splitlines()
  fetch_component = icon_component
  system_informations = [
    get_host(),
    getNameComponent(0),
    getNameComponent(1),
    getNameComponent(2),
    getNameComponent(3),
    getNameComponent(0),
    printSystemInfo('OS', 'system'),
    printSystemInfo('Host', 'host'),
    printSystemInfo('Kernel', 'kernel'),
    printSystemInfo('Uptime', 'uptime'),
    printSystemInfo('Boot Time', 'boottime'),
    printSystemInfo('Packages', 'packages'),
    printSystemInfo('Shell', 'shell'),
    printSystemInfo('Architecture', 'arch'),
    printSystemInfo('Display', 'resolution'),
    printSystemInfo('Memory', 'memory')
  ]

  for i in range(len(system_informations)):
    fetch_component[i+1] = fetch_component[i+1] + system_informations[i]

  return "\n".join(fetch_component)

def run():
  print("Starting Nola fetch...")
  print("Reading System information...")

  texts = fetch()

  os.system("clear")

  for p in texts:
    print(p, end='')
    sys.stdout.flush()
    time.sleep(0.00005)

if __name__ == '__main__':
  run()