def main():
    soma = 0
    while True:
        numero = float(input("digite um número (digite 0 para sair): "))
        if numero == 0:
            break
        soma += numero
    return soma