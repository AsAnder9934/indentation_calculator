from tkinter import *
import math

def okno_wciecia_liniowego():
    root = Toplevel()
    root.geometry('600x400')
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

    entry_A_X.grid(row=1, column=1)
    entry_A_Y.grid(row=2, column=1)
    entry_B_X.grid(row=1, column=3)
    entry_B_Y.grid(row=2, column=3)
    entry_distance_ac.grid(row=4, column=1)
    entry_distance_bc.grid(row=5, column=1)

    button_oblicz = Button(frame_linear, text='OBLICZ WSPÓŁRZĘDNE PUNKTU C', command=wspolrzedne_punktu_c)
    button_oblicz.grid(row=7, column=0, columnspan=3)

    button_mapa = Button(frame_linear, text='POKAŻ MAPĘ')
    button_mapa.grid(row=8, column=0, columnspan=3)

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
    azimuth = math.degrees(radian_azimuth) * (10 / 9)
    azimuth = (azimuth + 400) % 400
    return azimuth

def kat_gamma(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    odleglosc_ab_value = odleglosc_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    entry_distance_ac_value = float(entry_distance_ac.get())
    entry_distance_bc_value = float(entry_distance_bc.get())

    kat = math.atan((odleglosc_ab_value ** 2 - (entry_distance_ac_value ** 2 + entry_distance_bc_value ** 2)) / (
                -2 * entry_distance_ac_value * entry_distance_bc_value))
    return kat
def kat_beta(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    odleglosc_ab_value = odleglosc_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    entry_distance_ac_value = float(entry_distance_ac.get())
    entry_distance_bc_value = float(entry_distance_bc.get())

    kat = math.atan((entry_distance_ac_value ** 2 - (odleglosc_ab_value ** 2 + entry_distance_bc_value ** 2)) / (
                -2 * odleglosc_ab_value * entry_distance_bc_value))
    return kat

def kat_alfa(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    odleglosc_ab_value = odleglosc_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    entry_distance_ac_value = float(entry_distance_ac.get())
    entry_distance_bc_value = float(entry_distance_bc.get())

    kat = math.atan((entry_distance_bc_value ** 2 - (entry_distance_ac_value ** 2 + odleglosc_ab_value ** 2)) / (
                -2 * entry_distance_ac_value * odleglosc_ab_value))
    return kat
def azymut_A_ap(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    azymut_A_ab_value = azymut_A_ab(entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    kat_alfa_value = kat_alfa(entry_distance_ac, entry_distance_bc, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)

    azymut = azymut_A_ab_value - kat_alfa_value
    return azymut

def przyrosty_x(entry_distance_ac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    entry_distance_ac_value = float(entry_distance_ac.get())
    azymut_A_ap_value = azymut_A_ap(entry_distance_ac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)

    przyrost = entry_distance_ac_value * math.cos(math.radians(azymut_A_ap_value))
    return przyrost
def przyrosty_y(entry_distance_ac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    entry_distance_ac_value = float(entry_distance_ac.get())
    azymut_A_ap_value = azymut_A_ap(entry_distance_ac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)

    przyrost = entry_distance_ac_value * math.sin(math.radians(azymut_A_ap_value))
    return przyrost
def wspolrzedne_punktu_c(entry_distance_ac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y):
    entry_A_X_value = float(entry_A_X.get())
    entry_A_Y_value = float(entry_A_Y.get())

    x = entry_A_X_value + przyrosty_x(entry_distance_ac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    y = entry_A_Y_value + przyrosty_y(entry_distance_ac, entry_A_X, entry_A_Y, entry_B_X, entry_B_Y)
    return x, y

