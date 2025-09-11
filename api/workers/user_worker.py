from api.repositories.user_repository import userLogin, userSignup
import traceback

def login(info):
    try:
        email = info.get('email')
        senha = info.get('senha')
        return userLogin(email, senha)
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
        traceback.print_exc()
        return None, "Erro interno do servidor"