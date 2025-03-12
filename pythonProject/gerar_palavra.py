import random
import string
#nao use palavras com mais de 4 letras
palavra = input("qual palavta quer gerar:")
tamanho = int(len(palavra))
resposta = ""
cauter = 0
while resposta != palavra:
    
    resposta = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))
    cauter = cauter + 1


print(f"levou {cauter} tentadivas para formar {resposta}")
