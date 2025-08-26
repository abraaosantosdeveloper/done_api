class Usuario:
    def __init__(self, id, nome, apelido, email, hash_senha,):
        self.id = id
        self.nome = nome
        self.apelido = apelido
        self.email = email
        self.hash_senha = hash_senha
        
    def cadastrar_novo_usuario(self):
        pass
    
    def efetuar_login(self):
        pass
    
    def alterar_informacoes_usuario(self):
        pass
    
    def excluir_usuario(self):
        pass
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "apelido": self.apelido,
            "email": self.email,
            "hash_senha": self.hash_senha
        }