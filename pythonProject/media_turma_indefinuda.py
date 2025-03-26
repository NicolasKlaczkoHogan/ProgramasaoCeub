ct=0
total = 0
print("dijite -1 para parar")
disiplina = input("qual a disiplina: ")
while True:
    nota_aluno = int(input("nota de aluno:"))
    if nota_aluno == -1:
        break
    total += nota_aluno
    ct += 1
print(f"a turma tem {ct} alunos")
print(disiplina)
print(f"soma nota {total:.2f}")
print (f"a media da turma é { total / ct:.2f}")

