import api.sqlutils.connector as db

def getTasks():
    """
    Obtém todos os livros do banco de dados com informação de favorito
    para o usuário especificado.
    """
    
    query = """
    SELECT * FROM tarefas
    """
    
    tarefas = db.executarConsulta(query)
    
    tarefas_formatadas = []
    for tarefa in tarefas:
        tarefa_formatada = {
            "id": tarefa[0],
            "titulo": tarefa[1],
            "concluida": tarefa[2]
        }
        tarefas_formatadas.append(tarefa_formatada)
        
    return tarefas_formatadas

