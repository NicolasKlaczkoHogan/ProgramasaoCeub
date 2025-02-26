valor1 = float(input("insira valor 1= "))
valor2 = float(input("insira valor 2= "))
oprtasao = str(input("lista de operações:\n + soma\n - sumtração\n * mutiplicassão\n / divisão \n // divisão intero\n % resto de divisão\n ** elevado\n qual operação deseja realisar: "))
if oprtasao == "+":
    resultado = (valor1 + valor2)
    print (resultado)
elif oprtasao == "-":
    resultado = (valor1 - valor2)
    print("seu resultado é=", resultado)
elif oprtasao == "*":
    resultado = (valor1 * valor2)
    print("seu resultado é=", resultado)
elif oprtasao == "/":
    resultado = (valor1 / valor2)
    print("seu resultado é=", resultado)
elif oprtasao == "//":
    resultado = (valor1 // valor2)
    print("seu resultado é=", resultado)
elif oprtasao == "%":
    resultado = (valor1 % valor2)
    print("seu resultado é=", resultado)
elif oprtasao == "**":
    resultado = (valor1 ** valor2)
    print("seu resultado é=", resultado)
else:
    print ("operasao invalida")