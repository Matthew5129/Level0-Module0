import turtle
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def set_background(filename):
    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)


def add_moustache(filename):


    turtle.hideturtle()
    window.addshape
    turtle.shape()
    turtle.color()
    turtle.speed()

    return


# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))

    # 4. Show your moustache by calling the .showturtle() function
    # moustache.showturtle()
    moustache.showturtle(self=turtle)
    # 5. Move your moustache to a new location using .goto(x, y)


if __name__ == '__main__':
    window = turtle.Screen()

    # 1. Find an image of a face online that you want to put a moustache on and
    #    add the file to the folder with your code
    # 2. Call the set_background() function with the image filename inside of the parenthesis
    set_background(face.png)

    # 3. Create a variable called moustache and set it equal to add_moustache('moustache1.gif')
    # moustache = add_moustache('moustache1.gif')
    moustache = add_moustache('moustache1.gif')
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
    turtle.done
