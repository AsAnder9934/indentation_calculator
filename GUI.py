from tkinter import *
from functions import *

root = Tk()
root.geometry('600x400')
root.title('Kalkulator wcięć')

frame_options = Frame(root)
frame_options.grid(row=0, column=0, padx=50)

button_menu = Button(frame_options, text='MENU', command=lambda: [zmien_menu_na_wstecz(button_menu, button_wstecz), zmien_wyjscie_na_obliczenia(button_wyjscie, button_obliczenia)])
button_wstecz = Button(frame_options, text='WSTECZ', command=lambda: [wstecz(button_menu, button_wstecz, frame_options), obliczenia(button_wyjscie, button_obliczenia)])

button_menu.grid(row=1, column=0, pady=10)

button_wyjscie = Button(frame_options, text='WYJŚCIE', command=lambda: wyjscie(root))
button_obliczenia = Button(frame_options, text='OBLICZENIA', command=lambda: wywolywacz(frame_options))

button_wyjscie.grid(row=2, column=0, pady=10)

root.mainloop()

