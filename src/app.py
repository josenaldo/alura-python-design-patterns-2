from connection_factory import ConnectionFactorySQLite

# escondeu os detalhes de criação do banco
# tratamento de erro omitido
fabrica = ConnectionFactorySQLite()
conexao = fabrica.get_connection()

cursor = conexao.cursor()
cursor.execute('SELECT * from cursos')

for linha in cursor:
    print(linha)

conexao.close()
