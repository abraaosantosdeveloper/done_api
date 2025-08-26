from api.models.task import Tarefa
import api.sqlutils.connector as db


def getTasks():
    query = "SELECT * FROM tarefas"
    tarefas = db.executarConsulta(query)
    
    return [
        Tarefa(
            id=tarefa[0],
            nome_tarefa=tarefa[1],
            status=tarefa[2]
        ) for tarefa in tarefas
    ]


