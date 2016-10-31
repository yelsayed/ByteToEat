import pygame, sys
from pygame.locals import *
import random

#Initiates Pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

#Creates screen
size = width, height = 600, 430
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Byte to Eat")

#Loading Pictures
spike = pygame.image.load("spikes.png")
spikeDN = pygame.image.load("spikes2.png")
spikeL = pygame.image.load("spikes3.png")
spikeR = pygame.image.load("spikes4.png")
startGame = pygame.image.load("Start Game.png")
space = pygame.image.load("space.png")
controls = pygame.image.load("controls.png")
arrows = pygame.image.load("arrows.png")
cherries = pygame.image.load("stopsign.png")
GameOver = pygame.image.load("Game Over.png")


#Colors
Colors = []
white = 255,255,255
whiteColor = pygame.Color(255,255,255)
redColor = pygame.Color(255,0,0)
orangeColor = pygame.Color(255,69,0)
blackColor = pygame.Color(0,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)

#Variables
moment = 1.01
gravity = 4
Invgravity = -4
normGrav = True
numofDeaths = 0
level = 0
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
countl = 0

#Font
def text(screen,text,x,y,size,color,fontFamily):
        color = (0,0,0)
        text = str(text)
        font = pygame.font.SysFont(fontFamily,size)
        text = font.render(text,False,color)
        screen.blit(text,(x,y))

#Creates the Main Player
class Hero:
        def __init__(self,(x,y)):
                self.x = x
                self.y = y
                self.h = 40
                self.w = 30
                self.color = greenColor
                self.speed = 2
        def display(self):
                rx,ry = int(self.x), int(self.y)
                pygame.draw.rect(screen,self.color,(rx,ry,self.w,self.h),5)
        def moveR(self,collisionR):
                if collisionR == False:
                        self.speed *= 1.01
                        if self.speed >= 5:
                                self.speed = 5
                        self.x += self.speed

        def moveL(self,collisionL):
                if collisionL == False:
                        self.speed *= 1.01
                        if self.speed >= 5:
                                self.speed = 5
                        self.x -= self.speed

        def moveD(self,collisionB):
                if collisionB == False:
                        self.y += gravity
    
        def moveU(self,collisionT):
                if collisionT == False:
                        self.y += Invgravity

#Creates the Walls, floors and ceilings
class Square:
        def __init__(self,(h,w),(x,y),color):
                self.x = x
		self.y = y
                self.h = h
                self.w = w
		self.color = color
		self.speed = 2
	def display(self):
		rx,ry = int(self.x), int(self.y)
                pygame.draw.rect(screen,self.color,(rx,ry,int(self.w),int(self.h)),3)

#Creates the Spikes
class Spikes:
        def __init__(self,(x,y),position):
                self.x = x
                self.y = y
                self.position = position
                if position == "upright":
                        self.w = 40
                        self.h = 20
                if position == "upsideDN":
                        self.w = 40
                        self.h = 20
                if position == "right":
                        self.w = 20
                        self.h = 50
                if position == "left":
                        self.w = 20
                        self.h = 50

        def display(self):
                rx,ry = int(self.x), int(self.y)
                if self.position == "upright":
                        screen.blit(spike,(rx,ry))
                if self.position == "upsideDN":
                        screen.blit(spikeDN,(rx,ry))
                if self.position == "right":
                        screen.blit(spikeR,(rx,ry))
                if self.position == "left":
                        screen.blit(spikeL,(rx,ry))

#Creates Moving Obstacles
class Cherry:
        def __init__(self,(x,y),motion):
                self.x = x
                self.y = y
                self.h = 50
                self.w = 50
                self.speed = 3
                self.motion = motion

        def display (self):
                rx,ry = self.x, self.y
                screen.blit(cherries,(rx,ry))

        def moveH(self):
                if self.motion == "Horizental":
                        self.x += self.speed

        def moveV(self):
                if self.motion == "Vertical":
                        self.y += self.speed
        def bounce(self):
                if self.x <= 0 or self.x + self.w >= 600:
                        self.speed *= -1
                elif self.y <= 0 or self.y + self.h >= 400:
                        self.speed *= -1
        def bounceonHitV(self,collisionT,collisionB):
                if collisionT == True or collisionB == True:
                        self.speed = self.speed*-1
        def bounceonHitH(self,collisionL,collisionR):
                if collisionL == True or collisionR == True:
                        self.speed = self.speed*-1

#Bouncy bouncy line thingy.. yeah!
class line:
        def __init__(self,(x,y)):
                self.x = x
                self.y = y
                self.w = 50
                self.h = 3
                self.color = blackColor
        def display(self):
                pygame.draw.rect(screen,self.color,(int(self.x),int(self.y),int(self.w),int(self.h)))


#Main Collision Detection Function (split into four parts)
def detectCollisionsL(x1,y1,w1,h1,x2,y2,w2,h2):
        #Top Left corner
        if x2 + w2 + 5 >= x1 and x1 >= x2 + 5 and y2 + h2 - 5 >= y1 and y1 >= y2 - 5:
                return True
        #Bottom Left corner
        if x2 + w2 + 5 >= x1 and x1 >= x2 + 5 and y2 + h2 + 5 >= y1 + h1 and y1 + h1 >= y2 + 5:
                return True
        else:
                return False

def detectCollisionsR(x1,y1,w1,h1,x2,y2,w2,h2):
        #Top right corner
        if x1 + w1 + 5 >= x2 and x2 >= x1 + 5 and y2 + h2 - 5 >= y1 and y1 >= y2 - 5:
                return True
        #Bottom right corner
        if x2 + w2 - 3 >= x1 + w1 and x1 + w1 >= x2 - 3 and y2 + h2 + 5 >= y1 + h1 and y1 + h1 >= y2 + 5:
                return True
        else:
                return False

def detectCollisionsB(x1,y1,w1,h1,x2,y2,w2,h2):
        #Bottom Left corner
        if x2 + w2 > x1 and x1 > x2 and y2 + h2 > y1 + h1  and y1 + h1 > y2:
                return True
        #Bottom Right corner
        if x2 + w2 > x1 + w1 and x1 + w1 > x2 and y2 + h2 > y1 + h1 and y1 + h1 > y2:
                return True
        else:
                return False

def detectCollisionsT(x1,y1,w1,h1,x2,y2,w2,h2):
        #Top Right corner 
        if x1 + w1 > x2 + w2 and x1 + w1 > x2  and y2 + h2 < y1 and y1 < y2:
                return True
        #Top Left corner
        if x2 + w2 > x1 and x1 + w1 > x2 and y2 + h2 > y1 and y1 > y2:
                return True
        else:
                return False

#Main Function, creates the levels from pre-read text files
def createObjects(hashlist):
        listofObjects = []
        listofLines = []
        listofCherries = []
        listofSpikes = []
        #Goes through the already created list of strings
        for i in range(len(hashlist)):
                if "\n" in hashlist[i]:
                        hashlist[i].replace("\n","")
                for k in range(len(hashlist[i])):
                        if hashlist[i][k] == "S":
                                startingPosition = (50*k,i*50)
                                if k == 0:
                                        HTile = Square((50,50),(-75,i*50),whiteColor)
                                        listofObjects.append(HTile)
                                if k == 11:
                                        HTile = Square((50,50),(50*k+70,i*50),whiteColor)
                                        listofObjects.append(HTile)
                                if i == 0:
                                        HTile = Square((50,50),(50*k,i*50-50),whiteColor)
                                        listofObjects.append(HTile)
                        
                        if hashlist[i][k] == "E":
                                endingPosition = (50*k,i*50)
                        
                        if hashlist[i][k] == "#":
                                HTile = Square((50,50),(50*k,i*50),blueColor)
                                listofObjects.append(HTile)
                        
                        if hashlist[i][k] == "H":
                                Cher = Cherry((50*k,i*50),"Horizental")
                                listofCherries.append(Cher)
                        
                        if hashlist[i][k] == "V":
                                Cher = Cherry((50*k,i*50),"Vertical")
                                listofCherries.append(Cher)

                        if hashlist[i][k] == "-":
                                HTile = Square((25,50),(50*k,50*i),blueColor)
                                listofObjects.append(HTile)

                        if hashlist[i][k] == "_":
                                bounce = line((50*k,50*i))
                                listofLines.append(bounce)

                        if hashlist[i][k] == "=":
                                HTile = Square((25,50),(50*k,i*50+25),blueColor)
                                listofObjects.append(HTile)
                        
                        if hashlist[i][k] == "^":
                                Hspike = Spikes((50*k,i*50),"upright")
                                miniTile = Square((25,50),(50*k,i*50+25),blueColor)
                                listofObjects.append(miniTile)
                                listofSpikes.append(Hspike)
                        
                        if hashlist[i][k] == ">":
                                Hspike = Spikes((50*k+25,i*50),"left")
                                miniTile = Square((50,25),(50*k,i*50),blueColor)
                                listofObjects.append(miniTile)
                                listofSpikes.append(Hspike)
                        
                        if hashlist[i][k] == "<":
                                Hspike = Spikes((50*k,i*50),"right")
                                miniTile = Square((50,25),(50*k+25,i*50),blueColor)
                                listofSpikes.append(Hspike)
                                listofObjects.append(miniTile)
                        
                        if hashlist[i][k] == "v":
                                Hspike = Spikes((50*k,i*50+25),"upsideDN")
                                miniTile = Square((25,50),(50*k,i*50),blueColor)
                                listofSpikes.append(Hspike)
                                listofObjects.append(miniTile)
        return listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition


#Defines at what point can your player go to the next level
def goNextLevel(endingPosition,x1,w1,y1,h1):
        if x1 + w1 >= endingPosition[0] + 50 and endingPosition[0] + 50 >= x1 and endingPosition[1] + 50 >= y1 and y1 >= endingPosition[1]:
                return True
        if endingPosition[0] + 50 >= x1 + w1 and x1 + w1 >= endingPosition[0] + 50 and endingPosition[1] + 50 >= y1 + h1 and y1 + h1 >= endingPosition[1]:
                return True
        if endingPosition[0] + 50 >= x1 and x1 >= endingPosition[0] and endingPosition[1] + 50 >= y1 and y1 >= endingPosition[1]:
                return True
        if endingPosition[0] + 50 >= x1 and x1 >= endingPosition[0] and endingPosition[1] + 50 >= y1 + h1 and y1 + h1 >= endingPosition[1]:
                return True
        else:
                return False


#Next set of functions all read the levels from text files
def loadLevel0():
        Menu = open("help.txt")
        hashlist = []
        line = Menu.readline()
        name = "Read and learn"
        while line:
                hashlist.append(line)
                line = Menu.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel1():
        levelone = open("1-1.txt")
        hashlist = []
        line = levelone.readline()
        name = "Press space"
        while line:
                hashlist.append(line)
                line = levelone.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel2():
        leveltwo = open("1-2.txt")
        hashlist = []
        line = leveltwo.readline()
        name = "You got this!"
        while line:
                hashlist.append(line)
                line = leveltwo.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel3():
        levelthree = open("1-3.txt")
        hashlist = []
        line = levelthree.readline()
        name = "Even blocks have momentum"
        while line:
                hashlist.append(line)
                line = levelthree.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel4():
        levelfour = open("1-4.txt")
        hashlist = []
        line = levelfour.readline()
        name = "Stop, Drop, and Go"
        while line:
                hashlist.append(line)
                line = levelfour.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel5():
        levelfive = open("1-5.txt")
        hashlist = []
        line = levelfive.readline()
        name = "Pffft, easy!"
        while line:
                hashlist.append(line)
                line = levelfive.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel6():
        levelsix = open("1-6.txt")
        hashlist = []
        line = levelsix.readline()
        name = "Traffic Jam"
        while line:
                hashlist.append(line)
                line = levelsix.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel7():
        levelseven = open("1-7.txt")
        hashlist = []
        line = levelseven.readline()
        name = "Stop and think"
        while line:
                hashlist.append(line)
                line = levelseven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel8():
        leveleight = open("1-8.txt")
        hashlist = []
        line = leveleight.readline()
        name = "Well..."
        while line:
                hashlist.append(line)
                line = leveleight.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel9():
        levelnine = open("1-9.txt")
        hashlist = []
        line = levelnine.readline()
        name = "Leap of Faith"
        while line:
                hashlist.append(line)
                line = levelnine.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel10():
        levelten = open("1-10.txt")
        hashlist = []
        line = levelten.readline()
        name = "Tower of Hurt"
        while line:
                hashlist.append(line)
                line = levelten.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel11():
        leveleleven = open("1-11.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "You're Up and You're Daun"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition   

def loadLevel12():
        leveleleven = open("1-12.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "Close Shave"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel13():
        leveleleven = open("1-13.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "You're Hassan and You're Daun"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel14():
        leveleleven = open("1-14.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "Wait for it..."
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel15():
        leveleleven = open("1-15.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "Box of Death"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel16():
        leveleleven = open("1-16.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "Have a break"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel17():
        leveleleven = open("1-17.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "Remember this?"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel18():
        leveleleven = open("1-18.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "Under the Iceburg"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel19():
        leveleleven = open("1-19.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "It's a Trap!"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 

def loadLevel20():
        leveleleven = open("1-20.txt")
        hashlist = []
        line = leveleleven.readline()
        name = "You did it!"
        while line:
                hashlist.append(line)
                line = leveleleven.readline()
        listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = createObjects(hashlist)
        return name, listofObjects, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition 


right_pressed = False
left_pressed = False
up_pressed = False 
down_pressed = False
space_pressed = False

while True:
        #Sets frames per second to be 100, this makes the game a lot harder
	clock.tick(100)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN and event.key == K_RIGHT:
                        right_pressed = True
                if event.type == KEYUP and event.key == K_RIGHT:
                        right_pressed = False
                if event.type == KEYDOWN and event.key == K_LEFT:
                        left_pressed = True
                if event.type == KEYUP and event.key == K_LEFT:
                        left_pressed = False
                if event.type == KEYDOWN and event.key == K_SPACE:
                        #Flips the gravity of your player, and makes sure that you cannot flip midair
                        if normGrav == True and (collisionB == True or collisionT == True):
                                normGrav = False
                        elif normGrav == False and (collisionB == True or collisionT == True):
                                normGrav = True
        
        collisionL = False
        collisionR = False
        collisionB = False
        collisionT = False
        collisionKL = False
        collisionKR = False
        collisionKB = False
        collisionKT = False
        collisionSL = False
        collisionSR = False
        collisionSB = False
        collisionST = False

        #Calls the previous functinons to load the level, and only does it once
        if level == 0 and count0 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel0()
                square = Hero(startingPosition)
                count0 += 1
        
        elif level == 1 and count1 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel1()
                square = Hero(startingPosition)
                count1 += 1
        
        elif level == 2 and count2 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel2()
                square = Hero(startingPosition)
                count2 += 1
        
        elif level == 3 and count3 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel3()
                square = Hero(startingPosition)
                count3 += 1
        
        elif level == 4 and count4 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel4()
                square = Hero(startingPosition)
                count4 += 1
        
        elif level == 5 and count5 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel5()
                square = Hero(startingPosition)
                count5 += 1
        
        elif level == 6 and count6 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel6()
                square = Hero(startingPosition)
                count6 += 1
        
        elif level == 7 and count7 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel7()
                square = Hero(startingPosition)
                count7 += 1
        
        elif level == 8 and count8 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel8()
                square = Hero(startingPosition)
                count8 += 1
        
        elif level == 9 and count9 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel9()
                square = Hero(startingPosition)
                count9 += 1

        #So much hardcode
        elif level == 10 and count10 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel10()
                square = Hero(startingPosition)
                count10 += 1
        
        elif level == 11 and count11 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel11()
                square = Hero(startingPosition)
                count11 += 1
        
        elif level == 12 and count12 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel12()
                square = Hero(startingPosition)
                count12 += 1
        
        elif level == 13 and count13 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel13()
                square = Hero(startingPosition)
                count13 += 1
        
        elif level == 14 and count14 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel14()
                square = Hero(startingPosition)
                count14 += 1
        
        elif level == 15 and count15 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel15()
                square = Hero(startingPosition)
                count15 += 1
        
        elif level == 16 and count16 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel16()
                square = Hero(startingPosition)
                count16 += 1

        elif level == 17 and count17 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel17()
                square = Hero(startingPosition)
                count17 += 1

        elif level == 18 and count18 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel18()
                square = Hero(startingPosition)
                count18 += 1


        elif level == 19 and count19 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel19()
                square = Hero(startingPosition)
                count19 += 1

        elif level == 20 and count20 < 1:
                name, listofSquares, listofSpikes, listofCherries, listofLines, startingPosition, endingPosition = loadLevel20()
                square = Hero(startingPosition)
                count20 += 1

        if goNextLevel(endingPosition,square.x,square.w,square.y,square.h) == True:
                level += 1

        numofobjects  = len(listofSquares)
        numofSpikes = len(listofSpikes)
        numofCherries = len(listofCherries)
        numofLines = len(listofLines)

        #Calls the collision detection function a billion times to check if there is collision with anything in the current level
        for i in range(numofobjects):
                currentSquare = listofSquares[i]
                ###Detects collisions with blocks
                if detectCollisionsR(square.x,square.y,square.w,square.h,currentSquare.x,currentSquare.y,currentSquare.w,currentSquare.h) == True:
                        squareHit = currentSquare
                        collisionR = True
                if detectCollisionsL(square.x,square.y,square.w,square.h,currentSquare.x,currentSquare.y,currentSquare.w,currentSquare.h) == True:
                        squareHit = currentSquare
                        collisionL = True
                if detectCollisionsB(square.x,square.y,square.w,square.h,currentSquare.x,currentSquare.y,currentSquare.w,currentSquare.h) == True:
                        squareHit = currentSquare
                        collisionB = True
                if detectCollisionsT(square.x,square.y,square.w,square.h,currentSquare.x,currentSquare.y,currentSquare.w,currentSquare.h) == True:
                        squareHit = currentSquare
                        collisionT = True
        
                for j in range(numofCherries):
                        currentCherry = listofCherries[j]
                        collisionCT = False
                        collisionCR = False
                        collisionCL = False
                        collisionCB = False
                        if detectCollisionsR(currentSquare.x,currentSquare.y,currentSquare.w-10,currentSquare.h,currentCherry.x,currentCherry.y,currentCherry.w-10,currentCherry.h) == True:
                                collisionCR = True
                        if detectCollisionsL(currentSquare.x,currentSquare.y,currentSquare.w-10,currentSquare.h,currentCherry.x,currentCherry.y,currentCherry.w-10,currentCherry.h) == True:
                                collisionCL = True
                        if detectCollisionsT(currentSquare.x,currentSquare.y,currentSquare.w-10,currentSquare.h,currentCherry.x,currentCherry.y,currentCherry.w-10,currentCherry.h) == True:
                                collisionCB = True
                        if detectCollisionsT(currentCherry.x,currentCherry.y,currentCherry.w-10,currentCherry.h,currentSquare.x,currentSquare.y,currentSquare.w-10,currentSquare.h) == True:
                                collisionCT = True
                        if detectCollisionsR(square.x,square.y,square.w,square.h,currentCherry.x+7,currentCherry.y+7,currentCherry.w-10,currentCherry.h-10) == True:
                                collisionKR = True
                        if detectCollisionsL(square.x,square.y,square.w,square.h,currentCherry.x+7,currentCherry.y+7,currentCherry.w-10,currentCherry.h-10) == True:
                                collisionKL = True
                        if detectCollisionsB(square.x,square.y,square.w,square.h,currentCherry.x+7,currentCherry.y+7,currentCherry.w-10,currentCherry.h-10) == True:
                                collisionKB = True
                        if detectCollisionsT(square.x,square.y,square.w,square.h,currentCherry.x+7,currentCherry.y+7,currentCherry.w-10,currentCherry.h-10) == True:
                                collisionKT = True
                        currentCherry.bounceonHitV(collisionCB,collisionCT)
                        currentCherry.bounceonHitH(collisionCR,collisionCL)

        for i in range(numofSpikes):
                ###Detect collisions with spikes, sounds painful tbh
                currentSpike = listofSpikes[i]
                if currentSpike.position == "upright":
                        if detectCollisionsR(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y+5,currentSpike.w,currentSpike.h) == True:
                                collisionSR = True
                        if detectCollisionsL(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y+5,currentSpike.w,currentSpike.h) == True:
                                collisionSL = True
                        if detectCollisionsB(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y+5,currentSpike.w,currentSpike.h) == True:
                                collisionSB = True
                        if detectCollisionsT(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y+5,currentSpike.w,currentSpike.h) == True:
                                collisionST = True
                elif currentSpike.position == "right":
                        if detectCollisionsR(square.x,square.y,square.w,square.h,currentSpike.x+15,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSR = True
                        if detectCollisionsL(square.x,square.y,square.w,square.h,currentSpike.x+15,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSL = True
                        if detectCollisionsB(square.x,square.y,square.w,square.h,currentSpike.x+15,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSB = True
                        if detectCollisionsT(square.x,square.y,square.w,square.h,currentSpike.x+15,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionST = True
                elif currentSpike.position == "left":
                        if detectCollisionsR(square.x,square.y,square.w,square.h,currentSpike.x-5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSR = True
                        if detectCollisionsL(square.x,square.y,square.w,square.h,currentSpike.x-5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSL = True
                        if detectCollisionsB(square.x,square.y,square.w,square.h,currentSpike.x-5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSB = True
                        if detectCollisionsT(square.x,square.y,square.w,square.h,currentSpike.x-5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionST = True
                elif currentSpike.position == "upsideDN":
                        if detectCollisionsR(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSR = True
                        if detectCollisionsL(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSL = True
                        if detectCollisionsB(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionSB = True
                        if detectCollisionsT(square.x,square.y,square.w,square.h,currentSpike.x+5,currentSpike.y,currentSpike.w,currentSpike.h) == True:
                                collisionST = True

        for i in range(numofLines):
                ##Detect fun collision with lines
                currentLine = listofLines[i]
                if detectCollisionsR(square.x+10,square.y,square.w-50,square.h,currentLine.x,currentLine.y,currentLine.w,currentLine.h) == True and countl < 1:
                        if normGrav == True:
                                normGrav = False
                        elif normGrav == False:
                                normGrav = True
                        countl += 1
                elif detectCollisionsL(square.x+10,square.y,square.w-50,square.h,currentLine.x,currentLine.y,currentLine.w,currentLine.h) == True and countl < 1:
                        if normGrav == True:
                                normGrav = False
                        elif normGrav == False:
                                normGrav = True
                        countl += 1
                elif detectCollisionsB(square.x,square.y,square.w,square.h,currentLine.x,currentLine.y,currentLine.w,currentLine.h) == True and countl < 1:
                        if normGrav == True:
                                normGrav = False
                        elif normGrav == False:
                                normGrav = True
                        countl += 1
                elif detectCollisionsT(square.x,square.y,square.w,square.h,currentLine.x,currentLine.y,currentLine.w,currentLine.h) == True and countl < 1:
                        if normGrav == True:
                                normGrav = False
                        elif normGrav == False:
                                normGrav = True
                        countl += 1
        countl = 0


        if right_pressed == False and left_pressed == False:
                square.speed = 2
        if right_pressed == True:
                square.moveR(collisionR)
        if left_pressed == True:
                square.moveL(collisionL)
        if normGrav == True:
                square.moveD(collisionB)
        else:
                square.moveU(collisionT)

        #If collision with moving objects or collision with spikes, you die and restart from the beginning of the level
        #So many ways to die
        if collisionST == True or collisionSB == True or collisionSL == True or collisionSR == True or collisionKT == True or collisionKB == True or collisionKL == True or collisionKR == True:
                numofDeaths += 1
                square = Hero(startingPosition)

        #Prevents smearing across the screen
        screen.fill(white)
        #Prints the text on the first screen
        if level == 0:
                screen.blit(controls,(150,100))
                screen.blit(space,(50,200))
                screen.blit(startGame,(150,300))
                screen.blit(arrows,(250,145))

        #Prints the text on the last screen
        if level == 20:
                screen.blit(GameOver,(50,100))
       
        #Displays all the Moving objects
        for i in listofCherries:
                if i.motion == "Horizental":
                        i.bounce()
                        i.moveH()
                if i.motion == "Vertical":
                        i.bounce()
                        i.moveV()
                i.display()
      
        #Displays all the line
        for i in listofLines:
                i.display()
      
        #Displays all the spikes
        for i in listofSpikes:
                i.display()

        #Displays all the Blocks
        for i in listofSquares:
                i.display()

        #Displays the Main Hero
        square.display()

        Title = '"' + str(name) + '"'
        #Displays the number of deaths so far
        text(screen,"Deaths:" + str(numofDeaths),450,410,15,blackColor,"pressstart2p")
        #Displays the name of each level on screen
        text(screen,Title,0,410,14,blackColor,"pressstart2p")
        pygame.display.update()


pygame.quit()
sys.exit()
