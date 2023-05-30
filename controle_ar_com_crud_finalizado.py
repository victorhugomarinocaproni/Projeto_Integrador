from mysql.connector import connect

def obtemConexaoComMySQL (servidor, usuario, senha, bd):
    if obtemConexaoComMySQL.conexao==None:
        obtemConexaoComMySQL.conexao = \
        connect(host='localhost', user='root', passwd='1234', database='projeto_integrador')
    return obtemConexaoComMySQL.conexao
obtemConexaoComMySQL.conexao=None

resposta_usuario = ''
resposta_de_saida = ''
numero_da_linha = 1

resultado = []
resultado_aproximado = []


def formula_calculo(lista_de_dicionarios):

    for dicionario in lista_de_dicionarios:
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
        print('Pessoas de Grupos sensíveis como crianças, idosos, pessoas com doenças respiratórias e cardíacas, podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.')

    elif maior_valor_atual > 80 and maior_valor_atual <= 120:
        print('Qualidade N3 - RUIM')
        print('Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos  olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças cardíacas ou respiratórias) podem apresentar efeitos mais sérios na saúde.')

    elif maior_valor_atual > 120 and maior_valor_atual <= 200:
        print('Qualidade N4 - MUITO RUIM')
        print('Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda  falta de ar e respiração ofegante. Efeitos mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas.)')

    elif maior_valor_atual > 200:
        print('Qualidade N5 - PÉSSIMA')
        print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento do mortes prematuras em pessoas de grupos sensíveis.')


def create(numero_linha):

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    lista_valores_digitados = []

    for elemento in define_dicionarios():

        elemento = elemento['elemento']

        while True:

            try:
                valor_digitado = float(input(f'Digite a concentração de {elemento}: '))

                if valor_digitado < 0:
                    print('Valores negativos não são abordados no programa.')
                    print()
                    continue
                break

            except ValueError:
                print('Por favor, insira um valor numérico válido.')
                print()

        lista_valores_digitados.append(valor_digitado)


    mcp10,mp2_5,o3,mco,no2,so2 = lista_valores_digitados

    comando = f'INSERT INTO elementos (nmr_linha,MCP10,MP2_5,O3,MCO,NO2,SO2) VALUES {numero_linha,mcp10,mp2_5,o3,mco,no2,so2};'
    cursor.execute(comando)
    conexao.commit()

def read():

    banco_vazio = False

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    comando = 'select * from elementos;'
    cursor.execute(comando)
    dados_selecionados = cursor.fetchall() 

    if dados_selecionados == []:
        print('O Banco de Dados está vazio.')
        banco_vazio = True
        return banco_vazio

    else:

        print('Os valores selecionados foram: ')
        print()

        for lista_dados in dados_selecionados:

            indice_linha, mcp10, mp2_5,o3,mco,no2,so2 = lista_dados

            print(f'Linha: {indice_linha}')
            print(f'MCP10: {mcp10}, MP2_5: {mp2_5}, O3: {o3}, MCO: {mco}, NO2: {no2}, SO2: {so2}')
            print()

    return banco_vazio
    

def update():

    banco_vazio = read()

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    linha_validador = False
    elemento_validador = False
    valor_validador = False
    quantidade_de_linhas = pega_ultima_linha()

    if banco_vazio == True:
        linha_a_alterar = 0
        return linha_a_alterar
    
    else:

        while linha_validador == False:

            try:
                linha_a_alterar = int(input('Digite o índice da linha que deseja alterar: '))

                if linha_a_alterar > quantidade_de_linhas or linha_a_alterar < 1:
                    print('Por favor, insira o valor de uma linha existente.')
                    continue
                linha_validador = True

            except ValueError:
                print('Por favor, entre com um índice da linha.')
                continue

        while elemento_validador == False:

            try:
                elemento_a_alterar = input('Digite o nome do elemento que deseja alterar: ').upper()
                if elemento_a_alterar not in ['MCP10', 'MP2_5', 'O3', 'MCO', 'NO2', 'SO2']:
                    print('Por favor, entre com um nome de elemento existente no programa.')
                    continue
                elemento_validador = True

            except ValueError:
                print('Por favor, entre com o nome do elemento.')
                continue

        while valor_validador == False:

            try:
                novo_valor = float(input('Digite um novo valor de concentração: '))

                if novo_valor < 0:
                    print('Não existem valores negativos de concentração. Por favor, tente novamente!')
                    continue
                valor_validador = True

            except ValueError:
                print('Por favor, entre com um valor numérico para a concentração.')
                continue

        comando = f'UPDATE ELEMENTOS SET {elemento_a_alterar} = {novo_valor} where nmr_linha="{linha_a_alterar}"'
        cursor.execute(comando)
        conexao.commit()

        return linha_a_alterar

def delete():

    banco_vazio = read()

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()
    quantidade_de_linhas = pega_ultima_linha()

    if banco_vazio == True: 
        return 
    
    else:

        while True:

            try:
                linha_a_deletar = int(input('Digite a linha que deseja deletar: '))

                if linha_a_deletar > quantidade_de_linhas or linha_a_deletar < 1:
                    print('Entre com um valor de linha existente.')
                    continue
                break

            except ValueError:
                print('Por favor, insira um número inteiro correspondente à linha que deseja deletar.')
                continue

        comando = f'DELETE FROM ELEMENTOS WHERE nmr_linha = "{linha_a_deletar}"'
        cursor.execute(comando)
        conexao.commit()

        comando_le_banco = 'select * from elementos'
        cursor.execute(comando_le_banco)
        dados_lidos = cursor.fetchall()

        total_linhas = pega_ultima_linha()

        linha_a_ser_atualizada = 1

        for lista_dados in dados_lidos:

            indice_linha, mcp10, mp2_5, o3, mco, no2, so2 = lista_dados

            comando_atualiza_linha = f'UPDATE ELEMENTOS SET nmr_linha = "{linha_a_ser_atualizada}" where MCP10 = "{mcp10}" AND MP2_5 = "{mp2_5}" AND O3 = "{o3}" AND MCO = "{mco}" AND NO2 = "{no2}" AND SO2 = "{so2}" '
            cursor.execute(comando_atualiza_linha)
            conexao.commit()
            linha_a_ser_atualizada += 1
            


def geral_delete():

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    comando = f'DELETE FROM ELEMENTOS WHERE nmr_linha > -1 OR MCP10 > -1 OR MP2_5 > -1 OR O3 > -1 OR MCO > -1 OR NO2 > -1 OR SO2 > -1 '
    cursor.execute(comando)
    conexao.commit()


def pega_ultima_linha():

    conexao=obtemConexaoComMySQL('localhost','root','1234','projeto_integrador')
    cursor=conexao.cursor()

    comando = 'SELECT COUNT(*) FROM ELEMENTOS'
    cursor.execute(comando)
    lista_qtd_linhas = cursor.fetchall()

    for tupla_qtd_linhas in lista_qtd_linhas:
        for valor_linhas in tupla_qtd_linhas:

            qtd_linhas = valor_linhas
    
    return qtd_linhas


def define_dicionarios():

    lista_dicionarios = [{

        'elemento' : 'MCP10',
        'nome' : f'select MCP10 from elementos where nmr_linha="{numero_da_linha}"',
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
        'nome' : f'select MP2_5 from elementos where nmr_linha="{numero_da_linha}"',
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
        'nome' : f'select O3 from elementos where nmr_linha="{numero_da_linha}"',
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
        'nome' : f'select MCO from elementos where nmr_linha="{numero_da_linha}"',
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
        'nome' : f'select NO2 from elementos where nmr_linha="{numero_da_linha}"',
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
        'nome' : f'select SO2 from elementos where nmr_linha="{numero_da_linha}"',
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

    return lista_dicionarios



geral_delete()
passar_comeco = False
while True:

    resultado = []
    resultado_aproximado = []

    if passar_comeco:
        pass
    else:
        print('Insira as concentrações obtidas em campo para que o programa calcula a qualidade do ar.')
        print()

        create(numero_da_linha)
        formula_calculo(define_dicionarios())
        verifica_pior_indice(resultado)


    while True:

        passar_comeco = False
        print()
        resposta_usuario = input('Você deseja realizar alguma ação? [listar] ou [atualizar] ou [inserir] ou [deletar] ou [sair]: ').lower()
        print()

        if resposta_usuario in ['listar','atualizar','inserir','deletar','sair']:
            break
        else:
            print('Por favor, digite uma das opções corretamente')

    if resposta_usuario == 'listar':
        read()
        passar_comeco = True

    elif resposta_usuario == 'atualizar':
        numero_da_linha = update()

        if numero_da_linha == 0:
            passar_comeco = True
            pass

        else:
            resultado = []
            resultado_aproximado = []
            formula_calculo(define_dicionarios())
            verifica_pior_indice(resultado)
            passar_comeco = True
        
    elif resposta_usuario == 'inserir':

        numero_da_linha = pega_ultima_linha() + 1
        continue

    elif resposta_usuario == 'sair':
        break

    elif resposta_usuario == 'deletar':
        delete()
        passar_comeco = True

    if resposta_usuario == 'sair':
        break

print('Obrigado por utilizar nosso programa!')
print()