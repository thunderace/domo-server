#!/usr/bin/PYTHON
# -*- coding: utf-8 -*-

import os
import serial #pip install pyserial
import subprocess

#PORT_ID = "/dev/ttyUSB0"
PORT_ID = "COM4"
DB_NAME = "teleinfo"

def saveTrame(trameMap):
  return true

def analyseTrame(trame):
  trameMap = {} # new Map
  lines = trame.split("\r\n\r\n")
  for line in lines:
    values = line.split(" ")
    if len(values) >= 3:
      etiquette = values[0]
      valeur = values[1]
      checksum = values[2]
      trameMap[etiquette] = valeur
      # if (calcChecksum(etiquette, valeur) == checksum  
        # && calcMessageSize(etiquette) == valeur.length
        # ) {
          # trameMap.set(etiquette, valeur);
      # }      
  print(trameMap)
  return trameMap  

def test():
  trame = "ADCO 030222707626 <\r\n\r\nOPTARIF BASE 0\r\n\r\nISOUSC 30 9\r\n\r\nBASE 094304690 .\r\n\r\nPTEC TH.. $\r\n\r\nIINST 003 Z\r\n\r\nIMAX 032 D\r\n\r\nPAPP 00740 ,\r\n\r\nMOTDETAT 000000 B\r\n\r\n"
  trameMap = analyseTrame(trame)

def readSerial(portId):
  try:
    subprocess.call("stty -F " + portId + " 1200 sane evenp parenb cs7 -crtscts")
    print("config port " + portId + " ok")  
  except Exception:
    print("Exception ")  
  ser = serial.Serial(portId, 115200)
  print("opening " + portId)
  ser.open()
  if (ser.isOpen()):
    print("Port open")
    content = ser.readline()
    # doRead = true
    # while (doRead):
      # x = ser.read()
      # doRead = (x != chr(2))
    # content = ""      
    # doRead = true
    # while (doRead):
      # x = ser.read()
      # if (x != chr(2)):
        # content += x 
      # doRead = (x != chr(2))
    ser.close()  
  print(">>" + content)
  return content

def dumpTeleinfo(portId):
  trame = readSerial(portId)
  trameMap = analyseTrame(trame)
  saveTrame(trameMap)

print("teleinfo starting")
#dumpTeleinfo(PORT_ID)
test()
print("teleinfo end")
