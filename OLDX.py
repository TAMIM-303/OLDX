import os,platform
os.system('pkg install espeak -y --quiet 2>/dev/null')
os.system("clear")
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
xd=platform.architecture()[0]
if xd=="32bit":
    os.system("clear");exit("\033[91;1m 32Bit Device Not Supported")
    __import__("OLD")
elif xd=="64bit":
    __import__("OLD")
