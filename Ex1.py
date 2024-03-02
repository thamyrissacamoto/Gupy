def verificaFibonacci(numero):
    a, b = 0, 1
    
    if numero == a or numero == b:
        return True
    while b <= numero:
        a, b = b, a + b
        if b == numero:
            return True
    return False
    
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if verificaFibonacci(numero):
    print("{} pertence à sequência de Fibonacci.".format(numero))
else:
    print("{} não pertence à sequência de Fibonacci.".format(numero))
