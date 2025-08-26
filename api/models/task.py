# Classe tarefa
class Tarefa:
    def __init__(self, id, nome_tarefa, status:int):
        self.id = id
        self.nome_tarefa = nome_tarefa
        self.status = status
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome_tarefa": self.nome_tarefa,
            "status": self.status
        }
        