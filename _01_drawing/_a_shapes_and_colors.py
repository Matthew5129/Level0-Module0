import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    donkey_kong = turtle.Turtle()

    # Make your turtle shape 'turtle', .shape('turtle')
    donkey_kong.shape('turtle')
    # Set your turtle's speed using .speed(2)
    donkey_kong.speed(150)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    donkey_kong.color('red')
    # Move your turtle forward using .forward(100)
    donkey_kong.forward(5)
    # TEST    Did your turtle move forward?
    #Yes
    # Move your turtle left or right using .left(90) or .right(90)
    for i in range(0):
        donkey_kong.forward(90)
        donkey_kong.right(90)


    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    for i in range(9)
    donkey_kong.goto(90)
    donkey_kong.circle(90)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
