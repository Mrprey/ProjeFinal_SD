import Client

def options():
    print('-'*29)
    print('|1 - Tela inicial              |\n'
          '|2 - Todos produtos guardados  |\n'
          '|3 - Buscar produto  especifico|\n'
          '|4 - Adicionar produto         |\n'
          '|5 - Fechar aplicação          |')
    print('-' * 29)
    action = int(input('Selecione um número: '))

    return action

if __name__ == "__main__":
    action = 0
    link = 'http://127.0.0.1:5000'
    while action != 5:
        action = options()

        if action > 5:
            print("Número invalido")

        elif action == 1:
            print('Tela inicial')
            message = Client.wellcome_API(link)
            print(message)

        elif action == 2:
            print('Lista de todos os produtos disponiveis em estoque')
            message = Client.all_itens(link+"/datas")
            print(message)

        elif action == 3:
            message = Client.find_iten(link+"/datas", input('Numeração do item a ser verificado no sistema: '))
            print('produto localizado')
            print(message)

        elif action == 4:
            name = input("Digite nome do item a ser adicionado no sistema: ")
            preco = float(input('Informe preço do item a ser cadastrado: '))
            message = Client.post_iten(link+"/datas", name, preco)

            print('Produto Cadastrado com sucesso!')
            print(message)

    print("Obrigado por usar nossos programas")
