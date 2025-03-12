v_venda=float(input("valor de compra:"))
v_compra=float(input("valor de vanda:"))
p_nome=input("nome de produto:")
lucro=v_compra-v_venda
if lucro == 0:
    print(p_nome)
    print("sao iguais.")
    print(lucro)
elif lucro > 0:
    print(p_nome)
    print("impresa lucrou.")
    print(lucro)
else:
    print(p_nome)
    print("teve prejuiso.")
    print(lucro)