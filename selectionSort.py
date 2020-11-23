dizi =  [10,2,35,7,9,8,13]   #dizimiz
for i in range(len(dizi)):   #i 0'dan dizinin son indeksine kadar döngü
    for j in range(i+1,len(dizi)): #j i+1'den dizinin son indeksine kadar döngü
        if (dizi[i]>dizi[j]):  #eğer dizinin i. elemanı dizinin j. elemanından büyükse 
            temp=dizi[i]
            dizi[i]=dizi[j]
            dizi[j]=temp          
            #yer değiştirme işlemleri
print(dizi)  #diziyi yazdır


