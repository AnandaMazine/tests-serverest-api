import requests #Importando bibliotecas que me permite fazer chamadas HTTP para APIs
from utils.data_generator import generate_user #Função criada para gerar users com email único
import uuid

BASE_URL = "https://compassuol.serverest.dev" # Guarda a API numa variável

# 1- TESTE CADASTRAR UM USUÁRIO COM DADOS VÁLIDOS
def test_create_user_success(): #Início do teste
    payload = generate_user() #Função que cria os dados do usuário
    response = requests.post( #fazendo o POST e armazena em response
        f"{BASE_URL}/usuarios",
        json=payload
    )
    #print(response.json())
    assert response.status_code == 201 #Verifica se foi criado com sucesso

# 2- TESTE CADASTRA USUÁRIO COM EMAIL DUPLICADO
def test_create_user_with_duplicate_email():
    payload = generate_user()
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )
    assert response.status_code == 201

    segunda_tentativa = requests.post( #cadastrando novamente com o mesmo email
        f"{BASE_URL}/usuarios",
        json=payload
    )
    # print(segunda_tentativa.json()) # printa a saída pra verificar se está correto
    assert segunda_tentativa.status_code == 400

# 3- TESTE CADASTRA USUÁRIO SEM EMAIL
def test_create_user_without_email():
    payload = generate_user()
    payload.pop("email") #Função para remover o e-mail
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )
    #print(response.json())
    assert response.status_code == 400

# 4- TESTE CADASTRA USUÁRIO SEM NOME
def test_create_user_without_name():
    payload = generate_user()
    payload.pop("nome") #Função para remover o nome
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )
    #print(response.json())
    assert response.status_code == 400

# 5- TESTE CADASTRA USUÁRIO SEM SENHA
def test_create_user_without_password():
    payload = generate_user()
    payload.pop("password") #Função para remover a senha
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )
    #print(response.json())
    assert response.status_code == 400

# 6- TESTE BUSCA USUÁRIO POR ID VÁLIDO
def test_get_user_by_valid_id():
    payload = generate_user()
    response = requests.post( # primeiro cadastra um novo usuário
        f"{BASE_URL}/usuarios/",
        json=payload
    )
    assert response.status_code == 201

    user_id = response.json()["_id"] 
    usuario_cadastrado = requests.get(  # busca o usuário cadastrado
        f"{BASE_URL}/usuarios/{user_id}",
    )
    assert usuario_cadastrado.status_code == 200

# 7- TESTE ID INVÁLIDO
def test_get_user_by_invalid_id():
    invalid_id = "123456789" # Usa um ID inexistente
    response = requests.get(
        f"{BASE_URL}/usuarios/{invalid_id}", # vai procurar o id inexistente
    )
    #print(response.status_code)
    #print(response.json())
    assert response.status_code == 400

# 8- TESTE LISTA TODOS OS USUÁRIOS
def test_list_all_users():
    response = requests.get( # Função para buscar os usuários
        f"{BASE_URL}/usuarios/",
    )
    #print(response.json())
    assert response.status_code == 200

# 9- TESTE ATUALIZA USUÁRIOS
def test_update_user_successfully():
    payload = generate_user()
    create_response = requests.post( # Cria novo usuário
        f"{BASE_URL}/usuarios",
        json=payload
    )
    assert create_response.status_code == 201
    user_id = create_response.json()["_id"] # captura o id do usuário

    updated_user = { # cria novos dados do usuário
        "nome": "Usuário Atualizado",
        "email": f"novo_{uuid.uuid4().hex}@teste.com",
        "password": "123456",
        "administrador": "true"
    }
    update_response = requests.put( # faz a requisão put
        f"{BASE_URL}/usuarios/{user_id}",
        json=updated_user
    )
    #print(update_response.json())
    assert update_response.status_code == 200
    usuario_atualizado = requests.get( # busca o usuário atualizado
    f"{BASE_URL}/usuarios/{user_id}"
    )
    usuario_atualizado.status_code == 200

# 10- TESTE DELETA USUÁRIOS    
def test_delete_user_successfully():
    payload = generate_user() # Cria o usuário
    create_response = requests.post( # cadastra
        f"{BASE_URL}/usuarios",
        json=payload
    )
    assert create_response.status_code == 201
    user_id = create_response.json()["_id"] # pega a id
    
    delete_response = requests.delete( # exclui o usuário
        f"{BASE_URL}/usuarios/{user_id}",
    )
    assert delete_response.status_code == 200 # valida a exclusão

    get_response = requests.get( # tenta buscar e valida que o usuário não existe mais
        f"{BASE_URL}/usuarios/{user_id}",
    )
    assert get_response.status_code == 400