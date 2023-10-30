from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

#1.Fonksiyon
def k_kucuk(sayi, liste):
        liste.sort()
        k_kucuk_sonuc = liste[sayi - 1]
        return k_kucuk_sonuc


#2.Fonksiyon
def en_yakin_cift(sayi, liste):
    liste.sort()
    min_fark = float('inf') #Sonsuz büyüklükte bir sayi
    for i in range(len(liste) - 1):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs(sayi - toplam)

            if fark < min_fark:
                min_fark = fark
                en_yakin_cift_sonuc = (liste[i], liste[j])
    return en_yakin_cift_sonuc


#3.Fonksiyon
def tekrar_eden_elemanlar(liste):
    tekrar_eden_elemanlar_sonuc = list(set([sayi for sayi in liste if liste.count(sayi) > 1]))
    return tekrar_eden_elemanlar_sonuc


#4.Fonksiyon
def matris_carpimi(liste1, liste2):
    if len(liste1[0]) == len(liste2):
        matris_carpimi_sonuc = [[sum(a * b for a, b in zip(satir1, sutun2)) for sutun2 in zip(*liste2)] for satir1 in liste1]  # zip(*liste2) ile matrisin transpozu alınır.
        return matris_carpimi_sonuc
    else:
        return "Matris carpimi icin ilk matrisin satir sayisi, ikinci matrisin sutun sayisina esit olmalidir."


#5.Fonksiyon
def kelime_frekans(dosya_adi):
    with open(dosya_adi, "r") as dosya:
        metin = dosya.read()
        kelimeler = metin.split()
        kelime_frekans_sonuc = {}
        for kelime in set(kelimeler):
            kelime_frekans_sonuc[kelime] = kelimeler.count(kelime)
        return kelime_frekans_sonuc

            
#6.Fonksiyon
def en_kucuk_deger(liste):
    if len(liste) == 1:
        return liste[0]
    
    min_sayi = liste[0]
    min_sayi_adayi = en_kucuk_deger(liste[1:])
    if min_sayi_adayi < min_sayi:
        min_sayi = min_sayi_adayi
    return min_sayi


#7.Fonksiyon
def karekok(N, x0, tol=10**(-10), maxiter=10, dongu_iterasyonu = 0):  #Newton-Raphson yontemi
    if N == 0:
        return 0
    else:
        x1 = (1/2) * (x0 + (N/x0))
        hata_degeri = abs(x1**2 - N)
        if hata_degeri < tol or dongu_iterasyonu > maxiter:
            if dongu_iterasyonu > maxiter:
                return f"{maxiter} iterasyonda sonuca ulasilamadi. 'hata_degeri' veya 'maxiter' değerlerini degistirin."
            return x1
        return karekok(N, x1, tol, maxiter, dongu_iterasyonu + 1)

#8.Fonksiyon
def eb_ortak_bolen(sayi1, sayi2):  #oklid algoritmasi
    if sayi2 == 0:
        return sayi1
    else:
        return eb_ortak_bolen(sayi2, sayi1 % sayi2)


#9.Fonksiyon
def asal_veya_degil(sayi, bolen = 2):
    if sayi <= 1:
        return False
    elif sayi == bolen:
        return True
    elif sayi % bolen == 0:
        return False
    return asal_veya_degil(sayi, bolen + 1)
    

#10.Fonksiyon
def hizlandirici(n, k=1, fibk=1, fibk1=0):  #fibonacci sayisi hesabi
    if k == n:
        return fibk
    else:
        k+=1
        fibk, fibk1 = fibk + fibk1, fibk
        return hizlandirici(n, k, fibk, fibk1)



def fonksiyon1():
    try:
        sayi = simpledialog.askinteger("istenilen siradaki en kucuk sayi", "Bir sayi girin: ")
        if sayi < 0:
            messagebox.showerror("Hata", "Sira sayisi negatif olamaz!")
        else:
            sayilar = simpledialog.askstring("istenilen siradaki kucuk sayi", "Sayilari aralarina virgul koyarak girin: ")
            liste = [int(sayi) for sayi in sayilar.split(",")]
            sonuc = k_kucuk(sayi, liste)
            messagebox.showinfo("Sonuc", f"{sayi}. küçük sayi: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Gecersiz Giris!")
    except IndexError:
        messagebox.showerror("Hata", "Liste boyutu yeterli değil!")


def fonksiyon2():
    try:
        sayi = simpledialog.askinteger("toplamlari istenilen sayiya en yakin olan cift", "Bir sayi girin: ")
        sayilar = simpledialog.askstring("toplamlari istenilen sayiya en yakin olan cift", "Sayilari aralarina virgul koyarak girin: ")
        liste = [int(sayi) for sayi in sayilar.split(",")]
        sonuc = en_yakin_cift(sayi, liste)
        messagebox.showinfo("Sonuc", f"Toplamlari {sayi} sayisina en yakin sayi cifti: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Gecersiz Giris!")


def fonksiyon3():
    try:
        sayilar = simpledialog.askstring("tekrar eden sayilar", "Sayilari aralarina virgul koyarak girin: ")
        liste = [int(sayi) for sayi in sayilar.split(",")]
        sonuc = tekrar_eden_elemanlar(liste)
        messagebox.showinfo("Sonuc", f"Tekrar eden sayilar: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Gecersiz Giris!")


def fonksiyon4():
    try:
        matris1_str = simpledialog.askstring("Matris 1 Girisi", "Matris 1'i girin (a,b,c ; d,e,f): ")
        matris2_str = simpledialog.askstring("Matris 2 Girisi", "Matris 2'yi girin (k,l ; m,n ; p,r): ")
        matris1 = [list(map(int, satir.split(","))) for satir in matris1_str.split(";")]
        matris2 = [list(map(int, satir.split(","))) for satir in matris2_str.split(";")]
        if len(matris1[1]) == len(matris2):
            sonuc = matris_carpimi(matris1, matris2)
            messagebox.showinfo("Sonuc", f"Matris Carpimi Sonucu: {sonuc}")
        else:
            messagebox.showerror("Hata", "Matris carpimi icin ilk matrisin satir sayisi, ikinci matrisin sutun sayisina esit olmalidir!")
    except ValueError:
        messagebox.showerror("Hata", "Gecersiz Giris!")


def fonksiyon5():
    try:
        dosya_adi = simpledialog.askstring("Kelime Frekansi", "Dosya adini girin: ")
        sonuc = kelime_frekans(dosya_adi)
        messagebox.showinfo("Sonuc", f"Kelimelerin frekanslari: {sonuc}")
    except FileNotFoundError:
        messagebox.showerror("Hata", "Dosya bulunamadi!")


def fonksiyon6():
    try:
        sayilar = simpledialog.askstring("en kucuk sayi", "Sayilari aralarina virgul koyarak girin: ")
        liste = [int(sayi) for sayi in sayilar.split(",")]
        sonuc = en_kucuk_deger(liste)
        messagebox.showinfo("Sonuc", f"En kucuk sayi: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Gecersiz Giris!")


def fonksiyon7():
    try:
        sayi = simpledialog.askinteger("Karekok", "Bir sayi girin: ")
        if sayi < 0:
            messagebox.showerror("Hata", "Negatif sayilarin karekoku hesaplanamaz!")
        else:
            tahmin = simpledialog.askfloat("Karekok", "Bir tahmin girin: ")
            if tahmin < 0:
                messagebox.showerror("Hata", "Tahmin negatif olamaz.")
            else:
                sonuc = karekok(sayi, tahmin)
                messagebox.showinfo("Sonuc", f"{sayi} sayisinin karekoku: {sonuc}")
    except ZeroDivisionError:
        messagebox.showerror("Sonuc", "Tahmin sifirdan farkli olmalidir.")
        

def fonksiyon8():
        sayi1 = simpledialog.askinteger("ebob", "Birinci sayiyi girin: ")
        sayi2 = simpledialog.askinteger("ebob", "Ikinci sayiyi girin: ")
        sonuc = eb_ortak_bolen(sayi1, sayi2)
        messagebox.showinfo("Sonuc", f"Ebob({sayi1}, {sayi2}) = {sonuc}")


def fonksiyon9():
    sayi = simpledialog.askinteger("Asal sayi mi", "Bir sayi giriniz: ")
    sonuc = asal_veya_degil(sayi)
    if sonuc == True:
        messagebox.showinfo("Sonuc", f"{sayi} asaldir.")
    else:
        messagebox.showinfo("Sonuc", f"{sayi} asal degildir.")


def fonksiyon10():
    try:
        sayi = simpledialog.askinteger("Fibonacci", "Kacinci fibonacci sayisina ulasmak istediğinizi girin: ")
        sonuc = hizlandirici(sayi)
        messagebox.showinfo("Sonuc", f"{sayi}. fibonacci sayisi: {sonuc}")
    except RecursionError:
        messagebox.showerror("Hata", "Sira sayisi negatif olamaz!")


window = Tk()
window.title("Menu")
window.config(background="#B0C4DE")
window.geometry("400x400")

label = Label(window, text="Yapmak istediginiz islemi seciniz: ", font=("Arial", 13), bg="#B0C4DE", pady=4)
label.pack()

button1 = Button(window, text= "Istenilen Siradaki En Kucuk Eleman", font=("Arial", 10), bg="#D2daf1", fg="black", activebackground="#D2daf1", width=40, command=fonksiyon1)
button1.pack()

button2 = Button(window, text= "Toplamlari Istenilen Sayiya En Yakin Olan Cift", font=("Arial", 10), bg="#Fff1e7", fg="black", activebackground="#Fff1e7", width=40, command=fonksiyon2)
button2.pack()

button3 = Button(window, text= "Tekrar Eden Sayilar", font=("Arial", 10), bg="#e2ecd1", fg="black", activebackground="#e2ecd1", width=40, command=fonksiyon3)
button3.pack()

button4 = Button(window, text= "Matris Carpimi", font=("Arial", 10), bg="#F9e0ff", fg="black", activebackground="#F9e0ff", width=40, command=fonksiyon4)
button4.pack()

button5 = Button(window, text= "Kelime Frekansi", font=("Arial", 10), bg="#fbfbc5", fg="black", activebackground="#fbfbc5", width=40, command=fonksiyon5)
button5.pack()

button6 = Button(window, text= "En Kucuk Sayi", font=("Arial", 10), bg="#F7c6c8", fg="black", activebackground="#F7c6c8", width=40, command=fonksiyon6)
button6.pack()

button7 = Button(window, text= "Karekok", font=("Arial", 10), bg="#D0e1fd", fg="black", activebackground="#D0e1fd", width=40, command=fonksiyon7)
button7.pack()

button8 = Button(window, text= "En Buyuk Ortak Bolen", font=("Arial", 10), bg="#F9dbf2", fg="black", activebackground="#F9dbf2", width=40, command=fonksiyon8)
button8.pack()

button9 = Button(window, text= "Asal Sayi mi", font=("Arial", 10), bg="#Ddfde5", fg="black", activebackground="#Ddfde5", width=40, command=fonksiyon9)
button9.pack()

button10 = Button(window, text= "Fibonacci", font=("Arial", 10), bg="#E4e1e1", fg="black", activebackground="#E4e1e1", width=40, command=fonksiyon10)
button10.pack()

button11 = Button(window, text="Cikis", font=("Arial", 10),bg="#B3afc9" , fg="black", activebackground="#B3afc9", width=40, command=quit)
button11.pack()

window.mainloop()
