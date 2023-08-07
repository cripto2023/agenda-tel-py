'''
lista_alunos = []

while True:
    print('Menu Principal')
    opcao = int(input(f'Digite a opção, conforme indicado: \n'
                      'Opcao 1 - inserir aluno. \n'
                      'Opção 2 - consultar aluno. \n'
                      'Opção 3 - editar aluno. \n'
                      'Opção 4 - excluir aluno. \n'
                      'Opção 5 - sair. \n'
                      'Selecione a opção: '))
    if opcao == 1:
        nome = input('Digite o nome do aluno:  ')
        idade = int(input('Digite a idade: '))
        curso = input("Digite o nome do curso:  ")
        nota = float(input('Digite a nota: '))
        aluno = {'nome': nome, 'idade': idade, 'curso': curso, 'nota': nota}
        lista_alunos.append(aluno)
    elif opcao == 2:
        nome = input('Digite o nome do aluno ')
        for aluno in lista_alunos:
            if aluno['nome'] == nome:
                print("aluno encontrado")
                break
    elif opcao == 3:
        nome = input('Digite o nome do aluno para editar ')
        for aluno in lista_alunos:
            if aluno['nome'] == nome:
                aluno["nome"] = input("Digite o novo nome do aluno: ")
                aluno["curso"] = input("Digite o novo curso do aluno: ")
                aluno["idade"] = int(input("Digite a nova idade do aluno: "))
                aluno["nota"] = float(input("Digite a nova nota do aluno: "))
                print("Aluno editado com sucesso!\n")
                break
    elif opcao == 4:
        nome = input('Digite o nome do aluno para excluir ')
        for aluno in lista_alunos:
            if aluno['nome'] == nome:
                lista_alunos.remove(aluno)
                print('Aluno removido')
                break
    elif opcao == 5:
        break

print(lista_alunos)

#'''

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

