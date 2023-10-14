from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero.
    score = 0
    print(score)
    # ASK A QUESTION AND CHECK THE ANSWER
    username = simpledialog.askstring(title="user", prompt="Who warned us about Entity303?")
    if username== "Herobrine":
        score = score+1
    else:
        score = score-1
    #      // 2.  Ask the user a question 
    username = simpledialog.askstring(title="user", prompt="What is the bloody version of sonic?")
    #      // 3.  Use an if statement to check if their answer is correct
    if username== "Sonic.exe":
    #      // 4.  if the user's answer was correct, add one to their score
        score = score+1
    else:
        score = score-1

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    username = simpledialog.askstring(title="user", prompt="what creepypasta entity watches your every move and is slightly larger than Giant Alex?")
    if username== "Giant Steve":
        score = score+1
    else:
        score = score-1
    #      // Option: Subtract a point from their score for a wrong answer
    username = simpledialog.askstring(title="user", prompt="what creepypasta entity is from sesame street, but is taller, creepier, and can evil laugh?")
    if username== "Slender Elmo":
        score = score+1
    else:
        score = score-1
    username = simpledialog.askstring(title="user", prompt="what is the creepypasta word for uglier and creepier versions of notch, dream, Mr. Beast, Dream, Tommyinnit, and DanTDM?")
    if username== "Unearthed":
        score = score+1
    else:
        score = score-1
    username = simpledialog.askstring(title="CHALLENGE QUESTION", prompt="what creepypasta entity has purple eyes, the size of a player, and is black? Hint: it is not Ender Creeper!")
    if username== "Ender Dream":
        score = score+1
    else:
        score = score-1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    window.str()
    # Run the window's .mainloop() method
    window.mainloop()
