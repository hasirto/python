islem=input("""toplama=1
carpma=2
bölme=3
çıkarma=4
seçiminizi yapın: """)
sayi1=int(input("birinci sayıyı giriniz"))
sayi2=int(input("ikinci sayıyıy giriniz"))
if islem == "1":
    print("toplama yapacaksın")
elif islem == "2":
    print("carpma yapacaksın")
elif islem == "3":
    print("bölme yapacaksın")
elif islem == "4":
    print("çıkarma yapacaksın")
else:
    print("yanlış seçim")


