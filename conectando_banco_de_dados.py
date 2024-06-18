import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE =  ROOT_DIR / DB_NAME
TABLE_NAME = 'moradores'
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
def criar_tabela():
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, ap INTEGER)')
    connection.commit()

def adicionar_morador(nome, ap):
    inserir = f'INSERT INTO {TABLE_NAME} (name, ap) VALUES (?, ?)'
    cursor.execute(inserir, [nome, ap])
    connection.commit()

def visualizar():
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    for row in cursor.fetchall():
        _id, name, ap = row
        print(_id, name, ap)
    
def deletar_morador(id):
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = {id}')
    connection.commit()

def fechar_conexao_com_banco():
    cursor.close()
    connection.close()
    print("conexão feixada")

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
    

