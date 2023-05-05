from mysql.connector import connect

def obtemConexaoComMySQL (servidor, usuario, senha, bd):
    if obtemConexaoComMySQL.conexao==None:
        obtemConexaoComMySQL.conexao = \
        connect(host='localhost', user='root', passwd='1234', database='projeto_integrador')
    return obtemConexaoComMySQL.conexao
obtemConexaoComMySQL.conexao=None

resposta_usuario = ''
resposta_de_saida = ''

resultado = []
resultado_aproximado = []

lista_dicionarios = [{

    'elemento' : 'MCP10',
    'nome' : 'select MCP10 from elementos',
    'valor1' : 41,
    'valor2' : 81,
    'valor3' : 121,
    'concentracao1' : 50,
    'concentracao2' : 100, 
    'concentracao3' : 150,
    'concentracao4' : 250,
    'concentracao5' : 3000,
    'calculo_1' : 0.8, # --> 40/50
    'calculo_2' : 0.78, # -->(80-41)/(100-50)
    'calculo_3' : 0.78, # --> (120-81)/(150-100)
    'calculo_4' : 0.79, # --> (200-121)/(250-150)
    'calculo_5' : 0.029, # --> (200-121)/(3000-250)
},

{
    'elemento' : 'MP2_5',
    'nome' : 'select MP2_5 from elementos',
    'valor1' : 41,
    'valor2' : 81,
    'valor3' : 121,
    'concentracao1' : 25,
    'concentracao2' : 50, 
    'concentracao3' : 75,
    'concentracao4' : 125,
    'concentracao5' : 3000,
    'calculo_1' : 1.6, # --> 40/25
    'calculo_2' : 1.56, # --> (80-41)/(50-25)
    'calculo_3' : 1.56, # --> (120-81)/(75-50)
    'calculo_4' : 1.58, # --> (200-121)/(125-75)
    'calculo_5' : 0.02747826, # --> (200-121)/(3000-125)
},

{
    'elemento' : 'O3',
    'nome' : 'select O3 from elementos',
    'valor1' : 41,
    'valor2' : 81,
    'valor3' : 121,
    'concentracao1' : 100,
    'concentracao2' : 130, 
    'concentracao3' : 160,
    'concentracao4' : 200,
    'concentracao5' : 3000,
    'calculo_1' : 0.4, # --> 40/100
    'calculo_2' : 1.3, # --> (80-41)/(130-100)
    'calculo_3' : 1.3, # --> (120-81)/(160-130)
    'calculo_4' : 1.975, # --> (200-121)/(200-160)
    'calculo_5' : 0.00282143, # --> (200-121)/(3000-200)
},
{
    'elemento' : 'MCO',
    'nome' : 'select MCO from elementos',
    'valor1' : 41,
    'valor2' : 81,
    'valor3' : 121,
    'concentracao1' : 9,
    'concentracao2' : 11, 
    'concentracao3' : 13,
    'concentracao4' : 15,
    'concentracao5' : 3000,
    'calculo_1' : 4.44444444445, # --> 40/9
    'calculo_2' : 19.5, # --> (80-41)/(11-9)
    'calculo_3' : 19.5, # --> (120-81)/(13-11)
    'calculo_4' : 39.5, # --> (200-121)/(15-13)
    'calculo_5' : 0.0264657, # --> (200-121)/(3000-15)
},
{
    'elemento' : 'NO2',
    'nome' : 'select NO2 from elementos',
    'valor1' : 41,
    'valor2' : 81,
    'valor3' : 121,
    'concentracao1' : 200,
    'concentracao2' : 240, 
    'concentracao3' : 320,
    'concentracao4' : 1130,
    'concentracao5' : 3000,
    'calculo_1' : 0.2, # --> 40/200
    'calculo_2' : 0.975, # --> (80-41)/(240-200)
    'calculo_3' : 0.4875, # --> (120-81)/(320-240)
    'calculo_4' : 0.97531, # --> (200-121)/(1130-320)
    'calculo_5' : 0.042246, # --> (200-121)/(3000-1130)
},
{
    'elemento' : 'SO2',
    'nome' : 'select SO2 from elementos',
    'valor1' : 41,
    'valor2' : 81,
    'valor3' : 121,
    'concentracao1' : 20,
    'concentracao2' : 40, 
    'concentracao3' : 365,
    'concentracao4' : 800,
    'concentracao5' : 3000,
    'calculo_1' : 2, # --> 40/20
    'calculo_2' : 1.95, # --> (80-41)/(40-20)
    'calculo_3' : 0.12, # --> (120-81)/(365-40)
    'calculo_4' : 0.18161, # --> (200-121)/(800-365)
    'calculo_5' : 0.03591, # --> (200-121)/(3000-800)
},
]

def formula_calculo(lista_de_dicionarios):

    for dicionario in lista_dicionarios:
        dicionario = dicionario

        conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
        cursor=conexao.cursor()
        cursor.execute(dicionario['nome'])
        dadosSelecionados=cursor.fetchall()  # se for leitura do banco é fetchall

        for linha in dadosSelecionados:
            valor_concentracao = list(linha)

        valor_concentracao = valor_concentracao[0]

        if valor_concentracao < 1:
            print("Digite numeros positivos!")
        
        else:

            if valor_concentracao >= 0 and valor_concentracao <= dicionario['concentracao1']:

                calculo = dicionario['calculo_1']
                calculo_final = calculo * valor_concentracao
                resultado.append(calculo_final)
                continue

            elif valor_concentracao > dicionario['concentracao1'] and valor_concentracao <= dicionario['concentracao2']:

                calculo_2 = dicionario['calculo_2']    
                calculo_3 = valor_concentracao - dicionario['concentracao1']     
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + dicionario['valor1'] 
                resultado.append(calculo_final) 
                continue  

            elif valor_concentracao > dicionario['concentracao2'] and valor_concentracao <= dicionario['concentracao3']:

                calculo_2 = dicionario['calculo_3']
                calculo_3 = valor_concentracao - dicionario['concentracao2']
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + dicionario['valor2']
                resultado.append(calculo_final)
                continue

            elif valor_concentracao > dicionario['concentracao3'] and valor_concentracao < dicionario['concentracao4']:

                calculo_2 = dicionario['calculo_4']
                calculo_3 = valor_concentracao - dicionario['concentracao3']
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + dicionario['valor3']
                resultado.append(calculo_final)
                continue

            elif valor_concentracao > dicionario['concentracao4'] and valor_concentracao <= dicionario['concentracao5']:

                calculo_2 = dicionario['calculo_5']
                calculo_3 = valor_concentracao - dicionario['concentracao4']
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + dicionario['valor3']
                resultado.append(calculo_final)
                continue

def verifica_pior_indice(lista_resultado_aproximado):

    resultado_aproximado = []

    for valor in resultado:

        valor = f'{valor:.2f}'
        resultado_aproximado.append(valor)

    print()
    print(f'Os índices calculados foram: {resultado_aproximado}')

    maior_valor_atual = 0

    for maior_valor in resultado_aproximado:

        maior_valor = float(maior_valor)

        if maior_valor > maior_valor_atual:
            maior_valor_atual = maior_valor

    print()        
    print(f'O pior índice encontrado foi: {maior_valor_atual}')
    print()

    if maior_valor_atual >= 0 and maior_valor_atual <= 40:
        print('Qualidade N1 - BOA')

    elif maior_valor_atual > 40 and maior_valor_atual <= 80:
        print('Qualidade N2 - MODERADA')

    elif maior_valor_atual > 80 and maior_valor_atual <= 120:
        print('Qualidade N3 - RUIM')

    elif maior_valor_atual > 120 and maior_valor_atual <= 200:
        print('Qualidade N4 - MUITO RUIM')

    elif maior_valor_atual > 200:
        print('Qualidade N5 - PÉSSIMA')


def create():

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    lista_valores_digitados = []

    for elemento in lista_dicionarios:

        elemento = elemento['elemento']

        valor_digitado = float(input(f'Digite a concentração de {elemento}: '))

        lista_valores_digitados.append(valor_digitado)


    mcp10,mp2_5,o3,mco,no2,so2 = lista_valores_digitados

    comando = f'INSERT INTO elementos (MCP10,MP2_5,O3,MCO,NO2,SO2) VALUES {mcp10,mp2_5,o3,mco,no2,so2};'
    cursor.execute(comando)
    conexao.commit()

def read():

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    comando = 'select * from elementos;'
    cursor.execute(comando)
    dados_selecionados = cursor.fetchall() 
    print(f'Os valores inseridos foram: {dados_selecionados}.')


def update():

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    elemento_a_alterar = input('Qual elemento deseja alterar: ').upper()
    novo_valor = float(input('Digite um novo valor de concentração: '))

    comando = f'UPDATE ELEMENTOS SET {elemento_a_alterar} = {novo_valor}'
    cursor.execute(comando)
    conexao.commit()

def delete():

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    comando = f'DELETE FROM ELEMENTOS WHERE MCP10 > -1 OR MP2_5 > -1 OR O3 > -1 OR MCO > -1 OR NO2 > -1 OR SO2 > -1'
    cursor.execute(comando)
    conexao.commit()


while True:

    delete()
    print('Insira as concentrações obtidas em campo para que o programa calcula a qualidade do ar.')
    print()

    create()
    formula_calculo(lista_dicionarios)
    verifica_pior_indice(resultado)


    while True:

        print()
        resposta_usuario = input('Você deseja realizar alguma ação? [listar] ou [atualizar] ou [inserir]: ').lower()
        print()

        if resposta_usuario in ['listar','atualizar','inserir']:
            break
        else:
            print('Por favor, digite uma das opções corretamente')

    if resposta_usuario == 'listar':
        read()

    elif resposta_usuario == 'atualizar':
        update()
        resultado = []
        resultado_aproximado = []
        formula_calculo(lista_dicionarios)
        verifica_pior_indice(resultado)
        

    else:
        delete()
        continue

    while True:

        print()
        resposta_de_saida = input('Você deseja sair do programa? [sim] ou [nao]: ').lower()

        if resposta_de_saida in ['sim','s','nao','n']:
            break
        else:
            print('Por favor, digite [sim] ou [nao]')

    if resposta_de_saida in ['sim','s']:
        break

print()
print('Obrigado por utilizar nosso programa!')