import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    colors = ['red', 'blue', 'green', 'yellow', 'orange']

    baseSize = 200          # the size of the black part of the star
    flameSize = 130         # the length of the flaming arms
    
    # Make a new turtle
    ninja_star = turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    ninja_star.shape('turtle')
    # Set the turtle width to 2
    ninja_star.width(2)
    # Set the turtle speed to 0 (fastest)
    ninja_star.speed(0)
    # Use a for loop to repeat all of the code below ONE time (we will change
    # this later)
    for i in range(25):
        # TURN RIGHT     Turn the turtle 1/8 of a circle (hint: 360 degrees
        #                will turn a full circle)
        ninja_star.right(360/8)
        # DRAW           Move the turtle 64 pixels
        ninja_star.forward(64)
        # TURN LEFT      Turn the turtle 40 degrees to the LEFT. (Negative
        #                numbers will turn the turtle counter-clockwise.)
        ninja_star.left(40)
        # DRAW FLAME     Move the turtle the distance in the variable flameSize
        ninja_star.fillcolor('orange')

        ninja_star.begin_fill()

        ninja_star.forward(flameSize)
        #                Turn the turtle to the right 170 degrees
        ninja_star.right(170)
        #                Move the turtle the distance in the variable flameSize (again)
        ninja_star.forward(flameSize)
        #  TURN RIGHT    Turn the turtle 62 degrees to the right
        ninja_star.right(62)
        #  DRAW          Move the turtle the distance in the variable baseSize
        ninja_star.forward(baseSize)
        # Call the turtle .end_fill() method
        ninja_star.end_fill()
    # Hide your turtle so you can see the pattern.
    ninja_star.hideturtle()
    # TEST   Run the program. Check that your shape is the same as the first
    #        picture in the recipe. This is one arm of the ninja star.

    # COLOR  Change the turtle's pen color so that the flame is a different
    #        color to the rest of the star. Run the program again. Check the
    #        second picture in the recipe.

    # LOOP   When you have one arm looking right, change your for loop to
    #        repeat 25 times.

    # call the turtle .done() method
    turtle.done()
