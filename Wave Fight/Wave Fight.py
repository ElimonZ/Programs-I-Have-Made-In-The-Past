import turtle
import time
#
Win = turtle.Screen()
Win.tracer(0)
#Kopio LessIsMoreMiikaGamejamista
Hahmotin = turtle.Turtle()
Hahmotin.penup()
def Hahmo():
    Hahmotin.clear()
    Hahmotin.showturtle()
    Hahmotin.shape("square")
    Hahmotin.turtlesize(1)
    Hahmotin.color("#2218cf")
    Hahmotin.stamp()
    Hahmotin.hideturtle()
    Hahmotin.color("#45e0fc")
    Hahmotin.pensize(10)
    Hahmotin.forward(9)
    Hahmotin.pendown()
    Hahmotin.left(90)
    Hahmotin.forward(3)
    Hahmotin.right(45)
    Hahmotin.penup()
    Hahmotin.color("#caad77")
    Hahmotin.forward(10)
    Hahmotin.pendown()
    Hahmotin.forward(-1)
    Hahmotin.penup()
    Hahmotin.forward(-9)
    Hahmotin.left(225)
    Hahmotin.color("#45e0fc")
    Hahmotin.forward(6)
    Hahmotin.color("#caad77")
    Hahmotin.left(45)
    Hahmotin.forward(10)
    Hahmotin.pendown()
    Hahmotin.forward(-1)
    Hahmotin.penup()
    Hahmotin.forward(-9)
    Hahmotin.right(225)
    Hahmotin.color("#45e0fc")
    Hahmotin.penup()
    Hahmotin.forward(3)
    Hahmotin.left(90)
    Hahmotin.forward(9)
    Hahmotin.left(180)
    Hahmotin.forward(78)
    Hahmotin.color("yellow")
    Hahmotin.pendown()
    Hahmotin.forward(2)
    Hahmotin.penup()
    Hahmotin.forward(-80)
#
def A():
    Hahmotin.left(45)
    Hahmo()
#
def D():
    Hahmotin.right(45)
    Hahmo()
#
def W():
    Hahmotin.forward(10)
    Hahmo()
#
def S():
    Hahmotin.forward(-10)
    Hahmo()
#
Kartoitin = turtle.Turtle()
def Kartta():
    Kartoitin.goto(0,0)
    Kartoitin.shape("square")
    Kartoitin.turtlesize(30)
    Kartoitin.showturtle()
    Kartoitin.color("#107038")
    Kartoitin.stamp()
    Kartoitin.hideturtle()
    Kartoitin.penup()
    Kartoitin.goto(-300,0)
    Kartoitin.pendown()
    Kartoitin.color("darkgreen")
    Kartoitin.pensize(30)
    Kartoitin.goto(-180,0)
    Kartoitin.goto(-180,15)
    Kartoitin.color("#b3972b")
    Kartoitin.goto(-180,150)
    Kartoitin.goto(-120,150)
    Kartoitin.goto(-120,-90)
    Kartoitin.goto(-270,-90)
    Kartoitin.goto(-270,-210)
    Kartoitin.goto(120,-210)
    Kartoitin.goto(120,-90)
    Kartoitin.goto(120,120)
    Kartoitin.goto(300,120)
#
Peli = True
#
Viha = turtle.Turtle()
Viha.shape("square")
Viha.color("red")
Viha.penup()
Vihut = []
Aika = 40
X = -300
Y = 0
Askel = 5
#
def VihollistenLiike():
    global X
    global Y
    global Askel
    global Peli
    Laskin = 0
    Viha.clear()
    while Laskin != len(Vihut):
        if Vihut[Laskin][2] == 0:
            if Vihut[Laskin][0] == -180:
                Vihut[Laskin][2] = 1
                Vihut[Laskin][1] +=Askel
            else:
                Vihut[Laskin][0] +=Askel
        #
        elif Vihut[Laskin][2] == 1:
            if Vihut[Laskin][1] == 150:
                Vihut[Laskin][2] = 2
                Vihut[Laskin][0] +=Askel
            else:
                Vihut[Laskin][1] +=Askel
        #
        elif Vihut[Laskin][2] == 2:
            if Vihut[Laskin][0] == -125:
                Vihut[Laskin][2] = 3
                Vihut[Laskin][0] +=Askel
            else:
                Vihut[Laskin][0] +=Askel
        #
        elif Vihut[Laskin][2] == 3:
            if Vihut[Laskin][1] == -90:
                Vihut[Laskin][2] = 4
                Vihut[Laskin][0] -=Askel
            else:
                Vihut[Laskin][1] -=Askel
        #
        elif Vihut[Laskin][2] == 4:
            if Vihut[Laskin][0] == -270:
                Vihut[Laskin][2] = 5
                Vihut[Laskin][1] -=Askel
            else:
                Vihut[Laskin][0] -=Askel
        #
        elif Vihut[Laskin][2] == 5:
            if Vihut[Laskin][1] == -210:
                Vihut[Laskin][2] = 6
                Vihut[Laskin][0] +=Askel
            else:
                Vihut[Laskin][1] -=Askel
        #
        elif Vihut[Laskin][2] == 6:
            if Vihut[Laskin][0] == 120:
                Vihut[Laskin][2] = 7
                Vihut[Laskin][1] +=Askel
            else:
                Vihut[Laskin][0] +=Askel
        #
        elif Vihut[Laskin][2] == 7:
            if Vihut[Laskin][1] == 120:
                Vihut[Laskin][2] = 8
                Vihut[Laskin][0] +=Askel
            else:
                Vihut[Laskin][1] +=Askel
        #
        elif Vihut[Laskin][2] == 8:
            if Vihut[Laskin][0] == 300:
                Vihut[Laskin][2] = 9
            else:
                Vihut[Laskin][0] +=Askel
        #LLLLLLLLL
        elif Vihut[Laskin][2] == 9:
            Maali.goto(0,0)
            Peli = False
            Maali.write("L", font = ("Yu Gothic UI Semibold", 50, "italic"))
            time.sleep(10)
        #
        Viha.goto(Vihut[Laskin][0],Vihut[Laskin][1])
        if Vihut[Laskin][3] == 1:
            Viha.color("red")
        elif Vihut[Laskin][3] == 2:
            Viha.color("yellow")
        elif Vihut[Laskin][3] == 3:
            Viha.color("purple")
        elif Vihut[Laskin][3] == 4:
            Viha.color("black")
        Viha.showturtle()
        Viha.stamp()
        Viha.hideturtle()
        Laskin +=1
Vihut.append([-300,0,0, 1])
#
Maali = turtle.Turtle()
Maali.penup()
Maali.shape("triangle")
Maali.color("yellow")
#
CoolDown = 0
CoolUp = 20
Cooler = turtle.Turtle()
Cooler.penup()
Cooler.hideturtle()
Cooler.color("yellow")
Cooler.goto(80,150)
#
Ammus = turtle.Turtle()
Ammus.color("yellow")
Ammus.pensize(10)
def PelaajanTuli():
    global CoolDown
    global CoolUp
    Ammus.penup()
    Ammus.forward(20)
    Ammus.pendown()
    #
    Laskuri = 0
    if CoolDown > CoolUp:
        Ammus.forward(60)
    while Laskuri != len(Vihut) and len(Vihut) != 0 and CoolDown > CoolUp:
        #CoolDown = 0
        CoolDown -=20
        if Vihut[Laskuri][0] < Ammus.xcor()+20 and Vihut[Laskuri][0] > Ammus.xcor()-20 and Vihut[Laskuri][1] < Ammus.ycor()+20 and Vihut[Laskuri][1] > Ammus.ycor()-20:
            Vihut[Laskuri][3] -=1
            if Vihut[Laskuri][3] == 0:
                Vihut.pop(Laskuri)
        Laskuri +=1
    #
#
Levu = turtle.Turtle()
Levu.penup()
Levu.hideturtle()
Levu.color("yellow")
Taso = 0
Tulo = [[-300,0,0, 1],[-300,0,0, 2]]
def Level():
    global Taso
    global Aika
    global Tulo
    global Peli
    global Askel
    if 0 == len(Tulo) and len(Vihut) == 1:
        Taso +=1
    #
        if Taso == 1:
            Aika = 30
            Tulo = [[-300,0,0, 1],[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 2]]
        elif Taso == 2:
            Tulo = [[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 3],[-300,0,0, 1]]
        #
        elif Taso == 3:
            Aika = 15
            Tulo = [[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 2],[-300,0,0, 1]]
        #
        elif Taso == 4:
            Aika = 30
            Tulo = [[-300,0,0, 2],[-300,0,0, 3],[-300,0,0, 1],[-300,0,0, 2]]
        #
        elif Taso == 5:
            Aika = 25
            Tulo = [[-300,0,0, 4],[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 2]]
        #
        elif Taso == 6:
            Aika = 15
            Tulo = [[-300,0,0, 4],[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 2],[-300,0,0, 3]]
            #
        elif Taso == 7:
            Aika = 30
            Tulo = [[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 3],[-300,0,0, 2],[-300,0,0, 4]]
        #
        elif Taso == 8:
            Tulo = [[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 3],[-300,0,0, 2],[-300,0,0, 4],[-300,0,0, 4],[-300,0,0, 2]]
        #
        elif Taso == 9:
            Aika = 20
            Tulo = [[-300,0,0, 4],[-300,0,0, 4]]
        #
        elif Taso == 10:
            Aika = 15
            Tulo = [[-300,0,0, 4],[-300,0,0, 4]]
        #
        elif Taso == 11:
            Aika = 20
            Tulo = [[-300,0,0, 4],[-300,0,0, 4]]
        #
        elif Taso == 12:
            Aika = 25
            Tulo = [[-300,0,0, 2],[-300,0,0, 3],[-300,0,0, 2]]
        #
        elif Taso == 13:
            Aika = 15
            Tulo = [[-300,0,0, 2],[-300,0,0, 1],[-300,0,0, 3],[-300,0,0, 2],[-300,0,0, 4],[-300,0,0, 4],[-300,0,0, 2]]
        #
        elif Taso == 14:
            Tulo = [[-300,0,0, 1],[-300,0,0, 2],[-300,0,0, 3],[-300,0,0, 2],[-300,0,0, 4],[-300,0,0, 1],[-300,0,0, 3]]
        #
        elif Taso == 15:
            Aika = 15
            Tulo = [[-300,0,0, 1],[-300,0,0, 2],[-300,0,0, 3],[-300,0,0, 2],[-300,0,0, 4],[-300,0,0, 1],[-300,0,0, 3]]
        #Voitto
        elif True:
            Maali.goto(0,0)
            Peli = False
            Maali.write("W", font = ("Yu Gothic UI Semibold", 50, "italic"))
            time.sleep(10)
#
Kartta()
Hahmo()
Win.update()
#
Win.listen()
Ajastin = 0
while Peli:
    #
    Level()
    Ammus.clear()
    Cooler.clear()
    Levu.clear()
    Levu.goto(-280,180)
    Levu.write(str(len(Tulo)) + " still incoming!", font = ("Yu Gothic UI Semibold", 20, "italic"))
    Levu.goto(-280,210)
    Levu.write("Level: " + str(Taso) + "/15", font = ("Yu Gothic UI Semibold", 20, "italic"))
    Cooler.write(str(CoolDown) + "/" + str(CoolUp) + " for a shot!", font = ("Yu Gothic UI Semibold", 20, "italic"))
    #
    Maali.goto(300,131)
    Maali.left(15)
    Win.update()
    time.sleep(0.1)
    Maali.goto(300,130)
    Maali.left(15)
    Win.update()
    time.sleep(0.1)
    #
    Ammus.goto(Hahmotin.xcor(),Hahmotin.ycor())
    Ammus.setheading(Hahmotin.heading())
    #
    Win.onkeypress(A,"a")
    Win.onkeypress(D,"d")
    Win.onkeypress(W,"w")
    Win.onkeypress(S,"s")
    Win.onkeypress(PelaajanTuli,"space")
    #
    if Ajastin > Aika-1 and len(Tulo) != 0:
        Ajastin = 0
        Vihut.append(Tulo[0])
        Tulo.pop(0)
    VihollistenLiike()
    Ajastin +=1
    CoolDown +=1
#