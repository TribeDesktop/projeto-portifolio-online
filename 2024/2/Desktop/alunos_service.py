from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from db_connection import create_connection

# Configuração do servidor
hostName = "localhost"
serverPort = 5000

class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        """Configura os headers padrão."""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        """Lida com requisições GET para listar apenas os alunos sem o campo de senha."""
        self._set_headers()
        
        try:
            connection = create_connection()
            cursor = connection.cursor(dictionary=True)
            
            # Consulta para listar apenas alunos, excluindo o campo de senha
            cursor.execute("""
                SELECT usuarioID, nomeUsuario, dataNascUsuario, sexoUsuario, 
                       cpfUsuario, tipoUsuario, ufUsuarios, ativo, adminID
                FROM USUARIOS 
                WHERE tipoUsuario = 'aluno'
            """)
            result = cursor.fetchall()
            
            # Envia a resposta JSON com os dados dos alunos
            self.wfile.write(bytes(json.dumps(result, default=str), "utf-8"))
        
        except Exception as err:
            # Retorna um erro caso ocorra algum problema
            self.send_response(500)
            self.wfile.write(bytes(json.dumps({"error": str(err)}), "utf-8"))
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Servidor iniciado em http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Servidor encerrado.")