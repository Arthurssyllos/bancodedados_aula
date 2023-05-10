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


# Inserindo o estado na tabela
sql = 'SELECT * FROM estado'
cursor.execute(sql)


# Obter o resultado da consulta
result = cursor.fetchall()
print(result)

# Imprimindo os resultados
for linhas in result:
    print(linhas)
    
# Fehar a conexão e o cursor

conn.close()