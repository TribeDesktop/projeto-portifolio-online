import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connection import create_connection
from messages_front import *
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


class GradeHorariosHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        connection = create_connection()
        cursor = connection.cursor(dictionary=True)

        if self.path.startswith("/horarios/"):
            horarioid = int(self.path.split("/")[-1])
            cursor.execute("SELECT * FROM horarios WHERE horarioid = %s", (horarioid,))
            horario = cursor.fetchone()
            if horario:
                self.wfile.write(json.dumps(horario).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Horário não encontrado"}).encode())
                threading.Thread(target=exibir_popup, args=(Msg.title(0), Msg.error("read", "horário não encontrado"))).start()
        else:
            cursor.execute("""
                SELECT 
                    h.horarioID,
                    d.disciplinaID,
                    d.nomeDisciplina, 
                    h.horaInicio, 
                    h.horaFim, 
                    di.nomeDia, 
                    d.aulasTotaisSemestreDisciplina
                FROM 
                    disciplinas d
                INNER JOIN 
                    dias di ON di.disciplinaID = d.disciplinaID
                INNER JOIN 
                    horarios h ON h.horarioID = di.horarioID
                ORDER BY 
                    di.nomeDia, h.horaInicio
            """)
            horarios = cursor.fetchall()
            self.wfile.write(json.dumps(horarios, default=str).encode())

        cursor.close()
        connection.close()

    def do_POST(self):
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        novo_horario = json.loads(post_data)

        horainicio = novo_horario['horainicio']
        horafim = novo_horario['horafim']
        disciplina_id = novo_horario['disciplinaid']
        nome_dia = novo_horario['nomedia']

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM disciplinas WHERE disciplinaid = %s", (disciplina_id,))
        if not cursor.fetchone():
            self.send_response(400)
            self.wfile.write(json.dumps({"message": "Disciplina não encontrada."}).encode())
            threading.Thread(target=exibir_popup, args=(Msg.title(0), Msg.error("created", "horário", "disciplina não encontrada"))).start()
            cursor.close()
            connection.close()
            return

        cursor.execute("INSERT INTO horarios (horainicio, horafim) VALUES (%s, %s)", (horainicio, horafim))
        connection.commit()

        horario_id = cursor.lastrowid
        cursor.execute("INSERT INTO dias (nomedia, disciplinaid, horarioid) VALUES (%s, %s, %s)", (nome_dia, disciplina_id, horario_id))
        connection.commit()

        novo_horario['horarioid'] = horario_id
        self.wfile.write(json.dumps(novo_horario).encode())
        threading.Thread(target=exibir_popup, args=(Msg.title(1), Msg.success("created", "horário"))).start()

        cursor.close()
        connection.close()
            
    def do_PUT(self):
        if self.path.startswith("/horarios/"):
            horario_id = int(self.path.split("/")[-1])

            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            dados_atualizados = json.loads(put_data)

            horainicio = dados_atualizados['horainicio']
            horafim = dados_atualizados['horafim']
            disciplina_id = dados_atualizados['disciplinaid']
            nome_dia = dados_atualizados['nomedia']

            connection = create_connection()
            cursor = connection.cursor()

            # Atualiza o horário
            cursor.execute("UPDATE horarios SET horainicio = %s, horafim = %s WHERE horarioid = %s", 
                        (horainicio, horafim, horario_id))
            connection.commit()

            # Atualiza o registro em dias

            cursor.execute("UPDATE dias SET horarioid = %s, nomedia = %s, disciplinaid = %s WHERE horarioid = %s", 
                        (horario_id, nome_dia, disciplina_id, horario_id))

            connection.commit()

            # Resposta bem-sucedida
            self.send_response(200)
            self.wfile.write(json.dumps({"message": "Horário atualizado com sucesso"}).encode())
            threading.Thread(target=exibir_popup, args=(Msg.title(1), Msg.success("updated", "horário"))).start()

            cursor.close()
            connection.close()


    def do_DELETE(self):
        if self.path.startswith("/horarios/"):
            horarioid = int(self.path.split("/")[-1])

            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM dias WHERE horarioid = %s", (horarioid,))
            cursor.execute("DELETE FROM horarios WHERE horarioid = %s", (horarioid,))
            connection.commit()

            if cursor.rowcount > 0:
                self.send_response(200)
                self.wfile.write(json.dumps({"message": "Horário excluído com sucesso!"}).encode())
                threading.Thread(target=exibir_popup, args=(Msg.title(1), Msg.success("deleted", "horário"))).start()
            else:
                self.send_response(404)
                self.wfile.write(json.dumps({"message": "Horário não encontrado."}).encode())
                threading.Thread(target=exibir_popup, args=(Msg.title(0), Msg.error("deleted", "horário (não encontrado)"))).start()

            cursor.close()
            connection.close()

# Configuração do servidor
def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, GradeHorariosHandler)
    print("Servidor rodando na porta 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
