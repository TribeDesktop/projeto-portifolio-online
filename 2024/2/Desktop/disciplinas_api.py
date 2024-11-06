from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib
from urllib.parse import parse_qs
from db_connection import create_connection

# Configuração do servidor
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        """Configura os headers padrão."""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        """Lida com requisições GET (Leitura de disciplinas)."""
        self._set_headers()

        connection = create_connection()
        cursor = connection.cursor(dictionary=True)

        # Se uma ID de disciplina foi passada, buscar apenas aquela disciplina
        query_components = urllib.parse.urlparse(self.path)
        params = parse_qs(query_components.query)

        if "disciplinaID" in params:
            disciplina_id = params["disciplinaID"][0]
            cursor.execute(
                f"SELECT * FROM disciplinas WHERE disciplinaID = {disciplina_id}")
        else:
            cursor.execute("SELECT * FROM disciplinas")

        result = cursor.fetchall()
        cursor.close()
        connection.close()

        self.wfile.write(bytes(json.dumps(result, default=str), "utf-8"))

    def do_POST(self):
        """Lida com requisições POST (Criação de nova disciplina)."""
        self._set_headers()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        connection = create_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO disciplinas (nomeDisciplina, siglaDisciplina, aulasSemanaisDisciplina, aulasTotaisSemestreDisciplina, cargaHorariaDisciplina, ementa, turmaID, cursoID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['nomeDisciplina'], data['siglaDisciplina'], data['aulasSemanaisDisciplina'], data['aulasTotaisSemestreDisciplina'],
            data['cargaHorariaDisciplina'], data['ementa'], data['turmaID'], data['cursoID']
        )

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        response = {"message": "Disciplina criada com sucesso!"}
        self.wfile.write(bytes(json.dumps(response), "utf-8"))

    def do_PUT(self):
        """Lida com requisições PUT (Atualização de uma disciplina existente)."""
        self._set_headers()

        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        data = json.loads(put_data)

        disciplina_id = data['disciplinaID']

        connection = create_connection()
        cursor = connection.cursor()

        query = """
        UPDATE disciplinas
        SET nomeDisciplina = %s, siglaDisciplina = %s, aulasSemanaisDisciplina = %s, aulasTotaisSemestreDisciplina = %s, 
        cargaHorariaDisciplina = %s, ementa = %s, turmaID = %s, cursoID = %s
        WHERE disciplinaID = %s
        """
        values = (
            data['nomeDisciplina'], data['siglaDisciplina'], data['aulasSemanaisDisciplina'], data['aulasTotaisSemestreDisciplina'],
            data['cargaHorariaDisciplina'], data['ementa'], data['turmaID'], data['cursoID'], disciplina_id
        )

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        response = {"message": "Disciplina atualizada com sucesso!"}
        self.wfile.write(bytes(json.dumps(response), "utf-8"))

    def do_DELETE(self):
        """Lida com requisições DELETE (Exclusão de uma disciplina)."""
        self._set_headers()

        query_components = urllib.parse.urlparse(self.path)
        params = parse_qs(query_components.query)

        if "disciplinaID" in params:
            disciplina_id = params["disciplinaID"][0]

            connection = create_connection()
            cursor = connection.cursor()

            query = "DELETE FROM disciplinas WHERE disciplinaID = %s"
            cursor.execute(query, (disciplina_id,))
            connection.commit()
            cursor.close()
            connection.close()

            response = {"message": "Disciplina excluída com sucesso!"}
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            response = {"message": "ID da disciplina não informado."}
            self.wfile.write(bytes(json.dumps(response), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Servidor iniciado em http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Servidor encerrado.")
