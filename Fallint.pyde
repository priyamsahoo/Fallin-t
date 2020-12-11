from platform_class import *
from player_class import *
from functions import *

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
        
    global bg, go
    bg = loadImage("assets\\background.png")
    bg.resize(width, height)
    go = loadImage("assets\\gameover.jpg")
    go.resize(width, height)
        
    #list of platforms
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    
def draw():
    
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
        

    

        
        
