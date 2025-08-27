from api.repositories.taskrepository import getTasks, newTask
import traceback

def get_all_tasks():
    try:
        return getTasks()
    except Exception as e:
        print(f"Erro ao buscar tarefas: {e}")
        traceback.print_exc()
        return []

def create_task(data):
    pass