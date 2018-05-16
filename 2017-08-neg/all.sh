python photo.py

mv output.bmp asp.bmp
file=goki.bmp
while :
do
 sleep 30
 python photo.py
 ./hikaku output.bmp asp.bmp goki.bmp

 if [ -f $file ];then
    python send_gmail.py
    rm goki.bmp
    break
 fi
done
