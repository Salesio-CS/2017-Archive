
#Simple MPU6050 Demo on Raspberry pi 2 using ITG-MPU breakout board (MPU6050)
#This breakout board from aliexpress for $1.50. 40pin old IDE cable used to connect to raspi2
#no interrupt, +vcc of the board is connected to +5v of raspi2
#only sda, scl connected to raspi2.
#MPU data accessed regularly every 10ms (.01sec), sleep time reduced to allow data processing and draw.
#By Opata Padmasiri  
#codes for reading data from MPU6050 and complementary filter taken from the following blog: 
#http://blog.bitify.co.uk/2013/11/reading-data-from-mpu-6050-on-raspberry.html

#!/usr/bin/python

import pygame, sys
from pygame.locals import *
import smbus
import math
import time  
pygame.init()

yjsnpi = 0
syamu = 0
iwama = 0
c = 0
  
#set up the graphics window
#WINDOW = pygame.display.set_mode((400, 300), 0, 32)
#pygame.display.set_caption('MPU_6050 Demo')
  
# set up the colors
#BLACK = (  0,   0,   0)
#WHITE = (255, 255, 255)
#RED   = (255,   0,   0)
#GREEN = (  0, 255,   0)
#BLUE  = (  0,   0, 255)
  
# draw on the surface object
#WINDOW.fill(WHITE)
#==================================
#Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
 
gyro_scale = 131.0
accel_scale = 16384.0
 
address = 0x68  # This is the default I2C address of ITG-MPU breakout board

def read_all():
    raw_gyro_data = bus.read_i2c_block_data(address, 0x43, 6)
    raw_accel_data = bus.read_i2c_block_data(address, 0x3b, 6)

    gyro_scaled_x = twos_compliment((raw_gyro_data[0] << 8) + raw_gyro_data[1]) / gyro_scale
    gyro_scaled_y = twos_compliment((raw_gyro_data[2] << 8) + raw_gyro_data[3]) / gyro_scale
    gyro_scaled_z = twos_compliment((raw_gyro_data[4] << 8) + raw_gyro_data[5]) / gyro_scale
 
    accel_scaled_x = twos_compliment((raw_accel_data[0] << 8) + raw_accel_data[1]) / accel_scale
    accel_scaled_y = twos_compliment((raw_accel_data[2] << 8) + raw_accel_data[3]) / accel_scale
    accel_scaled_z = twos_compliment((raw_accel_data[4] << 8) + raw_accel_data[5]) / accel_scale
    
    return(gyro_scaled_x,gyro_scaled_y,gyro_scaled_z,accel_scaled_x,accel_scaled_y,accel_scaled_z)
#==========================================================
def twos_compliment(val):
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def dist(a, b):
    return math.sqrt((a * a) + (b * b))


bus = smbus.SMBus(1)  # SMBus(1) for Raspberry pi 2 board

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

now = time.time()
 
K = 0.98
K1 = 1 - K
time_diff = 0.01
(gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()
	
last_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
last_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)

gyro_offset_x = gyro_scaled_x
gyro_offset_y = gyro_scaled_y

gyro_total_x = (last_x) - gyro_offset_x
gyro_total_y = (last_y) - gyro_offset_y
#========================

# run the loop
while True:
#     for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
    
    time.sleep(time_diff - 0.005)
    (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z) = read_all()
    
    gyro_scaled_x -= gyro_offset_x
    gyro_scaled_y -= gyro_offset_y
     
    gyro_x_delta = (gyro_scaled_x * time_diff)
    gyro_y_delta = (gyro_scaled_y * time_diff)

    gyro_total_x += gyro_x_delta
    gyro_total_y += gyro_y_delta

    rotation_x = get_x_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
    rotation_y = get_y_rotation(accel_scaled_x, accel_scaled_y, accel_scaled_z)
 
    last_x = K * (last_x + gyro_x_delta) + (K1 * rotation_x)
    last_y = K * (last_y + gyro_y_delta) + (K1 * rotation_y)

    def mail():
	#File Edit Options Buffers Tools Python Help
	#!/Usr/bin/env python
	# -*- coding: utf-8 -*-

        import smtplib
        from email.mime.text import MIMEText

        class sendGmail:
                username, password = 's14508@salesio-sp.ac.jp', 'sabotendar510'

                def __init__(self, to, sub, body):
                        host, port = 'smtp.gmail.com', 465
                        msg = MIMEText(body)
                        msg['Subject'] = sub
                        msg['From'] = self.username
                        msg['To'] = to

                        smtp = smtplib.SMTP_SSL(host, port)
                        smtp.ehlo()
                        smtp.login(self.username, self.password)
                        smtp.mail(self.username)
                        smtp.rcpt(to)
                        smtp.data(msg.as_string())
                        smtp.quit()

        if __name__ == '__main__':
                to = 's14507@salesio-sp.ac.jp'
                sub = 'Open the door now.'
                body = 'Go back home.'
                sendGmail(to, sub, body)


    def motor():
        import wiringpi

        import time

        import sys

        # GPIO number
        servo_pin  =  18
        # kakudo set
        # set_degree = 90 def

        param = sys.argv
        set_degree = 90

        wiringpi.wiringPiSetupGpio()
        # PWM output
        wiringpi.pinMode( servo_pin, 2 )

        # motor PWM set
        wiringpi.pwmSetMode(0)
        wiringpi.pwmSetRange(1024)
        wiringpi.pwmSetClock(375)

        # -90 ~ 90 only move

            # PWM use number
        move_deg = int( 81 + 41 / 90 * set_degree )
            # send PWM motor move
        wiringpi.pwmWrite( servo_pin, move_deg )


    def motor2():
        import wiringpi

        import time

        import sys

        # GPIO number
        servo_pin  =  18
        # kakudo set
        # set_degree = 90 def

        param = sys.argv
        set_degree = 0

        wiringpi.wiringPiSetupGpio()
        # PWM output
        wiringpi.pinMode( servo_pin, 2 )

        # motor PWM set
        wiringpi.pwmSetMode(0)
        wiringpi.pwmSetRange(1024)
        wiringpi.pwmSetClock(375)

        # -90 ~ 90 only move

            # PWM use number
        move_deg = int( 81 + 41 / 90 * set_degree )
            # send PWM motor move
        wiringpi.pwmWrite( servo_pin, move_deg )
        
        return 0


    def iwao(x):
        if x > 1000:
            mail()
            motor()
            print ("Send e-mail.")
            return 0

    def iwao2(x):
        if x > 300:
            motor2()
            return 0

    def game(g):
        if g > 300:
            print ("open door")
            return 0

    def pr_closed(c):
        if c > 600:
            print ("The door is closed")
            return 0

#    print last_x,last_y on terminal window
#    print (last_x)
    
    delta_y = math.radians(last_y)
    
    if last_x > 0:
        iwama = 0
        yjsnpi += 1
        syamu += 1
	
    if last_x < 0:
        yjsnpi = 0
        iwama += 1

    if pr_closed(c) == 0:
        c = 0

    if iwao(yjsnpi) == 0:
        yjsnpi = 0

    if game(syamu) == 0:
        syamu = 0
    
    if iwao2(iwama) == 0:
        iwama = 0

    #z-is thickness of the line
    z = 2 * int(last_x)
    if z < 0 :
        z = -z 
#	COLOR = RED #change colour if x-axis reading is negative
#    else:
#	COLOR = BLUE
    if z == 0 :
        z = 1

#    x1 = 200 -(100 * math.cos(delta_y))
#    y1 = 150 +(100 * math.sin(delta_y))	
#    x2 = 200 +(100 * math.cos(delta_y))
#    y2 = 150 -(100 * math.sin(delta_y))
    
#    print (x1), (y1) ,(x2), (y2)
#    WINDOW.fill(WHITE) #clear window before redraw

    #simply draw the plane, z-is thickness: change thickness of the line to appear 3D
#    pygame.draw.line(WINDOW, COLOR, (x1,y1), (x2,y2), z) 
#    pygame.display.update()
    dtparam=i2c_baudrate=10000
