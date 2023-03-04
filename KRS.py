#coding=utf-8
import os, sys, platform

os.system('xdg-open https://www.facebook.com/groups/207678473842318')

#
try:
    if sys.argv[1]=='update':
        os.system('rm -rf PROTECT64.cpython-311.so PROTECT32.cpython-311.so')
except:
    pass
os.system('rm -rf PROTECT64.cpython-311.so PROTECT32.cpython-311.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('PROTECT64.cpython-311.so'):
        os.system('curl https://github.com/TEAM-KRS/DATA/blob/main/PROTECT64.cpython-311.so > PROTECT64.cpython-311.so') 
        import PROTECT64
    else:
        import PROTECT64

elif bit == '32bit':
    if not os.path.isfile('PROTECT32.cpython-311.so'):
        os.system('curl https://github.com/TEAM-KRS/DATA/blob/main/PROTECT32.cpython-311.so > PROTECT32.cpython-311.so') 
        import PROTECT32
    else:
        import PROTECT32
