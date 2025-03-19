sexo = str(input("qual seu sexo (f-feminino)(m-masculino): "))
altura = float(input("qual seua altura: "))
if sexo == "f":
    ideal = (62.1 * altura)-44.7
else:
    ideal = (72.7 * altura)-58
print (f"seu peso ideal:{ideal}") 