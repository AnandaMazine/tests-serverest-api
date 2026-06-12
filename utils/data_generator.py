import uuid


def generate_user():
    return {
        "nome": "Ananda Teste",
        "email": f"ananda_{uuid.uuid4().hex}@teste.com",
        "password": "123456",
        "administrador": "true"
    }