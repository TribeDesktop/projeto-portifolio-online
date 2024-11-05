import mysql.connector
from mysql.connector import Error
from messages_back import Msg

# Função para criar a conexão
def create_connection():
    try:
        # Configurações da conexão
        connection = mysql.connector.connect(
            host='localhost',
            database='escola',
            user='root',
            password=''
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None

# Função para fechar a conexão e o cursor
def close_connection(connection, cursor):
    if connection and connection.is_connected():
        cursor.close()
        connection.close()

# Função para cadastrar um novo curso no banco de dados
def cadastrar_curso(nome, sigla, tipo_duracao, periodo_curso, tipo_graduacao):
    try:
        conn = create_connection()  # Cria a conexão com o banco
        if conn:
            cursor = conn.cursor()  # Cria um cursor a partir da conexão para executar comandos SQL
            query = """INSERT INTO cursos (nomeCurso, siglaCurso, tipoDuração, periodoCurso, tipoGraduacaoCurso)
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (nome, sigla, tipo_duracao, periodo_curso, tipo_graduacao))
            conn.commit()  # Confirma a transação
            
            # Exibindo mensagem de sucesso
            titulo_mensagem = Msg.title(1)
            descricao_mensagem = Msg.success('created', 'curso', reference=nome, refType='nome')
            print(titulo_mensagem)
            print(descricao_mensagem)
            
            # Retorna 'sucesso' para poder exibir corretamente a mensagem no front
            return 'sucesso'

    except Exception as e:
        print(f"Erro ao adicionar o curso: {e}")
        
    finally:
        close_connection(conn, cursor) # Fecha a conexão e o cursor