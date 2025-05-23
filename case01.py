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

        if opcao == "1"
            cadastrar_usuario(usuarios)
        elif opcao == "2"
            listar_usuario(usuarios)
        elif opcao == "3"
            buscar_usuario(usuarios)
        elif opcao == "4"
            print("Saindo da aplicação...")            
            break
        else:
            print("Opção inválida. Por favor insira um número válido")    


    