from api.models.task import Tarefa

def getTasks():

    tarefas = Tarefa.get_all()
    resultado = [tarefa.to_dict() for tarefa in tarefas]
    print("Tarefas recuperadas:", resultado)
    return resultado

