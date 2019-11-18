# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:00:59 2019

@author: wohnzimmer
"""

import pygame, sys, math, datetime

windowMargin = 1
windowWidth = 600
windowHeight = windowWidth
windowCenter = windowWidth/2, windowHeight/2
clockMarginWidth = 20
secondColor = (255, 0, 0)
minuteColor = (100, 200, 0)
hourColor = (100, 200, 0)
clockMarginColor = (130, 130, 130)
clockBackgroundColor = (40, 40, 40)
backgroundColor = (0, 0, 0, 0)
hourCursorLength = windowWidth/2.0-windowMargin-140
minuteCursorLength = windowWidth/2.0-windowMargin-40
secondCursorLength = windowWidth/2.0-windowMargin-10
virtualSpeed = 1
useVirtualTimer = False

def getCursorPositionDegrees(position, scale):
# 12 Uhr entspricht -90 Grad
    cursorOffset = -90
    degrees = 360 / scale * position + cursorOffset
    return degrees

def gradToBogenmass(degrees):
# python bietet auch die Funktion math.radians(degrees),
# welche die Umrechnung genauso ausfuehrt, aber so wird
# der Sachverhalt deutlicher
    return degrees/180.0*math.pi
    
def getCirclePoint(position, scale, cursorLength):
    degrees = getCursorPositionDegrees(position, scale)
    bogenmass = gradToBogenmass(degrees)
    xPos = round(math.cos(bogenmass)*cursorLength+windowCenter[0])
    yPos = round(math.sin(bogenmass)*cursorLength+windowCenter[1])
    return (xPos, yPos)
    
def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit(0)    
def main():
# Initialisierung des Screens
    pygame.init()
    global screen 
    screen = pygame.display.set_mode((windowWidth, windowHeight),pygame.HWSURFACE | pygame.DOUBLEBUF);
    pygame.display.set_caption( ' Analog Clock ' );
    # Endlosschleife für den Hauptablauf der Uhr
    while True:
        handleEvents()
        screen.fill(backgroundColor)
        drawBackground()
        drawCurrentTime()
        drawForeground()
        pygame.display.flip()            
        pygame.time.delay(1000)
        
if __name__ == ' __main__ ' :
    main()
 
def drawBackground():
    screen.fill(backgroundColor)
    pygame.draw.ellipse(screen, clockMarginColor, (windowMargin,windowMargin, windowWidth-2*windowMargin,windowWidth-2*windowMargin))
    pygame.draw.ellipse(screen, clockBackgroundColor,(windowMargin+clockMarginWidth/2,windowMargin+clockMarginWidth/2,windowWidth-(windowMargin+clockMarginWidth/2)*2,windowWidth-(windowMargin+clockMarginWidth/2)*2))

def drawForeground():
    pygame.draw.ellipse(screen, clockMarginColor,(windowWidth/2.0-9, windowHeight/2.0-9, 18, 18))   
    
def drawCursor(color, width, length, position, scale):
    end = getCirclePoint(position, scale, length);
    pygame.draw.line(screen, color, windowCenter, end, width)    

def drawCurrentTime():
    if useVirtualTimer:
        global hour, minute, second, micro
        timeGoesOn()
    else:
        now = datetime.datetime.now()
        micro = now.microsecond
        hour = now.hour
        minute = now.minute
        second = now.second
        drawCursor(hourColor, 15, hourCursorLength, hour+minute/60.0, 12)
        drawCursor(minuteColor, 8, minuteCursorLength, minute+second/60.0, 60)
        drawCursor(secondColor, 3,secondCursorLength,second+micro/1000000.0, 60)    

hour = 0
minute = 0
second = 0
micro = 0
def timeGoesOn():
    global hour, minute, second, micro
    micro += virtualSpeed
    if micro >= 2: # halve seconds - not micro seconds
        second += 1
        micro %= 2
    if second > 60:
        minute += 1
        second %= 60        

main()        