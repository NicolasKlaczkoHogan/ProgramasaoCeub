genero = ""
m=0
f=0
maior=float('-inf')
menor=float('inf')
altura = 1
print ("insira 0 na altura para sair")
while True:
    altura=float(input("insira altura: "))
    if altura == 0:
        break
    if altura != 0:
        temp = str(input("a altura esta em cm ou m: "))
        if temp == "m":
            altura = altura * 100 
        genero=str(input("insira o genero f (mulher) m(homen): "))
        if genero == "m":
            m=m+1
        elif genero=="f":
            f=f+1
        else:
            print ("input invalido insira novamente")
    
    if altura < menor:
        menor=altura
    if altura >maior:
        maior=altura
print(f"numero de homem {m} \nnumero de mulher {f} \nmaior altura {maior}\nmenor altura {menor}")