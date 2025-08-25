from api.models.task import Tarefa

def getTasks():

    tarefas = Tarefa.get_all()
    return [tarefa.to_dict() for tarefa in tarefas]

