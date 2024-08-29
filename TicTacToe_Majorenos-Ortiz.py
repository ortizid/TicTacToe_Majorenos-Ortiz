import tkinter  # GUI library

def set_tile(row, column):
    global currentP, game_over
    
    if board[row][column]["text"] != "" or game_over:
        return
    
    board[row][column]["text"] = currentP  # mark the board

    if currentP == O:  # switch player
        currentP = X
    else:
        currentP = O

    label["text"] = currentP+"'s Turn"

    # check winner
    check_winner()

def check_winner():
    global turns, game_over, scoreX, scoreO, ties
    turns += 1

    # horizontal check
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=yellow)
            update_score(board[row][0]["text"])
            for column in range(3):
                board[row][column].config(foreground=yellow, background=light_gray)
            game_over = True
            return

    # vertical check
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=yellow)
            update_score(board[0][column]["text"])
            for row in range(3):
                board[row][column].config(foreground=yellow, background=light_gray)
            game_over = True
            return

    # diagonal check
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
            label.config(text=board[0][0]["text"]+" is the winner!", foreground=yellow)
            update_score(board[0][0]["text"])
            for i in range(3):
                board[i][i].config(foreground=yellow, background=light_gray)
            game_over = True
            return
    
    # other diagonal check
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
            label.config(text=board[0][2]["text"]+" is the winner!", foreground=yellow)
            update_score(board[0][2]["text"])
            board[0][2].config(foreground=yellow, background=light_gray)
            board[1][1].config(foreground=yellow, background=light_gray)
            board[2][0].config(foreground=yellow, background=light_gray)
            game_over = True
            return
    
    # tie
    if (turns == 9):
        game_over = True
        ties += 1
        label.config(text="Tie!", foreground=yellow)
        update_score(None)

def update_score(winner):
    global scoreX, scoreO, ties
    if winner == X:
        scoreX += 1
    elif winner == O:
        scoreO += 1
    score_label.config(text=f"Score: X = {scoreX}  O = {scoreO}  Ties = {ties}")

def new_game():
    global turns, game_over, currentP
    
    turns = 0
    game_over = False
    currentP = X  # Start with X again

    label.config(text=currentP+"'s Turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=blue, background=gray)

def reset_scores():
    global scoreX, scoreO, ties
    scoreX = 0
    scoreO = 0
    ties = 0
    score_label.config(text=f"Score: X = {scoreX}  O = {scoreO}  Ties = {ties}")

# Game setup
X = 'X'
O = 'O'
currentP = X
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

scoreX = 0
scoreO = 0
ties = 0

blue = "#4584b6"
yellow = "#ffde57"
gray = "#343434"
light_gray = "#646464"

turns = 0
game_over = False

# Window setup
window = tkinter.Tk()  # create game window
window.title('⨉ Tic-Tac-Toe ◯')
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=currentP+"'s Turn", font=("Arial", 20), background=gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

button = tkinter.Button(frame, text="Restart", font=("Arial", 20), background=gray, foreground="white", command=new_game)
button.grid(row=1, column=0, columnspan=3, sticky="we")

reset_button = tkinter.Button(frame, text="Reset Scores", font=("Arial", 20), background=gray, foreground="white", command=reset_scores)
reset_button.grid(row=2, column=0, columnspan=3, sticky="we")

score_label = tkinter.Label(frame, text=f"Score: X = {scoreX}  O = {scoreO}  Ties = {ties}", font=("Arial", 20), background=gray, foreground="white")
score_label.grid(row=3, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Arial", 50, "bold"),
                                             background=gray, foreground=blue, width=4, height=1, 
                                             command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+4, column=column)

frame.pack()

# Center window
window.update()
win_width = window.winfo_width()
win_height = window.winfo_height()
sc_width = window.winfo_screenwidth()
sc_height = window.winfo_screenheight()

winX = int((sc_width / 2) - (win_width / 2))
winY = int((sc_height / 2) - (win_height / 2))

# Format "(w)x(h)+(x)+(y)"
window.geometry(f"{win_width}x{win_height}+{winX}+{winY}")

window.mainloop()