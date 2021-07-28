#import os
import subprocess

#cmd = 'wc -l lib_for_trayicon > out_file.txt'
#os.system(cmd)

out = subprocess.Popen(['wc', '-l', 'lib_for_trayicon'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

stdout,stderr = out.communicate()
print(stdout)
