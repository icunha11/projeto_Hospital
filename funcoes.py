from bancoDeDados import listaUsuarios
def cadastrarUsuario(ID,
                     nomeDoUsuario,
                     dataNascimentoUsuario,
                     generoUsuario,
                     planoUsuario):
    usuario = {"nomeUsuario": nomeDoUsuario,
               "dataNascimento": dataNascimentoUsuario,
               "generoUsuario": generoUsuario,
               "planoUsuario": planoUsuario,
               "IDUsuario": ID}
    listaUsuarios.append(usuario)


def visualizarUsuarios():
    for usuario in listaUsuarios:
        print(f"ID: {usuario['IDUsuario']}")
        print(f"Nome: {usuario['nomeUsuario']}")
        print(f"Data de Nascimento: {usuario['dataNascimento']}")
        print(f"Gênero: {usuario['generoUsuario']}")
        print(f"Plano: {usuario['planoUsuario']}")
        print("-" * 20)


def atualizarCadastro(ID,
                      nomeAtualizado,
                      dataNascimentoAtualizada,
                      generoAtualizado,
                      planoAtualizado):
    
    for usuario in listaUsuarios:
        if usuario["IDUsuario"] == ID:
            usuario["nomeUsuario"] = nomeAtualizado
            usuario["dataNascimento"] = dataNascimentoAtualizada
            usuario["generoUsuario"] = generoAtualizado
            usuario["planoUsuario"] = planoAtualizado
            print("Cadastro atualizado com sucesso!")
            return
        else:
            print("Paciente não encontrado!")
    
def removerUsuario(IDremove,nomeDoPacienteremove):
    for usuario in listaUsuarios:
        if usuario["IDUsuario"] == IDremove and usuario["nomeUsuario"] == nomeDoPacienteremove:
            listaUsuarios.remove(usuario)
            print("Paciente removido!")
            return
    print("Paciente não encontrado!")