

def formula_calculo(lista_de_dicionarios):
    valor_concentracao = input("Digite o valor da concentração obtido em campo: ")
    valor_concentracao = float(valor_concentracao)

    if valor_concentracao < 1:
        print("Digite numeros positivos!")
    
    else:

        for elemento in lista_dicionarios:

            if valor_concentracao >= 0 and valor_concentracao <= elemento['concentracao1']:

                calculo = elemento['calculo_1']
                calculo_final = calculo * valor_concentracao
                resultado.append(calculo_final)

            elif valor_concentracao > elemento['concentracao1'] and valor_concentracao <= elemento['concentracao2']:

                calculo_2 = elemento['calculo_2']    
                calculo_3 = valor_concentracao - elemento['concentracao1']     
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + elemento['valor1'] 
                resultado.append(calculo_final)   

            elif valor_concentracao > elemento['concentracao3'] and valor_concentracao <= elemento['concentracao4']:

                calculo_2 = elemento['calculo_3']
                calculo_3 = valor_concentracao - elemento['concentracao2']
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + elemento['valor2']
                resultado.append(calculo_final)

            elif valor_concentracao > elemento['concentracao3'] and valor_concentracao < elemento['concentracao4']:

                calculo_2 = elemento['calculo_4']
                calculo_3 = valor_concentracao - elemento['concentracao3']
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + elemento['valor3']
                resultado.append(calculo_final)

            elif valor_concentracao < 250 and valor_concentracao <= 3000:

                calculo_2 = elemento['calculo_5']
                calculo_3 = valor_concentracao - elemento['concentracao4']
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + elemento['valor3']
                resultado.append(calculo_final)



resultado = []

lista_dicionarios = [{

    'nome' : 'MCP10',
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
]


formula_calculo(lista_dicionarios)
print(resultado)