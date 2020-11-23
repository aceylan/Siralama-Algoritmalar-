dizi =  [10,2,35,7,9,8,13]   #dizimiz
for i in range(len(dizi)-1): #dizinin eleman sayısının bir eksiği kadar döngü yap
    sirali=True  #eğer sıralanmışsa döngü sonuna kadar devam etmemesi amaçlı bir değişken
    for j in range(0, len(dizi)-i-1): #dizinin başından sonuna kadar ikişer ikişer karşılaştırma yapıp yer değiştirme yap
        if dizi[j] > dizi[j+1] : #dizi[j] büyük dizi[j+1] ise yer değiştir
            temp=dizi[j]
            dizi[j]=dizi[j+1]
            dizi[j+1]=temp
            sirali=False #sıralı değilmiş, sirali değişkenini false yap. 
    if (sirali):  #sirali False'a dönmediği için sıralama bitmiş. döngüden çık
        break
print(dizi)