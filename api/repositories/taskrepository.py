from api.models.task import Tarefa
import api.sqlutils.connector as db


def getTasks():
    query = "SELECT * FROM tarefas"
    tarefas = db.executarConsulta(query)
    
    resultado = []

    for tarefa in tarefas:
        nova_tarefa = Tarefa(
            id=tarefa[0],
            nome_tarefa=tarefa[1],
            status=tarefa[2]
        )
        resultado.append(
            nova_tarefa.to_dict()
        )
        
    return resultado
