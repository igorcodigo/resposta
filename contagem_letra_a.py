def verificar_a_em_string(input_string):
    contagem = input_string.lower().count('a')
    return contagem

def main():
    usuario_input = input("Informe uma string: ")
    contagem = verificar_a_em_string(usuario_input)
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

if __name__ == "__main__":
    main()
