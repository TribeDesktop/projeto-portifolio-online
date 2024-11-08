import mysql.connector
from mysql.connector import Error
from messages_back import Msg
from datetime import datetime

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

# Função para buscar os nomes dos alunos disponíveis no banco
def buscar_alunos_cadastrados():
    try:
        conn = create_connection()  # Cria a conexão com o banco
        if conn:
            cursor = conn.cursor()  # Cria um cursor a partir da conexão para executar comandos SQL
            query = """SELECT nomeUsuario FROM usuarios"""
            cursor.execute(query)  # Executa a consulta SQL
            # Obtém o resultado
            resultado = cursor.fetchall()  # Pega todas as linhas

            usuarios = [i[0] for i in resultado]  # Extrai cada nome de usuário e adiciona à lista
            
            return usuarios

    except Exception as e:
        print(f"Erro ao buscar os nomes dos usuários cadastrados: {e}")
        
    finally:
        close_connection(conn, cursor)  # Fecha a conexão e o cursor
        
# Função para buscar o cpf do aluno selecionado
def buscar_cpf(nomeUsuario):
    try:
        conn = create_connection()  # Cria a conexão com o banco
        if conn:
            cursor = conn.cursor()  # Cria um cursor a partir da conexão para executar comandos SQL
            query = """SELECT cpfUsuario FROM usuarios WHERE nomeUsuario = %s"""
            cursor.execute(query, (nomeUsuario,))
            # Obtém o resultado
            resultado = cursor.fetchone()  # Pega apenas uma linha

            if resultado:
                # Crie e retorna o dicionário com o cpf do aluno
                student_dict = {
                    "cpf": resultado[0]
                }
                return student_dict
            else:
                print("Nenhum usuário encontrado com o nome especificado.")
                return None

    except Exception as e:
        print(f"Erro ao buscar o cpf do usuário {nomeUsuario}: {e}")
        return None
        
    finally:
        close_connection(conn, cursor) # Fecha a conexão e o cursor
        
# Função para buscar o nome dos cursos disponíveis no banco
def buscar_cursos_cadastrados():
    try:
        conn = create_connection()  # Cria a conexão com o banco
        if conn:
            cursor = conn.cursor()  # Cria um cursor a partir da conexão para executar comandos SQL
            query = """SELECT nomeCurso FROM cursos"""
            cursor.execute(query)  # Executa a consulta SQL
            # Obtém o resultado
            resultado = cursor.fetchall()  # Pega todas as linhas

            cursos = [i[0] for i in resultado]  # Extrai cada nome de curso e adiciona à lista
            
            return cursos

    except Exception as e:
        print(f"Erro ao buscar os nomes dos cursos cadastrados: {e}")
        
    finally:
        close_connection(conn, cursor)  # Fecha a conexão e o cursor

# Função para buscar os dados do curso selecionado        
def buscar_curso(nomeCurso):
    try:
        conn = create_connection()  # Cria a conexão com o banco
        if conn:
            cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
            query = """SELECT cursoID, siglaCurso, tipoDuração, periodoCurso, tipoGraduacaoCurso FROM cursos WHERE nomeCurso = %s"""
            cursor.execute(query, (nomeCurso,))
            
            # Obtém o resultado
            resultado = cursor.fetchone()  # Pega apenas uma linha

            if resultado:
                # Cria e retorna o dicionário com os dados do curso
                curso_dict = {
                    "id": resultado[0],
                    "sigla": resultado[1],
                    "nome": nomeCurso,
                    "duracao": resultado[2],
                    "periodo": resultado[3],
                    "graduacao": resultado[4]
                }
                return curso_dict
            else:
                print("Nenhum curso encontrado com o nome especificado.")
                return None

    except Exception as e:
        print(f"Erro ao buscar os dados do curso {nomeCurso}: {e}")
        return None

    finally:
        close_connection(conn, cursor)  # Fecha a conexão e o cursor

        
# Função para cadastrar a matricula no banco de dados
def cadastrar_matricula(situacaoAluno, cursoID, cpfUsuario):
    try:
        conn = create_connection()  # Cria a conexão com o banco
        if conn:
            dataMatricula = datetime.now().date()
            cursor = conn.cursor()  # Cria um cursor a partir da conexão para executar comandos SQL
            # Pega o ID e o nome do usuário a partir do CPF
            query = """SELECT usuarioID, nomeUsuario FROM usuarios WHERE cpfUsuario = %s"""
            cursor.execute(query, (cpfUsuario,))
            # Obtém o resultado
            resultado = cursor.fetchone()  # Pega apenas uma linha

            if resultado:
                usuarioID = resultado[0]
                nomeUsuario = resultado[1]
            else:
                print("Nenhum usuário encontrado com o CPF especificado.")
                return None
            
            # Cadastra os dados na tabela matriculas    
            query2 = """INSERT INTO matriculas (situacaoAlunoMatricula, dataMatricula, cursoID, usuarioID)
                       VALUES (%s, %s, %s, %s)"""
            cursor.execute(query2, (situacaoAluno, dataMatricula, cursoID, usuarioID))
            conn.commit()  # Confirma a transação
            
            # Obtém o ID da matricula recém cadastrada
            matriculaID = cursor.lastrowid

            # Exibindo mensagem de sucesso
            titulo_mensagem = Msg.title(1)
            descricao_mensagem = Msg.success('created', 'matricula', message=f'O usuário {nomeUsuario} foi matriculado', refType='id', reference=matriculaID)
            print(titulo_mensagem)
            print(descricao_mensagem)
            
            return "sucesso"

    except Exception as e:
        print(f"Erro ao matricular o usuário: {e}")
        return None
        
    finally:
        close_connection(conn, cursor) # Fecha a conexão e o cursor