#Aplicação para realizar cadastro de usuario em lista, permitindo bucscar o usuário pelo nome e exibir suas informações, se encontrado.

def menu():
    #Função principal para gerenciar aplicação
    usuarios = []

    while True:
        print("Menu Principal")
        print("1. Cadastrar usuário")
        print("2. Listar usuário")
        print("3. Buscar usuário por nome")
        print("4. Sair")

        opcao = input("Escolha uma opção pelo número: ")    

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuario(usuarios)
        elif opcao == "3":
            buscar_usuario(usuarios)
        elif opcao == "4":
            print("Saindo da aplicação...")            
            break
        else:
            print("Opção inválida. Por favor insira um número válido")    


def cadastrar_usuario(usuarios):
    #Função para cadastrar novo usuário. 
    # Seus dados(nome, email e idade) serão inseridos na variavel 'usuarios', dentro da função 'menu', já que a variável 'usuario' foi passada como argumento da função 'cadastrar_usuario'

    print("Cadastro de Usuário")
    nome = input("Insira o nome do usuário")
    email = input("Insira o email do usuário")
    
    while True:
        try:
            idade= int(input("Insira a idade do usuário: "))
            if idade < 0:
                print("A idade não pode ser menor que zero. Insira um valor válido.")
            else:
                break
        except ValueError:
            print("Idade invalida, insira um número inteiro.")    
    
    #Dicionário criado para representar um usuário
    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }
    usuarios.append(usuario)
    print(f"Usuario {nome} cadastrado com sucesso!")


def listar_usuario(usuarios):
    #Funçãpo para retornar a lista com os usuários cadastrados.
    print("Lista de Usuários Cadastrados")
    if not usuarios:
        print("Não existem usuários cadastrados")
        return

    for i, usuario in enumerate(usuarios):
        print(f"Usuário #{i+1}")
        print(f"Nome: {usuario[nome]}")
        print(f"Email: {usuario[email]}")
        print(f"Idade: {usuario[idade]}")