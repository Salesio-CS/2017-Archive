#!/bin/bash
while true; do
date +"%H:%M:%S"
df -h
DATE=$(date +"%Y-%m-%d_%H%M")
raspistill -o /home/pi/$DATE.jpg
printf "[Type on the addres.]\n"
read addres
printf "[Type on the letter.]\n"
printf "[And,The letter want to finish pushing ctrl +[d].]\n"
mail -s program_applicaition -A $DATE.jpg $addres 
printf "[This program finishing can push ctrl + [c] ,or it can continue for 20s waittime.]\n"
sleep 20

done

