#Exemplo de Função

def soma (a, b):
    c = a + b
    return c

#Exemplo de Classe

class Funcionario: 
    def __init__ (self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario (self, porcentagem):
        self.salario += self.salario * porcentagem / 100


