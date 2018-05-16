#coding utf-8
import subprocess

dir = "./adxl345-python/adxlex.py"
cmd = "python " + dir
print("called: \'" + cmd + "\'")

adxl = subprocess.check_output(cmd, shell=True)
adxl = str(adxl)
adxl = adxl.split("\'")
adxl = adxl[1].split("\n")
adxl = list(adxl[0])
#
if adxl[0] == "-":
    print("sashiteru")
    #return True
else:
    print("no sashiteru")
    #return False

