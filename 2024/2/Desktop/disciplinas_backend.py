from db_connection import create_connection

def list_turma():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT turmaID, turma FROM turmas"
    cursor.execute(query)
    turmas = cursor.fetchall()
    cursor.close()
    connection.close()
    return turmas

def list_curso():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT cursoID, nomeCurso FROM cursos"
    cursor.execute(query)
    cursos = cursor.fetchall()
    cursor.close()
    connection.close()
    return cursos
