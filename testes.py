import pymysql

# Dados para conexão ao banco de dados
host = 'localhost'  # ou o endereço do seu servidor MySQL
user = 'root'
password = 'root'
database = 'world'

try:
    # Conectar ao banco de dados
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)

    # Exemplo de consulta
    with connection.cursor() as cursor:
        sql = "SELECT * FROM city;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

except pymysql.MySQLError as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if connection:
        connection.close()
        print("Conexão fechada.")