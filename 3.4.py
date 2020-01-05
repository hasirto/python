while True:
    islem=input("""toplama=1
çıkarma=2
bölme=3
çarpma=4
döngüden çıkmak için=e
yapacağınız işlemi seçin: """)
    if islem == "e":
        break
    sayi1=int(input("birinci sayıyı gir: "))
    sayi2=int(input("ikinci sayıyı gir: "))
    if islem == "1":
        print("toplama işleminin sonucu: ",sayi1+sayi2)
    elif islem == "2":
        print("çıkarma işleminin sonucu: ",sayi1-sayi2)
    elif islem == "3":
        print("bölme işleminin sonucu: ",sayi1/sayi2)
    elif islem == "4":
        print("çarpma işleminin sonucu: ",sayi1*sayi2)
    else:
        print("yanlış seçim")