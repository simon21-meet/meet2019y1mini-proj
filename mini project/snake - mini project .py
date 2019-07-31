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
snake.shape("circle")

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

turtle.listen()

snake.direction = "Up"
turtle.register_shape("apple2.gif") #Add trash picture
food = turtle.clone()
food.shape("apple2.gif") 

#Locations of food
food_pos = []
food_stamps = []


for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())
    turtle.hideturtle
    
  

UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400



def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")
turtle.onkeypress(up, "Up") # Create listener for up key

          
def down():
    snake.direction="Down"
    print("You pressed the down key!")
turtle.onkeypress(down, "Down")


def left():
    snake.direction= "Left"
    print("You pressed the left key!")
turtle.onkeypress(left, "Left")


def right():
    snake.direction="Right"
    print("You pressed the right key")
turtle.onkeypress(right, "Right")


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    food_pos.append(food.pos())
    foodid=food.stamp()
    food_stamps.append(foodid)
    
  
snake.Points_list = 0

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

    elif snake.direction=="Right":
          snake.goto(x_pos+SQUARE_SIZE, y_pos)
          print("You moved right!")
    elif snake.direction=="Left":
          snake.goto(x_pos-SQUARE_SIZE, y_pos)
          print('You moved left')

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos<=LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos>=UP_EDGE:
        print("You hit the top edge! Game over")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("You hit the bottom edge! Game over")
        quit()
        
          
   #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        snake.Points_list+=1
        print("You have " + str(snake.Points_list) + " points!")
    else:
        remove_tail()   
    

    if len(food_stamps)<1:
        make_food()

    turtle.ontimer(move_snake,TIME_STEP)

    if snake.pos() in pos_list[:-1]:
        quit()
    
move_snake()

    
turtle.mainloop()

