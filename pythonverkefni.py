#pythonverkefni
print("Dæmi 1")
tala1=int(input("sláðu inn tölu 1 "))
tala2=int(input("sláðu inn tölu 2 "))
summa=tala1+tala2
margfoldun=tala1*tala2
print("Summa talnanna er",summa)
print("Margföldun talnanna er",margfoldun)

print("Dæmi 2")
fornafn=input("Sláðu inn fornafn ")
eftirnafn=input("Sláðu inn eftirnafn ")
print("Halló ",fornafn,eftirnafn )

print("Dæmi 3")
hastafir=0
lagstafir=0
asdf=0
asd=0
texti=input("Sláðu inn texta ")
for i in (texti):
    if i.isupper():
        hastafir+=1
        if texti[asdf+1].islower():
            asd+=1
    if i.islower():
        lagstafir+=1
    asdf+=1
print(hastafir,"Hástafir")
print(lagstafir,"Lágstafir")
print(asd,"Lágstafir strax á eftir hástöfum")
