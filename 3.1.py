sayi1=int(input("birinci sayıyı giriniz: "))
sayi2=int(input("ikinci sayıyı giriniz: "))
islem=input("""toplama=1
çarpma=2
çıkarma=3
bölme=4
kalan bulma=5
seçiminizi yapın: """)
if islem == "1":
    print("toplama işleminin sonucu: ",sayi1+sayi2)
elif islem == "2":
    print("çarpma işleminin sonucu: ",sayi1*sayi2)
elif islem == "3":
    print("çıkarma işleminin sonucu: ",sayi1-sayi2)
elif islem == "4":
    print("bölme işleminin sonucu: ",sayi1/sayi2)
elif islem == "5":
    print("sayıların bölümünden kalan",sayi1%sayi2)
else:
    print("yanlış seçim")