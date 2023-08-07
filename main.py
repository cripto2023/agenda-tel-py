
agenda = {}

def adicionarContato (nome: str, telefone: str) -> None:
    agenda [nome] = telefone
    print('Contato adicionado com sucesso!')

def editarContato (nome: str, telefone: str) -> None:
    if nome in agenda.keys():
        agenda[nome] = telefone
        print('Dados alterados com sucesso!')
    else:
        print('O contato não existe: ')

def pesquisarContato (nome: str) -> None:
    if nome in agenda.keys():
        print('\n----------------')
        print(f"contato: {nome}")
        print(f"Telefone: {agenda[nome]}")
        print("n\ --------")
    else:
        print("Contato não encontrado!")

def deletarContato (nome:str) -> None:
    if nome in agenda.keys():
        del agenda[nome]
        print("Contato removido da agenda")
    else:
        print('Contato não existe! ')

def listarTodos():
    for nome in agenda:
        print('\n --------------')
        print(f'Contato: {nome}')
        print(f'Telefone: {agenda[nome]}')
        print('\n ---------------')

while True:
    print('----- Bem vindo ao menu ------')
    opcao = int(input("1 - Adicionar contato \n"
                      "2 - Editar contato  \n"
                      "3- Pesquisar contato  \n"
                      "4 - Deletar contato  \n"
                      "5 - Listar todod  \n"
                      "6- Sair  \n"
                      "Selecione uma opção: "))
    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        tel = input('Digite o telefone do contato: ')
        adicionarContato (nome, tel)
    elif opcao == 2:
        nome = input("Digite o nome do contato para alterar: ")
        tel = input('Digite o novo telefone do contato: ')
        editarContato(nome, tel)
    elif opcao == 3:
        nome = input('Digite o nome do contato: ')
        pesquisarContato(nome)
    elif opcao == 4:
        nome = input('Digite o nome do contato: ')
        deletarContato (nome)
    elif opcao == 5:
        listarTodos()
    elif opcao == 6:
        break
    else: print('Opção inválida!')

