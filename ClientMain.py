import Client

def options():
    print('-'*29)
    print('|1 - tela inicial           |\n'
          '|2 - Todos os filmes        |\n'
          '|3 - buscar filme especifico|\n'
          '|4 - adicionar filme        |\n'
          '|5 - fechar aplicação       |')
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
            print('Lista de todos os filmes')
            message = Client.all_movies(link+"/datas")
            print(message)

        elif action == 3:
            message = Client.find_movie(link+"/datas", input('Número do filme: '))
            print('Filme escolhido')
            print(message)

        elif action == 4:
            name = input("Nome do filme: ")
            time = int(input('Duração do filme: '))
            duration = str(time//60)+"h "+str(time%60)+"m "
            message = Client.post_movie(link+"/datas", name, duration)
            print('Filme adicionado')
            print(message)

    print("Obrigado por usar nossos programas")