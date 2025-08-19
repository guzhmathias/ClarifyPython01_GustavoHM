def divisao(a, b):
    try:
        # Tenta efetuar a divisão
        resultado = a/b
        print(f"Resultado da divisão de A por B é {resultado:.2f}")
    except ZeroDivisionError:
        # Se houver um erro de divisão por zero, o código entra dentro do except e é executado
        print("Erro: impossível dividir por 0")
    except TypeError:
        # Caso algum valor não seja um número, esse except será executado
        print("Ambos os valores precisam ser números")
    except Exception as erro:
        # Captura qualquer outro erro que tenha sido tratado nos anteriores
        print(f"Erro Inesperado {erro}")
    else:
        #Só é executado caso "Try" seja bem sucedido
        print("Operação realizada com sucesso!")
    finally:
        # Executado sempre, independentemente se deu erro ou sucesso
        print("Processo finalizado!")

# Teste 01 - Divisão Normal

divisao(10,2)

#Teste 02 - Divisão por Zero

divisao(10,0)

#Teste 03 - Operação com não números

divisao("dois", 10)
divisao(2, "dez")


        
