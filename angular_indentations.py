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

def kat_alfa(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    x1 = float(entry_A_X.get())
    y1 = float(entry_A_Y.get())
    x2 = float(entry_B_X.get())
    y2 = float(entry_B_Y.get())

    kat = math.atan((y2-y1)/(x2-x1))
    return kat * (200 / math.pi)

def azymut_A_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    x1 = float(entry_A_X.get())
    y1 = float(entry_A_Y.get())
    x2 = float(entry_B_X.get())
    y2 = float(entry_B_Y.get())

    delta_x = x2 - x1
    delta_y = y2 - y1
    if delta_x > 0 and delta_y > 0:
        azymut = kat_alfa(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
        return azymut * (math.pi / 200)
    elif delta_x > 0 and delta_y < 0:
        azymut = kat_alfa(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y) + 400
        return azymut * (math.pi / 200)
    elif delta_x < 0 and delta_y > 0:
        azymut = kat_alfa(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y) + 200
        return azymut * (math.pi / 200)
    elif delta_x < 0 and delta_y < 0:
        azymut = kat_alfa(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y) + 200
        return azymut * (math.pi / 200)

def azymut_A_ac(entry_kat_bac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y ):
    azymut_ab = azymut_A_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    azymut_bac = float(entry_kat_bac.get()) * (math.pi / 200)
    azymut_ac = azymut_ab + azymut_bac
    return azymut_ac

def odleglosc_ac(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    kat_bac = float(entry_kat_bac.get()) * (math.pi / 200)
    kat_cba = float(entry_kat_cba.get()) * (math.pi / 200)
    sin_bac = math.sin(kat_cba)
    sin_cba = math.sin(kat_cba + kat_bac)
    odleglosc = (odleglosc_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)) * (sin_bac)/(sin_cba)
    return odleglosc

def przyrosty_x(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    przyrost = odleglosc_ac(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y) * math.cos(azymut_A_ac(entry_kat_bac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y))
    return przyrost
def przyrosty_y(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    przyrost = odleglosc_ac(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y) * math.sin(azymut_A_ac(entry_kat_bac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y))
    return przyrost

def okno_wciecia_katowego():
    root = Toplevel()
    root.geometry('550x400')
    root.title('Okno Wcięcia Kątowego')

    frame_angular=Frame(root)
    frame_angular.grid(row=0, column=0)

    label_A = Label(frame_angular, text='POŁOŻENIE PUNKTU A')
    label_A_X = Label(frame_angular, text='WSPÓŁRZĘDNA X: ')
    label_A_Y =Label(frame_angular, text='WSPÓŁRZĘDNA Y: ')
    label_B = Label(frame_angular, text='POŁOŻENIE PUNKTU B')
    label_B_X = Label(frame_angular, text='WSPÓŁRZĘDNA X: ')
    label_B_Y = Label(frame_angular, text='WSPÓŁRZĘDNA Y: ')
    label_empty = Label(frame_angular, text='')
    label_info = Label(frame_angular, text="Prawidłowe wyswietlanie położenia pkt. w układzie '92")
    label_katy = Label(frame_angular, text='KĄTY DO PUNKTU C')
    label_kat_bac = Label(frame_angular, text='KĄT BAC')
    label_kat_cba = Label(frame_angular, text='KĄT CBA')

    entry_A_X = Entry(frame_angular)
    entry_A_Y = Entry(frame_angular)
    entry_B_X = Entry(frame_angular)
    entry_B_Y = Entry(frame_angular)
    entry_kat_bac = Entry(frame_angular)
    entry_kat_cba = Entry(frame_angular)

    label_A.grid(row=0, column=0, columnspan=2)
    label_A_X.grid(row=1, column=0, sticky=W)
    label_A_Y.grid(row=2, column=0, sticky=W)
    label_B.grid(row=0, column=2, columnspan=2)
    label_B_X.grid(row=1, column=2, sticky=W)
    label_B_Y.grid(row=2, column=2, sticky=W, pady=5)
    label_katy.grid(row=3, column=0, columnspan=2)
    label_kat_bac.grid(row=4, column=0)
    label_kat_cba.grid(row=5, column=0, pady=5)
    label_empty.grid(row=6, column=0)
    label_info.grid(row=3, column=2, columnspan=2)

    entry_A_X.grid(row=1, column=1)
    entry_A_Y.grid(row=2, column=1)
    entry_B_X.grid(row=1, column=3)
    entry_B_Y.grid(row=2, column=3)
    entry_kat_bac.grid(row=4, column=1)
    entry_kat_cba.grid(row=5, column=1)

    button_oblicz = Button(frame_angular, text='OBLICZ WSPÓŁRZĘDNE PUNKTU C', command=lambda: wspolrzedne_punktu_c(
        entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y))
    button_oblicz.grid(row=7, column=0, columnspan=2)

    button_mapa = Button(frame_angular, text='POKAŻ MAPĘ', command=lambda: widget(entry_kat_bac, entry_kat_cba,
                                                                                  entry_A_X, entry_A_Y, entry_B_X,
                                                                                  entry_B_Y))
    button_mapa.grid(row=8, column=0, columnspan=3)

    result_text = Text(frame_angular, height=4, width=25)
    result_text.grid(row=9, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
    def wspolrzedne_punktu_c(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
        if entry_kat_bac.get() and entry_kat_cba.get() and entry_A_X.get() and entry_A_Y.get() and entry_B_X.get() and entry_B_Y.get():
            entry_A_X_value = float(entry_A_X.get())
            entry_A_Y_value = float(entry_A_Y.get())

            x = entry_A_X_value + przyrosty_x(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
            y = entry_A_Y_value + przyrosty_y(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
            result_text.delete(1.0, END)
            result_text.insert(END, "Współrzędne punktu C:\n")
            result_text.insert(END, f"X: {x:.3f}\n")
            result_text.insert(END, f"Y: {y:.3f}\n")
            return x, y
        else:
            messagebox.showerror("Błąd", "Proszę wypełnić wszystkie pola.")

    # obrazek w formie instrukcji postepowania podczas wprowadznia danych
    image = Image.open("wciecie_katowe.png")

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

    def widget(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
        x_a = float(entry_A_X.get())
        y_a = float(entry_A_Y.get())
        x_b = float(entry_B_X.get())
        y_b = float(entry_B_Y.get())
        x_c, y_c = wspolrzedne_punktu_c(entry_kat_bac, entry_kat_cba, entry_A_X, entry_A_Y, entry_B_X,
                                        entry_B_Y)

        lat_a, lon_a = uklad_1992_to_wspolrzedne_geograficzne(x_a, y_a)
        lat_b, lon_b = uklad_1992_to_wspolrzedne_geograficzne(x_b, y_b)
        lat_c, lon_c = uklad_1992_to_wspolrzedne_geograficzne(x_c, y_c)

        label.grid_forget()

        map = tkintermapview.TkinterMapView(frame_angular, width=300, height=300)
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
                        outline_color='red', border_width=8, command=lambda: widget(entry_kat_bac, entry_kat_cba,
                                                                                    entry_A_X, entry_A_Y, entry_B_X,
                                                                                    entry_B_Y))
