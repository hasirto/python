islem=input("yapacağınız işlemi girin:\ntoplama=1 \ncarpma=2 \nbölme=3 \ncıkarma=4\n")

sayi1=int(input("ilk sayiyi gir"))
sayi2=int(input("ikinci sayiyi gir"))

if islem=="1":
    toplam=sayi1+sayi2
    print("yaptığın işlemin sonucu :",toplam)

elif islem=="2":
    carpim=sayi1*sayi2
    print("yaptığın işlemin sonucu :",carpim)

elif islem=="3":
    bolum=sayi1/sayi2
    print("yaptığın işlemin sonucu :",bolum)

elif islem=="4":
    cikarma=sayi1-sayi2
    print("yaptığın işlemin sonucu :",cikarma)

else:
    print("senin niyetin ne gardaşım")