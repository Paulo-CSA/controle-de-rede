import os


ESTOQUE = {}

def menu():
    print(" " )  
    print("    █████████")
    print("    █▄█████▄█")
    print("    █▼▼▼▼▼")
    print("    █")
    print("    █   CONTROLE DE REDES ")
    print("    █ 1 - Mostar todas as Unidades")
    print("    █ 2 - Buscar Unidade")
    print("    █ 3 - Inserir Unidade")
    print("    █ 4 - Remover Unidade")
    print("    █ 0 - Sair")
    print("    █")
    print("    █▲▲▲▲▲")
    print("    █████████")
    print("    ██ ██")
     
    
def mostrar_estoque():
    if ESTOQUE:
        for estoque in ESTOQUE:
            buscar(estoque)
    else:
        print('>>>> BANCO VAZIO')


def buscar(estoque):
    try:
        print(estoque,'| ','Tel:', ESTOQUE[estoque]['telefone'],'| ''Gateway:', ESTOQUE[estoque]['gateway'],'| ''Wan:', ESTOQUE[estoque]['wan'],'| ''Circuito:', ESTOQUE[estoque]['circuito'])
        print('---------------------------------------------------------------------------------------------------------------')
    except KeyError:
        print('>>>> Item inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)


def estoquekey(busca):
    try:
        for key in ESTOQUE:
            if busca != None and str(busca) in str(key):
                print('UNIDADE:',key,'|','TELEFONE:',ESTOQUE[key]['telefone'],'| ''GATEWAY:',ESTOQUE[key]['gateway'],'| ''WAN:',ESTOQUE[key]['wan'],'| ''CIRCUITO:',ESTOQUE[key]['circuito'])
                print('------------------------------------------------------------------------------------------------------------------------')
    except KeyError:
            print('>>>> Item inexistente')
    except Exception as error:
            print('>>>> Um erro inesperado ocorreu')
            print(error)


def inserir_item(estoque, telefone, gateway, wan, circuito):
    ESTOQUE[estoque] = {
        'telefone': telefone,
        'gateway': gateway,
        'wan': wan,
        'circuito': circuito,
    }
    salvar()


def remover_item():
    try:
        ESTOQUE.pop(estoque)
        salvar()
        print()
        print('>>>> O item {} excluido com sucesso'.format(estoque))
        print()
    except KeyError:
        print('>>>> Item inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)


def salvar():
    try:
        with open('database.csv', 'w') as arquivo:
            for estoque in ESTOQUE:
                telefone = ESTOQUE[estoque]['telefone'] 
                gateway = ESTOQUE[estoque]['gateway'] 
                wan = ESTOQUE[estoque]['wan'] 
                circuito = ESTOQUE[estoque]['circuito']
                arquivo.write("{},{},{},{},{}\n".format(estoque, telefone, gateway, wan, circuito))

    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar')
        print(error)


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                estoque = detalhes[0]
                telefone = detalhes[1]
                gateway = detalhes[2]
                wan = detalhes[3]
                circuito = detalhes[4]

                inserir_item(estoque, telefone, gateway, wan, circuito)
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)


carregar()


while True:
    menu()

    print(" ")
    print("    __ ")   
    print("  _/  \_")
    print("  (҂`_´)") 
    print('   <;=╦╤─ - - - - - - -')  
    opcao = input('   Escolha uma opção: ')
    os.system('cls')
    print('UNIDADES REDE GOVERNO 3 ')
    print(" ")


    if opcao == '1':
        mostrar_estoque()
        os.system('pause')
        os.system('cls')


    elif opcao == '2':
        busca = input('Mostrar unidades na Lista com: ')
        print('------------------------------------------------------------------------------------------------------------------------')
        estoquekey(busca.upper())
        os.system('pause')
        os.system ('cls')


    elif opcao == '3':
        estoque = input('Inserir o nome da Unidade: ')
        telefone = int(input('Inserir o Telefone: '))
        gateway = int(input('Inserir o Gateway: '))
        wan = int(input('Inserir a Wan: '))
        circuito = input('Inserir o Circuito: ')
        inserir_item(estoque, telefone, gateway, wan, circuito)
        os.system('pause')
        os.system('cls')


    elif opcao =='4':
        estoque = input('Inserir o item a ser removido do Estoque: ')
        remover_item()
        os.system('pause')
        os.system('cls')


    elif opcao == '0':
         break


    else:
        print("Opcao invalida")
      




