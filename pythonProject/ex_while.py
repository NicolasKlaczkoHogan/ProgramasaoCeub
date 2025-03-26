ct=0
print("dite [-1] para sair da repetisao")
while True:
    numero=int(input("digite um numero:"))
    if numero == -1:
        break
    ct=ct+1
print ("quantidade de numeros digitados", ct)