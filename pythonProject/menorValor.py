valor = 1
soma = 0
c=0
menor_valor = float('inf')
maior_valor=float('-inf')
print("digite 0 para sair")
while valor != 0:
    valor = float(input("valor= "))
    if valor < menor_valor and valor != 0:
        soma= soma+valor
        menor_valor = valor
        c=c+1
    if valor > maior_valor and valor != 0:
        maior_valor = valor
        soma= soma+valor
print (f"menor valor = {menor_valor} contador = {c} soma = {soma} maior valor = {maior_valor}")