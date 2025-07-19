import serial
import time
from PIL import Image, ImageEnhance, ImageGrab
import sys
import os
import cv2 as cv
import math

waitTimeInSeconds = 0.0025


def scaleNN(filename):
    im = Image.open(filename)
    im3 = ImageEnhance.Contrast(im)
    im3 = im3.enhance(5.0)
    im3.resize((72, 40), Image.NEAREST).save("ns_" + filename)
    img2 = cv.imread('ns_' + filename, 0)
    ret, thresh1 = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
    cv.imwrite("th_" + filename, thresh1)

def getSpriteData(filename):
    data = [0] * (72 * 5)
    img = Image.open(filename)
    img = img.convert('RGB')
    pixels = img.load()
    width = 72
    height = 40

    i = 0
    byteheight = 8
    byteIndex = 0

    for y in range(height):
        for x in range(width):
            p = pixels[x, y]
            if p[0] >= 216 and p[1] >= 216 and p[2] >= 216:
                j = (i % width) + (math.floor(i / (byteheight * width)) * width)
                data[j] += math.floor(math.pow(2, byteIndex))
            i += 1
            if (i % width == 0):
                byteIndex = (byteIndex + 1) % 8
    return data

def THUMBYIO(screenUpdate):
    ser.write(str.encode("thumby.display.fill(0)\r\x04"))
    ser.write(str.encode("thumby.display.blit(bytearray(" + str(screenUpdate) + "), 0, 0, 72, 40, 0, 0, 0)\r\x04"))
    ser.write(str.encode("thumby.display.update()\r\x04"))
    time.sleep(waitTimeInSeconds)

# === SERIAL SETUP ===
ser = serial.Serial()
ser.port = 'COM3'  
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS
ser.open()

ser.write(str.encode("\r\x03\x03"))
ser.write(str.encode("\r\x01"))
# ====================

time.sleep(1)
while ser.inWaiting() > 0:
    print(bytes.decode(ser.read(1)), end='')

ser.write(str.encode("import thumby\r\x04"))
time.sleep(1)
while ser.inWaiting() > 0:
    print(bytes.decode(ser.read(1)), end='')

def streamScreen():
    while True:
        img = ImageGrab.grab()
        img.save("screenshot.png")

        scaleNN("screenshot.png")
        spriteData = getSpriteData("th_screenshot.png")

        THUMBYIO(spriteData)

try:
    streamScreen()
except KeyboardInterrupt:
    print("Exiting...")
    ser.close()
