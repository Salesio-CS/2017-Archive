from img_trim import KnowledgeImgTrim
import datetime
import calendar
import time
import os

print("")
print("============================")
print("===== KNOWLEDGE START ======")
print("===== TEAM: TNK2.BROS. =====")
print("============================")
print("")


now = datetime.datetime.now()
dir_name = 'test'

# initialize
prc = KnowledgeImgTrim(dir_name, "zero_img")

# image trimming
for i in range(2):
    prc.trimming(dir_name, "img" + str(i))


print("\n============================")
print("===== KNOWLEDGE FINISH =====")
print("============================")
print("\n")
