from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)
    # 2. Print out the random variable that you made in step #1
    #print(str(random_num))
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        v = simpledialog.askinteger(title="user", prompt="Guess a number from 1 to 100")
        # 4. Ask the user for a guess using a pop-up window, and save their response
        if v == random_num:
            messagebox.showinfo(title="user", message="Correct!")
            sys.exit(0)

        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        elif v > random_num:
        # 7. if the guess is high
            messagebox.showinfo(title="user", message="Too high!")
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low
        elif v < random_num:
            messagebox.showinfo(title="user", message="Too low!")
        else:
            messagebox.showinfo(title="user", message="Wrong!")
    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo(title="user", message="You lost!")
    window.mainloop()
