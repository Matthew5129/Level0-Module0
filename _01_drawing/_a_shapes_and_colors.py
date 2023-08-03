import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    bobby1545 = turtle.Turtle()

    # Make your turtle shape 'turtle', .shape('turtle')
    bobby1545.shape('turtle')
    # Set your turtle's speed using .speed(2)
    bobby1545.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    bobby1545.color('dark green')
    bobby1545.pencolor('dark green')
    # Move your turtle forward using .forward(100)
    bobby1545.forward(5)
    # TEST    Did your turtle move forward?
    #Yes
    # Move your turtle left or right using .left(90) or .right(90)
    for i in range(0):
        bobby1545.forward(90)
        bobby1545.right(90)


    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    for i in range(1):
        bobby1545.fillcolor('dark green')
        bobby1545.begin_fill()

        bobby1545.circle(90)

        bobby1545.end_fill()
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done
