import laspy
import sys
import os
import subprocess
from colorama import Fore
import re

file_path = sys.argv[1]
file_name = os.path.basename(sys.argv[1]).split('.')

# if file_name[-1] == 'laz':
#     print(Fore.BLUE + "Start converting .laz file to .las")
#     file = laspy.read(file_path)
#     file = laspy.convert(file)
#     output = './tmp/{a}.las'.format(a=file_name[0])
#     file.write(output)
# if file_name[-1] == 'las':
# 	  output = file_path
# print(Fore.GREEN + "Finished converting")
output = "./tmp/lodz.las"
out: any
try:
    out = subprocess.run(
        ['entwine', 'info', output],
        check=True
    )
except  subprocess.CalledProcessError as e:
    print(f"Error with entwine: {e}")
    
print("-------------------------")
print(out)
    # outw = re.search(r'(?<=EPSG:)\d+', out)

# print(Fore.BLUE + "Get EPSG from file")
# EPSG: str
# try:
#     ps = subprocess.Popen(('entwine', 'info', output), stdout=subprocess.PIPE)
#     EPSG = subprocess.check_output(('grep', '-Po', '(?<=EPSG:)\d+'), stdin=ps.stdout)
#     ps.wait()
# except subprocess.CalledProcessError as e:
#     print(f"Error with entwine: {e}")
# print(Fore.GREEN + "EPSG has been download: {}".format(EPSG))
# print(EPSG)

# print(Fore.BLUE + "Start converting .laz file to 3DTiles")
# try:    
#     subprocess.run(
#         "./gocesiumtiler -i {f} -o {o} -e {e}"
#           .format(f=output, o=sys.argv[2], e=EPSG),
#         check=True
#     )
# except subprocess.CalledProcessError as e:
#     print(f"Error with gocesiumtiler: {e}")
# print(Fore.GREEN + "Finished converting")

sys.stdout.write(output)