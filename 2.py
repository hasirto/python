vize=int(input("vizeyi gir: "))
final=int(input("finali gir: "))
ortalama=vize*0.4+final*0.6
print("dönem sonu notunuz: ",ortalama)

if 100>=ortalama>=90:
    print("AA")
elif 90>=ortalama>=80:
    print("BA")
elif 80>=ortalama>=70:
    print("BB")
elif 70>=ortalama>=60:
    print("BC")
elif 60>=ortalama>=50:
    print("CC")
elif 50>=ortalama>=40:
    print("DC")
elif 40>=ortalama>0:
    print("FF")
elif ortalama>100 or ortalama>=0:
    print("böyle bir not yok ")