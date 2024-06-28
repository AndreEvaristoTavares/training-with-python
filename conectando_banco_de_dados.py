import pymysql.cursors
import pymysql.cursors
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'root'
DB_NAME = 'portaria'
TABLE_NAME = 'moradores'

connection = pymysql.connect(
    host=HOST,
    port=PORT,
    user=USER,
    passwd=PASSWORD,
    database=DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()
def criar_tabela():
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}(ID INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, ap INTEGER)')
    connection.commit()

def adicionar_morador(nome, ap):
    sql_inserir = f'INSERT INTO {TABLE_NAME} (name, ap) VALUES (%s, %s)'
    cursor.execute(sql_inserir, [nome, ap])
    connection.commit()

def visualizar():
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row['ID']} Nome: {row['name']} AP: {row['ap']}")
            print()
    else:
        print("Não há moradores cadastrados.")
    
def deletar_morador(id):
    sql_delete = f'DELETE FROM {TABLE_NAME} WHERE id = %s'
    cursor.execute(sql_delete, id)
    connection.commit()

def fechar_conexao_com_banco():
    cursor.close()
    connection.close()
    print("conexão encerrada...")

criar_tabela()
connection.commit()
while True:
    print("digite (c) para criar morador \n(r) para ler lista de moradores \n(u) para atualizar \n(d) para deletar morador pelo id")
    opcao = input("digite a opção: ")
    if opcao == 'c':
        nome_morador = str(input("digite o nome: "))
        numero_ap = int(input("digite o numero do ap: "))
        adicionar_morador(nome_morador, numero_ap)
        continue
    elif opcao == 'r':
        visualizar()
        continue
    elif opcao == 'u':
        print("update")
        continue
    elif opcao =='d':
        id = int(input("digite o id para deletar: "))
        deletar_morador(id)
        continue
    elif opcao == 's':
        print("saindo...")
        break
    else:
        print("opção inválida...")
        continue

fechar_conexao_com_banco()
    


