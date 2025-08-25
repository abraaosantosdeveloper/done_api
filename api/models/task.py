import api.sqlutils.connector as db

# Classe tarefa
class Tarefa:
    def __init__(self, id, titulo, status:int):
        self.id = id
        self.titulo = titulo
        self.status = status
    
    @staticmethod
    def get_all():
        query = "SELECT * FROM tarefas"
        tarefas = db.executarConsulta(query)
        
        return [
            Tarefa(
                id=tarefa[0],
                titulo=tarefa[1],
                concluida=tarefa[2]
            ) for tarefa in tarefas
        ]
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "concluida": self.concluida
        }