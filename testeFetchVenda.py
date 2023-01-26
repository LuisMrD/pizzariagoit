import mysql.connector
from vendas import Vendas

conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pizzariagoit"
    )
    
cursor = conexao.cursor()

comando = f'SELECT * FROM tb_vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
