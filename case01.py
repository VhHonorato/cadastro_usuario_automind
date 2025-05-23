#Aplicação para realizar cadastro de usuario em lista, permitindo bucscar o usuário pelo nome e exibir suas informações, se encontrado.

def menu():
    #Função principal para gerenciar aplicação
   
    usuarios = []

    while True:
        print("\nMenu Principal")
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

    print("\nCadastro de Usuário")
    nome = input("Insira o nome do usuário: ")
    email = input("Insira o email do usuário: ")
    
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
    print("\nLista de Usuários Cadastrados")
    if not usuarios:
        print("Não existem usuários cadastrados")
        return

    for i, usuario in enumerate(usuarios):  #Função utilizada para enumerar os objetos retornados pelo 'for', trazendo uma melhor legibilidade para o usuário
        print(f"Usuário #{i+1}")
        print(f"Nome: {usuario["nome"]}")
        print(f"Email: {usuario["email"]}")
        print(f"Idade: {usuario["idade"]}")

def buscar_usuario(usuarios):
    #Função para buscar o usuário pelo nome, na lista.
    #Se encontrado, retornar seus dados cadastrados
    print("\nBusca de Usuários")
    if not usuarios:
        print("Não existem usuários cadastrados")
        return
    
    nome_busca = input("Digite o nome do usuário: ")
    encontrado = False  #variável utilizada como indicador de estado, para tratar as ações em casos de encontrar ou não o nome desejado.
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca.lower():  #Utilizado função 'lower' para tornar a busca case-insensitive
            print("\nUsuário encontrado:")
            print(f"Nome: {usuario["nome"]}")
            print(f"Email: {usuario["email"]}")
            print(f"Idade: {usuario["idade"]}")
            encontrado = True

    if not encontrado:
        print(f"Usuário {nome_busca} não encontrado.")

if __name__ == "__main__":   #Bloco utilizado para determinar que a função menu continue sendo excutada
    menu()    

