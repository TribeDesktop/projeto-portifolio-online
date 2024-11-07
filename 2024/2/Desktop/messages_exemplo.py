from messages_front import *

exibir_popup(Msg.title(0),(Msg.error("created","aluno")))

#acima um exemplo simples de como usar a classe de mensagens

#chama-se a função exibir_popup, passando os parâmetros:

# Msg.title() com o titulo do popup. Com 0 para 'erro', 1 para 'sucesso' e 2 para 'parabéns'

#e Msg.error ou Msg.Success, com os detalhes do tipo de operação, entidade afetada e detalhes, caso existam (no arquivo messages_back é possível visualizar melhor os parâmetros e como enviá-los). Mas a ordem é ação, entidade, mensagem(ou seja, os detalhes), referencia e tipo de referência. Apenas ação e entidade são obrigatórios.

##obs: os parâmetros referência e tipo de referência: o tipo de referência pode ser "id", ou "nome", sendo a referêcia o valor propriamente dito: "12"(id) ou "João" (nome), para que seja exibido na mensagem se for interessante.