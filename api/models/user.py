class Usuario:
    def __init__(self, id, admin, nome, nascimento, apelido, email, hash_senha):
        self.id = id
        self.admin = admin
        self.nome = nome
        self.apelido = apelido
        self.data_nascimento = nascimento
        self.email = email
        self.hash_senha = hash_senha
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "apelido": self.apelido,
            "email": self.email,
            "hash_senha": self.hash_senha
        }