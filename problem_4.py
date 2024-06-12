def calcular_prestacao(valor_casa, salario, anos):
    meses = anos * 12
    prestacao = valor_casa / meses
    return prestacao

def aprovar_emprestimo():
    valor_casa = float(input("digite o valor da casa a comprar: "))
    salario = float(input("digite o salário: "))
    anos = int(input("digite a quantidade de anos a pagar: "))

    prestacao_maxima = salario * 0.3

    prestacao = calcular_prestacao(valor_casa, salario, anos)

    if prestacao <= prestacao_maxima:
        print("empréstimo aprovado! o valor da prestação mensal é de R$", prestacao)
    else:
        print("empréstimo negad! o valor da prestação mensal passa de 30% do salário.")

aprovar_emprestimo()