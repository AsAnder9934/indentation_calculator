from tkinter import messagebox
from tkinter import *
from linear_indentation import okno_wciecia_liniowego
from angular_indentations import okno_wciecia_katowego

def wyjscie(root):
    if messagebox.askokcancel("Potwierdzenie", "Czy na pewno chcesz zakończyć program?"):
        root.destroy()

def zmien_menu_na_wstecz(button_menu, button_wstecz):
    button_menu.grid_forget()
    button_wstecz.grid(row=1, column=0, pady=10)

def zmien_wyjscie_na_obliczenia(button_wyjscie, button_obliczenia):
    button_wyjscie.grid_forget()
    button_obliczenia.grid(row=2, column=0, pady=10)

def wstecz(button_menu, button_wstecz, frame_options):
    button_menu.grid(row=1, column=0, pady=10)
    button_wstecz.grid_forget()
    schowaj_przyciski(frame_options)

def obliczenia(button_wyjscie, button_obliczenia):
    button_wyjscie.grid(row=2, column=0, pady=10)
    button_obliczenia.grid_forget()

def wywolywacz(frame_options):
    button_obliczenie1 = Button(frame_options, text='WCIĘCIE LINIOWE', command=okno_wciecia_liniowego)
    button_obliczenie2 = Button(frame_options, text='WCIĘCIA KĄTOWE', command=okno_wciecia_katowego)
    button_obliczenie3 = Button(frame_options, text='3 opcja (w przyszłosci)', command=okno_do_okodowania)

    button_obliczenie1.grid(row=2, column=6, padx=100, pady=10)
    button_obliczenie2.grid(row=3, column=6, padx=100, pady=10)
    button_obliczenie3.grid(row=4, column=6, padx=100, pady=10)

def schowaj_przyciski(frame_options):
    for widget in frame_options.winfo_children():
        if isinstance(widget, Button) and widget['text'] in ['WCIĘCIE LINIOWE', 'WCIĘCIA KĄTOWE', '3 opcja (w przyszłosci)']:
            widget.grid_forget()

def okno_do_okodowania():
    root = Toplevel()
    root.geometry('600x400')
    root.title('Okno do dodania nowej funkcjonlnosci')



