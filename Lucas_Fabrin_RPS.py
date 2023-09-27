# This file was created by Lucas Fabrin
import turtle

from turtle import *

import os

print("The current working directory is (getcwd): " + os.getcwd())

print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

 

 

game_folder = os.path.dirname(__file__)

images_folder = os.path.join(game_folder, 'images')

 

 
# This sets the width and height of  the screen along with the all three images and their dimensions
WIDTH, HEIGHT = 1000, 400

 

rock_w, rock_h = 256, 280

 

paper_w, paper_h = 256, 204

 

scissors_w, scissors_h = 256, 170

 

 
def ycr():
    # setup the rock choosing gif using the os module as rock_image
    you_chose_rock_image = os.path.join(images_folder, 'you_chose_rock.gif')
    # instantiate (create an instance of) the Turtle class for the rock choosing gif
    you_chose_rock_instance = turtle.Turtle()
    # add the rock choosing image as a shape
    screen.addshape(you_chose_rock_image)
    # attach the rock_image to the rock_instance
    you_chose_rock_instance.shape(you_chose_rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    you_chose_rock_instance.penup()
    # assign vars for rock choosing position
    you_chose_rock_pos_x = 0
    you_chose_rock_pos_y = 150
    # set the position of the rock_instance
    you_chose_rock_instance.setpos(you_chose_rock_pos_x,you_chose_rock_pos_y)

def ycp():
    # setup the scissors choosing gif using the os module as scissor image
    you_chose_paper_image = os.path.join(images_folder, 'you_chose_paper.gif')
    # instantiate (create an instance of) the Turtle class for the rock
    you_chose_paper_instance = turtle.Turtle()
    # add the scissor choosing image as a shape
    screen.addshape(you_chose_paper_image)
    # attach the scissor choosing_image to the rock_instance
    you_chose_paper_instance.shape(you_chose_paper_image)
    # remove the pen option from the scissor choosing_instance so it doesn't draw lines when moved
    you_chose_paper_instance.penup()
    # assign vars for scissor position
    you_chose_paper_pos_x = 0
    you_chose_paper_pos_y = 150
    # set the position of the scissor choosing_instance
    you_chose_paper_instance.setpos(you_chose_paper_pos_x,you_chose_paper_pos_y)

def ycs():
    # setup the paper choosing gif using the os module as paper image
    you_chose_scissors_image = os.path.join(images_folder, 'you_chose_scissors.gif')
    # instantiate (create an instance of) the Turtle class for the paper choosing gif
    you_chose_scissors_instance = turtle.Turtle()
    # add the paper choosing image as a shape
    screen.addshape(you_chose_scissors_image)
    # attach the scissor choosing image to the scissor_instance
    you_chose_scissors_instance.shape(you_chose_scissors_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    you_chose_scissors_instance.penup()
    # assign vars for paper position
    you_chose_scissors_pos_x = 0
    you_chose_scissors_pos_y = 150
    # set the position of the paper choosing instance
    you_chose_scissors_instance.setpos(you_chose_scissors_pos_x,you_chose_scissors_pos_y)


 

screen = turtle.Screen()

screen.setup(WIDTH + 4, HEIGHT + 8)  

screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

 

cv = screen.getcanvas()


cv._rootwindow.resizable(False, False)

 

 

 
# sets up the path for the rock gif
rock_image = os.path.join(images_folder, 'rock.gif')

 

rock_instance = turtle.Turtle()

 
# sets up the path for the paper gif
paper_image = os.path.join(images_folder, 'paper.gif')

 

paper_instance = turtle.Turtle()

 
# sets up the path for the scissor gif
scissors_image = os.path.join(images_folder, 'scissors.gif')

 

scissors_instance = turtle.Turtle()

 

 
# defines show_rock and sets up x and y
def show_rock(x,y):

    screen.addshape(rock_image)

    rock_instance.shape(rock_image)

    rock_instance.penup()

    rock_instance.setpos(x,y)

 
# defines show_paper and sets up x and y 
def show_paper(x,y):

    screen.addshape(paper_image)  

    paper_instance.shape(paper_image)

    paper_instance.penup()  

    paper_instance.setpos(x,y)

 
# defines show_scissors and sets up x and y 
def show_scissors(x,y):

    screen.addshape(scissors_image)

    scissors_instance.shape(scissors_image)

    scissors_instance.penup()

    scissors_instance.setpos(x,y)

 

 
# sets up the text for the window 
t = turtle.Turtle()

text = turtle.Turtle()

text.color('deep pink')

t.penup()

text.hideturtle()

 

t.hideturtle()

 
# gives the rock, paper, and scissors images their x and y cordinates when shown
show_rock(-300, 0)

show_paper(0,0)

show_scissors (300,0)

 
# code for the text that asks which image does the player chooses
text.penup()

text.hideturtle()

text.setpos(-300,150)

text.write("What do you choose, rock, paper, or scissors?", False, "left", ("Arial", 24, "normal"))

 
# code for what constitutes for colliding with objects by using thier position and dimensions
def collide(x,y,obj,w,h):

    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:

        return True

    else:

        return False

    t.penup()

 

 

 # code for what happens if player collides with either, scissors, rock, or paper

def player(x, y):

    global text

 
# code for printing "you chose rock" when player collides with rock
    if (collide(x,y,rock_instance, rock_w, rock_h)):

        user_choice = "rock"
        ycr()
# code for printing "you chose paper" when player collides with paper image
    elif(collide(x,y,paper_instance,rock_w,rock_h)):

        user_choice = "paper"
        ycp()
#  code for printing "you chose sicssors" when player collides with scissors
    elif(collide(x,y,scissors_instance,scissors_w,scissors_h)):

        user_choice = "scissors"
        ycs()


   

 
# imports the random generator 
    from random import randint

 
# gives the computer the random choice of rock, paper, or scissors
    choices = ["rock", "paper", "scissors"]

    computer = choices[randint(0, 2)]

 

 
# code for printing what the computer chose
    message = f"Computer chooses... {computer}!"

    x, y = -200, -200

    target_x, target_y = -200, -200

    text.penup()

    text.goto(x, y)

    text.write(message, align="left", font=("Arial", 24, "normal"))

    text.goto(target_x, target_y)

 

 

    import time

 
# time inbetween texts that appear
    time.sleep(1)

 
# code for what the program types depending on the outcome of the player vs computer
    if user_choice == computer:

        result = "It's a tie!"

    elif (user_choice == "rock" and computer == "scissors") or \
  (user_choice == "paper" and computer == "rock") or \
 (user_choice == "scissors" and computer== "paper"):

        result = "You won!"

    else:

        result = "You lost!"

 
# clears the text allowing player to continously play the game
    text.clear()

    text.goto(-82, 0)

    text.write(result, align="left", font=("Arial", 24, "normal"))

   

 

playerchoice = screen.onclick(player)

 

playerchoice = screen.mainloop()