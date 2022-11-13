import platform
from subprocess import Popen
import sys


ip_addr = sys.argv[1]


param = "-n" if platform.system().lower() == 'windows' else "-c"
args = ['ping', param, '2', str(ip_addr)]
process = Popen(args)

print(ip_addr)
