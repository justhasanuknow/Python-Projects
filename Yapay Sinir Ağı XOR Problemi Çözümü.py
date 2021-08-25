import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import time

#Giriş - Çıkış Datasetleri
giris = np.array([[0,0],[0,1],[1,0],[1,1]])
beklenen_cikis = np.array([[0],[1],[1],[0]])

lr = float(input("Öğrenme oranını giriniz: "))
tekrar = int(input("Tekrar sayısını giriniz: "))

#------------------
hataOranı1 = list()
hataOranı2 = list()
hataOranı3 = list()
hataOranı4 = list()
toplamHata = list()
#-----------------

girisNoronlar, gizliNoronlar, cikisNoronlar = 2, 12, 1

#Sigmoid fonksiyonu
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Sigmoid türev : Gradyan inişi hesaplamak için kullanılır.
def sigmoid_turev(x):
    return x * (1 - x)

# Ağırlıkları rastgele başlatmak için gerekli olan ağırlık ve meyil değerleri
gizli_Agirlik = np.random.uniform(size = (girisNoronlar,gizliNoronlar))
gizli_Meyil = np.random.uniform(size = (1,gizliNoronlar))

cikis_Agirlik = np.random.uniform(size = (gizliNoronlar,cikisNoronlar))
cikis_Meyil = np.random.uniform(size = (1,cikisNoronlar))

print("\nGizli katman ağırlık başlama: ",end = '')
print(*gizli_Agirlik)
print("Gizli katman meyil başlama: ",end = '')
print(*gizli_Meyil)
print("Çıkış katman ağırlık başlama: ",end = '')
print(*cikis_Agirlik)
print("Çıkış katman meyil başlama: ",end = '')
print(*cikis_Meyil)

"""___Algoritmayı Eğitme___ """

print("\n\nYapay Sinir Ağı Eğitiliyor...\n")

for i in tqdm(range(tekrar)):

    #İleri yayılım fonksiyonu
    gizli_katman_aktiv = np.dot(giris, gizli_Agirlik)
    gizli_katman_aktiv += gizli_Meyil
    gizli_katman_cikis = sigmoid(gizli_katman_aktiv)
    
    cikis_katman_aktiv = np.dot(gizli_katman_cikis,cikis_Agirlik)
    cikis_katman_aktiv += cikis_Meyil
    alinan_cikis = sigmoid(cikis_katman_aktiv)
    
    #Geriyayılım Fonksiyonu
    hata = beklenen_cikis - alinan_cikis
    
    hataOranı1.append(hata[0])
    hataOranı2.append(hata[1])
    hataOranı3.append(hata[2])
    hataOranı4.append(hata[3])
    toplamHata.append( (1/2) * (np.sum(hata ** 2)))
    
    t_alinan_cikis = hata * sigmoid_turev(alinan_cikis)
    
    hata_gizli_katman = t_alinan_cikis.dot(cikis_Agirlik.T)
    t_gizli_katman = hata_gizli_katman * sigmoid_turev(gizli_katman_cikis)
    
    #Ağırlık ve meyil yenilenmesi
    cikis_Agirlik += gizli_katman_cikis.T.dot(t_alinan_cikis) * lr
    cikis_Meyil += np.sum(t_alinan_cikis, axis = 0, keepdims = True) * lr
    gizli_Agirlik += giris.T.dot(t_gizli_katman) * lr
    gizli_Meyil += np.sum(t_gizli_katman, axis = 0, keepdims = True) * lr
    
#Her bir çıkıştaki değişim------------#|
plt.plot(hataOranı1, label="Çıkış[0]")#|
plt.plot(hataOranı2, label="Çıkış[1]")#|
plt.plot(hataOranı3, label="Çıkış[2]")#|
plt.plot(hataOranı4, label="Çıkış[3]")#|
plt.ylabel("Hata Seviyesi")           #|
plt.xlabel("İterasyon Sayısı")        #|
plt.title("Her Bir Çıkıştaki Değişim")#|
plt.legend()                          #|  
plt.show()                            #|  
#-------------------------------------#|

#---Total Error--------------------------#|
plt.plot(toplamHata, label="Toplam Hata")#|
plt.ylabel("Hata Seviyesi")              #|
plt.xlabel("İterasyon Sayısı")           #|
plt.title("Toplam Hata Değişimi")        #|
plt.legend()                             #|
plt.show()                               #|
#----------------------------------------#|

print("\nEğitim tamamlandı.")

print("\nSon gizli ağırlık: ",*gizli_Agirlik)
print("Son gizli meyil: ",*gizli_Meyil)
print("Son çıkış ağırlık: ",*cikis_Agirlik)
print("Son çıkış meyil: ",*cikis_Meyil)

print("\nÖğrenme oranı: ",lr)
print("Tekrar sayısı:",tekrar)
print("\n{} yaklaşımdan sonra ağ çıktısı:".format(tekrar))
print(*alinan_cikis)

#sysWait = input("\nProgram Tamamlandı.\nÇıkmak için Enter'a basın.\n")
time.sleep(3)