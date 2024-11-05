class Msg:
    
    
    # Atenção! a função 'get_message' é para uso interno da classe, portanto não deve ser chamada diretamente.
    @staticmethod
    def get_message(action, entity, status, detail=None, refType=None, reference=None):
        
        
        """ 
        -param action: Ação realizada ('created', 'updated' ou 'deleted')
        -param entity: Entidade afetada ('teacher', 'student' ou 'course')
        -param detail: Detalhes da requisição (ex: "este cadastro não existe")
        
        -param reftype: Tipo do valor de referência do cadastro afetado ('id' ou 'nome')
        -param reference: O próprio valor de referência do cadastro afetado (ex: caso id: '1039241", caso nome: "Programação web")
        
        -return: Mensagem de sucesso
        """
        
        #-No tratamento das respostas, devem ser passado os parâmetros action (ação), entity(entidade) e detail (detalhe, que é opcional)
        #-devem ser passados na forma escrita à esquerda, para que o sistema mostre conforme escrito à direita.
        actions = {
            'created': 'cadastrado',
            'updated': 'atualizado',
            'deleted': 'deletado'
        }

        
        #refTypes = {
      #      'id': 'id',
       #     'name': 'nome',
     #   }

        action_message = actions.get(action, 'realizada')
    #quando for usado o método success, ele passa o parâmetro status como 1 (sucesso), quando for error, passa 0 (erro), de forma automática
    #assim, são geradas as seguintes respostas:
    
    #se a operação tiver sucesso:
        if status==1:
            if refType == None and reference == None:
                if detail:
                    return f"O/A {entity} foi {action_message} com sucesso. Detalhes: {detail}."
                else:
                    return f"O/A {entity} foi {action_message} com sucesso."
            else:
                if detail:
                    return f"O/A {entity} de {refType} '{reference}' foi {action_message} com sucesso. Detalhes: {detail}."
                else:
                    return f"O/A {entity} de {refType} '{reference}' foi {action_message} com sucesso."
            
    #se a operação tiver erro
        elif status==0:
            if refType == None and reference == None:
                if detail:
                    return f"O/A {entity} não foi {action_message}. Detalhes: {detail}."
                else:
                    return f"O/A {entity} não foi {action_message}."
                    
            else:
                if detail:
                    return f"O/A {entity} de {refType} {reference} não foi {action_message}. Detalhes: {detail}."
                    
                else:
                    return f"O/A {entity} de {refType} {reference} não foi {action_message}."
                    
    #Os ifs tratam as diferentes possibilidades, com ou sem identificador, detalhes, sucesso ou erro...
    
    #As classes abaixo devem ser chamadas diretamente
    #Para o título da mensagem:
    @staticmethod
    def title(situation):
        if situation == 0:
            return "Erro!"
        elif situation == 1:
            return "Sucesso!"
        elif situation == 2:
            return "Parabéns!"
        
    #Para a descrição da mensagem
    #se for sucesso, chamar:
    @staticmethod
    def success(action, entity, message=None, reference=None, refType=None):
     
        status = 1
        return Msg.get_message(action, entity, status, message, refType, reference)

    #se for de erro, chamar:
    @staticmethod
    def error(action, entity, message=None, reference=None, refType=None):
        status = 0
        return Msg.get_message(action, entity, status, message, refType, reference)
    
    
    
    #exemplos:
    
    #exemplo de como usar:
    # para tratar uma resposta de sucesso no cadastro de um professor chamado João
    """
    texto_titulo = title(1)
    texto_descricao = success(created, teacher, name,)
    """
    

    #exemplo de mensagem, com title retornando success e uma mensagem de success,
    # passando action = created, entity = teacher, refType = name e reference = João:
    """
            Sucesso! 
            O/A Professor de nome João foi cadastrado com sucesso
    """
    
