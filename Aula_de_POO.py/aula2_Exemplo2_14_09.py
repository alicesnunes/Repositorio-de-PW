#Arquivo de Teste

from modulo import soma, Funcionario

try: 
    resultado = soma (10, 5)
    assert resultado == 15
    print ('CORRETO')
except AssertionError:
    print ('ERRADO')

try:
    resultado = soma (-20,-30)
    assert resultado == -50
    print ('CORRETO')
except AssertionError:
    print ('ERRADO')

try:
    func1 = Funcionario ('Sara', 5000.00)
    func1.aumentar_salario (10) 
    assert func1.salario == 5500.00
    print ('CORRETO')
except AssertionError: 
    print ('ERRADO')