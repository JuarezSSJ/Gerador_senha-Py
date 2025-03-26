import random #biblioteca para gerar valores aleatorios 
import string #permite acessar letras, numeros e simbolos

#criar uma função para receber o tamanho da senha que o usuario deseja e usando o rondom realizar uma escolha aleatoria
def gerar_senha (tamanho):
    itens = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(itens) for i in range(tamanho))
    return senha

tamanho_senha = int(input("Qual o tamanho da sua senha: "))
#chamando a função
senha = gerar_senha(tamanho_senha)

print(senha)