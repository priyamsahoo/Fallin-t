from platform_class import *
from player_class import *
from functions import *

delay = 3000
startOfGame = False


# def keyPressed():
#     startOfGame = True
#     print(startOfGame)
#     if (keyCode == 'B'):
#         print("I am pressed")
#         startOfGame = True

def mousePressed():
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    loop()
    
    
def setup():
    #global setup options
    size(500, 800)
    rectMode(CENTER)
    
    # sb = loadImage("assets\\gameover.jpg")
    # sb.resize(width, height)
    # background(sb)
    
    global atStartUp
    atStartUp = True
    
    global startTimeMs
    startTimeMs = millis()
        
    global bg, go, sb
    bg = loadImage("assets\\background.png")
    bg.resize(width, height)
    go = loadImage("assets\\gameover.jpg")
    go.resize(width, height)
    sb = loadImage("assets\\start.png")
    sb.resize(width, height)
    
    global startOfGame
    startOfGame = False
        
    #list of platforms
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    
def draw():
    global atStartUp
    if (atStartUp):
        currentTimeMs = millis()
        startUpTimeRemaining = delay - (currentTimeMs - startTimeMs)
        startScreen(startUpTimeRemaining)
        atStartUp = startUpTimeRemaining > 0
        return
    
    frameRate(30)
    background(bg)
    for platform in platforms:
        # print (len(platforms))
        platform.display()
    p1.update(platforms)
    platform_manager(platforms)
    
    #this ends the game if the player falls off the screen
    if p1.ypos > height+25:
        background(go)
        fill(255, 255, 255)
        textAlign(CENTER, CENTER)
        textSize(80)
        text("GAME", width/2, 2*height/10)
        text("OVER", width/2, 3*height/10)
        textSize(30)
        fill(240,225,48)
        text("Score: "+str(p1.score/100), width/2, 0.5*height/10)
        textSize(20)
        fill(255, 255, 255)
        text("Click anywhere on the screen to RETRY", width/2, 8*height/10)
        text("Press ESC to exit", width/2, 8.5*height/10)
        textSize(10)
        fill(240,225,48)
        text("Made by Priyam Sahoo", width/2, 9.5*height/10)
        textAlign(LEFT)
        noLoop()
        
    
def startScreen(remainingTime):
    background(sb)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(40)
    fill(240,225,48)
    text("Welcome to Fallin't", width/2, 0.25*height/2)
    textSize(100)
    fill(50, 50, 50)
    text(ceil(remainingTime / 1000.0), width/2, 1.65*height/2)
        
        
