import turtle
from random import randint as R
import time

class GameWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.kerroin = 2
    
    def create_world(self):
        self.world = turtle.Screen()
        self.world.setup(self.width*60, self.height*60)
        self.world.tracer(10)

        self.berry = turtle.Turtle()
        self.berry.penup()
        self.berry.shape("square")
        self.berry.color("Red")

        rajoitin = turtle.Turtle()
        rajoitin.penup()
        rajoitin.hideturtle()
        rajoitin.goto(self.width*-20, self.height*20)
        rajoitin.pendown()
        rajoitin.pencolor("Yellow")
        rajoitin.pensize(10)
        rajoitin.goto(self.width*20, self.height*20)
        rajoitin.goto(self.width*20, self.height*-20)
        rajoitin.goto(self.width*-20, self.height*-20)
        rajoitin.goto(self.width*-20, self.height*20)
    
    def render_snake(self, snake):
        Laskin = 0
        body = snake.pos.copy()
        body.pop(-1)
        for i in body:
            snake.wormer[Laskin].goto(i[0]*self.kerroin,i[1]*self.kerroin)
            Laskin +=1
        snake.worm.goto(snake.pos[-1][0]*self.kerroin,snake.pos[-1][1]*self.kerroin)
    
    def render_food(self, food):
        self.berry.goto(food[0]*self.kerroin,food[1]*self.kerroin)

    def update(self):
        self.world.update()

    def check(self, food, snake, body):
        for i in body:
            if snake[-1][0] == i[0] and snake[-1][1] == i[1]:
                return 0
        if snake[-1][0] > self.width*9 or snake[-1][1] > self.height*9 or snake[-1][0] < self.width*-9 or snake[-1][1] < self.height*-9:
            return 0
        if snake[-1][0] == food[0] and snake[-1][1] == food[1]:
            return 1
        else:
            return 2
#
class Snake:
    def __init__(self,color, x, y):
        self.pos = [[x,y],[x,y+10]]
        self.dir = [0,10] #Tämä + Uusin = seuraava¨
        self.behind = [0,-10]
        self.color = color

        self.worm = turtle.Turtle()
        self.worm.penup()
        self.worm.shape("square")
        self.worm.color(color)

        self.wormer = []
        self.wormer = [turtle.Turtle()]
        self.wormer[0].penup()
        self.wormer[0].shape("square")
        self.wormer[0].color("Dark"+color)
    
    def move(self):
        new_list = self.pos[-1]
        new_x = new_list[0] + self.dir[0]
        new_y = new_list[1] + self.dir[1]
        new_list = [new_x,new_y]
        self.pos.append(new_list)
        self.pos.pop(0)
        self.behind = [(self.pos[-2][0]-self.pos[-1][0])*-1,(self.pos[-2][1]-self.pos[-1][1])*-1]
    
    def add(self):
        self.pos.insert(0,self.pos[0])
        self.wormer.append(turtle.Turtle())
        self.wormer[-1].penup()
        self.wormer[-1].shape("square")
        self.wormer[-1].color("Dark"+self.color)
    
    def up(self):
        if self.behind != [0,-10]:
            self.dir = [0,10]
    def down(self):
        if self.behind != [0,10]:
            self.dir = [0,-10]
    def left(self):
        if self.behind != [10,0]:
            self.dir = [-10,0]
    def right(self):
        if self.behind != [-10,0]:
            self.dir = [10,0]
#
class Food:
    def __init__(self,X,Y, pisteet):
        self.pos = [X,Y]
        self.points = 0
        self.kirjoitetaanko = pisteet
        self.kirjuri = turtle.Turtle()
        self.kirjuri.penup()
        self.kirjuri.hideturtle()
        self.kirjuri.goto(-200, 200)
        self.kirjuri.color("Black")
        #
    def move_food(self, max_width, max_height, suljetut):
        matrix = []
        for i in range(max_width*-1+1, max_width):
            for o in range(max_height*-1+1, max_height):
                matrix.append([i*10, o*10])
        for i in suljetut:
            if i in matrix:
                matrix.pop(matrix.index(i))
        if len(matrix) == 1 and self.kirjoitetaanko:
            self.kirjuri.clear()
            self.kirjuri.write("Voitit!", font=("Yu Gothic UI Semibold", 20, "italic"))
        if self.kirjoitetaanko:
            self.points +=1
            self.kirjuri.clear()
            self.kirjuri.write(self.points, font=("Yu Gothic UI Semibold", 20, "italic"))
        self.pos = matrix[R(0, len(matrix)-1)]
#
def two_player():
    game_world = GameWorld(10,10)
    food = Food(R(10*-1,10)*10,R(10*-1, 10)*10, False)
    snake = Snake("Green", -10,0)
    snake2 = Snake("Blue", 10, 0)
    game_world.create_world()
    game_world.world.listen()
    last = time.time()
    while True:
        turtle.onkey(snake.up, "w")
        turtle.onkey(snake.down, "s")
        turtle.onkey(snake.left, "a")
        turtle.onkey(snake.right, "d")

        turtle.onkey(snake2.up, "Up")
        turtle.onkey(snake2.down, "Down")
        turtle.onkey(snake2.left, "Left")
        turtle.onkey(snake2.right, "Right")

        game_world.render_snake(snake)
        game_world.render_snake(snake2)
        game_world.render_food(food.pos)

        if time.time() > last+0.3:
            snake2.move()
            snake.move()
            last = time.time()
        if game_world.check(food.pos, snake.pos, snake2.pos) == 0 and game_world.check(food.pos, snake2.pos, snake.pos) == 0:
            food.kirjuri.clear()
            food.kirjuri.pencolor("Orange")
            food.kirjuri.write("Crash!", font=("Yu Gothic UI Semibold", 20, "italic"))
            game_world.update()
            time.sleep(3)
            break
        elif game_world.check(food.pos, snake.pos, snake2.pos) == 0:
            food.kirjuri.clear()
            food.kirjuri.pencolor("Blue")
            food.kirjuri.write("Voitit!", font=("Yu Gothic UI Semibold", 20, "italic"))
            game_world.update()
            time.sleep(3)
            break
        elif game_world.check(food.pos, snake2.pos, snake.pos) == 0:
            food.kirjuri.clear()
            food.kirjuri.pencolor("Green")
            food.kirjuri.write("Voitit!", font=("Yu Gothic UI Semibold", 20, "italic"))
            game_world.update()
            time.sleep(3)
            break
        if game_world.check(food.pos, snake.pos, snake.pos[0::-2]) == 1:
            food.move_food(10,10, snake.pos+snake2.pos)
            snake.add()
        elif game_world.check(food.pos, snake.pos, snake.pos[0::-2]) == 0:
            food.kirjuri.clear()
            food.kirjuri.pencolor("Blue")
            food.kirjuri.write("Voitit!", font=("Yu Gothic UI Semibold", 20, "italic"))
            game_world.update()
            time.sleep(3)
            break
        if game_world.check(food.pos, snake2.pos, snake2.pos[0::-2]) == 1:
            food.move_food(10,10, snake2.pos+snake.pos)
            snake2.add()
        elif game_world.check(food.pos, snake2.pos, snake2.pos[0::-2]) == 0:
            food.kirjuri.clear()
            food.kirjuri.pencolor("Green")
            food.kirjuri.write("Voitit!", font=("Yu Gothic UI Semibold", 20, "italic"))
            game_world.update()
            time.sleep(3)
            break
        game_world.update()
    game_world.world.clear()
#
def single_player():
    game_world = GameWorld(10,10)
    food = Food(R(10*-1,10)*10,R(10*-1, 10)*10, True)
    snake = Snake("Green", -10,0)
    game_world.create_world()
    game_world.world.listen()
    last = time.time()
    while True:
        turtle.onkey(snake.up, "w")
        turtle.onkey(snake.down, "s")
        turtle.onkey(snake.left, "a")
        turtle.onkey(snake.right, "d")
        game_world.render_snake(snake)
        game_world.render_food(food.pos)

        if time.time() > last+0.3:
            snake.move()
            last = time.time()
        if game_world.check(food.pos, snake.pos, snake.pos[0::-2]) == 1:
            food.move_food(10,10, snake.pos)
            snake.add()
        elif game_world.check(food.pos, snake.pos, snake.pos[0::-2]) == 0:
            food.kirjuri.clear()
            food.kirjuri.write(str(food.points) + " + L", font=("Yu Gothic UI Semibold", 20, "italic"))
            game_world.update()
            time.sleep(3)
            break
        game_world.update()
    game_world.world.clear()
#
def menu_press(x,y):
    if x > -120.0 and y < 80.0 and x < -60.0 and y > 20.0:
        menu_screen.clearscreen()
        single_player()
        draw_menu()
    if x < 120.0 and y < 80.0 and x > 60.0 and y > 20.0:
        menu_screen.clearscreen()
        two_player()
        draw_menu()
def draw_menu():
    global menu_screen
    menu_screen = turtle.Screen()
    menu_screen.tracer(10)
    single = turtle.Turtle()
    single.penup()
    single.goto(-110,80)
    single.write("Yksin", font=("Yu Gothic UI Semibold", 15, "italic"))
    single.color("Green")
    single.shape("square")
    single.goto(-90,50)
    single.turtlesize(3)
    #
    couple = turtle.Turtle()
    couple.penup()
    couple.goto(60,80)
    couple.write("Kaksi", font=("Yu Gothic UI Semibold", 15, "italic"))
    couple.color("Blue")
    couple.shape("square")
    couple.goto(90,50)
    couple.turtlesize(3)
def game_loop():
    draw_menu()
    while True:
        menu_screen.update()
        menu_screen.onclick(menu_press)
game_loop()
