import funcoes
from bancoDeDados import listaUsuarios
while True:
    print("1 - Cadastrar pacientes")
    print("2 - Visualizar pacientes")
    print("3 - Atualizar cadastro")
    print("4 - Remover paciente")
    print("5 - sair")


    opcao = str(input("Digite a opção: "))
    if opcao < "1" or opcao > "5":
        print("Opção inválida!")

    if opcao == "1":
        nome = str(input("Digite o nome do PACIENTE: "))
        dataNascimento = str(input("Digite a data de nascimento do PACIENTE: "))
        genero = str(input("Digite o gênero do PACIENTE: "))
        plano = str(input("Digite o plano do PACIENTE: "))
        novo_id = len(listaUsuarios) + 1  # Aqui pega o total atual de usuários e soma 1
        funcoes.cadastrarUsuario(novo_id, nome, dataNascimento, genero, plano)
        print("Cadastro realizado!")
        print(f"Seu ID é: {novo_id}")
    


    elif opcao == "2":
        if len(listaUsuarios) == 0:
            print("Nenhum paciente encontrado")
        else:
            funcoes.visualizarUsuarios()


    elif opcao == "3":
        if len(listaUsuarios) >= 1:
            idUser = int(input("Digite o ID do PACIENTE: "))
            nomeAtualizado = str(input("Digite o nome atualizado do PACIENTE: "))
            dataNascimentoAtualizada= str(input("Digite a data de nascimento atualizada do PACIENTE: "))
            generoAtualizado = str(input("Digite o gênero atualizado do PACIENTE: "))
            planoAtualizado = str(input("Digite o plano atualizado do PACIENTE: "))
            funcoes.atualizarCadastro(idUser, nomeAtualizado, dataNascimentoAtualizada, generoAtualizado, planoAtualizado)
        else:
            print("Nenhum paciente não encontrado!")

    elif opcao == "4":
        IdPaciente = int(input("Digite o ID do PACIENTE!: "))
        nomePaciente = str(input("Digite o nome do PACIENTE: "))
        funcoes.removerUsuario(IdPaciente,nomePaciente)


    elif opcao == "5":
        print("Programa encerrado!")
        break

