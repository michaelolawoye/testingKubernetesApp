from tkinter import *
from tkinter import ttk


def convertDegrees(*args):
	try:
		val = float(celsius.get())
		fahrenheit.set(round(val*(9/5)+32, 3))
	except ValueError:
		pass

root = Tk()
root.title("Convert degrees")

gFrame = ttk.Frame(root, padding=(5, 5, 5, 5))

gFrame.grid(column=0, row=0, sticky=(W, N, E, S))

celsius = StringVar()
degree_entry = ttk.Entry(gFrame, width=10, textvariable=celsius)
degree_entry.grid(column=0, row=0)

ttk.Label(gFrame, text="Celsius").grid(column=1, row=0)

fahrenheit = StringVar()
ttk.Label(gFrame, textvariable=fahrenheit).grid(column=0, row=1)

ttk.Label(gFrame, text="Fahrenheit").grid(column=1, row=1)

ttk.Button(gFrame, text="Convert", command=convertDegrees).grid(column=0, row=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
gFrame.columnconfigure(0, weight=1)

for child in gFrame.winfo_children():
	child.grid_configure(padx=5, pady=5)


degree_entry.focus()
root.bind("<Return>", convertDegrees)

root.mainloop()
