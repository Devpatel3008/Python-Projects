from datetime import datetime
import pytz
from tkinter import *
import time

# Making root window of Tkinter
root = Tk(className = 'World Clock')
root.geometry("500x300")

# Function to display time
def times():
	home = pytz.timezone('Asia/Kolkata')
	local_time = datetime.now(home)
	current_date = local_time.date()
	current_time=local_time.strftime("%H: %M: %S")
	clock.config(text=current_time)
	date.config(text=current_date)
	name.config(text="India")

	home = pytz.timezone('America/Toronto')
	local_time = datetime.now(home)
	current_time=local_time.strftime("%H: %M: %S")
	clock1.config(text=current_time)
	date1.config(text=current_date)
	name1.config(text="Canada")

	home = pytz.timezone('Australia/Sydney')
	local_time = datetime.now(home)
	current_time=local_time.strftime("%H: %M: %S")
	clock2.config(text=current_time)
	date2.config(text=current_date)
	name2.config(text="Australia")

	home = pytz.timezone('US/Arizona')
	local_time = datetime.now(home)
	current_time=local_time.strftime("%H: %M: %S")
	clock3.config(text=current_time)
	date3.config(text=current_date)
	name3.config(text="USA")
	clock.after(200, times)

# Creating squares
canvas = Canvas()
canvas.create_rectangle(40, 5, 230, 140, outline="#000")
canvas.create_rectangle(270, 5, 470, 140, outline="#000")
canvas.create_rectangle(40, 155, 230, 290, outline="#000")
canvas.create_rectangle(270, 155, 470, 290, outline="#000")
canvas.pack(fill=BOTH, expand=1)

# Making and placing objects

# First Box
name = Label(root, font=("times", 20, "bold"))
name.place(x=103, y=10)
date = Label(root, font=("times", 15, "bold"))
date.place(x=83, y=40)
clock = Label(root, font=("times", 25, "bold"))
clock.place(x=60, y=70)
time_label = Label(root, text = "Hours : Minutes : Seconds", font= ("times", 10, "bold"))
time_label.place(x=60, y=110)

#Second Box
name1 = Label(root, font=("times", 20, "bold"))
name1.place(x=325, y=10)
date1 = Label(root, font=("times", 15, "bold"))
date1.place(x=325, y=40)
clock1 = Label(root, font=("times", 25, "bold"))
clock1.place(x=300, y=70)
time_label1 = Label(root, text = "Hours : Minutes : Seconds", font= ("times", 10, "bold"))
time_label1.place(x=300, y=110)

#Third Box
name2 = Label(root, font=("times", 20, "bold"))
name2.place(x=75, y=160)
date2 = Label(root, font=("times", 15, "bold"))
date2.place(x=83, y=190)
clock2 = Label(root, font=("times", 25, "bold"))
clock2.place(x=60, y=220)
time_label2 = Label(root, text = "Hours : Minutes : Seconds", font= ("times", 10, "bold"))
time_label2.place(x=60, y=260)

# Fourth Box
name3 = Label(root, font=("times", 20, "bold"))
name3.place(x=350, y=160)
date3 = Label(root, font=("times", 15, "bold"))
date3.place(x=330, y=190)
clock3 = Label(root, font=("times", 25, "bold"))
clock3.place(x=300, y=220)
time_label3 = Label(root, text = "Hours : Minutes : Seconds", font= ("times", 10, "bold"))
time_label3.place(x=300, y=260)

# Calling a function
times()

# Executing a window
root.mainloop()