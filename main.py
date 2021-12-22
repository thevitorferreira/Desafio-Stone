import pandas as pd     


pessoas = ['Vitor', 'Lucas', 'Guilherme', 'Lima']

dados = pd.read_excel("gastos.xlsx")

def divisao_despesa(dados,lista_pessoas):
    pessoas = {}
    for pessoa in lista_pessoas:
        pessoas[pessoa] = 0
    dados["Valor Total"] = dados["Valor Unitário"]*dados["Quantidade"]
    total_gasto = dados["Valor Total"].sum()

    quantidade = len(pessoas)
    centavos = int(str(total_gasto).split('.')[1][0:2])
    reais = int(total_gasto/1)
    reais_divididos = reais / quantidade
    centavos_divididos = centavos / quantidade
    centavos_divididos = centavos_divididos + int(str(reais_divididos).split('.')[1])
    reais_divididos = int(str(reais_divididos).split('.')[0])

    pagamento_a_mais_ultimo = 0
    if centavos_divididos%1!=0:
        pagamento_a_mais_ultimo = int((centavos_divididos%1) * quantidade)
    centavos_divididos = int(centavos_divididos)
    for pessoa in list(pessoas.keys()):
        pessoas[pessoa] = reais_divididos + centavos_divididos/100
    ultima_pessoa = list(pessoas.keys())[-1]
    pessoas[ultima_pessoa] = pessoas[ultima_pessoa]+pagamento_a_mais_ultimo/100
    return(pessoas)

print(divisao_despesa(dados,pessoas))

