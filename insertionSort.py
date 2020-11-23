dizi =  [10,2,35,7,9,8,13]   #dizimiz
for i in range(1,len(dizi)):  #dizinin ikinci elemanından dizinin son elemanına kadar döngü
    key=dizi[i]  #aktif elemanı hafızada tut
    j=i-1  #i'nin bir eksiğinden geri doğru döngü çalışacak
    while (j>=0 and key<dizi[j]):  #döngü kendinden büyüğü bulana kadar geri doğru çalışıyor
        dizi[j+1]=dizi[j]  #dizi[i]'den büyük olan varsa ilk bulunan büyük sayıyı bir sonraki konuma al
        j-=1 #j 0'a doğru düşürülüyor. while ile 0'dan büyük olma şartını koymuştuk
    dizi[j+1]=key  #hafızada tutulanı j+1. indexe yerleştir
print(dizi) #diziyi yazdır. 
