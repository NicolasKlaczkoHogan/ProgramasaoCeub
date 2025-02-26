nota_quant = int(input("quantas notas: "))
nota_quant_save = nota_quant
nota = float(0)
while nota_quant > 0:
    nota1 = float(input("nota: "))
    nota =  nota + nota1
    nota_quant = nota_quant - 1

media = nota / nota_quant_save
print (f"sua media é {media:.2f}")