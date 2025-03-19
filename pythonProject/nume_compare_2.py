nume = float(input("primeiro numero:"))
nume2 = float(input("segundo numero:"))
if nume > nume2:
    print(f"{nume} é maior q {nume2}")
elif nume < nume2:
    print(f"{nume2} é maior q {nume}")
else:
    print(f"{nume} é igual a {nume2}")