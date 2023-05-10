import mysql.connector as mysql

config = {
    
    'user': 'admin',
    'password': 'aulanoiteFaculdad3',
    'host': 'dbaula.c7yoa1780lci.us-east-1.rds.amazonaws.com',
    'database':'aula'
}

try:
    conn = mysql.connect(**config)
    print('Conexão executada com sucesso!')
except mysql.Error as err:
    print(f'Conexão falhou: {err}')
    
    
    
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()


# Pedindo ao usuário o nome e o código do estado
nome_estado = input ('Digite o nome do estado: ')
codigo_estado = int(input('Digite o código do estado: '))


# Inserindo o estado na tabela
sql = 'INSERT INTO estado (codigo, nome) VALUES (%s, %s)'
val = (codigo_estado, nome_estado)
cursor.execute(sql, val)


# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, 'Registro(s) inserido(s) com sucesso.')

conn.close()