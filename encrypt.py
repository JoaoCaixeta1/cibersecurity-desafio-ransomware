import os
from cryptography.fernet import Fernet

# Gerar uma chave de criptografia e salvar em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

# Carregar a chave existente
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografar um arquivo
def criptografar_arquivo(nome_arquivo, chave):
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as arquivo:
        dados = arquivo.read()
    
    dados_criptografados = fernet.encrypt(dados)

    with open(nome_arquivo + ".locked", "wb") as arquivo_cripto:
        arquivo_cripto.write(dados_criptografados)
    
    os.remove(nome_arquivo)  # Remove o arquivo original

# Criar chave se não existir
if not os.path.exists("chave.key"):
    gerar_chave()

chave = carregar_chave()

# Arquivo para criptografar
arquivo_alvo = "teste.txt"
criptografar_arquivo(arquivo_alvo, chave)

print(f"Arquivo {arquivo_alvo} foi criptografado!")
