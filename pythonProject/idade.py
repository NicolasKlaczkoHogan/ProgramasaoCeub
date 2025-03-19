anoNacimento = int(input("que ano vc naseu:"))
idade = 2025 - anoNacimento
if idade >= 16:
    print("voce pode votar")
    print(anoNacimento)
    print(idade)
else:
    print("voce nao pode votar")
    print(idade)
    print(anoNacimento)
if idade >= 18:
    print("pode pegar carteira de abilitasao")
else:
    print("nao pode pedagar cartera de abilitasao")
