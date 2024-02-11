from tkinter import *
import math
from tkinter import messagebox, Label
import pyproj
import tkintermapview
from PIL import Image, ImageTk

def odleglosc_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    x1 = float(entry_A_X.get())
    y1 = float(entry_A_Y.get())
    x2 = float(entry_B_X.get())
    y2 = float(entry_B_Y.get())

    odleglosc = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return odleglosc

def azymut_A_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    x1 = float(entry_A_X.get())
    y1 = float(entry_A_Y.get())
    x2 = float(entry_B_X.get())
    y2 = float(entry_B_Y.get())

    dx = x2 - x1
    dy = y2 - y1
    radian_azimuth = math.atan2(dy, dx)
    return radian_azimuth

def kat_alfa(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    odleglosc_ab_value = odleglosc_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    entry_distance_ac_value = float(entry_distance_ac.get())
    entry_distance_bc_value = float(entry_distance_bc.get())

    kat = math.acos((entry_distance_bc_value ** 2 - (entry_distance_ac_value ** 2 + odleglosc_ab_value ** 2)) /
                    ((-2) * entry_distance_ac_value * odleglosc_ab_value))
    return kat

def azymut_A_ap(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    azymut_A_ab_value = azymut_A_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    kat_alfa_value = kat_alfa(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)

    azymut = azymut_A_ab_value - kat_alfa_value
    return azymut

def przyrosty_x(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    entry_distance_ac_value = float(entry_distance_ac.get())

    azymut_A_ap_value = azymut_A_ap(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)

    przyrost = entry_distance_ac_value * math.cos(azymut_A_ap_value)
    return przyrost
def przyrosty_y(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    entry_distance_ac_value = float(entry_distance_ac.get())

    azymut_A_ap_value = azymut_A_ap(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)

    przyrost = entry_distance_ac_value * math.sin(azymut_A_ap_value)
    return przyrost

def okno_wciecia_liniowego():
    root = Toplevel()
    root.geometry('550x400')
    root.title('Okno Wcięcia Liniowego')

    frame_linear=Frame(root)
    frame_linear.grid(row=0, column=0)

    label_A = Label(frame_linear, text='POŁOŻENIE PUNKTU A')
    label_A_X = Label(frame_linear, text='WSPÓŁRZĘDNA X: ')
    label_A_Y =Label(frame_linear, text='WSPÓŁRZĘDNA Y: ')
    label_B = Label(frame_linear, text='POŁOŻENIE PUNKTU B')
    label_B_X = Label(frame_linear, text='WSPÓŁRZĘDNA X: ')
    label_B_Y = Label(frame_linear, text='WSPÓŁRZĘDNA Y: ')
    label_empty = Label(frame_linear, text='')
    label_info = Label(frame_linear, text="Prawidłowe wyswietlanie położenia pkt. w układzie '92")
    label_odleglosc = Label(frame_linear, text='ODLEGŁOŚCI PO PUNKTU C')
    label_distance_ac = Label(frame_linear, text='ODLEGŁOŚĆ A-C')
    label_distance_bc = Label(frame_linear, text='ODLEGŁOŚĆ B-C')

    entry_A_X = Entry(frame_linear)
    entry_A_Y = Entry(frame_linear)
    entry_B_X = Entry(frame_linear)
    entry_B_Y = Entry(frame_linear)
    entry_distance_ac = Entry(frame_linear)
    entry_distance_bc = Entry(frame_linear)

    label_A.grid(row=0, column=0, columnspan=2)
    label_A_X.grid(row=1, column=0, sticky=W)
    label_A_Y.grid(row=2, column=0, sticky=W)
    label_B.grid(row=0, column=2, columnspan=2)
    label_B_X.grid(row=1, column=2, sticky=W)
    label_B_Y.grid(row=2, column=2, sticky=W, pady=5)
    label_odleglosc.grid(row=3, column=0, columnspan=2)
    label_distance_ac.grid(row=4, column=0)
    label_distance_bc.grid(row=5, column=0, pady=5)
    label_empty.grid(row=6, column=0)
    label_info.grid(row=3, column=2, columnspan=2)

    entry_A_X.grid(row=1, column=1)
    entry_A_Y.grid(row=2, column=1)
    entry_B_X.grid(row=1, column=3)
    entry_B_Y.grid(row=2, column=3)
    entry_distance_ac.grid(row=4, column=1)
    entry_distance_bc.grid(row=5, column=1)

    button_oblicz = Button(frame_linear, text='OBLICZ WSPÓŁRZĘDNE PUNKTU C', command=lambda: wspolrzedne_punktu_c(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y))
    button_oblicz.grid(row=7, column=0, columnspan=2)

    button_mapa = Button(frame_linear, text='POKAŻ MAPĘ', command=lambda: widget(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y))
    button_mapa.grid(row=8, column=0, columnspan=3)

    result_text = Text(frame_linear, height=4, width=25)
    result_text.grid(row=9, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

    def wspolrzedne_punktu_c(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
        if entry_distance_ac.get() and entry_distance_bc.get() and entry_A_X.get() and entry_A_Y.get() and entry_B_X.get() and entry_B_Y.get():
            entry_A_X_value = float(entry_A_X.get())
            entry_A_Y_value = float(entry_A_Y.get())

            x = entry_A_X_value + przyrosty_x(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
            y = entry_A_Y_value + przyrosty_y(entry_distance_ac,entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
            result_text.delete(1.0, END)
            result_text.insert(END, "Współrzędne punktu C:\n")
            result_text.insert(END, f"X: {x:.3f}\n")
            result_text.insert(END, f"Y: {y:.3f}\n")
            return x, y
        else:
            messagebox.showerror("Błąd", "Proszę wypełnić wszystkie pola.")

    # obrazek w formie instrukcji postepowania podczas wprowadznia danych
    image = Image.open("wciecie_liniowe.png")

    szerokosc, wysokosc = image.size
    skalowanie = 0.48
    nowa_szerokosc = int(szerokosc * skalowanie)
    nowa_wysokosc = int(wysokosc * skalowanie)
    image = image.resize((nowa_szerokosc, nowa_wysokosc))

    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.image = photo
    label.grid(row=0, column=0, columnspan=10, rowspan=10, padx=250, pady=100)

    def uklad_1992_to_wspolrzedne_geograficzne(x, y):
        transformer = pyproj.Transformer.from_crs("EPSG:2180", "EPSG:4326", always_xy=True)
        lon, lat = transformer.transform(x, y)
        return lat, lon

    def widget(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
        x_a = float(entry_A_X.get())
        y_a = float(entry_A_Y.get())
        x_b = float(entry_B_X.get())
        y_b = float(entry_B_Y.get())
        x_c, y_c = wspolrzedne_punktu_c(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)

        lat_a, lon_a = uklad_1992_to_wspolrzedne_geograficzne(x_a, y_a)
        lat_b, lon_b = uklad_1992_to_wspolrzedne_geograficzne(x_b, y_b)
        lat_c, lon_c = uklad_1992_to_wspolrzedne_geograficzne(x_c, y_c)

        label.grid_forget()

        map = tkintermapview.TkinterMapView(frame_linear, width=300, height=300)
        map.set_position(lat_c, lon_c)
        map.set_zoom(15)
        map.grid(row=4, column=2, columnspan=10, rowspan=10, padx=10)

        a=map.set_marker(lat_a, lon_a)
        a.set_text('Punkt A')
        b=map.set_marker(lat_b, lon_b)
        b.set_text('Punkt B')
        c=map.set_marker(lat_c, lon_c)
        c.set_text('Punkt wcinany C')

        map.set_polygon([(lat_a, lon_a), (lat_b, lon_b), (lat_c, lon_c)], fill_color='blue',
                        outline_color='red', border_width=8, command=lambda: widget(entry_distance_ac,
                        entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y))

