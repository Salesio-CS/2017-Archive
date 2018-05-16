#!/usr/bin/python

import RPi.GPIO as GPIO
import time

SENSOR_ONE=26
SENSOR_TWO=13

CIRCUIT_READER=5
CIRCUIT_WRITER=9

def setup():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(SENSOR_ONE, GPIO.IN)
	GPIO.setup(SENSOR_TWO, GPIO.IN)
	GPIO.setup(CIRCUIT_READER, GPIO.IN)
	GPIO.setup(CIRCUIT_WRITER, GPIO.OUT)
	GPIO.output(CIRCUIT_WRITER, 0)

def read_sensor_one():
	return not GPIO.input(SENSOR_ONE)

def read_sensor_two():
	return not GPIO.input(SENSOR_TWO)

def write_circuit(flag):
	if read_circuit() != flag:
		GPIO.output(CIRCUIT_WRITER, 1)
		time.sleep(0.1)
		GPIO.output(CIRCUIT_WRITER, 0)
	return read_circuit()

def read_circuit():
	return GPIO.input(CIRCUIT_READER)

def cleanup():
	GPIO.cleanup()

