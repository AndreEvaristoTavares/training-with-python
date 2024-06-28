import pymysql.cursors
import pymysql.cursors
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'root'
DB_NAME = 'portaria'
TABLE_NAME = 'moradores'
class Morador:
    def __init__(self) -> None:
        
        self.connection = pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
            passwd=PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )

        self.cursor = self.connection.cursor()
    def criar_tabela(self):
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}(ID INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, ap INTEGER)')
            self.connection.commit()

    def adicionar_morador(self, nome, ap):
            sql_inserir = f'INSERT INTO {TABLE_NAME} (name, ap) VALUES (%s, %s)'
            self.cursor.execute(sql_inserir, [nome, ap])
            self.connection.commit()

    def atualizar_morador(self, id, nome, ap):
            sql_atualizar = f'UPDATE {TABLE_NAME} SET name=%s, ap=%s WHERE ID=%s'
            self.cursor.execute(sql_atualizar, [nome, ap, id])
            self.connection.commit()
    def visualizar(self):
            self.cursor.execute(f'SELECT * FROM {TABLE_NAME}')
            rows = self.cursor.fetchall()
            
            if rows:
                for row in rows:
                    print()
                    #print(f"ID: {row['ID']} Nome: {row['name']} AP: {row['ap']}")
                    print(row)
                    print()
            else:
                print("Não há moradores cadastrados.")
    
    def deletar_morador(self, id):
            sql_delete = f'DELETE FROM {TABLE_NAME} WHERE id = %s'
            self.cursor.execute(sql_delete, id)
            self.connection.commit()

    def fechar_conexao_com_banco(self):
            self.cursor.close()
            self.connection.close()
            print("conexão encerrada...")

morador = Morador()
morador.criar_tabela()
#connection.commit()
while True:
    print("digite (c) para criar morador \n(r) para ler lista de moradores \n(u) para atualizar \n(d) para deletar morador pelo id")
    opcao = input("digite a opção: ")
    if opcao == 'c':
        nome_morador = str(input("digite o nome: "))
        numero_ap = int(input("digite o numero do ap: "))
        morador.adicionar_morador(nome_morador, numero_ap)
        continue
    elif opcao == 'r':
        morador.visualizar()
        continue
    elif opcao == 'u':
        print('atualizar pelo id')
        id_morador = int(input("digite o id: "))
        nome_morador = str(input("digite o nome: "))
        numero_ap = int(input("digite o numero do ap: "))
        morador.atualizar_morador(id_morador, nome_morador, numero_ap)

        continue
    elif opcao =='d':
        id = int(input("digite o id para deletar: "))
        morador.deletar_morador(id)
        continue
    elif opcao == 's':
        print("saindo...")
        break
    else:
        print("opção inválida...")
        continue

morador.fechar_conexao_com_banco()
    


