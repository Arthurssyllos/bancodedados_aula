
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


# Solicitando a entrada do usuário
busca = input('Digite o nome que deseja buscar: ')


# Executando a consulta com LIKE
sql = 'SELECT * FROM estado WHERE nome LIKE %s'
val = ('%' + busca + '%',)
cursor.execute(sql, val)

# Obtendo os resultados
results = cursor.fetchall()

# Interando sobre os resultados
for result in results:
    print(result)
    
# Fechar a conexão e o cursor
conn.close()