import mysql.connector
from usuario import Usuario
from pizza import Pizza
from bebidas import Bebidas
from datetime import date
from vendas import Vendas
import os

today = date.today()
print("Today's date:", today)


def pizzaria():
    print('================================================================')
    print('             ##     PIZZARIA GO-IT    ##')
    print('================================================================')


def menu():
    print('''
               MENU:

               [1] - Iniciar Vendas
               [2] - Cadastrar Usuario
               [3] - Total de Vendas
               [4] - Desligar

             ===================================''')


pizzaria()
menu()
n1 = input('Escolha uma opção: ')
os.system('cls')
cont01 = 0
cont02 = 0
if (n1 == '1'):

    while True:
        os.system('cls')
        pizzaria()

        inputNomeUsuario = input('QUAL E SEU LOGIN--> ')

        inputSenha = input('QUAL É SUA SENHA --> ')

        cnx = mysql.connector.connect(
            host='localhost', database='pizzariagoit1', user='root', password='root')
        cursor = cnx.cursor()
        cursor.execute(
            f'select * from tb_usuarios where login_usuario = "{inputNomeUsuario}"')

        queryResult = cursor.fetchone()

        cursor.close()
        cnx.close()

        usuario = Usuario(0, "", "", "")

        if queryResult == None:
            erroUsuario = input("** Usuario incorreto **  [enter]")
            cont01 = cont01 + 1
            if cont01 == 3:
                break

            # repetir = input('você quer tentar de novo (s)sim ou (n)não ')

        else:
            usuario = Usuario(
                queryResult[0], queryResult[2], queryResult[3], queryResult[1])

        if inputSenha == usuario.senha:
            print("logado com sucesso !")

            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='root')
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM tb_pizza")

            queryResult = cursor.fetchall()

            cursor.close()
            cnx.close()

            print(queryResult)

            pizzas = []

            for i in queryResult:

                pizzas.append(Pizza(i[0], i[1], i[2]))
                os.system('cls')
                pizzaria()

            for pizza in pizzas:
                print(f'{pizza.id}        {pizza.nome}                {pizza.preco}')
                print('------------------------------------------------------')

            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='root')
            cursor = cnx.cursor()

            idPizzaSelecionada = input("Digite o numero pizza: ")

            cursor.execute("SELECT * FROM tb_bebidas")

            queryResult = cursor.fetchall()

            cursor.close()
            cnx.close()

            bebidas = []

            for i in queryResult:
                bebidas.append(Bebidas(i[0], i[1], i[2]))

            os.system('cls')
            pizzaria()

            for bebida in bebidas:
                print(
                    f'{bebida.id}        {bebida.nome}                {bebida.preco}')
                print('------------------------------------------------------')

            idBebidaSelecionada = input("Digite o numero da bebida: ")

            cnx = mysql.connector.connect(
                host='localhost', database='pizzariagoit1', user='root', password='root')
            cursor = cnx.cursor()

            nomeCliente = input('qual e o nome do cliente: ')
            dataPedido = date.today()

            add_venda = (
                f'INSERT INTO tb_vendas(id_pizza, totalpagar, nomecliente, id_bebidas, datavenda ) VALUES("{pizzas[int(idPizzaSelecionada) - 1].id}", {pizzas[int(idPizzaSelecionada) - 1].preco + bebidas[int(idBebidaSelecionada)-1].preco}, "{nomeCliente}",{bebidas[int(idBebidaSelecionada)-1].id}, now())')

            vendaOk = input('venda ok.. [enter]')

            cursor.execute(add_venda)
            cnx.commit()

            cursor.close()
            cnx.close()

            continuarVenda = input(' Continuar vendendo [s]sim ou [n]não ?')
            if continuarVenda == 'n':
                break

        else:
            erroSenha = input("** Senha incorreta **  [enter]")
            print('--------------------------------------------')
            print('')
            cont02 = cont02 + 1
            nomeroErros = input(
                f'Maximo de erro 3X usuario {cont01}X é senha {cont02}X [enter]')
            if cont02 == 3:
                break


if (n1 == '2'):
    os.system('cls')
    pizzaria()

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pizzariagoit1"
    )
    cursor = conexao.cursor()

    funcao = input('Qual é a função: ')
    login_usuario = input('Qual é o nome do usuario: ')
    senha_usuario = input('Qual é a senha: ')

    comando = f'INSERT INTO tb_usuarios (funcao, login_usuario, senha_usuario) VALUES ("{funcao}", "{login_usuario}", "{senha_usuario}")'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()


elif (n1 == '3'):
    os.system('cls')
    pizzaria()
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pizzariagoit1"
    )
    cursor = conexao.cursor()

    comando = f'SELECT * FROM tb_vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    vendas = []

    for i in resultado:
        vendas.append(Vendas(i[0], i[1], i[2],i[3], i[4], i[5]))


    cursor.close()
    conexao.close()
    
    os.system('cls')

    print('id venda      | id bebida     | id pizza     | valor     | clinte      | data     ')
    for venda in vendas:
                print(f'{venda.id}             | {venda.idBebida}             | {venda.idPizza}            | {venda.valor}      | {venda.cliente}       | {venda.data}')
                print('------------------------------------------------------')


else:
    os.system('cls')
    pizzaria()
    print('## FIM DO PROGRAMA ##')
