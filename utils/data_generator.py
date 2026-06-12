import uuid


def generate_user():
    return {
        "nome": "Usuário Teste",
        "email": f"usuario_{uuid.uuid4().hex}@teste.com",
        "password": "123456",
        "administrador": "true"
    }