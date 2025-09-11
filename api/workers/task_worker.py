from api.repositories.task_repository import getTasks, newTask
import traceback

def get_all_tasks():
    try:
        return getTasks()
    except Exception as e:
        print(f"Erro ao buscar tarefas: {e}")
        traceback.print_exc()
        return []

def create_task(data):
    try:
        return newTask(data)
    except Exception as e:
        print(f"Erro ao criar tarefa: {e}")
        traceback.print_exc()
        return None