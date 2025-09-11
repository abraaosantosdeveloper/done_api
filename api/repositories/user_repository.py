from api.models.user import User
import api.sqlutils.connector as db
import bcrypt

def userLogin(email, senha):
    query = "SELECT * FROM usuarios WHERE email = %s"
    params = (email,)
    usuario = db.executarConsulta(query, params)
    
    if not usuario:
        return None, "Usuário não encontrado"
    
    usuario = usuario[0]
    stored_hashed_senha = usuario[2]
    
    if bcrypt.checkpw(senha.encode('utf-8'), stored_hashed_senha.encode('utf-8')):
        user_obj = User(
            id=usuario[0],
            email=usuario[1],
            hash_senha=usuario[2]
        )
        return user_obj.to_dict(), None
    else:
        return None, "Senha incorreta"

def userSignup(email, senha):
    qurey = "INSERT INTO usuarios (email, hash_senha) VALUES (%s, %s)"
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    params = (email, hashed_senha)
    try:
        usuario_adicionado = db.executarComando(qurey, params)
        return usuario_adicionado
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")
        return None, str(e)

def deleteUser(email):
    query = "DELETE FROM usuarios WHERE email = %s"
    params = (email,)
    try:
        usuario_deletado = db.executarComando(query, params)
        return usuario_deletado
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        return None, str(e)