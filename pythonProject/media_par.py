ct = 0
ctt=0
n1=0
print("insira 0 para finalizar prorama.")
while True:
    n2=int(input("insira um numero: "))
    if n2 == 0:
        break
    elif n2 % 2 == 0:
        n1 += n2
        ct += 1
        ctt += 1
    else:
        ctt += 1
print(f"{ct} de {ctt} numeros inseridos sao pareses")
print(f"a media dos pares é {n1 / ct:.2f}")