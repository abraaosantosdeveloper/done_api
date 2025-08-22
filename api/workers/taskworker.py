from api.repositories.taskrepository import getTasks
import traceback

def get_all_tasks():
    try:
        return getTasks()
    except Exception as e:
        print(f"Erro ao buscar tarefas: {e}")
        traceback.print_exc()
        return []