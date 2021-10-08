from turtle import Turtle, Screen, setpos, hideturtle
import random
#Turtle_Game v.2.0
#Made by NthAccacuH

#bg
bg=Turtle()
bg.speed(0)
bg.ht()
bg.color("black")
bg.up()
bg.begin_fill()
bg.goto(-10000, -10000)
bg.down()
bg.goto(10000, -10000)
bg.goto(10000, 10000)
bg.goto(-10000, 10000)
bg.goto(-10000, -10000)
bg.end_fill()

#Кнопки
screen=Screen()

#Ловушки
boom=Turtle()
boom.up()
boom.speed(0)
boom.goto(-8000,8000)
screen.addshape("trap.gif")
boom.shape("trap.gif")
tX=-8000
tY=-8000

#Спуск
descent=Turtle()
lvl=1
screen.addshape("descent.gif")
descent.shape("descent.gif")
descent.up()
descent.speed(0)
descentX=random.randint(-9,9)*50
deds=random.randint(1,3)
if deds==1:
    descentY=150
else:
    if deds==2:
        descentY=-50
    else:
        if deds==3:
            descentY=400
descent.goto(descentX-5,descentY-25)
print(descentX,descentY)

def des():
    global descentX
    global descentY
    deds=random.randint(1,3)
    if deds==1:
        descentY=150
    else:
        if deds==2:
            descentY=-50
        else:
            if deds==3:
                descentY=400
    descentX=random.randint(-9,9)*50
    descent.goto(descentX-5,descentY-20)
    descent.clear()
    print(descentX-20,descentY)
def desif():
        global PlayerX
        global PlayerY
        global lvl
        global EnX
        global EnY
        print(PlayerX,PlayerY)
        if descentX==PlayerX:
            if descentY==PlayerY:
                des()
                level.clear()
                PlayerX=random.randint(-9,9)*50
                player.goto(PlayerX,PlayerY-20)
                EnX=random.randint(-9,9)*50
                e.goto(EnX,EnY)
                lvl=lvl+1
                boom.goto(-900000,-900000)
                boss1if()
                print("Descent on",descentX, descentY)

#Рамка
turtle=Turtle()
turtle.up()
t=turtle
t.ht()
t.speed(0)
t.color("red")
t.goto(-500, -450)
t.down()
t.goto(500, -450)
t.goto(500, -300)
t.goto(-500, -300)
t.goto(-500, -300)
t.goto(-500, -450)

#Пол
#bgr=Turtle()
#bgr.up()
#bgr.speed(0)
#psplayer=Turtle()
#psplayer.up()
#psplayer.speed(0)
#def bug():
#    screen.addshape("bg.gif")
#    bgr.shape("bg.gif


#Статистика
he=Turtle()
he.up()
he.goto(-450, -320)
he.ht()
he.color("green2")
he.down()
def Hel():
    level.goto(-450,-330)
    level.clear()
    level.write("Этаж№ ",lvl)
    level.write(lvl)
    print(lvl)
    he.clear()
    if PlayerX == EnX:
        if PlayerY == EnY:
            he.color("red")
            he.write("Вы проиграли.")
            he.exit()
    else:
        he.color("green2")
        he.write("Нажимайте WASD для передвижения. Если вы столкнётесь с врагом, вы проиграете. Собирайте предметы, чтобы вам было легче проходить уровни.")
level=Turtle()
level.ht()
level.speed(0)
level.up()
level.color("green2")
level.goto(-450,-330)


#Игрок
player=Turtle()
kng="kn.gif"
PlayerX=0
PlayerY=0
player.speed(0)
screen.addshape(kng)
player.shape(kng)
player.shapesize(50,50)
player.pensize(0.1)

#Управление игрока
def MoveA():
    Hel()
    bombs=0
    global PlayerX
    kng="kn2.gif"
    screen.addshape(kng)
    player.shape(kng)
    if PlayerX>-500:
        player.up()
        player.clear()
        PlayerX=PlayerX-50
        player.goto(PlayerX,PlayerY-20)
        player.down()
        h=random.randint(1,2)
        desif()
        if h==1:
            EnW()
        else:
            EnA()
        if bombs==0:
            if tX==PlayerX:
                if tY==PlayerY:
                    he.color("red")
                    he.clear()
                    he.write("Вы проиграли.")
                    he.exit()
                    
        
        
def MoveD():
    Hel()
    bombs=0
    global PlayerX
    kng="kn.gif"
    player.shape(kng)
    if PlayerX<500:
        player.up()
        player.clear()
        PlayerX=PlayerX+50
        player.goto(PlayerX,PlayerY-20)
        player.down()
        h=random.randint(1,2)
        desif()
        if h==1:
            EnW()
        else:
            EnA()
        if bombs==0:
            if tX==PlayerX:
                if tY==PlayerY:
                    he.color("red")
                    he.clear()
                    he.write("Вы проиграли.")
                    he.exit()
        

def MoveW():
    Hel()
    bombs=0
    global PlayerY
    if PlayerY<450:
        player.up()
        player.clear()
        PlayerY=PlayerY+50
        player.goto(PlayerX,PlayerY-20)
        player.down()
        h=random.randint(1,2)
        desif()
        if h==1:
            EnW()
        else:
            EnA()
        if bombs==0:
            if tX==PlayerX:
                if tY==PlayerY:
                    he.color("red")
                    he.clear()
                    he.write("Вы проиграли.")
                    he.exit()
        

def MoveS():
    Hel()
    bombs=0
    global PlayerY
    if PlayerY>-150:
        player.up()
        player.clear()
        PlayerY=PlayerY-50
        player.goto(PlayerX,PlayerY-20)
        player.down()
        h=random.randint(1,2)
        desif()
        if h==1:
            EnW()
        else:
            EnA()
        if bombs==0:
            if tX==PlayerX:
                if tY==PlayerY:
                    he.color("red")
                    he.clear()
                    he.write("Вы проиграли.")
                    he.exit()

def TraP():
    Hel()
    global tX
    global tY
    global bombs
    bombs=1
    boom.goto(PlayerX, PlayerY-20)
    tX=PlayerX
    tY=PlayerY
    

#Босс. 5ур
knb=Turtle()
screen.addshape("knb.gif")
knb.shape("knb.gif")
knb.up()
knb.speed(0)
knbX=-90000
knbY=0
bh=3
knb.goto(knbX,knbY)
def boss1if():
    global knbX
    global knbY
    if lvl==5:
        knbX=0
        knbY=0
        knb.goto(knbX, knbY)

screen.onkey(MoveA,"a")
screen.onkey(MoveD,"d")
screen.onkey(MoveW,"w")
screen.onkey(MoveS,"s")
screen.onkey(TraP,"space")

#Управление врага
e=Turtle()
EnX=200
EnY=0
e.speed(0)
e.ht()
screen.addshape("en.gif")
screen.addshape("en2.gif")
e.shape("en.gif")
def EnW():
    babah()
    global EnY
    if EnY>-90000:
        e.up()
        Y=random.randint(1,2)
        if Y==1:
            if lvl !=5:
                if EnY>-150:
                    e.clear()
                    EnY=EnY-50
                    e.goto(EnX,EnY)
            if Y==2:
                if lvl!=5:
                    if EnY<200:
                        e.clear()
                        EnY=EnY+50
                        e.goto(EnX,EnY)

def EnA():
    babah()
    e.st()
    global EnX
    if EnX>-90000:
        e.up()
        X=random.randint(1,2)
        if X==1:
            if EnX>-500:
                e.shape("en2.gif")
                e.clear()
                EnX=EnX-50
                e.goto(EnX,EnY-20)

        if X==2:
            if EnX<500:
                e.shape("en.gif")
                e.clear()
                EnX=EnX+50
                e.goto(EnX,EnY-20)

def babah():
    global EnX
    global EnY
    global tX
    global tY
    if EnX==tX:
        if EnY==tY:
            EnX=-9000000
            EnY=-9000000
            e.up()
            e.clear()
            e.goto(-9000000,-9000000)
            tX=-900000
            tY=-900000
            boom.goto(-900000,-900000)


screen.listen()
