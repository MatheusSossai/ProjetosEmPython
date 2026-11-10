import os
from calendar import error
from operator import truediv

AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contatos(contato)
    else:
        print('>>>>> Agenda Vazia')

def buscar_contatos(contato):
    telefone = AGENDA[contato]['telefone']
    email = AGENDA[contato]['email']
    endereco = AGENDA[contato]['endereco']

    if contato not in AGENDA:
        print('ATENCAO!!!!!!! ')
        print('contacto nn encontrado na agenda')
    else:
        print('Nome:', contato)
        print('telefone:', telefone)
        print('email:', email)
        print('endereco:', endereco)
        print('=======================================================================================')


def detalhes_contato():
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereco: ')

    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print()
    print(">>>> Contato {} adicionado/editado com sucesso <<<<".format(contato))
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(">>>>> Contato {} excluido com sucesso <<<<".format(contato))
        print()
    except KeyError:
        print('>>>>> contato inexistente')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as file:
            file.write('nome,telefone,email,endereco\n')
            for contato in AGENDA:
                #atribuindo as variaveis
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']

                file.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('>>>>> Agenda exportada com sucesso <<<<<')
    except:
        print('>>>>> Algum erro ocorreu ao exportar contatos')
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                 #split divide a string em uma lista e #strip tira \n

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('????? File nao encontrado ?????')
    except:
        print('?????? algum erro aconteceu ai ??????')
        print(error)

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',') # split divide a string em uma lista e #strip tira \n
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('>>>>> Database carregado com sucesso hehehe')
        print('>>>>> {} contatos carregados'.format(len(AGENDA))) #len -> length que significa comprimento
    except FileNotFoundError:
        print('????? File nao encontrado ?????')
    except:
        print('?????? algum erro aconteceu ai ??????')
        print(error)

def imprimir_menu():
    print('1 - Mostrar contatos da agenda')
    print('2 - Buscar contato na agenda')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos')
    print('0 - Sair')


# inicio do programa
carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opcao: ')
    print(opcao)

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contatos(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>> Contato ja existente')
        except KeyError:
            telefone, email, endereco = detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>> Editando contato', contato)
            telefone, email, endereco = detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>>>> Contato inexistente')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos()

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)

    elif opcao == '0':
        print('Encerrando...')
        break

    else:
        print("Opcao invalida!")
