import api.sqlutils.connector as db

# Classe tarefa
class Tarefa:
    def __init__(self, id, nome_tarefa, status:int):
        self.id = id
        self.nome_tarefa = nome_tarefa
        self.status = status
    
    @staticmethod
    def get_all():
        query = "SELECT * FROM tarefas"
        tarefas = db.executarConsulta(query)
        
        return [
            Tarefa(
                id=tarefa[0],
                nome_tarefa=tarefa[1],
                status=tarefa[2]
            ) for tarefa in tarefas
        ]

    def to_dict(self):
        return {
            "id": self.id,
            "nome_tarefa": self.nome_tarefa,
            "status": self.status
        }
        