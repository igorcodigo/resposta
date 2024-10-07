def gerar_fibonacci_ate(n):
    fibonacci = [0, 1]
    while True:
        proximo = fibonacci[-1] + fibonacci[-2]
        if proximo > n:
            break
        fibonacci.append(proximo)
    return fibonacci

def main():
    numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    sequencia_fibonacci = gerar_fibonacci_ate(numero_informado)
    
    if numero_informado in sequencia_fibonacci:
        print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
