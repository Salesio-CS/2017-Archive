from adxl345 import ADXL345

adxl345 = ADXL345()

axes = adxl345.getAxes(True)
print axes['x']
#
