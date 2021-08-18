from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image

with sqlite3.connect("wt.db") as db:
    cursor = db.cursor()


def urunEkle():
    urunEkle = LabelFrame(window, text = "Ürün Ekle")
    urunEkle.place(relwidth=.9, relheight=.9 ,relx =.05, rely = .03,)

    isim = Label(urunEkle, text = "İsim:",font = "bold")
    isim.place(relx = .01, rely = .03)
    isimGiris = Entry(urunEkle, width = 30)
    isimGiris.place(relx =.22, rely = .045 )

    alisFiyati = Label(urunEkle, text = "Alış Fiyatı:",font = "bold")
    alisFiyati.place(relx = .01, rely = .13)
    alisFiyatiGiris = Entry(urunEkle, width = 10)
    alisFiyatiGiris.place(relx =.22, rely = .145)

    satisFiyati = Label(urunEkle, text = "Satış Fiyatı:",font = "bold")
    satisFiyati.place(relx = .01, rely = .23)
    satisFiyatiGiris = Entry(urunEkle, width = 10)
    satisFiyatiGiris.place(relx =.22, rely = .245)

    stokMiktari = Label(urunEkle, text = "Stok Miktarı:",font = "bold")
    stokMiktari.place(relx = .01, rely = .33)
    stokMiktariGiris = Entry(urunEkle, width = 10)
    stokMiktariGiris.place(relx = .22, rely = .345)

    urunEkleButon = Button(urunEkle, text = "Ürün Ekle .../command_gelecek" )
    urunEkleButon.place(relx = .03 ,rely = .45)

    anasayfaButon = Button(urunEkle, text = "Ana Sayfa", command = lambda: urunEkle.place_forget())
    anasayfaButon.place(relx = .45, rely = 0.9)

def urunGuncelle():
    urunGuncelle = LabelFrame(window, text = "Ürün Güncelle")
    urunGuncelle.place(relwidth=.9, relheight=.9 ,relx =.05, rely = .03,)

    isim = Label(urunGuncelle, text = "İsim:",font = "bold")
    isim.place(relx = .01, rely = .03)
    isimGiris = ttk.Combobox(urunGuncelle, width = 30)
    isimGiris.place(relx =.22, rely = .045 )

    alisFiyati = Label(urunGuncelle, text = "Alış Fiyatı:",font = "bold")
    alisFiyati.place(relx = .01, rely = .13)
    alisFiyatiGiris = Entry(urunGuncelle, width = 10)
    alisFiyatiGiris.place(relx =.22, rely = .145)

    satisFiyati = Label(urunGuncelle, text = "Satış Fiyatı:",font = "bold")
    satisFiyati.place(relx = .01, rely = .23)
    satisFiyatiGiris = Entry(urunGuncelle, width = 10)
    satisFiyatiGiris.place(relx =.22, rely = .245)

    stokMiktari = Label(urunGuncelle, text = "Stok Miktarı:",font = "bold")
    stokMiktari.place(relx = .01, rely = .33)
    stokMiktariGiris = Entry(urunGuncelle, width = 10)
    stokMiktariGiris.place(relx = .22, rely = .345)

    urunGuncelleButon = Button(urunGuncelle, text = "Ürün Güncelle .../command_gelecek" )
    urunGuncelleButon.place(relx = .03 ,rely = .45)

    anasayfaButon = Button(urunGuncelle, text = "Ana Sayfa", command = lambda: urunGuncelle.place_forget())
    anasayfaButon.place(relx = .45, rely = 0.9)

def urunListele(): # Düzenlenecek --TODO
    urunListele = LabelFrame(window, text = "Ürün Listele")
    urunListele.place(relwidth = .9, relheight = .9, relx = .05, rely = .03)

    urunTable = ttk.Treeview(urunListele)
    # Defining columns
    urunTable['columns'] = ("İsim", "Alış Fiyatı", "Satış Fiyatı", "Stok Miktarı", "ID")

    # Formatting columns
    urunTable.column("#0", width = 120, minwidth = 25)
    urunTable.column("İsim", anchor = W, width = 120, minwidth = 25)
    urunTable.column("Alış Fiyatı", anchor = W, width = 80)
    urunTable.column("Satış Fiyatı", anchor = W, width = 120)
    urunTable.column("Stok Miktarı", anchor = W, width = 120)
    urunTable.column("ID", anchor = E, width = 50)

    # Creating Headings
    urunTable.heading("#0", text = "label", anchor =W)
    urunTable.heading("İsim", text = "Ürün İsmi", anchor = W)
    urunTable.heading("Alış Fiyatı", text = "Alış Fiyatı", anchor = W)
    urunTable.heading("Satış Fiyatı", text = "Satış Fiyatı", anchor = W)
    urunTable.heading("Stok Miktarı", text = "Stok Miktarı", anchor = W)
    urunTable.heading("ID", text = "ID", anchor = E)

    # Add Data --TODO: otomatikleştirilecek
    urunTable.insert(parent = '', index = 'end', iid = 0, text = "Parent", values = ("Ametist", 25, 50, 1000,0))

    # Packing
    urunTable.pack(pady = 20)

    anasayfaButon = Button(urunListele, text = "Ana Sayfa", command = lambda: urunListele.place_forget())
    anasayfaButon.place(relx = .45, rely = 0.9)

def urunSatis(): # Commands eklenecek --TODO
    urunSatis = LabelFrame(window, text = "Ürün Satış")
    urunSatis.place(relwidth = .9, relheight = .9, relx = .05, rely = .03)
    urunSatisLabel = Label(urunSatis, text = "Ürün Seçiniz:", font = "bold")
    urunSatisLabel.place(relx = .01, rely = .1)
    urunSatisGiris = ttk.Combobox(urunSatis, width = 30)
    urunSatisGiris.place(relx = .25, rely = .11)
    urunSatisButton = Button(urunSatis, text = "Seç ../Command Eklenecek")
    urunSatisButton.place(relx = .25, rely = .18)


    anasayfaButon = Button(urunSatis, text = "Ana Sayfa", command = lambda: urunSatis.place_forget())
    anasayfaButon.place(relx = .45, rely = 0.9)

def karCiro():
    karCiro = LabelFrame(window, text = "Ürün Listele")
    karCiro.place(relwidth = .9, relheight = .9, relx = .05, rely = .03)

    urunTable = ttk.Treeview(karCiro)
    # Defining columns
    urunTable['columns'] = ("ID", "Tarih", "İsim", "Satış Fiyatı", "Satış Miktarı", "Kar TL", "Kar Oran")

    # Formatting columns
    urunTable.column("#0", width = 120, minwidth = 25)
    urunTable.column("ID", anchor = E, width = 50)
    urunTable.column("Tarih", anchor = W, width = 50, minwidth = 25)
    urunTable.column("İsim", anchor = W, width = 50, minwidth = 25)
    urunTable.column("Tarih", anchor = W, width = 50, minwidth = 25)
    urunTable.column("Satış Fiyatı", anchor = W, width = 50, minwidth = 25)
    urunTable.column("Satış Miktarı", anchor = W, width = 50, minwidth = 25)
    urunTable.column("Kar TL", anchor = W, width = 50, minwidth = 25)
    urunTable.column("Kar Oran", anchor = W, width = 50, minwidth = 25)

    # Creating Headings
    urunTable.heading("#0", text = "label", anchor =W)
    urunTable.heading("ID", text = "ID", anchor = E)
    urunTable.heading("Tarih", text = "Tarih", anchor = W)
    urunTable.heading("İsim", text = "İsim", anchor = E)
    urunTable.heading("Satış Fiyatı", text = "Satış Fiyatı", anchor = W)
    urunTable.heading("Satış Miktarı", text = "Satış Miktarı", anchor = W)
    urunTable.heading("Kar TL", text = "Kar TL", anchor = W)
    urunTable.heading("Kar Oran", text = "Kar Oran", anchor = W)

    # Add Data --TODO: otomatikleştirilecek
    urunTable.insert(parent = '', index = 'end', iid = 0, text = "Parent", values = ("Kaplangözü", 250, 550, 7700,123))

    # Packing
    urunTable.place(relx = .01, rely = .01)

    anasayfaButon = Button(karCiro, text = "Ana Sayfa", command = lambda: karCiro.place_forget())
    anasayfaButon.place(relx = .45, rely = 0.9)




cursor.execute("""CREATE TABLE IF NOT EXISTS urunler (id INT AUTO_INCREMENT PRIMARY KEY, isim VARCHAR(25), alis_fiyat VARCHAR(10), satis_fiyat VARCHAR(10), stok_miktar VARCHAR(10))""")
db.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS para (id INT AUTO_INCREMENT PRIMARY KEY, tarih VARCHAR(20), isim VARCHAR(25), satis_fiyat VARCHAR(10), satis_miktar VARCHAR(10), kar_tl VARCHAR(10), kar_oran VARCHAR(10))")
db.commit()

window = Tk()
window.title("Turkuaz Doğal Taş ve Takı")

hosgeldinMesaji = ttk.Label(window, text = "Turkuaz İç Muhasebe Programına Hoşgeldiniz...", font = "bold")
hosgeldinMesaji.place(relx = .05, rely = .05)

menubar = Menu(window)


# resim = PhotoImage(file = "C:/Users/mhyms/Pictures/Bugs.png")
#resim = ImageTk.PhotoImage(Image.open('C:/Users/mhyms/Pictures/C:/Users/mhyms/Pictures/aZByxnX_460swp.jpg'))
#snoopDogg = Label(image = resim)
#snoopDogg.place(relx = .15, rely = .2)


fileMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Menü", menu=fileMenu)
fileMenu.add_command(label = "Ürün Ekle", command = urunEkle)
fileMenu.add_separator()
fileMenu.add_command(label = "Ürün Güncelle", command = urunGuncelle)
fileMenu.add_separator()
fileMenu.add_command(label = "Ürün Listele", command = urunListele)
fileMenu.add_separator()
fileMenu.add_command(label = "Ürün Satış", command = urunSatis)
fileMenu.add_separator()
fileMenu.add_command(label = "Kar-Ciro", command = karCiro)

window.geometry("640x480")
window.resizable(False, False)
window.config(menu=menubar)
mainloop()