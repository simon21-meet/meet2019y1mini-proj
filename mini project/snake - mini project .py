
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) # It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH =6
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    stamp = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(stamp)


#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i  in range (START_LENGTH) :
    x_pos=snake.pos()[0]#-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+= SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()


#snake.direction = "Up"

def up():
    snake.direction="Up" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")
turtle.onkeypress(up, "Up") # Create listener for up key
turtle.listen()
          
def down():
    turtle.direction="Down"
    move_snake()
turtle.onkeypress(down, "Down")
turtle.listen()

def left():
    turtle.direction= "Left"
    move_snake()
turtle.onkeypress(left, "Left")
turtle.listen()

def right():
    turtle.direction="Right"
    move_snake()
turtle.onkeypress(right, "Right")
turtle.listen()


def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    if snake.direction=="Right":
          snake.goto(x_pos, y_pos+SQUARE_SIZE)
          print("You moved right!")
    elif snake.direction=="Down":
          snake.goto(x_pos, y_pos-SQUARE_SIZE)
          print('You moved left')
          
   #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    ___________()

    

turtle.mainloop()

