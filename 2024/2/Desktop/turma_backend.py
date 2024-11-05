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

# Função para fechar a conexão
def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()

# Função para converter a data do formato dia/mês/ano para ano-mês-dia
def converter_data(data):
    try:
        if len(data.split('/')) == 2:  # Se faltar o ano
            data += f"/{datetime.now().year}"  # Adiciona o ano atual
        return datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError as e:
        print(f"Erro ao converter a data: {e}")
        return None

# Função para processar e validar os dias não letivos
def processar_dias_nao_letivos(dias_nao_letivos_input, descricao_dia_nao_letivo_input):
    try:
        # Se ambos os campos estiverem vazios, retorna uma lista vazia
        if not dias_nao_letivos_input and not descricao_dia_nao_letivo_input:
            return []
        
        # Separa os dias e descrições
        dias = dias_nao_letivos_input.split(",")
        descricoes = descricao_dia_nao_letivo_input.split(",")
        
        # Remove espaços em branco dos elementos
        dias = [dia.strip() for dia in dias]
        descricoes = [descricao.strip() for descricao in descricoes]
        
        # Verifica se o número de dias e descrições coincide, e que cada descrição não seja vazia
        if len(dias) == len(descricoes):
            # Verifica se há apenas um dia sem descrição e retorna erro se for o caso
            if len(dias) == 1 and not descricoes[0]:
                print("Erro: O número de dias não letivos e descrições não coincide.")
                return 'erro'
            
            # Retorna a lista de tuplas de dias e descrições
            return list(zip(dias, descricoes))
        
        else:
            raise ValueError("O número de dias não letivos e descrições não coincide.")
    except ValueError as e:
        print(f"Erro: {str(e)}")
        return 'erro'

# Função para cadastrar dias não letivos
def cadastrar_dias_nao_letivos(dias_nao_letivos, turma_id):
    conn = create_connection()
    if not conn:
        return  # Se não conseguiu conectar, encerra a função

    try:
        with conn.cursor() as cursor:
            query = """INSERT INTO diasnaoletivos (turmaID, dataDia, descricaoDia)
                       VALUES (%s, %s, %s)"""
            
            # Itera sobre os dias não letivos e suas descrições
            for dia, descricao in dias_nao_letivos:
                # Converte a data do dia não letivo
                data_convertida = converter_data(dia)
                cursor.execute(query, (turma_id, data_convertida, descricao))
            
            conn.commit()  # Confirma a transação
            
            # Retorna 'sucesso' para poder exibir corretamente a mensagem no front
            return 'sucesso'

    except Error as e:
        print(f"Erro ao cadastrar dias não letivos: {e}")
    
    finally:
        close_connection(conn)  # Fecha a conexão

# Função para verificar se todos os dias não letivos estão no intervalo
def verificar_dias_nao_letivos(dias_nao_letivos, data_inicio, data_fim):
    for dia, descricao in dias_nao_letivos:
        data_convertida = converter_data(dia)
        if not data_convertida:  # Verifica se a conversão foi bem-sucedida
            print(f"Erro: Data inválida '{dia}'")
            return False
        if not (data_inicio <= data_convertida <= data_fim):
            return False  # Retorna False se algum dia estiver fora do intervalo
    return True  # Retorna True se todos os dias estiverem dentro do intervalo

# Função para cadastrar uma nova turma no banco de dados
def cadastrar_turma(nome, sigla, data_inicio, data_fim, dias_nao_letivos):
    conn = create_connection()  # Cria a conexão com o banco
    if not conn:
        return  # Se não conseguiu conectar, encerra a função

    # Converte as datas antes de realizar o cadastro
    data_inicio_convertida = converter_data(data_inicio)
    data_fim_convertida = converter_data(data_fim)

    if not data_inicio_convertida or not data_fim_convertida:
        print("Erro: uma ou mais datas não foram convertidas corretamente.")
        close_connection(conn)
        return

    if data_inicio_convertida >= data_fim_convertida:
        print("Erro: a data de início deve ser anterior à data de fim.")
        close_connection(conn)
        return

    # Verifica se os dias não letivos estão dentro do intervalo antes de cadastrar a turma
    if not verificar_dias_nao_letivos(dias_nao_letivos, data_inicio_convertida, data_fim_convertida):
        print("Erro: Há dias não letivos fora do intervalo da turma.")
        close_connection(conn)
        return

    try:
        with conn.cursor() as cursor:
            query = """INSERT INTO turmas (turma, siglaTurma, dataInicio, dataFim)
                       VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (nome, sigla, data_inicio_convertida, data_fim_convertida))
            conn.commit()  # Confirma a transação
            
            # Obtém o ID da turma recém cadastrada
            turma_id = cursor.lastrowid

            # Cadastrar os dias não letivos, passando também as datas de início e fim da turma
            cadastrar_dias = cadastrar_dias_nao_letivos(dias_nao_letivos, turma_id)
    
            # Exibindo mensagem de sucesso
            titulo_mensagem = Msg.title(1)
            descricao_mensagem = Msg.success('created', 'turma', reference=nome, refType='nome')
            print(titulo_mensagem)
            print(descricao_mensagem)
            
            # Retorna 'sucesso' para poder exibir corretamente a mensagem no front
            return 'sucesso'
            
    except Error as e:
        print(f"Erro ao adicionar a turma: {e}")
    
    finally:
        close_connection(conn)  # Fecha a conexão

