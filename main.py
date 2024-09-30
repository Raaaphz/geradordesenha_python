from random import choice
import string

tamanho = int(input("Quantos digitos quer na sua senha? "))
caracteres = string.ascii_letters1 + string.digits + string.punctuation
senha = ''

for i in range(tamanho):
    senha += choice(caracteres)

print (senha)