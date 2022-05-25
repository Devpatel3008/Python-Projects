from tkinter import *
import tkinter.font as font
import random
from PIL import ImageTk, Image

root = Tk()
root.title("Rock Paper Scissors Game")
app_font = font.Font(size = 12)
root.config(bg = '#FFE873')
root.geometry('700x500')

player_score = 0
computer_score = 0
options = [('Rock', 0), ('Paper', 1), ('Scissors', 2)]

#Displaying Game Title
Label(text = 'Rock Paper Scissors', font = font.Font(size = 24), bg = '#FFE873').pack()



# define function to choice player input
def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if player_input == computer_input:
        winner_label.config(text = "Tie")
    elif (player_input[1]-computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Your Score : ' + str(computer_score))

#Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)


#Label to display, who wins each time
winner_label = Label(text = "Let's Start the Game...", fg = 'green', bg = '#FFE873', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(root, bg = '#FFE873')
input_frame.pack()

#Displaying player options
player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey', bg = '#FFE873')
player_options.grid(row = 0, column = 0, pady = 8)

image_rock = Image.open('rock.png')
resize_image_rock = image_rock.resize((120, 120))
img_rock = ImageTk.PhotoImage(resize_image_rock)
rock_label = Label(input_frame, text = 'Rock', fg = 'black', font = app_font)
rock_btn = Button(input_frame, text = 'Rock', image = img_rock, width = 120, height = 120, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_label.grid(row = 1, column = 1)
rock_btn.grid(row = 2, column = 1, padx = 8, pady = 5)

image_paper = Image.open('paper.png')
resize_image_paper = image_paper.resize((120, 120))
img_paper = ImageTk.PhotoImage(resize_image_paper)
paper_label = Label(input_frame, text = 'Paper', fg = 'black', font = app_font)
paper_btn = Button(input_frame, text = 'Paper',image = img_paper, width = 120, height = 120, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
paper_label.grid(row = 1, column = 2)
paper_btn.grid(row = 2, column = 2, padx = 8, pady = 8)

image_scissors = Image.open('scissors.png')
resize_image_scissors = image_scissors.resize((120, 120))
img_scissors = ImageTk.PhotoImage(resize_image_scissors)
scissors_label = Label(input_frame, text = 'Scissors', fg = 'black', font = app_font)
scissors_btn = Button(input_frame, text = 'Scissors',image = img_scissors, width = 120, height = 120, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_label.grid(row = 1, column = 3)
scissors_btn.grid(row = 2, column = 3, padx = 20, pady = 5)

#Displaying Score and players choise
score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey', bg = '#FFE873')
score_label.grid(row = 3, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font, bg = '#FFE873')
player_choice_label.grid(row = 4, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : 0', font = app_font, bg = '#FFE873')
player_score_label.grid(row = 4, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black', bg = '#FFE873')
computer_choice_label.grid(row = 5, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : 0', font = app_font, fg = 'black', bg = '#FFE873')
computer_score_label.grid(row = 5, column = 2, padx = (10,0), pady = 5)

root.mainloop()


