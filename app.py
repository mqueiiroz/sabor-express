import os

restaurantes = [{'nome':'Pizzaria','categoria':'Pizzas','status':False},
                {'nome':'Sushi','categoria':'Japonesa','status':True}]

def exibir_nome():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█ 
      ''')

def exibir_opcoes():
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Alterar estados dos Restaurantes.')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o App')

def opcao_invalida():
    print('Opção Invalida\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('digite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurantes():
    exibir_subtitulo('Cadastro De Novos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante para cadastro: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'status':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'ativado' if restaurante['status'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}')
    voltar_ao_menu_principal()

def alterar_status():
    exibir_subtitulo('Alterando o status')
    nome_restaurante = input('Digite o restaurante que você quer alterar status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')
    
    voltar_ao_menu_principal()


def escolher_opcao():
    try:    
        opcao_escolhida = int(input('Escolha a sua opção: '))
    
        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
